# Guia de Testes para Agentes Bable Pet

## Visão Geral
Este documento fornece instruções para testar o sistema multiagente Bable Pet usando requisições CURL simuladas.

## Endpoint de Teste
**Webhook URL**: `https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5`

## Estrutura do Payload Correto

### Formato Base para ChatWoot/Evolution API
```json
{
  "account": {
    "id": 2,
    "name": "Synapse Automações Inteligentes"
  },
  "additional_attributes": {},
  "content_attributes": {},
  "content_type": "text",
  "content": "[MENSAGEM_DO_CLIENTE]",
  "conversation": {
    "additional_attributes": {},
    "can_reply": true,
    "channel": "Channel::Api",
    "contact_inbox": {
      "id": 6,
      "contact_id": 2,
      "inbox_id": 4,
      "source_id": "ad58e367-35ef-4353-bc4c-4bb5c6a0a360",
      "created_at": "2025-07-16T16:30:01.544Z",
      "updated_at": "2025-07-16T16:30:01.544Z",
      "hmac_verified": false,
      "pubsub_token": "3HKrTnRYh3ueCSYsG7EqLF2v"
    },
    "id": 4,
    "inbox_id": 4,
    "messages": [
      {
        "id": 429,
        "content": "[MENSAGEM_DO_CLIENTE]",
        "account_id": 2,
        "inbox_id": 4,
        "conversation_id": 4,
        "message_type": 0,
        "created_at": 1753659002,
        "updated_at": "2025-07-27T23:30:02.693Z",
        "private": false,
        "status": "sent",
        "source_id": "WAID:BA51D54DD5AD1660E451B0114E369124",
        "content_type": "text",
        "content_attributes": {},
        "sender_type": "Contact",
        "sender_id": 2,
        "external_source_ids": {},
        "additional_attributes": {},
        "processed_message_content": "[MENSAGEM_DO_CLIENTE]",
        "sentiment": {},
        "conversation": {
          "assignee_id": 2,
          "unread_count": 2,
          "last_activity_at": 1753659002,
          "contact_inbox": {
            "source_id": "ad58e367-35ef-4353-bc4c-4bb5c6a0a360"
          }
        },
        "sender": {
          "additional_attributes": {},
          "custom_attributes": {},
          "email": null,
          "id": 2,
          "identifier": "5516993448117@s.whatsapp.net",
          "name": "Gabriel Batista",
          "phone_number": "+5516993448117",
          "thumbnail": "https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg",
          "blocked": false,
          "type": "contact"
        }
      }
    ],
    "labels": [],
    "meta": {
      "sender": {
        "additional_attributes": {},
        "custom_attributes": {},
        "email": null,
        "id": 2,
        "identifier": "5516993448117@s.whatsapp.net",
        "name": "Gabriel Batista",
        "phone_number": "+5516993448117",
        "thumbnail": "https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg",
        "blocked": false,
        "type": "contact"
      },
      "assignee": {
        "id": 2,
        "name": "Gabriel Teodoro Batista",
        "available_name": "Gabriel Teodoro Batista",
        "avatar_url": "",
        "type": "user",
        "availability_status": null,
        "thumbnail": ""
      },
      "team": null,
      "hmac_verified": false
    },
    "status": "open",
    "custom_attributes": {},
    "snoozed_until": null,
    "unread_count": 2,
    "first_reply_created_at": "2025-07-16T16:38:07.618Z",
    "priority": null,
    "waiting_since": 1753659002,
    "agent_last_seen_at": 1752717500,
    "contact_last_seen_at": 0,
    "last_activity_at": 1753659002,
    "timestamp": 1753659002,
    "created_at": 1752683401,
    "updated_at": 1753659002.722044
  },
  "created_at": "2025-07-27T23:30:02.693Z",
  "id": 429,
  "inbox": {
    "id": 4,
    "name": "Recepção Inteligente (Bable Pet)"
  },
  "message_type": "incoming",
  "private": false,
  "sender": {
    "account": {
      "id": 2,
      "name": "Synapse Automações Inteligentes"
    },
    "additional_attributes": {},
    "avatar": "https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg",
    "custom_attributes": {},
    "email": null,
    "id": 2,
    "identifier": "5516993448117@s.whatsapp.net",
    "name": "Gabriel Batista",
    "phone_number": "+5516993448117",
    "thumbnail": "https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg",
    "blocked": false
  },
  "source_id": "WAID:BA51D54DD5AD1660E451B0114E369124",
  "event": "message_created"
}
```

