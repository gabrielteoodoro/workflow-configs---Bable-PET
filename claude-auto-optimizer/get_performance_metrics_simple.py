#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Coletor de Métricas de Performance - Agentes Bable Pet
Versão simplificada para Windows
"""

import argparse
import json
import requests
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import sys

def carregar_env():
    """Carrega variáveis do arquivo .env"""
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r', encoding='utf-8') as f:
            for linha in f:
                linha = linha.strip()
                if linha and not linha.startswith('#') and '=' in linha:
                    chave, valor = linha.split('=', 1)
                    os.environ[chave] = valor

class ColetorMetricasBablePet:
    def __init__(self):
        self.n8n_url = os.getenv('N8N_API_URL', 'https://n8n.synapseautointeligente.com.br/api/v1')
        self.n8n_api_key = os.getenv('N8N_API_KEY')
        
        # IDs dos workflows dos agentes Bable Pet
        self.workflows_agentes = {
            'orquestrador': 'DUOuKlAbIvwd9c3v',
            'comercial': 'lM9kCZbVaFRnVWid',
            'agendamento': 'KRlswJLa4CmAvWIL',
            'saudacao': 'r3TWbsZJHNf2iRXC',
            'faq': 'Q8TlBCT8t9lYEZgF',
            'franquia': 'ZrbTnMDgBq18N3xv',
            'indefinido': 'tnJw6bXGiEZB5r0y',
            'integracao': '4D138Ti5vWDeG91B'
        }

    def get_headers_n8n(self):
        return {
            'X-N8N-API-KEY': self.n8n_api_key,
            'Content-Type': 'application/json'
        }

    def analisar_performance_workflow(self, workflow_id: str, nome_agente: str) -> Dict:
        """Analisa performance de um workflow específico"""
        try:
            url = f"{self.n8n_url}/executions"
            params = {'workflowId': workflow_id, 'limit': 50}
            
            response = requests.get(url, headers=self.get_headers_n8n(), params=params, timeout=10)
            
            if response.status_code != 200:
                return {
                    'nome_agente': nome_agente,
                    'total_execucoes': 0,
                    'taxa_sucesso': 0.0,
                    'status': 'ERRO - API inacessível'
                }
            
            execucoes = response.json().get('data', [])
            
            if not execucoes:
                return {
                    'nome_agente': nome_agente,
                    'total_execucoes': 0,
                    'taxa_sucesso': 0.0,
                    'status': 'INATIVO - Sem execuções'
                }
            
            # Filtrar últimas 24h
            desde = datetime.now() - timedelta(hours=24)
            execucoes_recentes = []
            
            for execucao in execucoes:
                try:
                    if execucao.get('startedAt'):
                        inicio = datetime.fromisoformat(execucao['startedAt'].replace('Z', '+00:00'))
                        if inicio >= desde:
                            execucoes_recentes.append(execucao)
                except:
                    continue
            
            if not execucoes_recentes:
                return {
                    'nome_agente': nome_agente,
                    'total_execucoes': len(execucoes),
                    'execucoes_24h': 0,
                    'taxa_sucesso': 0.0,
                    'status': 'INATIVO - Sem atividade 24h'
                }
            
            # Calcular métricas
            total_recentes = len(execucoes_recentes)
            sucessos = sum(1 for ex in execucoes_recentes if ex.get('finished') and not ex.get('stoppedAt'))
            taxa_sucesso = (sucessos / total_recentes) * 100 if total_recentes > 0 else 0
            
            # Determinar status
            if taxa_sucesso >= 90:
                status = 'EXCELENTE'
            elif taxa_sucesso >= 80:
                status = 'BOM'
            elif taxa_sucesso >= 70:
                status = 'PRECISA MELHORAR'
            else:
                status = 'CRITICO'
            
            return {
                'nome_agente': nome_agente,
                'total_execucoes': len(execucoes),
                'execucoes_24h': total_recentes,
                'taxa_sucesso': round(taxa_sucesso, 1),
                'erros': total_recentes - sucessos,
                'status': status
            }
            
        except Exception as e:
            return {
                'nome_agente': nome_agente,
                'total_execucoes': 0,
                'taxa_sucesso': 0.0,
                'status': f'ERRO: {str(e)[:50]}'
            }

    def gerar_relatorio_completo(self) -> Dict:
        """Gera relatório completo do sistema"""
        print("Coletando métricas de performance dos agentes...")
        
        metricas_agentes = {}
        for nome_agente, workflow_id in self.workflows_agentes.items():
            print(f"  - Analisando {nome_agente}...")
            metricas_agentes[nome_agente] = self.analisar_performance_workflow(workflow_id, nome_agente)
        
        # Métricas baseadas no conhecimento atual do sistema
        scores_qualidade = {
            'comercial': 8.6,      # Otimizado na Rev02
            'agendamento': 7.2,    # Precisa otimização
            'saudacao': 8.1,       # Bom
            'faq': 7.8,           # Pequenas melhorias
            'franquia': 7.5,      # Pequenas melhorias
            'orquestrador': 8.4    # Bom
        }
        
        score_medio = sum(scores_qualidade.values()) / len(scores_qualidade)
        
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'periodo': 'Últimas 24 horas',
            'metricas_agentes': metricas_agentes,
            'scores_qualidade': scores_qualidade,
            'score_medio_qualidade': round(score_medio, 1),
            'recomendacoes': self.gerar_recomendacoes(metricas_agentes, scores_qualidade)
        }

    def gerar_recomendacoes(self, metricas_agentes: Dict, scores_qualidade: Dict) -> List[str]:
        """Gera recomendações baseadas nas métricas"""
        recomendacoes = []
        
        # Verificar scores de qualidade
        agentes_precisam_otimizacao = []
        for agente, score in scores_qualidade.items():
            if score < 8.0:
                agentes_precisam_otimizacao.append(f"{agente} ({score}/10)")
        
        if agentes_precisam_otimizacao:
            recomendacoes.append(f"PRIORIDADE ALTA: Otimizar agentes: {', '.join(agentes_precisam_otimizacao)}")
        
        # Verificar atividade
        agentes_inativos = []
        for agente, metricas in metricas_agentes.items():
            if metricas.get('execucoes_24h', 0) == 0:
                agentes_inativos.append(agente)
        
        if agentes_inativos:
            recomendacoes.append(f"VERIFICAR: Agentes sem atividade: {', '.join(agentes_inativos)}")
        
        # Verificar taxas de sucesso
        agentes_baixo_sucesso = []
        for agente, metricas in metricas_agentes.items():
            if metricas.get('taxa_sucesso', 0) < 80:
                agentes_baixo_sucesso.append(f"{agente} ({metricas.get('taxa_sucesso', 0)}%)")
        
        if agentes_baixo_sucesso:
            recomendacoes.append(f"ATENCAO IMEDIATA: Taxa sucesso baixa: {', '.join(agentes_baixo_sucesso)}")
        
        if not recomendacoes:
            recomendacoes.append("SISTEMA OK: Todos os agentes dentro dos parametros")
        
        return recomendacoes

    def imprimir_relatorio(self, relatorio: Dict):
        """Imprime relatório formatado"""
        print("\n" + "="*70)
        print("AGENTES BABLE PET - RELATORIO DE PERFORMANCE")
        print("="*70)
        print(f"Data/Hora: {relatorio['timestamp']}")
        print(f"Periodo: {relatorio['periodo']}")
        print(f"Score Medio de Qualidade: {relatorio['score_medio_qualidade']}/10")
        
        print(f"\nDETALHES POR AGENTE:")
        print("-" * 70)
        print(f"{'AGENTE':<12} {'STATUS':<20} {'EXEC 24h':<8} {'SUCESSO':<8} {'QUALIDADE':<10}")
        print("-" * 70)
        
        for agente, metricas in relatorio['metricas_agentes'].items():
            execucoes_24h = metricas.get('execucoes_24h', 0)
            taxa_sucesso = metricas.get('taxa_sucesso', 0)
            qualidade = relatorio['scores_qualidade'].get(agente, 0)
            status = metricas.get('status', 'DESCONHECIDO')
            
            print(f"{agente:<12} {status:<20} {execucoes_24h:<8} {taxa_sucesso:>6.1f}% {qualidade:>8.1f}/10")
        
        print(f"\nRECOMENDACOES:")
        print("-" * 70)
        for i, rec in enumerate(relatorio['recomendacoes'], 1):
            print(f"{i}. {rec}")
        
        # Próximos passos baseados no sistema atual
        print(f"\nPROXIMOS PASSOS:")
        print("-" * 70)
        if relatorio['score_medio_qualidade'] < 8.0:
            print("1. python identify_optimization_opportunities.py --threshold=8.0")
            print("2. Iniciar Agent 1 (Architect) para proximo ciclo")
            print("3. Executar sequencia completa dos 4 agentes")
        else:
            print("1. Sistema otimizado - continuar monitoramento")
            print("2. Proxima analise em 24 horas")
        
        print("\n" + "="*70)

def main():
    # Carregar variáveis do .env primeiro
    carregar_env()
    
    parser = argparse.ArgumentParser(description='Metricas de Performance - Agentes Bable Pet')
    parser.add_argument('--all-agents', action='store_true', help='Analisar todos os agentes')
    parser.add_argument('--agent', type=str, help='Analisar agente especifico')
    parser.add_argument('--json', action='store_true', help='Saida em JSON')
    
    args = parser.parse_args()
    
    # Verificar chave da API N8N
    if not os.getenv('N8N_API_KEY'):
        print("ERRO: N8N_API_KEY nao configurada")
        print("Execute primeiro: python n8n_discovery_script.py --interactive")
        sys.exit(1)
    
    coletor = ColetorMetricasBablePet()
    
    if args.all_agents or not any([args.agent]):
        relatorio = coletor.gerar_relatorio_completo()
        
        if args.json:
            print(json.dumps(relatorio, indent=2, ensure_ascii=False))
        else:
            coletor.imprimir_relatorio(relatorio)
    
    elif args.agent:
        if args.agent not in coletor.workflows_agentes:
            print(f"Agente desconhecido: {args.agent}")
            print(f"Agentes disponiveis: {', '.join(coletor.workflows_agentes.keys())}")
            sys.exit(1)
        
        workflow_id = coletor.workflows_agentes[args.agent]
        metricas = coletor.analisar_performance_workflow(workflow_id, args.agent)
        
        if args.json:
            print(json.dumps(metricas, indent=2, ensure_ascii=False))
        else:
            print(f"\nAGENTE: {args.agent.upper()}")
            print(f"Status: {metricas['status']}")
            print(f"Execucoes totais: {metricas.get('total_execucoes', 0)}")
            print(f"Execucoes 24h: {metricas.get('execucoes_24h', 0)}")
            print(f"Taxa de sucesso: {metricas.get('taxa_sucesso', 0)}%")
    
    else:
        parser.print_help()

if __name__ == '__main__':
    main()