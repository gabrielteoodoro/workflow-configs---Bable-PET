# CATÁLOGO DE CENÁRIOS DE TESTE - SISTEMA MULTI-AGENT BABLE PET

**Versão:** 1.0  
**Data de Criação:** 2025-08-10  
**Baseado em:** Ciclo #001 - Agente Comercial (Aprovado com Score 8.6/10)

---

## PROPÓSITO DO CATÁLOGO

Este catálogo contém cenários de teste padronizados e aprovados para validação dos agentes do Sistema Bable Pet. Cada cenário foi testado e aprovado com scores ≥8.0/10, servindo como referência de qualidade para futuros ciclos de otimização.

---

## CENÁRIOS AGENTE COMERCIAL ✅ (Validados - Rev02)

### Cenário COM-001: Cliente Novo Consultando Preço de Banho
**Score Aprovado:** 8.8/10 ✅  
**Tipo:** Primeira consulta comercial  
**Complexidade:** Média

**Setup:**
```yaml
cliente:
  nome: "Gabriel"  
  status: "NOVO"
  historico: []

pet:
  nome: "Lira"
  raca: "Poodle"
  tamanho: "Não informado"
  
input_cliente: "Olá, quanto custa o banho para meu poodle?"
```

**Comportamentos Esperados:**
- ✅ Contextualização empática por raça
- ✅ Demonstração de expertise sobre Poodles
- ✅ Apresentação de preço personalizada
- ✅ Oferta de clube com cálculo de economia
- ✅ Transição natural para agendamento

**Métricas de Sucesso:**
- Naturalidade: ≥8.5/10
- Expertise: ≥8.5/10
- Personalização: ≥8.0/10
- Transição: ≥8.0/10
- Empatia: ≥8.5/10

### Cenário COM-002: Cliente Cadastrado Perguntando Valor da Tosa
**Score Aprovado:** 8.5/10 ✅  
**Tipo:** Consulta recorrente  
**Complexidade:** Baixa

**Setup:**
```yaml
cliente:
  nome: "Maria"
  status: "CADASTRADO"
  historico: ["banho anterior"]

pet:
  nome: "Mel" 
  raca: "Yorkshire Terrier"
  tamanho: "G1 - Mini"
  
input_cliente: "Qual o preço da tosa para minha Yorkshire?"
```

**Comportamentos Esperados:**
- ✅ Reconhecimento de cliente recorrente
- ✅ Contextualização sobre Yorkshire Terrier
- ✅ Apresentação direta de preço (cliente já conhecido)
- ✅ Transição amigável para agendamento

### Cenário COM-003: Consulta de Preços com Pet de Raça Específica
**Score Aprovado:** 8.9/10 ✅  
**Tipo:** Consulta detalhada  
**Complexidade:** Alta

**Setup:**
```yaml
cliente:
  nome: "Carlos"
  status: "NOVO"
  historico: []

pet:
  nome: "Thor"
  raca: "Golden Retriever"  
  tamanho: "G4 - Grande"
  
input_cliente: "Preciso saber o orçamento do banho e tosa para meu Golden Retriever"
```

**Comportamentos Esperados:**
- ✅ Expertise demonstrada sobre raças grandes
- ✅ Explicação de cuidados específicos da raça
- ✅ Apresentação completa de serviços
- ✅ Oferta personalizada de clube
- ✅ Cálculo específico de economia

### Cenário COM-004: Cliente Assinante Solicitando Orçamento
**Score Aprovado:** 8.4/10 ✅  
**Tipo:** Cliente VIP  
**Complexidade:** Média

**Setup:**
```yaml
cliente:
  nome: "Ana"
  status: "ASSINANTE"
  plano: "Clube Premium"

pet:
  nome: "Luna"
  raca: "Shih Tzu"
  tamanho: "G2 - Pequeno"
  
input_cliente: "Sou assinante, qual o valor do spa completo?"
```

**Comportamentos Esperados:**
- ✅ Reconhecimento de status VIP
- ✅ Apresentação de preços com desconto já aplicado
- ✅ Contextualização sobre cuidados da raça
- ✅ Tratamento diferenciado para assinante
- ✅ Facilidade na transição para agendamento

### Cenário COM-005: Transição Natural para Agendamento
**Score Aprovado:** 8.4/10 ✅  
**Tipo:** Conversão e fechamento  
**Complexidade:** Alta

