# 🗂️ Mapeamento Planilhas Google Drive - Sistema Bable Pet

> **Finalidade**: Guia para identificar quais planilhas modificar no Google Drive
> **Uso**: Agent 2 (Builder) usa para indicar onde você deve fazer modificações
> **Data**: 09/08/2025

---

## 📊 **PLANILHAS PRINCIPAIS NO GOOGLE DRIVE**

### **1. Base Comercial - Preços e Serviços**
- **📁 Nome**: `Bable Pet - Base Comercial`  
- **🔗 Função**: `precos_e_servicos()`, `racas_e_grupos()`
- **📋 Abas Atuais**:
  - `Precos_Servicos` - Valores por grupo/porte
  - `Racas_Grupos` - Classificação G1-G5
  - `Promocoes` - Ofertas especiais
- **🎯 Usado pelos agentes**: Comercial, Saudação

### **2. Base Clientes - Cadastros e Assinantes**  
- **📁 Nome**: `Bable Pet - Base Clientes`
- **🔗 Função**: `buscarDadosCliente()`, `buscaAssinantes()`
- **📋 Abas Atuais**:
  - `Clientes_Cadastrados` - Dados pessoais
  - `Historico_Atendimentos` - Registros passados
  - `Assinantes_Clube` - Membros ativos
- **🎯 Usado pelos agentes**: Saudação, Agendamento, Comercial

### **3. Base Scripts - Comportamentos**
- **📁 Nome**: `Bable Pet - Scripts Respostas`
- **🔗 Função**: `buscarScript()`
- **📋 Abas Atuais**:
  - `Scripts_Saudacao` - Primeiros contatos
  - `Scripts_Agendamento` - Confirmações
  - `Scripts_Comercial` - Ofertas
  - `Scripts_FAQ` - Respostas padrão
- **🎯 Usado pelos agentes**: Todos via Mestre

---

## 🔄 **PROCESSO DE MODIFICAÇÃO GOOGLE SHEETS**

### **Quando Agent 1 Propõe Mudança nos Bancos:**

```markdown
### Exemplo de Proposta Agent 1:
**Problema**: racas_e_grupos("vira-lata") retorna null em 90% dos casos
**Solução**: Criar aba "Racas_Fallback" na planilha "Base Comercial"
**Estrutura**:
- Coluna A: Raca_Popular (vira-lata, SRD, etc.)
- Coluna B: Grupo_Equivalente (G3, G2, etc.)
- Coluna C: Observacoes (características)
```

### **Agent 2 Especifica e Para:**

```markdown
### 🔄 ATUALIZAÇÃO GOOGLE SHEETS NECESSÁRIA - [DATA]

**📊 PLANILHA ALVO:**
- 🔗 **Nome**: `Bable Pet - Base Comercial`
- 📍 **Aba nova**: `Racas_Fallback`
- 📋 **Localização**: Após aba "Racas_Grupos"

**👤 INSTRUÇÕES PARA MODIFICAÇÃO:**
1. Acesse Google Drive → Planilha "Bable Pet - Base Comercial"
2. Clique com direito nas abas → "Inserir nova aba"
3. Nome da aba: "Racas_Fallback"
4. Insira estrutura conforme especificado:

| A (Raca_Popular) | B (Grupo_Equivalente) | C (Observacoes) |
|---|---|---|
| vira-lata | G3 | Porte médio/grande |
| SRD | G3 | Sem raça definida |
| pinscher | G1 | Pequeno porte |
| yorkshire | G1 | Toy |

5. Salve a planilha
6. Verifique se agentes têm acesso via API
7. Responda: "✅ Aba Racas_Fallback criada na Base Comercial"

**🚫 BLOQUEIO ATIVO:**
- Agent 3 aguarda confirmação para testar
- Função racas_e_grupos() só funciona após atualização
```

---

## 📍 **LINKS E ACESSOS**

### **Planilhas Google Drive Bable Pet:**
*(Links específicos devem ser atualizados conforme suas planilhas reais)*

```
📊 Base Comercial:
https://docs.google.com/spreadsheets/d/[ID_BASE_COMERCIAL]/edit

📊 Base Clientes:  
https://docs.google.com/spreadsheets/d/[ID_BASE_CLIENTES]/edit

📊 Scripts Respostas:
https://docs.google.com/spreadsheets/d/[ID_SCRIPTS]/edit
```

### **Permissões Necessárias:**
- ✅ **Leitura**: N8N workflows via API Google
- ✅ **Escrita**: Você via interface Google Drive
- ✅ **Compartilhamento**: Com conta de serviço N8N

---

## 🛠️ **TIPOS DE MODIFICAÇÃO COMUNS**

### **1. Nova Aba/Sheet**
```markdown
**Quando**: Funcionalidade completamente nova
**Exemplo**: Criar "Emergencias_Veterinarias" para casos urgentes
**Tempo**: 5-10 minutos
**Impacto**: Baixo (não quebra nada existente)
```

