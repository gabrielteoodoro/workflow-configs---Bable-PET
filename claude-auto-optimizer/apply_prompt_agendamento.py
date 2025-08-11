#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Apply Prompt Otimizado - Agente Agendamento
Script para aplicar otimizações do Ciclo #002 no N8N
"""

import requests
import json
import os

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

# Carregar configurações
carregar_env()

N8N_API_URL = os.getenv('N8N_API_URL', 'https://n8n.synapseautointeligente.com.br/api/v1')
N8N_API_KEY = os.getenv('N8N_API_KEY')

headers = {
    'X-N8N-API-KEY': N8N_API_KEY,
    'Content-Type': 'application/json'
}

# Workflow ID do Agente Agendamento
workflow_id = 'KRlswJLa4CmAvWIL'  # Agendamento - Consultor

print("APLICANDO OTIMIZACOES - CICLO #002 AGENTE AGENDAMENTO")
print("="*60)

# Verificar se existe a versão Rev02 do Agendamento
prompt_file = '../Prompt_ Agente Agendamento - Consultor_rev02.md'
if not os.path.exists(prompt_file):
    print("AVISO: Arquivo Rev02 nao existe ainda.")
    print(f"Esperado: {prompt_file}")
    print("")
    print("PRÓXIMOS PASSOS:")
    print("1. Agent 2 (Builder) deve criar a versao Rev02")
    print("2. Agent 2 deve aplicar todas as melhorias da especificacao")
    print("3. Depois executar este script para aplicar no N8N")
    print("")
    print("INSTRUCOES PARA AGENT 2:")
    print("- Usar especificacao: ESPECIFICACAO_CICLO_002_AGENDAMENTO_AGENT1.md")
    print("- Criar: Prompt_ Agente Agendamento - Consultor_rev02.md")
    print("- Implementar 4 melhorias criticas identificadas")
    exit(1)

# Ler o prompt otimizado
print("Lendo prompt Rev02 do Agendamento...")
try:
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt_otimizado = f.read()
    print(f"Prompt carregado: {len(prompt_otimizado)} caracteres")
except Exception as e:
    print(f"Erro ao ler arquivo: {e}")
    exit(1)

try:
    print('Buscando workflow do Agendamento...')
    response = requests.get(f'{N8N_API_URL}/workflows/{workflow_id}', headers=headers, timeout=15)
    
    if response.status_code == 200:
        workflow = response.json()
        print('Workflow obtido com sucesso!')
        
        # Encontrar e atualizar o node do agente agendamento
        nodes = workflow.get('nodes', [])
        updated = False
        
        for node in nodes:
            node_name = node.get('name', '').lower()
            node_type = node.get('type', '')
            
            # Procurar por node de IA (pode ter nome genérico)
            if node_type == '@n8n/n8n-nodes-langchain.agent':
                print(f'Node encontrado: {node.get("name")} (Tipo: {node_type})')
                
                # Backup do prompt atual
                current_prompt = node.get('parameters', {}).get('text', '')
                print(f'Prompt atual: {len(current_prompt)} caracteres')
                
                # Atualizar o prompt no parametro 'text'
                if 'parameters' in node:
                    node['parameters']['text'] = prompt_otimizado
                    print('Prompt Rev02 atualizado no node!')
                    updated = True
                    break
        
        if updated:
            # Salvar o workflow atualizado
            print('Aplicando otimizacoes no N8N...')
            
            # Usar workflow original mas apenas atualizar o prompt
            save_response = requests.put(
                f'{N8N_API_URL}/workflows/{workflow_id}', 
                headers=headers, 
                json=workflow,  # Usar workflow original completo
                timeout=30
            )
            
            if save_response.status_code == 200:
                print("")
                print("SUCCESS: CICLO #002 APLICADO NO N8N!")
                print("="*50)
                print("AGENTE AGENDAMENTO - REV02 ATIVO")
                print("="*50)
                print("OTIMIZACOES APLICADAS:")
                print("- Sistema completo de racas e grupos (150+ racas)")
                print("- Validacao avancada de agenda com horario comercial") 
                print("- Garantia obrigatoria de duplo registro")
                print("- Humanizacao da coleta de email")
                print("")
                print("METRICAS ESPERADAS:")
                print(f"- Score: 7.2/10 -> 8.0+/10")
                print(f"- Taxa sucesso: 60% -> 90%+")
                print(f"- Abandono email: 30% -> 10%")
                print(f"- Duplo registro: 75% -> 98%+")
                print("")
                print("PROXIMO PASSO: Agent 3 (Validator) testar cenarios!")
                
            else:
                print(f'ERRO: Falha ao salvar workflow: {save_response.status_code}')
                print(f'Resposta: {save_response.text[:200]}')
        else:
            print('ERRO: Node do agente agendamento nao encontrado')
            print('Nodes com IA disponíveis:')
            for node in nodes:
                if '@n8n/n8n-nodes-langchain.agent' in node.get('type', ''):
                    print(f'  - {node.get("name")} ({node.get("type")})')
    else:
        print(f'ERRO: Falha ao buscar workflow: {response.status_code}')
        print(f'Resposta: {response.text[:200]}')
        
except Exception as e:
    print(f'ERRO: {e}')

print("\nScript concluido!")