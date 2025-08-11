# Template: Geração de Cenários de Teste com Conversas Humanas Realistas - Integração Claude Auto-Optimizer

> **🔗 INTEGRAÇÃO COMPLETA**: Testes A/B + n8n + GitHub + Claude Auto-Optimizer

## 📋 IDENTIFICAÇÃO DO CENÁRIO

**ID do Cenário:** [CENARIO_XXX]  
**Data de Criação:** [DD/MM/YYYY]  
**Criado por:** Agent [1-4]  
**Complexidade:** [BAIXA|MÉDIA|ALTA|EXTREMA]  
**Tipo de Cliente:** [NOVO|CADASTRADO|ASSINANTE|INSATISFEITO|PRIMEIRA_VEZ]

---

## 🎯 OBJETIVO DO TESTE

### Funcionalidade Alvo
- **Agente Principal**: [Saudação|Agendamento|Comercial|Franquia|FAQ|Indefinido]
- **Agentes Secundários**: [outros agentes que devem ser acionados]
- **Fluxo Esperado**: [sequência de ações esperadas]

### Aspectos a Validar
- [ ] **Identificação de intenção**: Orquestrador identifica corretamente
- [ ] **Delegação**: Saudação delega para agente correto
- [ ] **Coleta de dados**: Agente coleta informações necessárias
- [ ] **Consulta de bases**: Ferramentas funcionam corretamente
- [ ] **Resposta final**: Script adequado e bem personalizado
- [ ] **Naturalidade**: Resposta parece humana, não robótica

---

## 🎭 CONTEXTO DO CLIENTE

### Perfil do Cliente
**Nome:** [Nome realista brasileiro]  
**Status:** [Novo cliente|Cliente cadastrado|Assinante clube|Ex-cliente]  
**Pet:** [Nome do pet] - [Raça] - [Porte G1-G5]  
**Histórico:** [breve histórico relevante]  

### Estado Emocional
- **Tom da conversa**: [Amigável|Neutro|Impaciente|Frustrado|Ansioso|Apressado]
- **Nivel de conhecimento**: [Primeira vez|Conhece serviços|Cliente experiente]
- **Expectativa**: [O que o cliente espera alcançar]

### Contexto Situacional
- **Horário**: [Dentro do expediente|Fora do horário|Próximo ao fechamento]  
- **Urgência**: [Normal|Urgente|Emergência]
- **Canal**: WhatsApp (padrão do sistema)
- **Dispositivo**: [Mobile|Desktop - afeta como cliente digita]

---

## 💬 CONVERSAS REALISTAS

### Cenário Base: Mensagem Inicial do Cliente
```
Cliente: "[mensagem exatamente como cliente real digitaria]"
```

**Variações da Mensagem** (para testar robustez):
```
Variação 1: "[forma mais direta]"
Variação 2: "[forma mais elaborada]" 
Variação 3: "[com erros de digitação/gírias]"
Variação 4: "[mensagem ambígua]"
```

### Fluxo de Conversa Completa (Exemplo)
```
🔵 Cliente: "oi boa tarde, queria saber quanto fica um banho pro meu golden"

🤖 Sistema: [resposta esperada do sistema]

🔵 Cliente: "ah, ele é grande sim, tipo uns 35kg. quanto fica?"

🤖 Sistema: [resposta esperada]

🔵 Cliente: [continuação natural da conversa]
```

### Cenários de Resposta do Cliente
**Se sistema pede dados:**
```
Resposta cooperativa: "Claro! O nome dele é Thor, é um Golden Retriever"
Resposta incompleta: "Golden"  
Resposta confusa: "É grande, dourado, sabe?"
```

**Se sistema oferece opções:**
```
Escolha clara: "Quero o banho completo"
Indecisão: "Hmm, qual a diferença mesmo?"
Mudança de ideia: "Na verdade, quero só cortar a unha"
```

---

## 📊 RESULTADOS ESPERADOS

### Agentes que Devem ser Acionados
1. **Orquestrador**: Deve identificar intenção "[INTENÇÃO]"  
2. **Saudação**: Deve delegar para "[AGENTE_ESPECIALISTA]"
3. **[Especialista]**: Deve executar "[AÇÃO_ESPECÍFICA]"  
4. **Mestre**: Deve usar script "[ID_SCRIPT]"