## Comandos CURL para Testes

### Headers Obrigatórios
```bash
-H "Content-Type: application/json"
-H "Accept: application/json"
-H "User-Agent: rest-client/2.1.0 (linux-musl aarch64) ruby/3.4.4p34"
-H "Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3"
```

### 1. Teste de Saudação Simples
```bash
curl -X POST "https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "User-Agent: rest-client/2.1.0 (linux-musl aarch64) ruby/3.4.4p34" \
-H "Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3" \
-d '{"account":{"id":2,"name":"Synapse Automações Inteligentes"},"additional_attributes":{},"content_attributes":{},"content_type":"text","content":"Oi, tudo bem?","conversation":{"additional_attributes":{},"can_reply":true,"channel":"Channel::Api","contact_inbox":{"id":6,"contact_id":2,"inbox_id":4,"source_id":"ad58e367-35ef-4353-bc4c-4bb5c6a0a360","created_at":"2025-07-16T16:30:01.544Z","updated_at":"2025-07-16T16:30:01.544Z","hmac_verified":false,"pubsub_token":"3HKrTnRYh3ueCSYsG7EqLF2v"},"id":4,"inbox_id":4,"messages":[{"id":429,"content":"Oi, tudo bem?","account_id":2,"inbox_id":4,"conversation_id":4,"message_type":0,"created_at":1753659002,"updated_at":"2025-07-27T23:30:02.693Z","private":false,"status":"sent","source_id":"WAID:BA51D54DD5AD1660E451B0114E369124","content_type":"text","content_attributes":{},"sender_type":"Contact","sender_id":2,"external_source_ids":{},"additional_attributes":{},"processed_message_content":"Oi, tudo bem?","sentiment":{},"conversation":{"assignee_id":2,"unread_count":2,"last_activity_at":1753659002,"contact_inbox":{"source_id":"ad58e367-35ef-4353-bc4c-4bb5c6a0a360"}},"sender":{"additional_attributes":{},"custom_attributes":{},"email":null,"id":2,"identifier":"5516993448117@s.whatsapp.net","name":"Gabriel Batista","phone_number":"+5516993448117","thumbnail":"https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg","blocked":false,"type":"contact"}}],"labels":[],"meta":{"sender":{"additional_attributes":{},"custom_attributes":{},"email":null,"id":2,"identifier":"5516993448117@s.whatsapp.net","name":"Gabriel Batista","phone_number":"+5516993448117","thumbnail":"https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg","blocked":false,"type":"contact"},"assignee":{"id":2,"name":"Gabriel Teodoro Batista","available_name":"Gabriel Teodoro Batista","avatar_url":"","type":"user","availability_status":null,"thumbnail":""},"team":null,"hmac_verified":false},"status":"open","custom_attributes":{},"snoozed_until":null,"unread_count":2,"first_reply_created_at":"2025-07-16T16:38:07.618Z","priority":null,"waiting_since":1753659002,"agent_last_seen_at":1752717500,"contact_last_seen_at":0,"last_activity_at":1753659002,"timestamp":1753659002,"created_at":1752683401,"updated_at":1753659002.722044},"created_at":"2025-07-27T23:30:02.693Z","id":429,"inbox":{"id":4,"name":"Recepção Inteligente (Bable Pet)"},"message_type":"incoming","private":false,"sender":{"account":{"id":2,"name":"Synapse Automações Inteligentes"},"additional_attributes":{},"avatar":"https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg","custom_attributes":{},"email":null,"id":2,"identifier":"5516993448117@s.whatsapp.net","name":"Gabriel Batista","phone_number":"+5516993448117","thumbnail":"https://chatwoot.synapseautointeligente.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBHZz09IiwiZXhwIjpudWxsLCJwdXIiOiJibG9iX2lkIn19--faf81b188b33df2440a782296716159b06a1b4c2/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdCem9MWm05eWJXRjBTU0lJYW5CbkJqb0dSVlE2RTNKbGMybDZaVjkwYjE5bWFXeHNXd2RwQWZvdyIsImV4cCI6bnVsbCwicHVyIjoidmFyaWF0aW9uIn19--67ea28d24ee095fb49ecb7d8fc0a316ea10f6266/482877372_9548019198609585_6928739706476523512_n.jpg","blocked":false},"source_id":"WAID:BA51D54DD5AD1660E451B0114E369124","event":"message_created"}'
```

