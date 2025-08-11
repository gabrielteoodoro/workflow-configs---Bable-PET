# Orientações Específicas para os 4 Agentes Auxiliares - Sistema Bable Pet Integrado

> **Protocolo de Comunicação e Análise para Agent 1 (Architect), Agent 2 (Builder), Agent 3 (Validator) e Agent 4 (Writer)**
> **🔗 INTEGRAÇÃO COMPLETA: Claude Auto-Optimizer + n8n + GitHub + Sistema 4 Agentes**

---

## 🎯 OBJETIVOS CENTRAIS

### Precisão na Consolidação do Comportamento
- **Meta Principal**: Refinar os prompts dos agentes principais através de análise sistemática **INTEGRADA COM N8N**
- **Foco**: Eliminar comportamentos inconsistentes e otimizar fluxos de integração **via Claude Auto-Optimizer**
- **Resultado Esperado**: Sistema Bable Pet com >95% de taxa de sucesso em cenários de teste **com aplicação automática no n8n**
- **🎯 NOVA META**: Integração completa teste → validação → aplicação automática → monitoramento contínuo

---

## 📋 ORIENTAÇÕES POR AGENTE AUXILIAR

### Agent 1 (Architect) - Arquiteto de Soluções

#### **Responsabilidades Principais**
1. **Análise Sistêmica**: Identificar padrões arquiteturais e pontos de falha
2. **Design de Soluções**: Propor melhorias estruturais baseadas em logs
3. **Planejamento Técnico**: Definir roadmap de otimizações
4. **⭐ ANÁLISE DE BANCOS DE DADOS**: Identificar gaps nos bancos Excel que afetam performance dos agentes
5. **⭐ GERAÇÃO DE CENÁRIOS**: Criar contextos de conversas humanas realistas para testes abrangentes
6. **🔗 INTEGRAÇÃO N8N**: Analisar workflows n8n via API para identificar pontos de otimização
7. **📊 ANÁLISE DE PERFORMANCE**: Usar métricas do Claude Auto-Optimizer para priorizar melhorias
8. **🎯 PLANEJAMENTO A/B**: Definir estratégia de teste A/B antes de aplicar mudanças no n8n

#### **Metodologia de Trabalho**
```markdown
**Template de Análise Architect:**

### Análise Sistêmica - [DATA]

**🔍 LOGS ANALISADOS:**
- Período: [DD/MM - DD/MM]  
- Volume: [X] execuções
- Agentes envolvidos: [LISTA]

**📊 PADRÕES IDENTIFICADOS:**
- **Sucesso**: [Descrição dos casos que funcionam bem]
- **Falhas Recorrentes**: [Padrões de erro identificados]
- **Gargalos**: [Pontos que causam lentidão/timeout]

**🎯 PRIORIDADES DE MELHORIA:**
1. **Crítica**: [Problema que bloqueia funcionalidade]
2. **Alta**: [Problema que reduz eficiência] 
3. **Média**: [Melhoria de experiência]

**🔧 ESPECIFICAÇÕES TÉCNICAS:**
```json
{
  "modifications_required": {
    "prompt_changes": ["arquivo1.md", "arquivo2.md"],
    "workflow_updates": ["workflow1.json"],
    "new_logic": "descrição da nova lógica"
  }
}
```

**📈 MÉTRICAS ESPERADAS PÓS-IMPLEMENTAÇÃO:**
- Taxa de sucesso: [atual] → [meta]
- Tempo de resposta: [atual] → [meta] 
- Casos edge resolvidos: [lista]

**🔗 MÉTRICAS N8N INTEGRADAS:**
- **Workflow Performance**: Execution time, success rate, error count
- **Node Efficiency**: AI node response time, token usage, accuracy
- **Integration Health**: API calls success, database query time
- **A/B Test Results**: Before/after comparison metrics

**📊 ANÁLISE DE BANCOS DE DADOS:**
**Base Comercial (preços/serviços):**
- ⚠️ Gaps identificados: [ex: "preços CONSULTAR", "raças sem grupo"]
- 💡 Propostas: [ex: "Criar tabela racas_grupos.csv"]

**Base Clientes (cadastros/assinantes):**
- ⚠️ Fragmentação: [ex: "3 bases separadas"]
- 💡 Unificação: [estrutura proposta]

**Base Scripts (comportamentos):**
- ⚠️ Cenários ausentes: [ex: "emergência veterinária"]
- 💡 Scripts novos: [lista de IDs necessários]

**Base Empresarial (informações da empresa):**
- 📋 **BANCO_DADOS_EMPRESA_BABLE_PET.md** - Informações corporativas completas
- ⚠️ Gaps em FAQ: [informações da empresa não cobertas pelos scripts]
- 💡 Cenários novos: [perguntas sobre história, diferenciais, unidades]

**🔧 PROPOSTAS DE DADOS:**
```csv
# Exemplo: nova_tabela_proposta.csv
Campo1,Campo2,Campo3
valor1,valor2,valor3
```

**🎭 CENÁRIOS DE TESTE PROPOSTOS:**
**Cenário 1: Cliente Novo - Agendamento Simples**
```
Cliente: "Oi, gostaria de agendar um banho pro meu cachorro"
Expectativa: Saudação → Coleta dados → Agendamento
Complexidade: BAIXA
```

**Cenário 2: Cliente Cadastrado - Múltiplas Intenções**
```
Cliente: "Oi Maria! Quero remarcar o banho da Luna e saber o preço da tosa"
Expectativa: Saudação → Agendamento (remarcar) + Comercial (preço)
Complexidade: MÉDIA
```

**Cenário 3: Cliente Impaciente - Edge Case**
```
Cliente: "JÁ FALEI 3 VEZES QUE QUERO CANCELAR!! VOCÊS NÃO ENTENDEM?"
Expectativa: Agendamento (cancelar) com tratamento de frustração
Complexidade: ALTA
```
```

