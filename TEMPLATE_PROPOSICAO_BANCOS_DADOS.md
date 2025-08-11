# Template: Proposição de Modificações em Bancos de Dados - Sistema Integrado

> **🔗 INTEGRAÇÃO COMPLETA**: Template integrado com Claude Auto-Optimizer + Métricas + Testes A/B

## 📋 IDENTIFICAÇÃO DA PROPOSTA

**Data:** [DD/MM/YYYY]  
**Agente Propositor:** Agent [1-4] ([Architect|Builder|Validator|Writer])  
**Workflow n8n Afetado:** [ID do workflow - ex: DUOuKlAbIvwd9c3v]  
**Prioridade:** [CRÍTICA|ALTA|MÉDIA|BAIXA]  
**Tipo de Modificação:** [NOVA_TABELA|ATUALIZAÇÃO|UNIFICAÇÃO|CORREÇÃO]  
**Impacto Claude Auto-Optimizer:** [Bloqueia otimização|Reduz performance|Baixo impacto]

---

## 🎯 PROBLEMA IDENTIFICADO

### Descrição do Gap/Problema
[Descrever claramente o problema atual nos bancos de dados]

### Impacto nos Agentes + Sistema Integrado
- **Agente Afetado:** [Nome do agente principal - ex: Comercial]
- **Workflow n8n ID:** [ex: lM9kCZbVaFRnVWid]
- **Ferramenta Bloqueada:** [ex: racas_e_grupos(), precos_e_servicos()]
- **Tipo de Falha:** [ex: "retorna null", "timeout", "dados inconsistentes"]
- **Frequência:** [ex: "100% dos casos", "apenas raças específicas"]
- **📉 Métrica Impactada:** [success_rate|response_time|human_score]
- **🎯 Score Atual:** [ex: 6.5/10 - abaixo do threshold 8.0]

### 📈 **Evidências Integradas**

#### Logs de Debug GitHub
```
# GitHub Debug Logs
Repositório: https://github.com/gabrielteoodoro/bable-pet-debug/tree/main/debug_logs
Arquivo: debug_YYYY-MM-DD_HH-mm-ss_X.json

[Colar logs específicos com execution_id]
```

#### Métricas de Performance
```
# GitHub Performance Metrics
Repositório: https://github.com/gabrielteoodoro/workflow-configs---Bable-PET/tree/main/performance
Arquivo: metrics.json

{
  "agent_id": "comercial-consultor",
  "current_metrics": {
    "human_score": 6.5,
    "success_rate": 0.73,
    "response_time": 3200
  }
}
```

#### Análise n8n API
```
# Dados via n8n API
python claude-auto-optimizer/get_workflow_performance.py [workflow-id]

[Resultado da análise de performance do workflow]
```

---

## 💡 SOLUÇÃO PROPOSTA

### Tipo de Intervenção
- [ ] **Nova Aba/Sheet**: Criar aba completamente nova na planilha Google Drive
- [ ] **Atualização**: Adicionar campos/registros em aba existente  
- [ ] **Unificação**: Combinar múltiplas abas/planilhas fragmentadas
- [ ] **Correção**: Fixar dados inconsistentes/incorretos nas células
- [ ] **Otimização**: Melhorar performance de consultas via API Google

### Estrutura Proposta

#### Nova Aba: `[nome_aba]` na planilha `[Nome da Planilha Google]`
```
Coluna A | Coluna B | Coluna C | Coluna D
Campo1   | Campo2   | Campo3   | Campo4
exemplo1 | exemplo2 | exemplo3 | exemplo4
exemplo1 | exemplo2 | exemplo3 | exemplo4
```

**Descrição dos Campos:**
- **Campo1** (Coluna A): [Descrição e tipo de dado]
- **Campo2** (Coluna B): [Descrição e tipo de dado]  
- **Campo3** (Coluna C): [Descrição e tipo de dado]

#### OU: Modificação em Aba Existente
**Planilha:** `[Nome da Planilha Google]`
**Aba:** `[nome_aba_existente]`  
**Modificações:**
- [ ] Adicionar colunas: [lista de novas colunas]
- [ ] Atualizar células: [quais linhas/valores específicos]
- [ ] Reorganizar dados: [nova estrutura proposta]

---

## 🔧 ESPECIFICAÇÕES TÉCNICAS

### Integração com Ferramentas
**Ferramentas que usarão os dados:**
- [ ] `racas_e_grupos(raca: string)` → retorna grupo G1-G5
- [ ] `precos_e_servicos(servico: string, grupo: string)` → retorna preços
- [ ] `buscaAssinantes(sessionId: string)` → verifica assinatura
- [ ] `buscarDadosCliente(sessionId: string)` → dados completos
- [ ] `buscarScript(ID_Cenario: string)` → scripts padronizados

