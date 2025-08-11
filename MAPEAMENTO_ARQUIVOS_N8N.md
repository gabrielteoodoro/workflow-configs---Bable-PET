# 🗺️ Mapeamento Arquivos → N8N Workflows

> **Finalidade**: Guia para saber qual arquivo .md corresponde a qual workflow N8N
> **Uso**: Agent 2 (Builder) usa para indicar onde você deve colar os prompts editados
> **Data**: 09/08/2025

---

## 📋 **MAPEAMENTO PRINCIPAL**

### **Agentes Principais Bable Pet**

| Arquivo Local (.md) | Workflow N8N Correspondente | ID/Descrição |
|---|---|---|
| `Prompt_ Agente Orquestrador Bable Pet_rev01.md` | **Agente Orquestrador - Bable Pet** | Central coordinator |
| `Prompt_ Agente Saudação - Consultor_rev02.md` | **Consultor Saudação - Bable Pet** | First interaction |
| `Prompt_ Agente Agendamento - Consultor_rev01.md` | **Consultor Agendamento - Bable Pet** | Appointment management |
| `Prompt_ Agente Comercial - Consultor_rev01.md` | **Consultor Comercial - Bable Pet** | Pricing inquiries |
| `Prompt_ Agente Franquia - Consultor_rev01.md` | **Consultor Franquia - Bable Pet** | Franchise inquiries |
| `Prompt_ Agente FAQ - Consultor_rev01.md` | **Consultor FAQ - Bable Pet** | General questions |
| `Prompt_ Agente Indefinido - Consultor_rev01.md` | **Consultor Indefinido - Bable Pet** | Undefined intentions |
| `Prompt_ Agente Mestre - Bable Pet_rev01.md` | **Agente Mestre - Bable Pet** | Script executor |

---

## 🎯 **COMO USAR ESTE MAPEAMENTO**

### **Para Agent 2 (Builder):**
Quando editar um arquivo, sempre inclua na sua resposta:

```markdown
**🔄 AÇÃO MANUAL OBRIGATÓRIA:**

1. **📋 Arquivo editado**: `Prompt_ Agente Comercial - Consultor_rev01.md`
2. **🎯 Workflow N8N**: **Consultor Comercial - Bable Pet**
3. **👤 Ação necessária**: Copie o prompt editado e cole no campo correspondente do workflow
4. **📍 Localização**: Node "Execute Workflow" → Campo "Prompt" 
5. **⏰ Tempo estimado**: 2-3 minutos
```

### **Para Você (Operador):**
1. ✅ **Leia** a indicação do Agent 2
2. ✅ **Abra** o N8N no workflow indicado  
3. ✅ **Copie** o prompt editado do arquivo .md
4. ✅ **Cole** no campo correspondente do workflow
5. ✅ **Salve** o workflow
6. ✅ **Responda**: "Prompt atualizado no N8N"

---

## 📁 **ESTRUTURA DOS WORKFLOWS N8N**

### **Workflow Principal:**
```
Agente Orquestrador e Mestre - Bable Pet (9).json
├── Node: Orquestrador Analysis
│   └── Campo: "Prompt Orquestrador"
└── Node: Execute Sub-workflows
    ├── Consultor Saudação
    ├── Consultor Agendamento  
    ├── Consultor Comercial
    ├── Consultor Franquia
    ├── Consultor FAQ
    ├── Consultor Indefinido
    └── Agente Mestre
```

### **Sub-workflows Individuais:**
Cada agente tem seu próprio sub-workflow:
- **Entrada**: Recebe dados do orquestrador
- **Processamento**: Executa prompt específico
- **Ferramentas**: Acessa APIs (Google Sheets, etc.)
- **Saída**: Retorna JSON estruturado

---

## 🔄 **PROCESSO PASSO-A-PASSO**

### **Quando Agent 2 Edita um Prompt:**

#### **Passo 1: Agent 2 Implementa**
```markdown
Agent 2 edita: "Prompt_ Agente Comercial - Consultor_rev01.md"
Agent 2 indica: "Workflow correspondente: Consultor Comercial - Bable Pet"
```