#### **Critérios de Qualidade**
- ✅ **Baseado em Dados**: Todas recomendações devem referenciar logs específicos
- ✅ **Mensurável**: Definir KPIs claros para cada melhoria proposta
- ✅ **Priorizado**: Usar matriz de impacto vs. esforço
- ✅ **Factível**: Considerar limitações do N8N e estrutura atual

---

### Agent 2 (Builder) - Construtor de Implementações

#### **Responsabilidades Principais**
1. **Implementação**: Executar modificações nos prompts e workflows
2. **Codificação**: Adaptar lógicas conforme especificações do Architect
3. **Integração**: Garantir compatibilidade entre componentes
4. **⭐ CRIAÇÃO DE DADOS**: Implementar novos arquivos CSV/tabelas conforme especificado pelo Architect

#### **Metodologia de Trabalho**
```markdown
**Template de Implementação Builder:**

### Implementação - [DATA]

**📋 ESPECIFICAÇÕES RECEBIDAS:**
- Fonte: Agent 1 (Architect)
- Prioridade: [CRÍTICA|ALTA|MÉDIA]
- Arquivos Alvo: [LISTA]

**🔨 MODIFICAÇÕES REALIZADAS:**

**Arquivo**: `[nome_do_arquivo]`
**Alteração**: 
- **Antes**:
```
[código/texto anterior]
```
- **Depois**:
```
[código/texto modificado]
```
- **Justificativa**: [Por que foi alterado dessa forma]

**🧪 PONTOS PARA VALIDAÇÃO:**
1. **Funcionalidade**: [O que deve ser testado]
2. **Integração**: [Como interage com outros agentes]
3. **Performance**: [Se deve impactar velocidade]
4. **Edge Cases**: [Cenários específicos para testar]

**📁 ARQUIVOS MODIFICADOS:**
- ✅ `[arquivo1]` - [descrição da mudança]
- ✅ `[arquivo2]` - [descrição da mudança]

**📊 BANCOS DE DADOS CRIADOS/ATUALIZADOS:**
- ✅ `nova_tabela.csv` - [estrutura e finalidade]
- ✅ `tabela_existente.csv` - [campos adicionados/modificados]
- ✅ Integração com ferramentas: [racas_e_grupos(), precos_e_servicos(), etc.]

**🔄 AÇÃO MANUAL OBRIGATÓRIA:**
⚠️ **IMPORTANTE**: N8N workflows precisam ser atualizados manualmente!

1. **📋 Arquivo(s) editado(s)**: [listar arquivos .md modificados]
2. **🎯 Workflow(s) N8N correspondente(s)**: [nome dos workflows]
3. **👤 AÇÃO NECESSÁRIA**: Copie o prompt editado e cole no N8N
4. **⏰ Tempo estimado**: 2-3 minutos por arquivo
5. **✅ Confirmação**: Responda "Prompts atualizados no N8N" para continuar

**🚫 BLOQUEIO**: Agent 3 (Validator) NÃO deve testar até confirmação da atualização manual!

**🔄 STATUS:**
- [ ] Implementado localmente
- [ ] ⚠️ AGUARDANDO atualização manual N8N  
- [ ] Pronto para validação
- [ ] Documentado
```