### Requisitos de Performance
- **Tempo de consulta via API Google:** < 2 segundos
- **Tamanho estimado:** [número de linhas da planilha]  
- **Frequência de uso:** [ex: "toda consulta comercial"]
- **Limite de API:** Considerar quotas do Google Sheets API

### Compatibilidade
- **N8N Workflows:** [quais workflows acessam esta planilha]
- **Google Drive API:** [versão e permissões necessárias]
- **Backward Compatibility:** [se quebra acessos existentes às planilhas]

---

## 📊 DADOS DE IMPLEMENTAÇÃO

### Cronograma Sugerido
- **Fase 1** (24h): [ex: "Criar nova aba 'Racas_Grupos' na planilha Comercial"]
- **Fase 2** (48h): [ex: "Configurar acesso API e testar com Agente Comercial"]  
- **Fase 3** (72h): [ex: "Validar todos os cenários via N8N"]

### Responsabilidades
- **Agent 1 (Architect)**: [definir esta proposta e estrutura da planilha]
- **Agent 2 (Builder)**: [especificar modificações → PAUSAR e avisar para atualização manual]
- **👤 VOCÊ (Operador)**: [acessar Google Drive → modificar planilhas conforme especificado]
- **Agent 3 (Validator)**: [testar acesso API e funcionamento APENAS após confirmação]
- **Agent 4 (Writer)**: [documentar mudanças e URLs das planilhas atualizadas]

---

## 🧪 PLANO DE TESTES

### Cenários de Teste Obrigatórios

#### Teste 1: Funcionalidade Básica
```bash
# Comando de teste
curl -X POST "[webhook_url]" -d '{"content": "[mensagem_teste]"}'

# Resultado Esperado
[descrever resultado esperado]

# Critério de Sucesso
[como medir se passou]
```

#### Teste 2: Casos Extremos
```bash
# Teste com dados limite
[comando de teste para edge cases]

# Resultado Esperado  
[resultado para casos extremos]
```

#### Teste 3: Performance
- **Volume de dados:** [quantidade a testar]
- **Tempo máximo:** 2 segundos
- **Taxa de sucesso:** >95%

---

## 📈 MÉTRICAS DE SUCESSO

### Antes da Implementação
- **Taxa de sucesso atual:** [X]%
- **Tempo médio de resposta:** [X]s  
- **Casos de falha por dia:** [X]

### Metas Pós-Implementação
- **Taxa de sucesso meta:** [X]%
- **Tempo médio meta:** [X]s
- **Redução de falhas:** [X]%

### KPIs de Acompanhamento
- [ ] Zero retornos "CONSULTAR" → preço definido
- [ ] 100% das raças mapeadas para grupos
- [ ] Dados de cliente unificados (sem fragmentação)
- [ ] [outros KPIs específicos]

---

## ⚠️ RISCOS E MITIGAÇÕES

### Riscos Identificados
1. **Risco:** [ex: "Quebrar workflow N8N existente"]  
   **Probabilidade:** [Alta|Média|Baixa]  
   **Impacto:** [Crítico|Alto|Médio|Baixo]  
   **Mitigação:** [como evitar/resolver]

2. **Risco:** [ex: "Dados inconsistentes durante migração"]  
   **Probabilidade:** [Alta|Média|Baixa]  
   **Impacto:** [Crítico|Alto|Médio|Baixo]  
   **Mitigação:** [como evitar/resolver]

### Plano de Rollback
```bash
# Comandos para reverter em caso de falha
[sequência de comandos para voltar ao estado anterior]
```

---

## 📋 CHECKLIST DE APROVAÇÃO

### Pré-Implementação
- [ ] **Architect**: Especificação técnica completa
- [ ] **Builder**: Estrutura CSV definida e validada
- [ ] **Validator**: Plano de testes aprovado
- [ ] **Writer**: Documentação preparada

### Pós-Implementação  
- [ ] **Funcional**: Todos os testes passaram
- [ ] **Performance**: Métricas dentro do SLA
- [ ] **Integração**: N8N workflows funcionando
- [ ] **Documentação**: CLAUDE.md atualizado

---

## 🔄 STATUS DA PROPOSTA

**Status Atual:** [PROPOSTA|APROVADA|EM_IMPLEMENTAÇÃO|TESTANDO|CONCLUÍDA|REJEITADA]

### Histórico de Mudanças
- **[DD/MM]**: Proposta criada por Agent [X]
- **[DD/MM]**: [mudança/aprovação/etc.]

### Aprovações Necessárias
- [ ] **Architect**: Especificação técnica
- [ ] **Builder**: Viabilidade de implementação  
- [ ] **Validator**: Plano de testes
- [ ] **Writer**: Impacto na documentação

---

*Este template deve ser usado sempre que um dos 4 agentes auxiliares identificar necessidade de modificação nos bancos de dados CSV durante o processo de edição dos prompts dos agentes Bable Pet.*