### 2. Teste de Agendamento
```bash
curl -X POST "https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "User-Agent: rest-client/2.1.0 (linux-musl aarch64) ruby/3.4.4p34" \
-H "Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3" \
-d '[SUBSTITUA content E processed_message_content por: "Gostaria de agendar um banho para meu cachorro"]'
```

### 3. Teste Comercial (Preços)
```bash
curl -X POST "https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "User-Agent: rest-client/2.1.0 (linux-musl aarch64) ruby/3.4.4p34" \
-H "Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3" \
-d '[SUBSTITUA content E processed_message_content por: "Quanto custa o banho e tosa?"]'
```

### 4. Teste de Franquia
```bash
curl -X POST "https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5" \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-H "User-Agent: rest-client/2.1.0 (linux-musl aarch64) ruby/3.4.4p34" \
-H "Accept-Encoding: gzip;q=1.0,deflate;q=0.6,identity;q=0.3" \
-d '[SUBSTITUA content E processed_message_content por: "Tenho interesse em abrir uma franquia"]'
```

## Campos Importantes para Modificar em Cada Teste

### Obrigatórios
- **content**: Mensagem principal do cliente
- **processed_message_content**: Mesmo conteúdo da mensagem
- **id**: ID único da mensagem (incremente: 429, 430, 431...)
- **created_at/updated_at**: Timestamps atuais

### Opcionais para Variações
- **name**: Nome do cliente testador
- **phone_number**: Número do cliente
- **identifier**: WhatsApp ID do cliente

## Monitoramento

### Respostas Esperadas
- **Sucesso**: `{"message":"Workflow was started"}`
- **Erro**: Qualquer outra resposta ou timeout

### Logs N8N
- Acompanhe a execução em: `/debug/[execution_id]`
- Verifique se passa pelo Anti-Loop
- Monitore quais agentes são acionados

## Desabilitando Saída WhatsApp
Para testes sem enviar mensagens reais:
1. Desabilite o nó "Response WhatsApp" no workflow de integração
2. OU modifique a condição final para não enviar

## Troubleshooting

### Problema: Workflow não inicia
- Verifique headers HTTP obrigatórios
- Confirme estrutura JSON completa
- Teste payload menor primeiro

### Problema: Para no Anti-Loop
- Confirme `sender_type: "Contact"`
- Verifique estrutura `body.conversation.messages[0]`

### Problema: Timeout no Redis
- Verifique se há dados de timeout conflitantes
- Limpe cache Redis se necessário

## Metodologia de Análise via GitHub Debug Logs

### Acesso aos Logs
**Repositório**: `https://github.com/gabrielteoodoro/bable-pet-debug`
**Diretório**: `debug_logs/`
**Formato**: `debug_YYYY-MM-DD_HH-mm-ss_X.json`