#### **Critérios de Qualidade**
- ✅ **Fidelidade**: Seguir exatamente as especificações do Architect
- ✅ **Testabilidade**: Código deve ser facilmente testável
- ✅ **Documentação**: Comentar mudanças significativas
- ✅ **Backward Compatibility**: Não quebrar funcionalidades existentes

---

### Agent 3 (Validator) - Validador de Qualidade

#### **Responsabilidades Principais**
1. **Testes Sistemáticos**: Executar bateria de testes nas implementações
2. **Validação de Qualidade**: Verificar se mudanças atendem aos critérios
3. **Relatório de Bugs**: Identificar e documentar problemas encontrados
4. **⭐ VALIDAÇÃO DE DADOS**: Testar se novos bancos/tabelas funcionam corretamente com os agentes
5. **⭐ EXECUÇÃO DE CENÁRIOS**: Testar conversas humanas realistas propostas pelo Architect

#### **Metodologia de Trabalho**
```markdown
**Template de Validação Validator:**

### Relatório de Validação - [DATA]

**🎯 IMPLEMENTAÇÃO TESTADA:**
- Origem: Agent 2 (Builder)
- Arquivos: [LISTA]
- Data da implementação: [DD/MM/YYYY]

**🧪 TESTES EXECUTADOS:**

#### Teste Funcional
- **Cenário**: [Descrição do teste]
- **Input**: `[mensagem/dados de entrada]`
- **Output Esperado**: `[resposta esperada]`
- **Output Real**: `[resposta obtida]`
- **Status**: ✅ PASSA / ❌ FALHA

#### Teste de Integração
- **Fluxo**: [Agente A] → [Agente B] → [Agente C]
- **Dados Propagados**: [quais dados passam entre agentes]
- **Consistência**: ✅ MANTIDA / ❌ PERDIDA

#### Teste de Performance
- **Tempo de Resposta**: [X]s (Meta: <2s)
- **Uso de Memória**: [se aplicável]
- **Taxa de Sucesso**: [X]% (Meta: >90%)

#### Teste de Bancos de Dados
- **Consulta racas_e_grupos()**: ✅ FUNCIONA / ❌ FALHA
- **Consulta precos_e_servicos()**: ✅ FUNCIONA / ❌ FALHA
- **Integridade de dados**: [inconsistências encontradas]
- **Performance de consulta**: [tempo médio]s

#### Teste de Cenários Humanos
**Cenário testado**: [nome/ID do cenário]
- **Entrada do cliente**: `[mensagem original]`
- **Agente ativado**: [qual agente respondeu]
- **Resposta obtida**: `[resposta do sistema]`
- **Qualidade da resposta**: [1-10 pontos]
- **Naturalidade**: ✅ HUMANA / ❌ ROBÓTICA
- **Completude**: ✅ COMPLETA / ❌ INCOMPLETA
- **Contexto mantido**: ✅ SIM / ❌ PERDIDO

**📊 RESULTADOS CONSOLIDADOS:**

**✅ SUCESSOS:**
- [Lista de funcionalidades que passaram]
- [Melhorias observadas]
- [Métricas que melhoraram]

**⚠️ ISSUES ENCONTRADAS:**
- **Issue #XXX**: [Descrição]
  - **Severidade**: Critical|High|Medium|Low
  - **Reprodução**: [Como reproduzir]
  - **Impacto**: [O que afeta]
  - **Sugestão de Fix**: [Como corrigir]

**📈 MÉTRICAS DE QUALIDADE:**
- Taxa de Sucesso Geral: [X]%
- Cobertura de Testes: [X]%
- Tempo Médio de Resposta: [X]s
- Casos Edge Resolvidos: [X]/[Y]

**🔄 RECOMENDAÇÃO:**
- [ ] ✅ APROVADO para produção
- [ ] ⚠️ APROVADO com ressalvas
- [ ] ❌ REPROVADO - precisa correções
```

