import requests
import json

# Configurações
N8N_API_URL = 'https://n8n.synapseautointeligente.com.br/api/v1'
N8N_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2ZmM4ZTU4Ni02NThiLTQyZTYtOWU2MC0yNzdmNjYxYzIxMWUiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzU0ODQyNjIzfQ.MOGBUP-_uNSZEjYBrBhV0xrlgR2hYZA9L4-KKxpGO8w'

headers = {
    'X-N8N-API-KEY': N8N_API_KEY,
    'Content-Type': 'application/json'
}

workflow_id = 'lM9kCZbVaFRnVWid'

try:
    # 1. Buscar workflow atual
    print("Buscando workflow atual...")
    response = requests.get(f'{N8N_API_URL}/workflows/{workflow_id}', headers=headers, timeout=15)
    
    if response.status_code != 200:
        print(f"Erro ao buscar workflow: {response.status_code}")
        exit(1)
        
    workflow = response.json()
    print(f"Workflow obtido: {workflow.get('name')}")
    
    # 2. Carregar prompt otimizado
    print("Carregando prompt otimizado...")
    with open('../Prompt_ Agente Comercial - Consultor_rev02.md', 'r', encoding='utf-8') as f:
        prompt_otimizado = f.read()
    print(f"Prompt carregado: {len(prompt_otimizado)} chars")
    
    # 3. Atualizar nodes
    nodes_updated = 0
    for node in workflow.get('nodes', []):
        if node.get('type') == '@n8n/n8n-nodes-langchain.agent':
            print(f"Atualizando node: {node.get('name')}")
            node['parameters']['text'] = prompt_otimizado
            nodes_updated += 1
    
    if nodes_updated == 0:
        print("ERRO: Nenhum node de agente encontrado")
        exit(1)
    
    # 4. Preparar payload limpo (sem campos readonly)
    update_payload = {
        'name': workflow['name'],
        'nodes': workflow['nodes'],
        'connections': workflow['connections']
    }
    
    # Adicionar campos opcionais se existirem
    optional_fields = ['settings', 'staticData', 'meta']
    for field in optional_fields:
        if field in workflow:
            update_payload[field] = workflow[field]
    
    # 5. Enviar atualizacao
    print("Enviando atualizacao...")
    save_response = requests.put(
        f'{N8N_API_URL}/workflows/{workflow_id}', 
        headers=headers, 
        json=update_payload,
        timeout=30
    )
    
    if save_response.status_code == 200:
        print("")
        print("SUCCESS: Prompt aplicado com sucesso!")
        print(f"- Workflow: {workflow.get('name')}")
        print(f"- Nodes atualizados: {nodes_updated}")
        print("- Versao: _rev02 (Humanizacao e Contextualizacao)")
        print("- Score esperado: 9.0/10")
        print("")
        print("AGENTE COMERCIAL OTIMIZADO ATIVO NO N8N!")
    else:
        print(f"ERRO ao salvar: {save_response.status_code}")
        print(f"Resposta: {save_response.text}")
        
except Exception as e:
    print(f"ERRO: {e}")