### Estrutura dos Logs de Debug
Cada log contém:
```json
{
  "timestamp": "2025-08-09T16:22:17.418Z",
  "execution_id": "abc123",
  "workflow_name": "Nome do Workflow",
  "customer_input": {
    "message": "Mensagem do cliente",
    "customer_name": "Nome",
    "customer_id": "ID único"
  },
  "agent_data": {
    "feedback_[agente]": {
      "script_id_sugerido": "ID_SCRIPT",
      "script_sugerido": "Texto da resposta",
      "analise": "Análise do agente",
      "status_operacao": "Status atual"
    }
  },
  "agent_type": "ORQUESTRADOR|SAUDACAO|AGENDAMENTO|COMERCIAL|FRANQUIA|FAQ|MESTRE",
  "ready_for_claude_analysis": true
}
```

### Framework de Avaliação de Integração

#### 1. Análise de Fluxo de Agentes
**Verificações:**
- ✅ **Orquestrador**: Identificou intenções corretas?
- ✅ **Saudação**: Delegou para agente apropriado?
- ✅ **Especialista**: Executou tarefa conforme escopo?
- ✅ **Mestre**: Montou resposta final adequada?

**Métricas de Sucesso:**
- Taxa de identificação correta de intenções: >90%
- Tempo de resposta por agente: <2s
- Taxa de escalação desnecessária: <5%
- Consistência de dados entre agentes: 100%

**Métricas de Qualidade Principal (Integradas com Claude Auto-Optimizer):**
- **Human-like Interaction Score (0-10):** ≥8/10 - Respostas naturais e empáticas
- **Contextual Relevance Score (0-10):** ≥8/10 - Resposta precisa ao contexto  
- **Specialist Expertise Level (0-10):** ≥8/10 - Conhecimento especializado demonstrado
- **Functional Logic Integrity (0-10):** ≥8/10 - Regras de negócio seguidas corretamente

### 📈 **Métricas A/B Testing (NOVAS):**
- **Performance Delta**: Comparação versão atual vs. otimizada
- **Success Rate**: Taxa de sucesso antes/depois da otimização
- **Response Time**: Tempo de resposta médio por agente
- **Token Efficiency**: Uso de tokens otimizado
- **Error Rate**: Taxa de erro por tipo de cenário

#### 2. Pontos Críticos de Integração
**A. Handoff Orquestrador → Saudação**
```json
"intencoes": ["AGENDAMENTO", "COMERCIAL"]
```
- Verificar se ambas intenções são processadas
- Confirmar priorização correta

**B. Delegação Saudação → Especialistas**
```json
"dados_cliente": {
  "nome": "string",
  "status": "NOVO|CADASTRADO",
  "telefone": "string"
}
```
- Dados do cliente são propagados?
- Status NOVO/CADASTRADO influencia script?

**C. Resposta Especialista → Mestre**
```json
"script_sugerido": "Texto com [placeholders]",
"variaveis": {
  "[Nome]": "João",
  "[Servico]": "Banho e Tosa"
}
```
- Placeholders são substituídos corretamente?
- Formatação final está adequada?

#### 3. Padrões de Análise por Tipo de Agente

**ORQUESTRADOR:**
- **Sucesso**: `intencoes` array não vazio, JSON válido
- **Falha**: Intenção "INDEFINIDO" para mensagens claras
- **Red Flag**: Não usa ferramenta `think1`
- **Qualidade**: Score ≥8/10 em análise contextual e identificação de múltiplas intenções

**SAUDAÇÃO:**
- **Sucesso**: `script_sugerido` ou delegação clara
- **Falha**: Não busca dados do cliente quando necessário
- **Red Flag**: Responde diretamente sem verificar store status

**AGENDAMENTO:**
- **Sucesso**: Mantém "Ficha de Atendimento" consistente
- **Falha**: Cria evento no calendário sem usar `criaAtendimento`
- **Red Flag**: Pula etapas obrigatórias do fluxo

**COMERCIAL:**
- **Sucesso**: Só ativa com keywords explícitas de preço
- **Falha**: Ativa para mensagens não comerciais
- **Red Flag**: Não oferece assinatura para não membros

**FRANQUIA:**
- **Sucesso**: Identifica interesse em franquia corretamente
- **Falha**: Responde perguntas fora do escopo
- **Red Flag**: Não faz handoff para especialista humano

