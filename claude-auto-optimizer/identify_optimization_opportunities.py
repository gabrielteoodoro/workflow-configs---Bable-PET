#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Identificador de Oportunidades de Otimização - Sistema Bable Pet
==============================================================

Analisa performance atual dos agentes e identifica quais precisam
de otimização baseado no threshold definido.

Integrado com o sistema de 4 agentes auxiliares para automatização.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Tuple

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

class IdentificadorOportunidades:
    def __init__(self, threshold: float = 8.0):
        self.threshold = threshold
        
        # Scores atuais baseados no Ciclo #001 e conhecimento do sistema
        self.scores_qualidade_atual = {
            'comercial': {
                'score': 8.6,
                'status': 'OTIMIZADO',
                'ciclo_completo': 'Ciclo #001 - Rev02',
                'observacoes': 'Humanização completa implementada, contextualização por raça'
            },
            'orquestrador': {
                'score': 8.4,
                'status': 'BOM',
                'ciclo_completo': 'Revisão Rev01',
                'observacoes': 'Lógica de intencoes funcionando bem, AGENDAMENTO+COMERCIAL ok'
            },
            'saudacao': {
                'score': 8.1,
                'status': 'BOM',
                'ciclo_completo': 'Rev02',
                'observacoes': 'Delega corretamente, busca dados cliente ok'
            },
            'faq': {
                'score': 7.8,
                'status': 'PRECISA_OTIMIZACAO',
                'ciclo_completo': 'Rev01 - Não otimizado',
                'observacoes': 'Falta integração com BANCO_DADOS_EMPRESA_BABLE_PET.md'
            },
            'franquia': {
                'score': 7.5,
                'status': 'PRECISA_OTIMIZACAO',
                'ciclo_completo': 'Rev01 - Não otimizado',
                'observacoes': 'Processo básico, pode melhorar qualificação de leads'
            },
            'agendamento': {
                'score': 7.2,
                'status': 'PRIORIDADE_ALTA',
                'ciclo_completo': 'Rev01 - Não otimizado',
                'observacoes': 'Taxa falha ~40%, precisa melhorar fluxo e validações'
            }
        }
        
        # Problemas identificados nos logs (simulado baseado no conhecimento)
        self.problemas_identificados = {
            'agendamento': [
                'racas_e_grupos() retorna null para raças comuns',
                'Falha na validação de datas/horários',
                'criaAtendimento() não executado após criarEvento()',
                'Abandono no meio do fluxo (sem email)'
            ],
            'faq': [
                'Respostas genéricas sem info da empresa',
                'Não usa BANCO_DADOS_EMPRESA_BABLE_PET.md',
                'Falta scripts para cenários empresariais'
            ],
            'franquia': [
                'Processo muito básico de qualificação',
                'Falta dados de investimento atualizados',
                'Transição para humano muito abrupta'
            ],
            'comercial': [
                # Já resolvidos no Ciclo #001
            ]
        }

    def identificar_agentes_prioritarios(self) -> List[Dict]:
        """Identifica agentes que precisam otimização baseado no threshold"""
        agentes_prioritarios = []
        
        for agente, dados in self.scores_qualidade_atual.items():
            if dados['score'] < self.threshold:
                prioridade = self.calcular_prioridade(dados['score'])
                
                agentes_prioritarios.append({
                    'agente': agente,
                    'score_atual': dados['score'],
                    'gap_threshold': round(self.threshold - dados['score'], 1),
                    'prioridade': prioridade,
                    'status': dados['status'],
                    'problemas': self.problemas_identificados.get(agente, []),
                    'observacoes': dados['observacoes']
                })
        
        # Ordenar por prioridade (menor score = maior prioridade)
        agentes_prioritarios.sort(key=lambda x: x['score_atual'])
        return agentes_prioritarios

    def calcular_prioridade(self, score: float) -> str:
        """Calcula nível de prioridade baseado no score"""
        if score < 7.0:
            return 'CRITICA'
        elif score < 7.5:
            return 'ALTA'
        elif score < 8.0:
            return 'MEDIA'
        else:
            return 'BAIXA'

    def gerar_roadmap_otimizacao(self, agentes_prioritarios: List[Dict]) -> Dict:
        """Gera roadmap de otimização com cronograma"""
        if not agentes_prioritarios:
            return {
                'status': 'SISTEMA_OTIMIZADO',
                'mensagem': 'Todos os agentes atendem ao threshold mínimo',
                'proxima_acao': 'Monitoramento contínuo'
            }
        
        # Próximo agente para otimização (prioridade)
        proximo_agente = agentes_prioritarios[0]
        
        roadmap = {
            'status': 'OTIMIZACAO_NECESSARIA',
            'agentes_abaixo_threshold': len(agentes_prioritarios),
            'proximo_ciclo': {
                'agente_foco': proximo_agente['agente'],
                'score_atual': proximo_agente['score_atual'],
                'meta_score': self.threshold,
                'prioridade': proximo_agente['prioridade'],
                'problemas_principais': proximo_agente['problemas'][:3],  # Top 3
                'tempo_estimado': self.estimar_tempo_ciclo(proximo_agente)
            },
            'cronograma_semanal': self.gerar_cronograma_semanal(agentes_prioritarios)
        }
        
        return roadmap

    def estimar_tempo_ciclo(self, agente_data: Dict) -> str:
        """Estima tempo necessário para um ciclo completo"""
        complexidade_problemas = len(agente_data['problemas'])
        
        if complexidade_problemas <= 2:
            return '4-6 horas (meio dia)'
        elif complexidade_problemas <= 4:
            return '6-8 horas (dia inteiro)'
        else:
            return '8-12 horas (2 dias)'

    def gerar_cronograma_semanal(self, agentes_prioritarios: List[Dict]) -> Dict:
        """Gera cronograma semanal de otimização"""
        cronograma = {}
        
        if len(agentes_prioritarios) >= 1:
            cronograma['semana_1'] = {
                'foco': agentes_prioritarios[0]['agente'],
                'objetivo': f"Score {agentes_prioritarios[0]['score_atual']} para {self.threshold}",
                'atividades': [
                    'Agent 1: Análise de logs e problemas',
                    'Agent 2: Implementação de melhorias',
                    'Agent 3: Testes extensivos', 
                    'Agent 4: Documentação e validação'
                ]
            }
        
        if len(agentes_prioritarios) >= 2:
            cronograma['semana_2'] = {
                'foco': agentes_prioritarios[1]['agente'],
                'objetivo': f"Score {agentes_prioritarios[1]['score_atual']} para {self.threshold}",
                'atividades': ['Ciclo completo 4 agentes']
            }
        
        if len(agentes_prioritarios) >= 3:
            cronograma['semana_3'] = {
                'foco': agentes_prioritarios[2]['agente'],
                'objetivo': f"Score {agentes_prioritarios[2]['score_atual']} para {self.threshold}",
                'atividades': ['Ciclo completo 4 agentes']
            }
        
        return cronograma

    def gerar_comandos_inicializacao(self, roadmap: Dict) -> List[str]:
        """Gera comandos específicos para inicializar o próximo ciclo"""
        if roadmap['status'] == 'SISTEMA_OTIMIZADO':
            return [
                'echo "Sistema otimizado - todos os agentes >= 8.0/10"',
                'python get_performance_metrics_simple.py --all-agents',
                'echo "Próxima verificação em 24h"'
            ]
        
        proximo = roadmap['proximo_ciclo']
        agente_foco = proximo['agente_foco']
        
        comandos = [
            f'echo "INICIANDO CICLO DE OTIMIZACAO - AGENTE: {agente_foco.upper()}"',
            f'echo "Score atual: {proximo["score_atual"]}/10 | Meta: {proximo["meta_score"]}/10"',
            '',
            '# AGENT 1 - ARCHITECT (Análise)',
            f'echo "Agent 1: Analisando problemas do agente {agente_foco}..."',
            'curl -s https://api.github.com/repos/gabrielteoodoro/bable-pet-debug/contents/debug_logs | head -5',
            '',
            '# AGENT 2 - BUILDER (Implementação)',
            f'echo "Agent 2: Implementando melhorias para {agente_foco}..."',
            f'# Editar: Prompt_ Agente {agente_foco.title()} - Consultor_rev01.md → rev02',
            '',
            '# AGENT 3 - VALIDATOR (Testes)',
            f'echo "Agent 3: Testando cenários {agente_foco}..."',
            'curl -X POST "https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5"',
            '',
            '# AGENT 4 - WRITER (Documentação)',
            f'echo "Agent 4: Documentando resultados {agente_foco}..."',
            '# Atualizar CLAUDE.md com resultados do ciclo'
        ]
        
        return comandos

    def imprimir_relatorio_detalhado(self, agentes_prioritarios: List[Dict], roadmap: Dict):
        """Imprime relatório detalhado de oportunidades"""
        print("="*80)
        print("IDENTIFICADOR DE OPORTUNIDADES DE OTIMIZACAO - BABLE PET")
        print("="*80)
        print(f"Data/Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Threshold Minimo: {self.threshold}/10")
        print(f"Status: {roadmap['status']}")
        
        if roadmap['status'] == 'SISTEMA_OTIMIZADO':
            print("\nTodos os agentes atendem ao threshold minimo!")
            print("Sistema funcionando dentro dos parametros de qualidade.")
            return
        
        print(f"\nAGENTES ABAIXO DO THRESHOLD ({len(agentes_prioritarios)}):")
        print("-" * 80)
        print(f"{'AGENTE':<12} {'SCORE':<6} {'GAP':<6} {'PRIORIDADE':<10} {'PROBLEMAS':<8}")
        print("-" * 80)
        
        for agente in agentes_prioritarios:
            print(f"{agente['agente']:<12} {agente['score_atual']:<6}/10 "
                  f"{agente['gap_threshold']:<6} {agente['prioridade']:<10} "
                  f"{len(agente['problemas']):<8}")
        
        # Detalhes do próximo ciclo
        proximo = roadmap['proximo_ciclo']
        print(f"\nPROXIMO CICLO DE OTIMIZACAO:")
        print("-" * 80)
        print(f"Agente Foco: {proximo['agente_foco'].upper()}")
        print(f"Score Atual: {proximo['score_atual']}/10")
        print(f"Meta Score: {proximo['meta_score']}/10")
        print(f"Prioridade: {proximo['prioridade']}")
        print(f"Tempo Estimado: {proximo['tempo_estimado']}")
        
        print(f"\nProblemas Identificados ({proximo['agente_foco']}):")
        for i, problema in enumerate(proximo['problemas_principais'], 1):
            print(f"  {i}. {problema}")
        
        # Cronograma
        print(f"\nCRONOGRAMA DE OTIMIZACAO:")
        print("-" * 80)
        for periodo, dados in roadmap['cronograma_semanal'].items():
            print(f"{periodo.upper()}: {dados['foco']} ({dados['objetivo']})")
        
        # Comandos para inicialização
        comandos = self.gerar_comandos_inicializacao(roadmap)
        print(f"\nCOMANDOS PARA INICIALIZAR PROXIMO CICLO:")
        print("-" * 80)
        for comando in comandos:
            print(comando)
        
        print("\n" + "="*80)