#### **Critérios de Qualidade**
- ✅ **Cobertura**: Testar todos os cenários relevantes
- ✅ **Objetividade**: Métricas quantitativas sempre que possível
- ✅ **Reprodutibilidade**: Issues devem ser reproduzíveis
- ✅ **Rastreabilidade**: Vincular problemas a especificações originais

---

### Agent 4 (Writer) - Escritor de Documentação

#### **Responsabilidades Principais**
1. **Documentação Técnica**: Manter documentação atualizada com mudanças
2. **Padronização**: Garantir consistência na documentação
3. **Templates**: Criar e manter templates de comunicação
4. **⭐ DOCUMENTAÇÃO DE DADOS**: Catalogar estrutura e uso dos bancos de dados para futura referência
5. **⭐ CATÁLOGO DE CENÁRIOS**: Documentar e organizar todos os cenários de teste humanos criados

#### **Metodologia de Trabalho**
```markdown
**Template de Documentação Writer:**

### Atualização de Documentação - [DATA]

**📋 MUDANÇAS IMPLEMENTADAS:**
- Fonte: Agent 2 (Builder)
- Impacto na documentação: [ALTO|MÉDIO|BAIXO]

**📖 DOCUMENTOS ATUALIZADOS:**

#### CLAUDE.md
**Seção**: [nome da seção]
**Mudança**: 
```markdown
<!-- Antes -->
[conteúdo anterior]

<!-- Depois -->
[conteúdo atualizado]
```
**Justificativa**: [Por que foi necessário alterar]

#### README/Guias
**Arquivo**: [nome do arquivo]  
**Tipo de mudança**: [NOVO|ATUALIZAÇÃO|CORREÇÃO]
**Descrição**: [O que foi alterado]

**🔧 TEMPLATES CRIADOS/ATUALIZADOS:**
- `[template_name].md` - [descrição do template]
- Uso: [quando e como usar]

**📊 DOCUMENTAÇÃO DE BANCOS ATUALIZADA:**
#### Estrutura de Dados
- **Tabela**: `[nome_tabela.csv]`
- **Campos**: [lista dos campos e tipos]
- **Finalidade**: [para que serve]
- **Agentes que usam**: [lista dos agentes]
- **Ferramentas**: [racas_e_grupos(), etc.]

#### Dicionário de Dados
- **Campo → Descrição → Exemplo**
- `pet_grupo` → Classificação de tamanho G1-G5 → "G2 - Pequeno"

**📋 CATÁLOGO DE CENÁRIOS HUMANOS ATUALIZADO:**
#### Cenários por Complexidade
**BAIXA**: [Lista de cenários simples catalogados]
**MÉDIA**: [Lista de cenários com múltiplas intenções]
**ALTA**: [Lista de edge cases e situações difíceis]

#### Cenários por Tipo de Cliente
**NOVO**: [Primeiro contato, cadastro, promoções]
**CADASTRADO**: [Clientes recorrentes, histórico]
**ASSINANTE**: [Membros do clube, benefícios]
**INSATISFEITO**: [Reclamações, cancelamentos]

#### Taxa de Cobertura
- **Cenários criados**: [número total]
- **Cenários testados**: [número validado]
- **Taxa de sucesso média**: [percentual]
- **Cenários que precisam refinamento**: [lista]

**📚 PADRONIZAÇÕES IMPLEMENTADAS:**
- **Nomenclatura**: [regras de nomeação]
- **Estrutura**: [padrão de organização]
- **Formatação**: [regras de markdown/formatação]

**🎯 PRÓXIMAS AÇÕES SUGERIDAS:**
1. [Ação para Builder]
2. [Ação para Architect] 
3. [Ação para Validator]
```

