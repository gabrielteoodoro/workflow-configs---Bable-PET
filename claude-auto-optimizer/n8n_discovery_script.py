#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para descobrir automaticamente os IDs dos seus workflows n8n
"""

import os
import requests
import json
import sys
from typing import List, Dict
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Fix encoding issues on Windows
if sys.platform == "win32":
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

class N8NDiscovery:
    """Descobre informações dos workflows n8n automaticamente"""
    
    def __init__(self):
        self.api_url = os.getenv('N8N_API_URL', 'https://n8n.synapseautointeligente.com.br/api/v1')
        self.api_key = os.getenv('N8N_API_KEY')
        
        if not self.api_key:
            print("❌ N8N_API_KEY não encontrada!")
            print("Configure no arquivo .env ou variável de ambiente")
            exit(1)
        
        self.headers = {
            'X-N8N-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def test_connection(self) -> bool:
        """Testa conexão com n8n"""
        try:
            response = requests.get(f"{self.api_url}/workflows", headers=self.headers, timeout=10)
            
            if response.status_code == 200:
                print("✅ Conexão com n8n OK!")
                return True
            elif response.status_code == 401:
                print("❌ API Key inválida!")
                return False
            else:
                print(f"❌ Erro de conexão: {response.status_code}")
                return False
                
        except requests.RequestException as e:
            print(f"❌ Erro de rede: {e}")
            return False
    
    def discover_workflows(self) -> List[Dict]:
        """Descobre todos os workflows"""
        try:
            response = requests.get(f"{self.api_url}/workflows", headers=self.headers)
            
            if response.status_code == 200:
                response_data = response.json()
                # Handle different response formats
                if isinstance(response_data, dict) and 'data' in response_data:
                    workflows = response_data['data']
                else:
                    workflows = response_data
                    
                print(f"📊 Encontrados {len(workflows)} workflows:")
                
                discovered = []
                for i, workflow in enumerate(workflows, 1):
                    workflow_info = {
                        'id': workflow['id'],
                        'name': workflow['name'],
                        'active': workflow.get('active', False),
                        'created': workflow.get('createdAt', 'N/A'),
                        'updated': workflow.get('updatedAt', 'N/A')
                    }
                    
                    print(f"\n{i}. 🔧 {workflow_info['name']}")
                    print(f"   ID: {workflow_info['id']}")
                    print(f"   Status: {'🟢 Ativo' if workflow_info['active'] else '🔴 Inativo'}")
                    print(f"   Criado: {workflow_info['created'][:10]}")
                    
                    discovered.append(workflow_info)
                
                return discovered
            else:
                print(f"❌ Erro ao buscar workflows: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Erro: {e}")
            return []
    
    def analyze_workflow_details(self, workflow_id: str) -> Dict:
        """Analisa detalhes de um workflow específico"""
        try:
            response = requests.get(f"{self.api_url}/workflows/{workflow_id}", headers=self.headers)
            
            if response.status_code == 200:
                workflow = response.json()
                
                # Encontrar nodes com prompts
                prompt_nodes = []
                total_nodes = len(workflow.get('nodes', []))
                
                for node in workflow.get('nodes', []):
                    node_type = node.get('type', '')
                    parameters = node.get('parameters', {})
                    
                    # Verificar se é um node de IA
                    if any(ai_type in node_type.lower() for ai_type in [
                        'anthropic', 'claude', 'openai', 'gpt', 'llm'
                    ]):
                        prompt_content = self.extract_prompt_preview(parameters)
                        prompt_nodes.append({
                            'node_name': node.get('name', 'Unnamed'),
                            'node_type': node_type,
                            'prompt_preview': prompt_content[:100] + '...' if len(prompt_content) > 100 else prompt_content
                        })
                
                return {
                    'id': workflow_id,
                    'name': workflow['name'],
                    'total_nodes': total_nodes,
                    'prompt_nodes': prompt_nodes,
                    'has_ai_nodes': len(prompt_nodes) > 0
                }
            else:
                return {'error': f"Erro {response.status_code}"}
                
        except Exception as e:
            return {'error': str(e)}
    
    def extract_prompt_preview(self, parameters: Dict) -> str:
        """Extrai preview do prompt"""
        prompt_fields = ['prompt', 'systemMessage', 'message', 'input', 'text']
        
        for field in prompt_fields:
            if field in parameters:
                return str(parameters[field])
        
        return "Prompt não encontrado"
    
    def generate_config_files(self, workflows: List[Dict]):
        """Gera arquivos de configuração automaticamente"""
        
        # Filtrar workflows que têm nodes de IA
        ai_workflows = []
        
        print("\n🤖 Analisando workflows para IA...")
        for workflow in workflows:
            details = self.analyze_workflow_details(workflow['id'])
            
            if details.get('has_ai_nodes'):
                ai_workflows.append(details)
                print(f"✅ {details['name']} - {len(details['prompt_nodes'])} nodes de IA")
            else:
                print(f"⏭️ {workflow['name']} - sem nodes de IA")
        
        if not ai_workflows:
            print("❌ Nenhum workflow com IA encontrado!")
            return
        
        print(f"\n📝 Gerando configurações para {len(ai_workflows)} workflows...")
        
        # Gerar .env atualizado
        self.generate_env_file(ai_workflows)
        
        # Gerar estrutura GitHub
        self.generate_github_structure(ai_workflows)
        
        print("✅ Configurações geradas!")
    
    def generate_env_file(self, workflows: List[Dict]):
        """Gera arquivo .env com os IDs descobertos"""
        
        env_content = f"""# ================================