**FAQ:**
- **Sucesso**: Status "AGUARDANDO" quando não é sua vez
- **Falha**: Responde perguntas específicas de outros agentes
- **Red Flag**: Ativa para mensagens de saudação

#### 4. Roteiro de Análise de Logs

**Passo 1: Análise Individual**
1. Baixar logs mais recentes do GitHub
2. Verificar `agent_type` vs conteúdo da mensagem
3. Validar estrutura JSON do `feedback_[agente]`
4. Confirmar se `analise` reflete comportamento correto

**Passo 2: Análise de Sequência**
1. Mapear executions_id relacionados
2. Verificar ordem de ativação dos agentes
3. Rastrear propagação de dados entre agentes
4. Identificar pontos de falha na cadeia

**Passo 3: Identificação de Padrões**
1. Agrupar por `agent_type` e `intencoes`
2. Calcular taxa de sucesso por cenário
3. Identificar mensagens que causam confusão
4. Mapear casos edge que precisam de tratamento

**Passo 4: Recomendações de Ajuste**
1. Listar prompts que precisam refinamento
2. Identificar lógicas de trigger incorretas
3. Sugerir melhorias na delegação entre agentes
4. Propor novos cenários de teste
5. **Controle de Qualidade:** Se score <8/10, rollback imediato para versão funcional
6. **Proposições de Conteúdo:** Identificar gaps nas bases de dados Excel
7. **Otimização de Scripts:** Sugerir novos scripts para cenários não cobertos

**Passo 5: Análise e Proposição de Bancos de Dados**
1. **Identificar Gaps Críticos:** Dados ausentes que bloqueiam agentes
2. **Propor Estruturas Novas:** Templates CSV para dados faltantes
3. **Unificação de Bases:** Eliminar fragmentação de dados de clientes
4. **Validação de Integridade:** Verificar consistência entre tabelas relacionadas
5. **Performance de Consultas:** Otimizar estrutura para consultas <2s

### Comandos de Análise via GitHub

#### Listar Logs Recentes
```bash
curl -H "Accept: application/vnd.github+json" \
     "https://api.github.com/repos/gabrielteoodoro/bable-pet-debug/contents/debug_logs"
```

#### Baixar Log Específico
```bash
curl -H "Accept: application/vnd.github+json" \
     "https://api.github.com/repos/gabrielteoodoro/bable-pet-debug/contents/debug_logs/[filename]"
```

#### Análise Automatizada
```bash
# Contar logs por tipo de agente nas últimas 24h
grep -r "agent_type" debug_logs/ | grep $(date +%Y-%m-%d) | sort | uniq -c

# Buscar falhas específicas
grep -r "INDEFINIDO\|ERROR\|null" debug_logs/ | tail -10

# Verificar taxa de sucesso de intenções
grep -r "intencoes" debug_logs/ | grep -v "\[\]" | wc -l

# Analisar falhas de consulta de dados
grep -r "racas_e_grupos\|precos_e_servicos\|CONSULTAR" debug_logs/ | wc -l

# Identificar dados de clientes inconsistentes
grep -r "dados_cliente.*null\|email.*null" debug_logs/ | wc -l
```

### Protocolo de Testes para Bancos de Dados

#### Teste 1: Validação de Estrutura
```bash
# Verificar integridade dos CSVs
curl -X POST "[webhook_url]" -d '{"content": "Quanto custa banho para golden retriever?"}'
# Verificar se racas_e_grupos() retorna grupo correto
# Verificar se precos_e_servicos() encontra preço
```

#### Teste 2: Gaps Críticos  
```bash
# Testar serviços "CONSULTAR"
curl -X POST "[webhook_url]" -d '{"content": "Quanto custa desembolo para poodle?"}'
# Deve falhar → propor preços definidos

# Testar raças não mapeadas
curl -X POST "[webhook_url]" -d '{"content": "Quanto custa banho para vira-lata?"}'
# Deve falhar → propor mapeamento raça→grupo
```