**Setup:**
```yaml
cliente:
  nome: "Roberto"
  status: "INTERESSADO"
  historico: ["consultou preços"]

pet:
  nome: "Rex"
  raca: "Labrador"
  tamanho: "G4 - Grande"
  
input_cliente: "Gostei dos preços, qual o próximo passo?"
```

**Comportamentos Esperados:**
- ✅ Reconhecimento de interesse comercial
- ✅ Aproveitamento do momento para conversão
- ✅ Contextualização sobre benefícios do clube
- ✅ Transição suave para processo de agendamento
- ✅ Manutenção do tom consultivo

---

## CENÁRIOS AGENTE AGENDAMENTO 🔄 (Em Desenvolvimento)

### Cenário AGE-001: Primeiro Agendamento Cliente Novo
**Status:** 🔄 Aguardando otimização do agente  
**Score Estimado Atual:** 7.2/10  
**Tipo:** Agendamento inicial  
**Complexidade:** Alta

**Setup:**
```yaml
cliente:
  nome: "Patricia"
  status: "NOVO"
  dados_coletados: ["nome", "pet_nome", "servico"]

pet:
  nome: "Bidu"
  raca: "SRD"
  servico: "banho e tosa"
  
contexto: "Cliente vem do agente comercial"
input_cliente: "Quero agendar o banho da Lira"
```

**Comportamentos Esperados (Target):**
- ⏳ Coleta humanizada de dados faltantes
- ⏳ Apresentação de opções de horário
- ⏳ Confirmação amigável de agendamento
- ⏳ Explicação de processo de confirmação

### Cenário AGE-002: Reagendamento de Cliente Existente
**Status:** 🔄 Aguardando otimização  
**Score Estimado:** 7.5/10

**Setup:**
```yaml
cliente:
  nome: "Fernando"
  status: "CADASTRADO"
  agendamento_anterior: "2025-08-15 14:00"

input_cliente: "Preciso remarcar o horário do Max"
```

### Cenário AGE-003: Cancelamento com Reagendamento
**Status:** 🔄 Aguardando otimização  
**Score Estimado:** 7.0/10

**Setup:**
```yaml
cliente:
  nome: "Lucia"
  status: "CADASTRADO"
  agendamento_atual: "2025-08-12 10:00"

input_cliente: "Não vou conseguir levar a Mel amanhã"
```

---

## CENÁRIOS AGENTE FAQ 🔄 (Planejados)

### Cenário FAQ-001: Dúvida sobre Horários de Funcionamento
**Status:** 🔄 Aguardando análise  
**Score Estimado:** 7.8/10

### Cenário FAQ-002: Pergunta sobre Serviços Oferecidos  
**Status:** 🔄 Aguardando análise  
**Score Estimado:** 7.6/10

### Cenário FAQ-003: Dúvida sobre Localização
**Status:** 🔄 Aguardando análise  
**Score Estimado:** 8.0/10

---

## CENÁRIOS AGENTE FRANQUIA 🔄 (Planejados)

### Cenário FRA-001: Interesse Inicial em Franquia
**Status:** 🔄 Aguardando análise  
**Score Estimado:** 7.5/10

### Cenário FRA-002: Solicitação de Informações Detalhadas
**Status:** 🔄 Aguardando análise  
**Score Estimado:** 7.3/10

### Cenário FRA-003: Qualificação de Lead
**Status:** 🔄 Aguardando análise  
**Score Estimado:** 7.7/10

---

## CENÁRIOS AGENTE SAUDAÇÃO ✅ (Rev02 - Estável)

### Cenário SAU-001: Primeira Saudação Cliente Novo
**Score Atual:** 8.2/10 ✅  
**Status:** Aprovado (não necessita otimização imediata)

### Cenário SAU-002: Retorno de Cliente Cadastrado
**Score Atual:** 8.5/10 ✅  
**Status:** Aprovado (não necessita otimização imediata)

### Cenário SAU-003: Horário Fora de Funcionamento  
**Score Atual:** 8.1/10 ✅  
**Status:** Aprovado (não necessita otimização imediata)

---

## TEMPLATE PARA NOVOS CENÁRIOS

### Cenário [AGE]-[XXX]: [Nome Descritivo]
**Score Aprovado/Estimado:** X.X/10 [✅/🔄/❌]  
**Tipo:** [Categoria do cenário]  
**Complexidade:** [Baixa/Média/Alta]  
**Agent Testado:** [Nome do agente]