# CONFIGURAÇÃO CLAUDE AUTO-OPTIMIZER
# Gerado automaticamente em {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# ================================

# === N8N CONFIGURATION ===
N8N_API_URL={self.api_url}
N8N_API_KEY={self.api_key}

# === GITHUB CONFIGURATION ===
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx     # ← CONFIGURE SEU GITHUB TOKEN
GITHUB_OWNER=seu-usuario                  # ← CONFIGURE SEU USERNAME
GITHUB_REPO=workflow-configs              # ← NOME DO REPOSITÓRIO

# === CLAUDE CONFIGURATION ===
CLAUDE_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxx # ← CONFIGURE SUA CHAVE CLAUDE

# === WORKFLOW MAPPING (Descoberto automaticamente) ===
"""
        
        for workflow in workflows:
            safe_name = workflow['name'].upper().replace(' ', '_').replace('-', '_')
            safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '_')
            env_content += f"WORKFLOW_{safe_name}_ID={workflow['id']}  # {workflow['name']}\n"
        
        with open('.env.generated', 'w', encoding='utf-8') as f:
            f.write(env_content)
        
        print("📄 Arquivo .env.generated criado!")
        print("   Renomeie para .env e configure os tokens necessários")
    
    def generate_github_structure(self, workflows: List[Dict]):
        """Gera estrutura de configuração para GitHub"""
        
        github_structure = {
            'workflows_detected': [],
            'recommended_structure': {}
        }
        
        for workflow in workflows:
            safe_name = workflow['name'].lower().replace(' ', '-').replace('_', '-')
            safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '-')
            
            workflow_config = {
                'workflow_id': f"wf_{safe_name}_001",
                'name': workflow['name'],
                'version': '1.0.0',
                'n8n_workflow_id': workflow['id'],
                'status': 'active',
                'auto_optimization': {
                    'enabled': True,
                    'frequency': 'daily',
                    'performance_threshold': 0.85
                },
                'current_performance': {
                    'success_rate': 0.0,
                    'avg_response_time': 0.0,
                    'total_tests': 0,
                    'last_updated': None
                },
                'settings': {
                    'max_tokens': 1000,
                    'temperature': 0.7,
                    'timeout': 30
                }
            }
            
            github_structure['workflows_detected'].append(safe_name)
            github_structure['recommended_structure'][safe_name] = workflow_config
        
        with open('github_structure.json', 'w', encoding='utf-8') as f:
            json.dump(github_structure, f, indent=2)
        
        print("📁 Arquivo github_structure.json criado!")
        print("   Use este para criar a estrutura no GitHub")
    
    def interactive_setup(self):
        """Setup interativo completo"""
        print("🚀 DESCOBERTA AUTOMÁTICA DE WORKFLOWS N8N")
        print("=" * 50)
        
        # Testar conexão
        if not self.test_connection():
            return
        
        # Descobrir workflows
        workflows = self.discover_workflows()
        
        if not workflows:
            print("❌ Nenhum workflow encontrado!")
            return
        
        # Analisar e gerar configurações
        self.generate_config_files(workflows)
        
        print("\n🎯 PRÓXIMOS PASSOS:")
        print("1. Renomeie .env.generated para .env")
        print("2. Configure os tokens no arquivo .env")
        print("3. Use github_structure.json para criar repo")
        print("4. Execute: python claude_code_mcp_integration.py optimize")

def main():
    """Função principal"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Descobrir workflows n8n')
    parser.add_argument('--interactive', '-i', action='store_true', 
                       help='Modo interativo completo')
    parser.add_argument('--list', '-l', action='store_true',
                       help='Apenas listar workflows')
    parser.add_argument('--analyze', '-a', 
                       help='Analisar workflow específico (ID)')
    
    args = parser.parse_args()
    
    discovery = N8NDiscovery()
    
    if args.interactive:
        discovery.interactive_setup()
    elif args.list:
        discovery.discover_workflows()
    elif args.analyze:
        details = discovery.analyze_workflow_details(args.analyze)
        print(json.dumps(details, indent=2))
    else:
        print("Use --interactive para setup completo")
        print("Use --list para listar workflows")
        print("Use --analyze ID para analisar workflow específico")

if __name__ == "__main__":
    main()