### Dados que Devem ser Coletados
- **Cliente**: [nome, telefone, status]
- **Pet**: [nome, raça, grupo G1-G5]  
- **Serviço**: [tipo específico solicitado]
- **Contexto adicional**: [outros dados relevantes]

### Script Final Esperado
**ID do Script**: [ID_CENARIO_ESPERADO]  
**Personalização**: [quais placeholders devem ser preenchidos]  
**Tom**: [cordial, profissional, empático, etc.]

### Métricas de Sucesso
- **Tempo de resposta**: < 2 segundos por interação  
- **Taxa de identificação**: 100% das intenções corretas
- **Coleta de dados**: 100% dos dados necessários obtidos  
- **Qualidade da resposta**: Score ≥ 8/10 em naturalidade
- **Fluxo completo**: Do início ao script final sem erros

---

## 🔄 VARIAÇÕES E EDGE CASES

### Variações de Complexidade

#### BAIXA - Fluxo Linear
```
Cliente: "Quero agendar banho para minha poodle"
Fluxo: Saudação → Agendamento → Dados → Confirmação
Desafio: Nenhum, fluxo padrão
```

#### MÉDIA - Múltiplas Intenções  
```
Cliente: "Oi! Quero remarcar o banho da Lola e saber preço da tosa"
Fluxo: Saudação → Agendamento (remarcar) + Comercial (preço)
Desafio: Duas intenções simultâneas
```

#### ALTA - Cliente Frustrado
```
Cliente: "TODA VEZ QUE VENHO AQUI VCS ATRASAM! QUERO CANCELAR TUDO!"
Fluxo: Saudação → Agendamento (cancelar) + Tratamento de reclamação
Desafio: Tom emocional + intenção negativa
```

#### EXTREMA - Cenário Complexo
```
Cliente: "Minha cachorra tá com alergia depois do último banho, vocês podem me ressarcir? E outra coisa, quero saber sobre franquia em outra cidade"
Fluxo: FAQ (reclamação) + Franquia + possível Agendamento veterinário
Desafio: Múltiplas questões, tom de reclamação, mudança de tópico
```

---

## 🧪 INSTRUÇÕES DE TESTE

### 🔗 **NOVO: Integração com Claude Auto-Optimizer**

#### Fluxo de Teste A/B Integrado
```bash
# 1. TESTE LOCAL (Versão Otimizada)
python claude-auto-optimizer/claude_auto_optimizer.py test-scenario [cenario-id]
# Executa cenário com prompts otimizados localmente

# 2. TESTE PRODUÇÃO (Versão Atual)
curl -X POST "$WEBHOOK_URL" [...] 
# Executa mesmo cenário no n8n atual

# 3. COMPARAÇÃO AUTOMÁTICA
python claude-auto-optimizer/compare_results.py [execution-id-1] [execution-id-2]
# Compara métricas: tempo, qualidade, tokens

# 4. DECISÃO APLICAÇÃO
if score_otimizado > score_atual + 0.5:
    python claude-auto-optimizer/apply_optimization.py [workflow-id]
    # Só aplica se melhoria significativa (>0.5 pontos)
```

### Para o Agent 3 (Validator)

#### Passo 1: Preparação
```bash
# Usar webhook de teste (sem envio real WhatsApp)
export WEBHOOK_URL="https://n8n.synapseautointeligente.com.br/webhook/[test-id]"
```

#### Passo 2: Execução do Cenário
```bash
curl -X POST "$WEBHOOK_URL" \
-H "Content-Type: application/json" \
-d '{
  "content": "[MENSAGEM_DO_CLIENTE]",
  "sender": {
    "name": "[NOME_CLIENTE_TESTE]",
    "phone_number": "+5519999999999"
  }
}'
```

#### Passo 3: Análise de Logs
- Verificar logs no GitHub: debug_logs/debug_YYYY-MM-DD_*.json
- Validar sequência de agentes acionados
- Conferir dados coletados e scripts sugeridos

### Critérios de Aprovação
- [ ] **Intenção identificada corretamente**
- [ ] **Agente especialista acionado**  
- [ ] **Dados coletados completamente**
- [ ] **Script final apropriado**
- [ ] **Tom natural e empático**
- [ ] **Tempo de resposta <2s**

---