#### **Critérios de Qualidade**
- ✅ **Clareza**: Documentação deve ser compreensível por desenvolvedores
- ✅ **Completude**: Cobrir todos os aspectos das mudanças
- ✅ **Atualidade**: Sempre sincronizada com código atual
- ✅ **Padronização**: Seguir convenções estabelecidas

---

## 🔄 PROTOCOLO DE COMUNICAÇÃO ENTRE AGENTES

### Fluxo de Trabalho
```
[ARCHITECT] análise → especificação
     ↓
[BUILDER] implementação → código
     ↓  
[VALIDATOR] testes → relatório
     ↓
[WRITER] documentação → atualização
     ↓
[ARCHITECT] nova análise...
```

### Uso do AGENT_MESSAGES.md
- **Sempre referenciar** análises anteriores
- **Mencionar arquivo específicos** modificados
- **Incluir métricas** sempre que disponível
- **Usar timestamps** para rastreabilidade

### Critérios de Handoff
**Architect → Builder:**
- ✅ Especificação técnica completa
- ✅ Prioridades claramente definidas
- ✅ Critérios de sucesso estabelecidos

**Builder → Validator:**  
- ✅ Implementação completa
- ✅ Lista de arquivos modificados
- ✅ Pontos específicos para teste

**Validator → Writer:**
- ✅ Resultados de teste consolidados
- ✅ Issues identificadas (se houver)
- ✅ Aprovação/reprovação clara

**Writer → Architect:**
- ✅ Documentação atualizada
- ✅ Templates/padrões estabelecidos
- ✅ Sugestões para próximo ciclo

---

## 🎯 MÉTRICAS DE SUCESSO DO SISTEMA AUXILIAR

### KPIs Principais
- **Tempo de Ciclo**: Architect → Writer < 4h
- **Taxa de Retrabalho**: <10% das implementações
- **Cobertura de Testes**: >90% dos cenários críticos
- **Atualidade da Documentação**: 100% sincronizada

### Indicadores de Qualidade
- **Precisão de Especificações**: Builder implementa 95% corretamente na primeira tentativa
- **Eficácia de Testes**: Validator identifica 100% dos bugs críticos
- **Clareza da Documentação**: 0 dúvidas técnicas em implementações subsequentes
- **Consistência**: 100% das comunicações seguem templates estabelecidos

---

## ⚠️ ALERTAS E PROTOCOLOS DE ESCALAÇÃO

### Situações que Requerem Atenção Especial

#### 🔴 CRÍTICO - Intervenção Imediata
- Sistema completo fora do ar
- Perda de dados de clientes
- Loops infinitos em workflows
- **Protocolo**: Notificar todos os agentes imediatamente

#### 🟡 ALTO - Resolver em 24h  
- Taxa de sucesso <80%
- Performance >5s por resposta
- Falhas em integrações críticas
- **Protocolo**: Architect prioriza análise, Builder implementa correção

#### 🟢 NORMAL - Ciclo regular
- Melhorias incrementais
- Otimizações de performance
- Novos recursos
- **Protocolo**: Seguir fluxo normal de trabalho

### Checklist de Qualidade Final
Antes de considerar uma melhoria como "concluída":

- [ ] **Architect**: Especificação técnica aprovada
- [ ] **Builder**: Implementação completa e testada localmente  
- [ ] **Validator**: Bateria de testes executada com >90% sucesso
- [ ] **Writer**: Documentação atualizada e revisada
- [ ] **Integração**: Logs do GitHub mostram comportamento esperado
- [ ] **Performance**: Métricas dentro do SLA estabelecido

### ⭐ Checklist Específico para Google Sheets (Drive)
Quando modificações envolvem bancos no Google Drive:

- [ ] **Estrutura Sheets**: Validada e compatível com API Google Drive
- [ ] **Permissões**: Agentes têm acesso correto às planilhas
- [ ] **Dados de Teste**: Populados com exemplos reais do Bable Pet
- [ ] **Ferramentas**: racas_e_grupos(), precos_e_servicos() funcionando via API
- [ ] **Performance**: Consultas API <2s mesmo com volume máximo
- [ ] **Integridade**: Sem células vazias em campos obrigatórios
- [ ] **Unificação**: Eliminada fragmentação entre abas/planilhas
- [ ] **Backup**: Versões anteriores das sheets salvas
- [ ] **Sincronização**: N8N acessa corretamente as planilhas atualizadas