#### **Passo 2: Você Atualiza N8N**
1. Abra N8N
2. Vá para workflow "Consultor Comercial - Bable Pet"
3. Encontre o node com o prompt do agente
4. Copie o conteúdo completo do arquivo editado
5. Cole no campo "Prompt" ou "System Message"
6. Salve o workflow

#### **Passo 3: Confirmação**
```bash
# Você responde:
"✅ Prompt Agente Comercial atualizado no N8N - Workflow salvo"
```

#### **Passo 4: Agent 3 Testa**
Só agora Agent 3 pode executar testes na versão nova!

---

## ⚠️ **PONTOS DE ATENÇÃO**

### **Backup Obrigatório:**
- ✅ **Sempre** faça backup do prompt anterior antes substituir
- ✅ **Salve** versão anterior com timestamp
- ✅ **Teste** básico após alterar

### **Campos Específicos N8N:**
- 🎯 **System Message**: Prompt principal do agente
- 🎯 **User Message**: Contexto/instruções específicas  
- 🎯 **Temperature**: Geralmente 0.7-0.9
- 🎯 **Max Tokens**: Conforme necessidade

### **Validação Rápida:**
Após colar o prompt:
```bash
# Teste rápido no próprio N8N:
Input: "teste rápido"
Output: [deve responder conforme novo comportamento]
```

---

## 📊 **TEMPLATE DE ATUALIZAÇÃO**

### **Para Agent 2 usar sempre:**

```markdown
### 🔄 ATUALIZAÇÃO N8N NECESSÁRIA - [DATA]

**📁 ARQUIVO(S) EDITADO(S):**
- ✅ `[arquivo.md]` - [descrição da mudança]

**🎯 WORKFLOW(S) CORRESPONDENTE(S):**
- 🔗 **[Nome do Workflow N8N]**
  - 📍 **Node**: [nome do node específico]  
  - 📝 **Campo**: [System Message/User Message/etc.]
  - ⏰ **Tempo**: 2-3 minutos

**👤 INSTRUÇÕES PARA ATUALIZAÇÃO:**
1. Abra N8N → Workflow "[Nome]"
2. Localize node "[Node name]"
3. Copie INTEGRALMENTE o arquivo `[arquivo.md]`
4. Cole no campo "[Campo]"
5. Salve workflow
6. Responda: "✅ [Arquivo] atualizado no N8N"

**🚫 BLOQUEIO ATIVO:**
- Agent 3 (Validator) aguarda confirmação
- Testes só executam após atualização
```

---

## 🔮 **FUTURA AUTOMAÇÃO (ROADMAP)**

### **Fase 2 - Semi-Automática:**
- 🔧 **Script Python** para sincronizar arquivos
- 🔧 **API N8N** para atualizar workflows
- 🔧 **Backup automático** antes alterar

### **Fase 3 - Totalmente Automática:**
- 🔧 **Git hooks** para detectar mudanças
- 🔧 **CI/CD pipeline** para deploy automático
- 🔧 **Rollback automático** se testes falharem

### **Estimativa:**
- **Fase 2**: 2-3 dias desenvolvimento
- **Fase 3**: 1-2 semanas desenvolvimento
- **ROI**: Economiza 2-3 min por mudança

---

## 🎯 **CHECKLIST DE VERIFICAÇÃO**

### **Antes de Testar (Agent 3):**
- [ ] Agent 2 concluiu implementação local
- [ ] Arquivo .md foi editado e salvo
- [ ] Workflow N8N foi identificado corretamente
- [ ] Prompt foi copiado e colado no N8N
- [ ] Workflow N8N foi salvo
- [ ] Confirmação "Atualizado no N8N" foi dada
- [ ] ✅ **AGORA** Agent 3 pode testar!

### **Pós-Atualização:**
- [ ] Teste rápido no N8N funcionou
- [ ] Comportamento novo está ativo
- [ ] Backup da versão anterior foi feito
- [ ] Agent 3 pode prosseguir com bateria completa

---

**🎯 LEMBRE-SE**: Este processo manual garante **controle total** e **segurança máxima**. Cada mudança é aprovada por você antes ir para produção! 🛡️

*Mapeamento atualizado conforme estrutura atual N8N Bable Pet - 09/08/2025*