#### Teste 3: Fragmentação de Clientes
```bash
# Cliente que está em base Assinantes mas não em Clientes
curl -X POST "[webhook_url]" -d '{"content": "Oi, sou Maria Elisete"}'
# Verificar se buscarDadosCliente() encontra todos os dados
```

### Protocolo de Testes com Cenários Humanos

#### Biblioteca de Cenários por Complexidade

**BAIXA - Fluxos Simples**
```bash
# Cenário: Cliente novo quer agendar banho
curl -X POST "[webhook_url]" -d '{"content": "Oi, queria agendar um banho pro meu cachorro"}'
# Expectativa: Saudação → Agendamento → Coleta dados

# Cenário: Cliente quer saber preço
curl -X POST "[webhook_url]" -d '{"content": "Quanto custa banho para poodle pequeno?"}'
# Expectativa: Saudação → Comercial → Consulta preço
```

**MÉDIA - Múltiplas Intenções**
```bash
# Cenário: Reagendamento + preço
curl -X POST "[webhook_url]" -d '{"content": "Oi Maria! Preciso remarcar o banho da Luna e saber preço da tosa"}'
# Expectativa: Saudação → Agendamento (remarcar) + Comercial (preço)

# Cenário: Cliente cadastrado com dúvida
curl -X POST "[webhook_url]" -d '{"content": "Olá, sou a Ana. Meu poodle precisa de vacina para ir aí?"}'
# Expectativa: Saudação → FAQ (vacina)
```

**ALTA - Edge Cases Complexos**
```bash
# Cenário: Cliente frustrado
curl -X POST "[webhook_url]" -d '{"content": "JÁ FALEI 3 VEZES QUE QUERO CANCELAR O BANHO! VOCÊS NÃO ESCUTAM!"}'
# Expectativa: Saudação → Agendamento (cancelar) + Tratamento empático

# Cenário: Múltiplas questões
curl -X POST "[webhook_url]" -d '{"content": "Oi! Meu golden teve alergia no último banho. Vocês ressarcem? Ah, e quero saber sobre franquia."}'
# Expectativa: FAQ (reclamação) + Franquia + possível Agendamento
```

**EXTREMA - Situações Desafiadoras**  
```bash
# Cenário: Cliente indeciso com múltiplos pets
curl -X POST "[webhook_url]" -d '{"content": "Tenho 3 cachorros: poodle, golden e vira-lata. Não sei se faço banho completo ou simples. Quanto sai tudo? E se eu virar assinante?"}'
# Expectativa: Comercial (múltiplos cálculos) + Oferta clube

# Cenário: Emergência veterinária  
curl -X POST "[webhook_url]" -d '{"content": "Socorro! Meu cachorro está sangrando muito depois da tosa! O que faço???"}'
# Expectativa: FAQ/Indefinido → Script emergência + Handoff veterinário
```

#### Validação de Naturalidade Humana

**Critérios de Avaliação (1-10):**
- **Naturalidade**: Resposta parece de pessoa real?
- **Empatia**: Demonstra compreensão do cliente?  
- **Clareza**: Linguagem clara e objetiva?
- **Completude**: Responde completamente à pergunta?
- **Proatividade**: Oferece informações úteis adicionais?

**Exemplos de Respostas:**

❌ **Robótica (Score 3/10):**
```
"Processando solicitação. Identificada intenção: AGENDAMENTO. Necessário coletar: nome_cliente, pet_raca, servico_desejado."
```

✅ **Humana (Score 9/10):**
```
"Oi! Que bom que você entrou em contato! 😊 Para agendar o banho do seu amigo de quatro patas, preciso saber seu nome e a raça do pet. Pode me contar?"
```

## Conclusão
Use este guia para testar sistematicamente cada agente e cenário do sistema Bable Pet. O monitoramento via GitHub Debug Logs permite análise detalhada do comportamento dos agentes e identificação precisa de pontos de melhoria. Sempre desabilite a saída do WhatsApp durante os testes para evitar spam aos usuários reais.