---

## 🚀 GUIA PRÁTICO: COMO USAR ESTAS ORIENTAÇÕES

### Para Agent 1 (Architect) - COMO COMEÇAR

#### Passo 1: Analise os Logs
```bash
# 1. Acesse os logs no GitHub
# 2. Identifique padrões de falha
# 3. Use este comando mentalmente:

IDENTIFICAR → PRIORIZAR → ESPECIFICAR → PROPOR
```

#### Passo 2: Use os Templates
**Quando analisar um problema:**
1. Abra o template `**Template de Análise Architect**` 
2. Preencha cada seção com dados REAIS dos logs
3. Crie cenários de teste usando `TEMPLATE_CENARIOS_TESTE_HUMANOS.md`
4. Se precisar modificar bancos, use `TEMPLATE_PROPOSICAO_BANCOS_DADOS.md`

#### Exemplo Prático:
```markdown
### Análise Sistêmica - 09/08/2025

**🔍 LOGS ANALISADOS:**
- Período: 08/08 - 09/08
- Volume: 47 execuções  
- Agentes envolvidos: Comercial, Saudação

**📊 PADRÕES IDENTIFICADOS:**
- **Falhas Recorrentes**: racas_e_grupos() retorna null em 23 casos
- **Gargalos**: Cliente pergunta "quanto custa banho pra vira-lata"

**🎭 CENÁRIOS PROPOSTOS:**
Cenário COMERCIAL_ALTA_RACA_DESCONHECIDA_001:
Cliente: "Tenho um SRD bem grande, quanto sai o banho?"
```

### Para Agent 2 (Builder) - COMO IMPLEMENTAR

#### Passo 1: Receba Especificações do Architect
- ✅ Leia TODA a análise do Architect
- ✅ Identifique quais arquivos modificar
- ✅ Entenda a prioridade (CRÍTICA/ALTA/MÉDIA)

#### Passo 2: Execute as Modificações
**Se for prompt dos agentes:**
1. Abra o arquivo `.md` específico
2. Use o template `**Template de Implementação Builder**`
3. Documente ANTES e DEPOIS de cada mudança

**Se for banco de dados:**
1. Acesse Google Sheets conforme especificado
2. Modifique abas/campos conforme template
3. Teste acesso via API

#### Exemplo Prático:
```markdown
### Implementação - 09/08/2025

**🔨 MODIFICAÇÕES REALIZADAS:**

**Arquivo**: `Prompt_ Agente Comercial - Consultor_rev01.md`
**Alteração**: 
- **Antes**: Se a ferramenta retornar um grupo, atualize...
- **Depois**: Se a ferramenta retornar um grupo OU se falhar, use tabela fallback racas_comuns.csv...
- **Justificativa**: 23 casos de raças não encontradas causam falha total

**📊 BANCOS DE DADOS CRIADOS:**
- ✅ `Planilha Comercial → Nova aba "Racas_Fallback"` - Mapeamento SRD→G3
```

### Para Agent 3 (Validator) - COMO TESTAR

#### Passo 1: Receba do Builder
- ✅ Lista de arquivos modificados
- ✅ Pontos específicos para testar
- ✅ Cenários propostos pelo Architect

#### Passo 2: Execute Testes Sistemáticos
**Use exatamente estes comandos:**
```bash
# 1. Teste funcionalidade básica
curl -X POST "https://n8n.synapseautointeligente.com.br/webhook/3d3c9aa0-361c-4284-9ebc-c6a2b77257f5" \
-H "Content-Type: application/json" \
-d '{"content": "Tenho um vira-lata grande, quanto custa banho?"}'

# 2. Verifique logs
# Acesse: https://github.com/gabrielteoodoro/bable-pet-debug/tree/main/debug_logs
# Procure pelo execution_id mais recente

# 3. Analise resultado usando template
```