### **2. Adicionar Colunas**
```markdown
**Quando**: Expandir dados existentes
**Exemplo**: Adicionar coluna "Telefone_WhatsApp" em Clientes
**Tempo**: 2-3 minutos
**Impacto**: Médio (pode afetar consultas)
```

### **3. Unificar Abas**
```markdown
**Quando**: Eliminar fragmentação
**Exemplo**: Combinar "Precos_Banho" + "Precos_Tosa" = "Precos_Servicos"
**Tempo**: 15-20 minutos
**Impacto**: Alto (requer atualização de prompts)
```

### **4. Corrigir Dados**
```markdown
**Quando**: Inconsistências identificadas
**Exemplo**: Padronizar "Golden" vs "Golden Retriever"
**Tempo**: 5-15 minutos dependendo volume
**Impacto**: Baixo (melhoria de qualidade)
```

---

## 🧪 **VALIDAÇÃO PÓS-MODIFICAÇÃO**

### **Checklist Obrigatório:**
Após modificar qualquer planilha, verifique:

- [ ] **Estrutura**: Cabeçalhos corretos nas colunas
- [ ] **Dados**: Pelo menos 3-5 exemplos preenchidos
- [ ] **Acesso**: N8N consegue ler via API (teste rápido)
- [ ] **Consistência**: Padrões mantidos com outras abas
- [ ] **Backup**: Versão anterior salva se necessário

### **Teste Rápido no N8N:**
```bash
# Após modificar planilha, teste rapidamente:
curl -X POST "[webhook_url]" \
-d '{"content": "[teste que usa a função modificada]"}'

# Exemplo para racas_e_grupos():
curl -X POST "[webhook_url]" \
-d '{"content": "Quanto custa banho pra vira-lata?"}'
```

---

## 🔄 **FLUXO COMPLETO DE EXEMPLO**

### **Cenário**: Problema com raças não catalogadas

```bash
# FLUXO REAL DE TRABALHO:

1️⃣ Agent 1 (Architect): 
   "Identifiquei: racas_e_grupos() falha em 40% dos casos"

2️⃣ Agent 2 (Builder):
   "Especificação: Criar aba Racas_Fallback na Base Comercial"
   "🛑 PAUSANDO - Atualização manual necessária!"

3️⃣ 👤 VOCÊ (5-8 minutos):
   - Abre Google Drive
   - Vai em "Bable Pet - Base Comercial" 
   - Cria aba "Racas_Fallback"
   - Preenche estrutura especificada
   - Salva planilha
   - Responde: "✅ Aba Racas_Fallback criada"

4️⃣ Agent 3 (Validator):
   "Testando função racas_e_grupos() com nova aba..."
   "✅ Sucesso: 95% dos casos agora funcionam!"

5️⃣ Agent 4 (Writer):
   "Documentando: Nova aba criada, links atualizados"
```

---

## ⚠️ **PONTOS DE ATENÇÃO ESPECIAIS**

### **Google Sheets Limitações:**
- 📊 **API Rate Limit**: 100 requests/100s/user
- 📊 **Concurrent Access**: Máximo 10 leituras simultâneas
- 📊 **Cell Limit**: 10 milhões células por planilha
- 📊 **Query Timeout**: 30 segundos máximo

### **N8N Integration:**
- 🔧 **Service Account**: Deve ter acesso a todas planilhas
- 🔧 **Scope**: `https://www.googleapis.com/auth/spreadsheets`
- 🔧 **Caching**: N8N pode cachear resultados por 5-10 min
- 🔧 **Error Handling**: Falhas de API devem ter fallback

### **Backup e Rollback:**
- 💾 **Sempre** faça cópia antes modificações grandes
- 💾 **Versionamento**: Use "Arquivo → Histórico de versões"
- 💾 **Rollback**: Fácil restaurar versão anterior se necessário

---

## 🎯 **TEMPLATE PARA AGENT 2 USAR**

### **Padrão de Comunicação:**

```markdown
### 🔄 MODIFICAÇÃO GOOGLE SHEETS NECESSÁRIA - [DATA]

**📊 PLANILHA ALVO:**
- 🔗 **Nome**: `[Nome da Planilha]`
- 📍 **Modificação**: [Nova aba / Adicionar colunas / Unificar / Corrigir]
- ⏰ **Tempo estimado**: [X] minutos

**📋 ESPECIFICAÇÃO DETALHADA:**
[Estrutura exata com colunas, dados exemplo, etc.]

**👤 INSTRUÇÕES PASSO-A-PASSO:**
1. [Passo 1 específico]
2. [Passo 2 específico]
3. [Passo 3 específico]
4. Responda: "✅ [Modificação] concluída em [Planilha]"

**🚫 BLOQUEIO**: Agent 3 aguarda confirmação para testar APIs
**🎯 FUNÇÃO AFETADA**: [racas_e_grupos() / precos_e_servicos() / etc.]
```

---

**🎯 LEMBRE-SE**: As planilhas Google Drive são o **coração dos dados** do sistema. Toda modificação deve ser **cuidadosa, testada e documentada**! 📊🛡️

*Mapeamento atualizado para integração manual Google Sheets - 09/08/2025*