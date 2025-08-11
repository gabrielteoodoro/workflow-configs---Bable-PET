# Quick Start Guide - 4 Agentes Auxiliares + Claude Auto-Optimizer

> **🔗 SISTEMA INTEGRADO**: 4 Agentes + Claude Auto-Optimizer + n8n + GitHub + Testes A/B

## 🚀 INÍCIO RÁPIDO (5 minutos) - NOVA VERSÃO INTEGRADA

### 🏢 **Agent 1 (Architect) - VERSÃO INTEGRADA**
```
1. NOVA FONTE: GitHub Metrics + n8n API + Debug logs
   - Acesse: https://github.com/gabrielteoodoro/workflow-configs---Bable-PET/tree/main/performance
   - Execute: python claude-auto-optimizer/get_performance_metrics.py
   - Logs: https://github.com/gabrielteoodoro/bable-pet-debug/tree/main/debug_logs

2. ANÁLISE INTEGRADA:
   - Identifique workflows com score <8.0
   - Use: METRICAS_PERFORMANCE_AGENTES.md para thresholds
   - Correlacione: Métricas + Logs + Performance n8n

3. PROPOSTA DE OTIMIZAÇÃO:
   - Use: ORIENTACOES_4_AGENTES_AUXILIARES.md → "Agent 1 Integrado"
   - Gere: Cenários A/B + Especificações Claude Auto-Optimizer
   - Documente: CONFIG_TESTES_N8N.md para configurações
```

### 🔨 **Agent 2 (Builder) - VERSÃO INTEGRADA**
```
1. RECEBA ESPECIFICAÇÃO:
   - Leia: Análise completa do Agent 1 com workflows identificados
   - Valide: IDs de workflows n8n + prioridades + cenários A/B

2. IMPLEMENTAÇÃO CLAUDE AUTO-OPTIMIZER:
   - Execute: python claude-auto-optimizer/optimize_prompt.py [workflow-id]
   - NÃO aplique ainda! Apenas gere versão otimizada
   - Use: Templates "Implementação Builder" INTEGRADO

3. PREPARAÇÃO TESTE A/B:
   - Configure: CONFIG_TESTES_N8N.md para teste paralelo
   - Documente: Versão atual vs. versão otimizada
   - Entregue: Especificação para Agent 3 validar

⚠️ **CRÍTICO**: Só aplica no n8n DEPOIS da aprovação do Agent 3!
```

### ✅ **Agent 3 (Validator) - VERSÃO INTEGRADA**
```
1. EXECUÇÃO TESTE A/B:
   - Receba: Versão atual + versão otimizada do Agent 2
   - Execute: python claude-auto-optimizer/run_ab_test.py [workflow-id] [scenario-id]
   - Use: PROTOCOLO_VALIDACAO_PROMPTS.md (5 layers de validação)

2. VALIDAÇÃO RIGOROSA:
   - Layer 1: Estrutural (compatibilidade n8n)
   - Layer 2: Funcional (cenários críticos)
   - Layer 3: Qualidade (score ≥8/10)
   - Layer 4: Performance (tempo + tokens)
   - Layer 5: Segurança (sem regressão)

3. DECISÃO DE APROVAÇÃO:
   - Compare: Métricas A/B usando METRICAS_PERFORMANCE_AGENTES.md
   - Aprove: Somente se melhoria >0.5 pontos + score ≥8/10
   - Documente: Relatório completo com evidências
```

### 📝 **Agent 4 (Writer) - VERSÃO INTEGRADA**
```
1. APLICAÇÃO APROVADA:
   - Aguarde: Aprovação Agent 3 (score ≥8/10 + todas validações)
   - Execute: python claude-auto-optimizer/apply_optimization.py [workflow-id]
   - Monitore: 48h de monitoramento pós-aplicação

2. DOCUMENTAÇÃO INTEGRADA:
   - Atualize: GitHub performance/metrics.json
   - Commit: GitHub performance/optimization-history.json
   - Sincronize: CLAUDE.md + METRICAS_PERFORMANCE_AGENTES.md
   - Catalogue: TEMPLATE_CENARIOS_TESTE_HUMANOS.md

3. MONITORAMENTO CONTÍNUO:
   - Configure: python claude-auto-optimizer/monitor_all.py
   - Alerte: Se score <8.0 → rollback automático
   - Prepare: Próximo ciclo baseado em métricas GitHub
```

---

## 📁 ARQUIVOS ESSENCIAIS - SISTEMA INTEGRADO

### 🔗 **Para TODOS os Agentes (NOVA VERSÃO):**
- **ORIENTACOES_4_AGENTES_AUXILIARES.md** ← MANUAL INTEGRADO (ATUALIZADO)
- **CONFIG_TESTES_N8N.md** ← Configurações de integração completa
- **PROTOCOLO_VALIDACAO_PROMPTS.md** ← Validação rigorosa 5 layers
- **METRICAS_PERFORMANCE_AGENTES.md** ← Sistema de métricas unificado
- **GUIA_TESTES_AGENTES.md** ← Testes A/B + cenários integrados
- **TEMPLATE_CENARIOS_TESTE_HUMANOS.md** ← Cenários com Claude Auto-Optimizer

### 📊 **Arquivos de Referência:**
- **CLAUDE.md** ← Visão geral do sistema Bable Pet
- **BANCO_DADOS_EMPRESA_BABLE_PET.md** ← Informações da empresa

### Templates Específicos:
- **TEMPLATE_CENARIOS_TESTE_HUMANOS.md** ← Agent 1 (criar cenários)
- **TEMPLATE_PROPOSICAO_BANCOS_DADOS.md** ← Agent 1 (propor dados)
- **RESUMO_BANCOS_DADOS_ANALISE.md** ← Todos (entender bases atuais)