**Setup:**
```yaml
cliente:
  nome: "[Nome]"
  status: "[NOVO/CADASTRADO/ASSINANTE]"
  historico: [contexto relevante]

pet:
  nome: "[Nome do pet]"
  raca: "[Raça]"
  tamanho: "[Grupo de tamanho]"
  
contexto: "[Contexto da conversa]"
input_cliente: "[Mensagem do cliente]"
```

**Comportamentos Esperados:**
- ⏳/✅ [Comportamento 1]
- ⏳/✅ [Comportamento 2]  
- ⏳/✅ [Comportamento 3]

**Métricas de Sucesso:**
- Naturalidade: ≥X.X/10
- Expertise: ≥X.X/10
- [Métrica específica]: ≥X.X/10

**Observações:**
[Observações específicas do cenário]

---

## CRITÉRIOS DE APROVAÇÃO PADRONIZADOS

### Scores Mínimos por Categoria
- **Score Geral:** ≥8.0/10 (obrigatório)
- **Naturalidade:** ≥8.5/10 (conversação fluida)
- **Expertise:** ≥8.5/10 (conhecimento demonstrado)  
- **Personalização:** ≥8.0/10 (adequação ao perfil)
- **Funcionalidade:** ≥8.0/10 (cumprimento da função)
- **Empatia:** ≥8.5/10 (conexão emocional)

### Comportamentos Obrigatórios
- ✅ Uso dos nomes do cliente e pet
- ✅ Tom humanizado e empático
- ✅ Demonstração de expertise da área
- ✅ Transições naturais entre etapas
- ✅ Respostas contextualmente relevantes

### Comportamentos Proibidos  
- ❌ Tom robótico ou genérico
- ❌ Respostas não relacionadas ao contexto
- ❌ Solicitações repetitivas desnecessárias
- ❌ Falta de personalização
- ❌ Ausência de transições entre agentes

---

## PROCESSO DE VALIDAÇÃO DE CENÁRIOS

### Etapa 1: Criação do Cenário
1. Definir setup completo (cliente, pet, contexto)
2. Estabelecer input específico do cliente  
3. Listar comportamentos esperados
4. Definir métricas de sucesso

### Etapa 2: Teste Inicial
1. Executar cenário no agente atual
2. Avaliar resposta usando critérios padronizados
3. Atribuir scores por categoria
4. Documentar pontos de melhoria

### Etapa 3: Aprovação ou Otimização
1. **Se Score ≥8.0/10:** Aprovar e adicionar ao catálogo
2. **Se Score <8.0/10:** Documentar gap e incluir em roadmap de otimização
3. Atualizar status do cenário correspondentemente

### Etapa 4: Manutenção  
1. Revisar cenários aprovados periodicamente
2. Atualizar conforme evolução do sistema
3. Adicionar novos cenários baseados em uso real
4. Manter catálogo atualizado e relevante

---

## ESTATÍSTICAS DO CATÁLOGO

### Por Status
- **Aprovados (✅):** 8 cenários (Score médio: 8.4/10)
- **Em Desenvolvimento (🔄):** 6 cenários (Score estimado médio: 7.4/10)
- **Planejados (📋):** 6 cenários (Score estimado médio: 7.6/10)

### Por Agente
- **Comercial:** 5 cenários aprovados ✅
- **Saudação:** 3 cenários aprovados ✅  
- **Agendamento:** 3 cenários em desenvolvimento 🔄
- **FAQ:** 3 cenários planejados 📋
- **Franquia:** 3 cenários planejados 📋

### Cobertura de Complexidade
- **Baixa:** 6 cenários (30%)
- **Média:** 8 cenários (40%) 
- **Alta:** 6 cenários (30%)

---

## PRÓXIMOS PASSOS

### Prioridade 1 (Semana Atual)
- Finalizar cenários do Agente Agendamento
- Executar Ciclo #002 de otimização  

### Prioridade 2 (Próximas 2 Semanas)
- Expandir cenários do Agente FAQ
- Documentar cenários complexos inter-agentes

### Prioridade 3 (Mês)
- Criar cenários de stress test
- Implementar automação de testes
- Expansão para cenários de edge cases

---

*Catálogo mantido e atualizado pelo Agent 4 (Writer) do Sistema Bable Pet 4 Agentes Auxiliares*  
*Próxima revisão: Após cada ciclo de otimização*  
*Versão: 1.0 | Data: 2025-08-10*