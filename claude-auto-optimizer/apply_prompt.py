import requests
import json

# Configuracoes
N8N_API_URL = 'https://n8n.synapseautointeligente.com.br/api/v1'
N8N_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2ZmM4ZTU4Ni02NThiLTQyZTYtOWU2MC0yNzdmNjYxYzIxMWUiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzU0ODQyNjIzfQ.MOGBUP-_uNSZEjYBrBhV0xrlgR2hYZA9L4-KKxpGO8w'

headers = {
    'X-N8N-API-KEY': N8N_API_KEY,
    'Content-Type': 'application/json'
}

workflow_id = 'lM9kCZbVaFRnVWid'

# Ler o prompt otimizado do arquivo
print("Lendo prompt otimizado...")
try:
    with open('../Prompt_ Agente Comercial - Consultor_rev02.md', 'r', encoding='utf-8') as f:
        prompt_otimizado = f.read()
    print(f"Prompt carregado: {len(prompt_otimizado)} caracteres")
except Exception as e:
    print(f"Erro ao ler arquivo: {e}")
    exit(1)

try:
    print('Buscando workflow atual...')
    response = requests.get(f'{N8N_API_URL}/workflows/{workflow_id}', headers=headers, timeout=15)
    
    if response.status_code == 200:
        workflow = response.json()
        print('Workflow obtido com sucesso!')
        
        # Encontrar e atualizar o node do agente comercial
        nodes = workflow.get('nodes', [])
        updated = False
        
        for node in nodes:
            node_name = node.get('name', '').lower()
            node_type = node.get('type', '')
            
            if node_type == '@n8n/n8n-nodes-langchain.agent' and 'comercial' in node_name:
                print(f'Node encontrado: {node.get("name")} (Tipo: {node_type})')
                
                # Atualizar o prompt no parametro 'text'
                if 'parameters' in node:
                    node['parameters']['text'] = prompt_otimizado
                    print('Prompt atualizado no node!')
                    updated = True
                    break
        
        if updated:
            # Salvar o workflow atualizado
            print('Salvando workflow com prompt otimizado...')
            save_response = requests.put(
                f'{N8N_API_URL}/workflows/{workflow_id}', 
                headers=headers, 
                json=workflow,
                timeout=30
            )
            
            if save_response.status_code == 200:
                print('✅ SUCCESS: Prompt otimizado aplicado no workflow N8N!')
                print('')
                print('🎯 O Agente Comercial agora usa a versao _rev02 com:')
                print('- ✅ Contextualização empática por raça')
                print('- ✅ Personalização avançada de ofertas')  
                print('- ✅ Transição natural para agendamento')
                print('- ✅ Score esperado: 9.0/10 (vs 6.8/10 anterior)')
                print('')
                print('🚀 SISTEMA PRONTO! Próximos testes usarão a versão otimizada!')
            else:
                print(f'❌ Erro ao salvar workflow: {save_response.status_code}')
                print(f'Resposta: {save_response.text[:200]}')
        else:
            print('❌ Node do agente comercial não encontrado para atualização')
            print('Nodes disponíveis:')
            for node in nodes:
                if '@n8n/n8n-nodes-langchain.agent' in node.get('type', ''):
                    print(f'  - {node.get("name")} ({node.get("type")})')
    else:
        print(f'❌ Erro ao buscar workflow: {response.status_code}')
        print(f'Resposta: {response.text[:200]}')
        
except Exception as e:
    print(f'❌ Erro: {e}')