---

## ⚡ COMANDOS ESSENCIAIS

### Agent 3 (Validator) - Testes Rápidos:
```bash
# URL do webhook (sempre a mesma)
WEBHOOK="https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5"

# Teste básico - agendamento
curl -X POST "$WEBHOOK" -H "Content-Type: application/json" \
-d '{"content": "Oi, quero agendar banho pro meu poodle"}'

# Teste médio - preço
curl -X POST "$WEBHOOK" -H "Content-Type: application/json" \
-d '{"content": "Quanto custa banho completo pra golden retriever?"}'

# Teste difícil - múltiplas intenções
curl -X POST "$WEBHOOK" -H "Content-Type: application/json" \
-d '{"content": "Preciso remarcar o banho da Luna e saber preço da tosa"}'
```

### Verificar Resultados:
```bash
# Acesse os logs no GitHub:
https://github.com/gabrielteoodoro/bable-pet-debug/tree/main/debug_logs

# Procure pelo arquivo mais recente:
debug_YYYY-MM-DD_HH-mm-ss_X.json
```

---

## 🎯 FOCO DE CADA AGENTE

### Agent 1 (Architect) → IDENTIFICA E PLANEJA
**Sempre pergunte:**
- Que padrão de falha aparece nos logs?
- Que cenários humanos testam isso?
- Que dados estão faltando nos bancos?
- Como priorizar as correções?
- **FAQ precisa de informações da empresa?** (consultar BANCO_DADOS_EMPRESA_BABLE_PET.md)

### Agent 2 (Builder) → IMPLEMENTA E CONSTRÓI  
**Sempre pergunte:**
- O que exatamente preciso modificar?
- Como documento antes/depois?
- Como testo localmente antes de enviar?
- Quebrei alguma funcionalidade existente?

### Agent 3 (Validator) → TESTA E VALIDA
**Sempre pergunte:**
- Os cenários propostos passaram?
- A resposta parece humana (score ≥8/10)?
- Todos os dados foram coletados?
- O fluxo completo funciona?

### Agent 4 (Writer) → DOCUMENTA E ORGANIZA
**Sempre pergunte:**
- Que documentos preciso atualizar?
- Como organizar os cenários testados?
- Que lições aprendidas devo registrar?
- Como preparar o próximo ciclo?

---

## 🔄 CICLO COMPLETO (Exemplo Prático)

### Situação: "Cliente reclama que robô não entende raça 'vira-lata'"

#### Agent 1 (30 min):
```markdown
### Análise - 09/08/2025
**Problema**: racas_e_grupos("vira-lata") retorna null
**Proposta**: Criar aba "Racas_Fallback" com SRD→G3
**Cenários**: 3 testes com raças não catalogadas
```

#### Agent 2 (45 min):
```markdown
### Implementação - 09/08/2025  
**Modificado**: Prompt_Agente_Comercial_rev01.md linha 47
**Antes**: Se falhar, pare aqui
**Depois**: Se falhar, use tabela fallback
**Criado**: Google Sheets "Comercial" → aba "Racas_Fallback"
```

#### Agent 3 (30 min):
```bash
# Testou 3 cenários:
curl -X POST "$WEBHOOK" -d '{"content": "Quanto custa banho pra vira-lata?"}'
curl -X POST "$WEBHOOK" -d '{"content": "Tenho um SRD grande, qual preço?"}'  
curl -X POST "$WEBHOOK" -d '{"content": "É um cachorro sem raça definida pequeno"}'

# Resultados: 3/3 passaram com score 9/10
```

#### Agent 4 (15 min):
```markdown
### Documentação Atualizada - 09/08/2025
- CLAUDE.md: Adicionada tabela fallback
- Catálogo: +3 cenários COMERCIAL_ALTA_RACA_INDEFINIDA  
- Taxa sucesso: 95% → 98%
```

### Total: 2 horas → Problema resolvido!

---

## 📋 CHECKLIST DIÁRIO

### Antes de começar qualquer tarefa:
- [ ] Li as orientações do meu agente específico?
- [ ] Entendi qual template usar?
- [ ] Tenho acesso aos logs/arquivos necessários?
- [ ] Sei como comunicar com próximo agente?

### Antes de finalizar qualquer tarefa:
- [ ] Segui todos os passos do template?
- [ ] Documentei adequadamente minhas ações?
- [ ] Testei/validei meu trabalho?
- [ ] Score de qualidade ≥8/10 mantido?

---

## 🆘 EM CASO DE DÚVIDA

### Perguntas Frequentes:

**"Não sei qual template usar"**
→ Consulte ORIENTACOES_4_AGENTES_AUXILIARES.md seção do seu agente

**"Como testar se funcionou?"**
→ Use comandos curl do GUIA_TESTES_AGENTES.md

**"Não encontrei os logs"**
→ https://github.com/gabrielteoodoro/bable-pet-debug/tree/main/debug_logs

**"Como editar Google Sheets?"**
→ Consulte TEMPLATE_PROPOSICAO_BANCOS_DADOS.md

**"Score de qualidade baixo"**  
→ Veja exemplos de respostas humanas vs robóticas no GUIA_TESTES_AGENTES.md

### Hierarquia de Consulta:
1. **QUICK_START_4_AGENTES.md** ← Você está aqui (início rápido)
2. **ORIENTACOES_4_AGENTES_AUXILIARES.md** ← Manual detalhado  
3. **Templates específicos** ← Para tarefas específicas
4. **GUIA_TESTES_AGENTES.md** ← Para testes e validação

---

**🎯 LEMBRE-SE: Seu objetivo é manter qualidade ≥8/10 em todas as interações do sistema Bable Pet. Siga os processos, use os templates, documente tudo!**