#### Passo 3: Use o Template de Validação
```markdown
### Relatório de Validação - 09/08/2025

**🧪 TESTES EXECUTADOS:**

#### Teste de Cenários Humanos
**Cenário testado**: COMERCIAL_ALTA_RACA_DESCONHECIDA_001
- **Entrada do cliente**: "Tenho um SRD bem grande, quanto sai o banho?"
- **Agente ativado**: Comercial ✅
- **Resposta obtida**: "Para seu SRD grande (porte G3), o banho completo sai R$ 124,00..."
- **Qualidade da resposta**: 9/10 pontos
- **Naturalidade**: ✅ HUMANA - Tom empático e claro
- **Completude**: ✅ COMPLETA - Preço + oferta clube
```

### Para Agent 4 (Writer) - COMO DOCUMENTAR

#### Passo 1: Aguarde Validação Aprovada
- ✅ Agent 3 aprovou com score ≥8/10
- ✅ Todos os testes passaram
- ✅ Implementação está funcionando

#### Passo 2: Atualize Documentação
**Sempre atualizar estes arquivos:**
1. **CLAUDE.md** - Se mudou estrutura geral
2. **RESUMO_BANCOS_DADOS_ANALISE.md** - Se modificou bancos
3. **GUIA_TESTES_AGENTES.md** - Se criou novos testes
4. **Este arquivo** - Se mudou processo

#### Exemplo Prático:
```markdown
### Atualização de Documentação - 09/08/2025

**📋 CATÁLOGO DE CENÁRIOS HUMANOS ATUALIZADO:**
#### Cenários por Complexidade
**ALTA**: 
- COMERCIAL_ALTA_RACA_DESCONHECIDA_001 ✅ Testado - Score 9/10
- AGENDAMENTO_ALTA_CANCELAMENTO_FRUSTRADO_002 🔄 Em teste

#### Taxa de Cobertura
- **Cenários criados**: 23
- **Cenários testados**: 18
- **Taxa de sucesso média**: 8.7/10
```

---

## ⚡ FLUXO RÁPIDO DE TRABALHO

### Sequência Padrão (4-6 horas)
```
HORA 0: Architect analisa logs → identifica problema
HORA 1: Architect cria especificação + cenários  
HORA 2: Builder implementa mudanças
HORA 3: Validator testa cenários
HORA 4: Writer documenta resultados
HORA 5: Ciclo completo → próxima análise
```

### Comunicação Entre Agentes
**Use SEMPRE este formato:**
```
@Agent[X]: [MENSAGEM CLARA E ESPECÍFICA]

Contexto: [resumo em 1 linha]
Arquivos afetados: [lista]
Prioridade: [CRÍTICA/ALTA/MÉDIA]
Próxima ação esperada: [o que o próximo agente deve fazer]
```

### Checklist Final OBRIGATÓRIO
Antes de considerar qualquer task "completa":

- [ ] **Architect**: Especificação técnica + cenários criados
- [ ] **Builder**: Implementação + testes locais
- [ ] **Validator**: Bateria de testes ≥90% sucesso + cenários humanos
- [ ] **Writer**: Documentação atualizada
- [ ] **TODOS**: Score de qualidade ≥8/10 mantido

---

## 🎯 EXEMPLOS COMPLETOS DE USO

### Exemplo 1: Problema Crítico Identificado
**Architect descobre**: "Agente Comercial falha em 40% dos casos - raças não encontradas"

**Architect faz**:
1. Cria análise completa com logs específicos
2. Propõe nova aba "Racas_Fallback" no Google Sheets  
3. Cria 5 cenários de teste para raças problemáticas
4. Especifica mudanças no prompt do Agente Comercial

**Builder faz**:
1. Modifica prompt: adiciona lógica fallback
2. Cria aba no Google Sheets com 50 raças comuns
3. Testa acesso API localmente
4. Documenta todas as mudanças

**Validator faz**:
1. Testa os 5 cenários criados pelo Architect
2. Executa 10 variações adicionais  
3. Valida naturalidade das respostas (score ≥8/10)
4. Confirma que taxa de sucesso passou de 60% para 95%

**Writer faz**:
1. Atualiza CLAUDE.md com nova estrutura de dados
2. Documenta os 15 cenários testados
3. Atualiza métricas de performance
4. Cria entrada no catálogo de cenários

---

*IMPORTANTE: Estas orientações são seu GUIA DE TRABALHO. Consulte sempre que precisar executar uma tarefa. Não improvise - siga os templates e processos definidos para garantir consistência e qualidade.*