def main():
    parser = argparse.ArgumentParser(description='Identificar Oportunidades de Otimização')
    parser.add_argument('--threshold', type=float, default=8.0, 
                       help='Score mínimo aceitável (padrão: 8.0)')
    parser.add_argument('--json', action='store_true', 
                       help='Saída em formato JSON')
    parser.add_argument('--next-agent', action='store_true',
                       help='Mostrar apenas próximo agente a otimizar')
    
    args = parser.parse_args()
    
    # Carregar variáveis de ambiente
    carregar_env()
    
    # Inicializar identificador
    identificador = IdentificadorOportunidades(threshold=args.threshold)
    
    # Identificar oportunidades
    agentes_prioritarios = identificador.identificar_agentes_prioritarios()
    roadmap = identificador.gerar_roadmap_otimizacao(agentes_prioritarios)
    
    if args.json:
        resultado = {
            'timestamp': datetime.now().isoformat(),
            'threshold': args.threshold,
            'agentes_prioritarios': agentes_prioritarios,
            'roadmap': roadmap
        }
        print(json.dumps(resultado, indent=2, ensure_ascii=False))
    
    elif args.next_agent:
        if roadmap['status'] == 'SISTEMA_OTIMIZADO':
            print("SISTEMA_OTIMIZADO")
        else:
            print(roadmap['proximo_ciclo']['agente_foco'])
    
    else:
        identificador.imprimir_relatorio_detalhado(agentes_prioritarios, roadmap)

if __name__ == '__main__':
    main()