## 📈 MÉTRICAS E ACOMPANHAMENTO

### 📊 **NOVAS MÉTRICAS A/B Testing**

#### Comparação Automática
```json
{
  "scenario_id": "AGENDAMENTO_BAIXA_PRIMEIRO_001",
  "test_results": {
    "current_version": {
      "response_time": 2.3,
      "success_rate": 0.87,
      "human_score": 7.2,
      "token_usage": 245
    },
    "optimized_version": {
      "response_time": 1.8,
      "success_rate": 0.94,
      "human_score": 8.6,
      "token_usage": 198
    },
    "improvement": {
      "response_time": "-21.7%",
      "success_rate": "+8.0%", 
      "human_score": "+19.4%",
      "token_efficiency": "+19.2%",
      "overall_score": 8.1
    },
    "recommendation": "APPLY - Melhoria significativa em todas métricas"
  }
}
```

### Coleta de Dados Pós-Teste
**Execution ID**: [obtido dos logs N8N]  
**Agentes Acionados**: [lista real vs esperada]  
**Tempo Total**: [segundos]  
**Taxa de Sucesso**: [% de objetivos alcançados]

### Classificação de Resultado
- **✅ PASSOU**: Todos os critérios atendidos (Score ≥ 8/10)
- **⚠️ PASSOU COM RESSALVAS**: Funcional mas pode melhorar (Score 6-7/10)  
- **❌ FALHOU**: Não atende critérios mínimos (Score <6/10)

### Feedback para Próxima Iteração
**Se FALHOU:**
- [ ] Ajustar prompt do agente [qual agente]
- [ ] Corrigir dados da base [qual base/campo]  
- [ ] Criar novo script [ID necessário]
- [ ] Melhorar trigger de identificação

**Se PASSOU:**
- [ ] Adicionar cenário ao catálogo oficial
- [ ] Criar variações similares
- [ ] Documentar lições aprendidas

---

## 📚 BIBLIOTECA DE CENÁRIOS

### Categorias de Cenários
- **AGENDAMENTO**: Primeiro agendamento, reagendamento, cancelamento
- **COMERCIAL**: Preços, promoções, planos de assinatura  
- **FRANQUIA**: Interesse inicial, qualificação, handoff
- **FAQ**: Dúvidas gerais, horários, vacinas, políticas
- **FAQ_EMPRESA**: História, diferenciais, unidades, missão (usar BANCO_DADOS_EMPRESA_BABLE_PET.md)
- **EMERGÊNCIA**: Pet machucado, urgência veterinária
- **RECLAMAÇÃO**: Insatisfação, reembolso, problemas

### Cenários FAQ Empresariais (Exemplos com Base Real)

#### FAQ_EMPRESA_BAIXA_HISTORIA_001
```
Cliente: "Como surgiu a Bable Pet? Qual a história de vocês?"
Dados da Base: História do Tito (cão dos fundadores), problema com ruído, solução criativa
Resposta Esperada: História pessoal + evolução para empresa + diferencial criado
```

#### FAQ_EMPRESA_MÉDIA_DIFERENCIAIS_002  
```
Cliente: "O que vocês têm de diferente dos outros pet shops? Por que escolher vocês?"
Dados da Base: Sem agendamento + ambiente spa + isolamento acústico + feromônios
Resposta Esperada: Lista dos 6 diferenciais principais + benefícios para o pet
```

#### FAQ_EMPRESA_ALTA_EXPANSAO_003
```
Cliente: "Vocês têm unidade em Campinas? E em outras cidades? Como funciona a franquia?"
Dados da Base: Lista de unidades atuais + modelo de franquia + investimento
Resposta Esperada: Unidades confirmadas + processo de expansão + direcionamento franquia
```

### Template de Nomeação
**Formato**: [CATEGORIA]_[COMPLEXIDADE]_[SITUAÇÃO]_[NUMERO]  
**Exemplos**:
- AGENDAMENTO_BAIXA_PRIMEIRO_001
- COMERCIAL_MÉDIA_MULTIPLOS_PETS_002  
- FRANQUIA_ALTA_CLIENTE_IMPACIENTE_003

---

*Este template deve ser usado pelo Agent 1 (Architect) para criar cenários realistas que testem todas as funcionalidades dos agentes Bable Pet em situações que espelhem conversas reais de clientes.*