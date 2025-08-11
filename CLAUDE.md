# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains the multi-agent system for **Bable Pet**, a pet service business that provides grooming, scheduling, commercial, and franchise services. The system is built as a collection of specialized AI agents coordinated through N8N workflows and integrated with ChatWoot and Evolution API for WhatsApp messaging.

## System Architecture

### Agent Hierarchy and Flow

The system follows a hierarchical agent architecture with clear delegation patterns:

1. **Agente Orquestrador** (`Prompt_ Agente Orquestrador Bable Pet_rev01.md`)
   - Central coordinator that analyzes customer messages
   - Identifies intentions: "AGENDAMENTO", "COMERCIAL", "FAQ", "FRANQUIA", "SAUDACAO", "INDEFINIDO"
   - Uses mandatory `think1` tool for reasoning
   - Returns JSON with `intencoes` array
   - **Key Rules:**
     - AGENDAMENTO always includes COMERCIAL (pricing questions are common)
     - COMERCIAL always includes AGENDAMENTO (customers may want to schedule after pricing)
     - SAUDACAO detection for greeting + action combinations

2. **Agente Saudação** (`Prompt_ Agente Saudação - Consultor_rev02.md`)
   - First interaction handler and context provider
   - Manages customer data retrieval and caching
   - Handles pure greetings and closed store scenarios
   - Delegates to specialists based on intentions
   - **Tools:** `buscarDadosCliente()`, `buscarScript()`
   - **Key Logic:** Store status checks, customer status (NOVO/CADASTRADO), delegation rules

3. **Agente Agendamento** (`Prompt_ Agente Agendamento - Consultor_rev01.md`)
   - Manages complete appointment lifecycle (create, reschedule, cancel)
   - Maintains "Ficha de Atendimento" internal memory
   - **Tools:** Calendar integration (`listarEvento`, `criarEvento`), spreadsheet management (`criaAtendimento`)
   - **Process Flow:** Customer data → Pet info → Service → Date → Time → Email → Confirmation
   - **Critical:** Always use `criaAtendimento` after `criarEvento`

4. **Agente Comercial** (`Prompt_ Agente Comercial - Consultor_rev02.md`) ✅ **OTIMIZADO**
   - Handles pricing inquiries and subscription offers with humanized approach
   - Maintains "Ficha Comercial" internal memory with contextual expertise
   - **Trigger Logic:** Expanded keywords ("preço", "valor", "quanto custa", "orçamento") + contextual validation
   - **Tools:** `racas_e_grupos()`, `precos_e_servicos()`, `buscaAssinantes()`, `precosAssinatura()`, `beneficiosAssinatura()`
   - **Process:** Pet size determination → **Breed contextualização** → Pricing lookup → **Humanized** subscription offers → **Natural transition to scheduling**
   - **Quality Score:** 8.6/10 (upgraded from 6.8/10) - **APPROVED**

5. **Agente Franquia** (`Prompt_ Agente Franquia - Consultor_rev01.md`)
   - Handles franchise inquiries and initial interest nurturing
   - **Tools:** `buscarInfoFranquia()` for investment and profit data
   - **Process:** Interest detection → Information gathering → Handoff to specialist

6. **Agente FAQ** (`Prompt_ Agente FAQ - Consultor_rev01.md`)
   - Handles general questions and support inquiries

7. **Agente Mestre** (`Prompt_ Agente Mestre - Bable Pet_rev01.md`)
   - Pure executor that takes `script_sugerido` and fills placeholders
   - **Only function:** Replace placeholders like `[Nome]` with customer data
   - **Critical:** Never adds, removes, or modifies content

### N8N Workflow Integration

The system runs on N8N with these key workflows:
- **Main Orchestrator:** `Agente Orquestrador e Mestre - Bable Pet (9).json`
- **Chat Integration:** `Integração CHAT WOOT e Evolution API - Bable Pet.json`
- **Specialized Consultants:** Individual JSON files for each agent type

### Data Flow Pattern

1. **Message Reception:** ChatWoot → N8N webhook
2. **Intent Analysis:** Orquestrador analyzes and categorizes
3. **Agent Delegation:** Saudação delegates to appropriate specialist
4. **Execution:** Specialist agent performs task and suggests script
5. **Message Assembly:** Mestre agent fills script placeholders
6. **Response:** Final message sent via Evolution API

## Agent Communication Protocol

### Standard JSON Response Format
All agents must return structured JSON reports in format `feedback_[agent_name]`:

```json
{
  "feedback_[agent]": {
    "script_id_sugerido": "SCRIPT_ID_OR_NULL",
    "script_sugerido": "FULL_SCRIPT_TEXT_OR_NULL", 
    "variaveis": { /* placeholder values */ },
    "analise": "Analysis summary",
    "status_operacao": { /* operation details */ }
  }
}
```

### Critical Integration Points

1. **Customer Data Consistency:** All agents inherit `dados_cliente` from Saudação
2. **Script Management:** Use `buscarScript(ID_Cenario)` for standardized responses
3. **State Management:** Each agent maintains internal "Ficha" for context
4. **Tool Usage:** Mandatory `think1` for reasoning, specific tools per agent
5. **Delegation Chain:** Clear priority handling through `prioridade_mestre` field

## Agent Quality Standards and Performance Metrics

### Primary Quality Metrics

**Main Metric: Response Quality and Human-like Context**
- **Human-like Interaction Score (0-10):** Agents must maintain conversational flow that feels natural and empathetic
- **Contextual Relevance Score (0-10):** Responses must be precisely relevant to customer intent and situation
- **Specialist Expertise Level (0-10):** Each agent must demonstrate deep domain knowledge in their area
- **Functional Logic Integrity (0-10):** All procedural steps and business rules must be followed without deviation

### Quality Monitoring and Control

**Performance Thresholds:**
- Minimum acceptable score: 8/10 across all metrics
- If any metric drops below 8/10: Immediate rollback to last functional version required
- Continuous monitoring via customer satisfaction feedback and conversation analysis

**Specialist Behavior Requirements:**
- Agents must work as domain experts, not generic assistants
- Maintain consistent personality and knowledge depth
- Provide proactive suggestions and insights within their specialty
- Demonstrate understanding of business context and customer journey

### Version Control and Quality Assurance

**Rollback Procedures:**
- All agent modifications must maintain backward-compatible functionality
- If response quality degrades, immediately revert to previous stable version
- New approaches must be tested in parallel before replacing functional versions
- Document all changes with quality impact assessment

**Database Content Enhancement:**
- Agents should identify gaps in available data and propose new content
- Suggest new scripts for common scenarios not covered
- Recommend database expansions based on customer interaction patterns
- Propose optimization of existing content for better user experience

## Development Guidelines

### Working with Agent Prompts

- Each agent has specific trigger conditions and scope limitations
- Follow the procedural steps exactly as defined in each prompt
- Maintain internal state through "Ficha" structures
- Always validate tool availability before use
- Use JSON schema validation for responses
- **Quality First:** Never deploy changes that reduce response quality or human-like interaction

### Testing Agent Interactions

- Test individual agents with mock inputs matching expected format
- Verify tool calls return expected data structures
- Validate JSON response format compliance
- Test delegation chains and priority handling

### Modifying Agent Behavior

- Agent prompts are version-controlled (e.g., `_rev01`, `_rev02`)
- Changes must maintain backward compatibility with N8N workflows
- Tool signatures must remain consistent across agents
- JSON response schemas are fixed contracts

### N8N Workflow Development

- Workflows are stored as JSON exports in `Fluxos N8N Json Versão 1/`
- Main orchestrator handles timeout management via Redis
- Integration workflow manages ChatWoot-Evolution API bridge
- Sub-workflows execute individual agent consultations

### Database Integration and Content Management

**Excel Database Structure (located in `Bancos de Dados/`):**
- **Comercial - Bable Pet (3).xlsx:** Pricing data, service catalog, subscription plans
- **Comportamento Integrado - Agente Bable Pet (3).xlsx:** Agent behavior patterns and responses
- **INPUT DADOS CHAT - Bable Pet (3).xlsx:** Customer data integration templates

**Database Access Tools:**
- `racas_e_grupos(raca: string)`: Pet size classification from breed data
- `precos_e_servicos(servico: string, grupo: string)`: Service pricing lookup
- `buscaAssinantes(sessionId: string)`: Customer subscription status
- `buscarScript(ID_Cenario: string)`: Standardized response templates
- `buscarDadosCliente(sessionId: string)`: Customer profile retrieval

**Content Enhancement Responsibilities:**
Agents should actively identify and propose:
- New scripts for unhandled customer scenarios
- Missing pricing data for service variations
- FAQ gaps discovered during interactions  
- Customer profile fields that would improve personalization
- Service categorizations that need refinement
- **Corporate information** gaps (use BANCO_DADOS_EMPRESA_BABLE_PET.md for company details)

**Database Quality Standards:**
- All database queries must complete within 2 seconds
- Data consistency across all agent interactions
- Immediate escalation if database returns null/empty for standard queries
- Regular content audits based on customer interaction patterns

## Key Business Rules

1. **Operating Hours:** System checks `statusFuncionamento` for ABERTO/FECHADO
2. **Customer Classification:** NOVO vs CADASTRADO affects script selection  
3. **Service Pricing:** Requires pet size/breed classification for accurate quotes
4. **Subscription Offers:** Non-members automatically get club membership offers
5. **Franchise Leads:** Qualified leads get handed off to human specialists

## File Structure

- `Prompt_*.md` - Individual agent instruction files
- `Fluxos N8N Json Versão 1/` - N8N workflow exports
- Each agent has corresponding N8N sub-workflow for execution

This system represents a sophisticated customer service automation with clear separation of concerns, robust state management, and seamless integration between AI agents and business systems.

---

## Ciclos de Otimização Concluídos

### Ciclo #001 - Agente Comercial Humanização (Concluído em 2025-08-10)

#### Resumo Executivo
- **Agente otimizado:** Agente Comercial (`Prompt_ Agente Comercial - Consultor`)
- **Versão:** rev01 → rev02  
- **Problema identificado:** Score de qualidade 6.8/10 (abaixo do threshold mínimo de 8.0/10)
- **Solução implementada:** Humanização completa com contextualização por raça e abordagem empática
- **Resultados:** 6.8/10 → 8.6/10 (Score médio em 5 cenários de teste)
- **Status:** ✅ **APROVADO** - Sistema em produção

#### Melhorias Implementadas na Rev02

1. **Contextualização Empática por Raça**
   - Adicionada expertise específica sobre características de cada raça de pet
   - Conexão emocional antes da apresentação de preços
   - Exemplo: "Que fofinho! Poodles têm uma pelagem linda que precisa de cuidados especiais"

2. **Humanização da Abordagem Comercial**
   - Tom consultivo ao invés de robótico
   - Uso frequente dos nomes do cliente e pet
   - Cálculo e apresentação da economia específica para cada caso
   - Scripts otimizados: `INFORMAR_PRECO_COM_OFERTA_CLUBE_HUMANIZADO`, `INFORMAR_PRECO_ASSINANTE_VIP`

3. **Transição Natural para Agendamento**
   - Toda cotação agora inclui ponte natural para próximo passo
   - Integração fluida entre agentes Comercial e Agendamento
   - Exemplos: "Que tal agendarmos o primeiro banho da Lira?", "Quer que eu já te ajude a agendar?"

4. **Triggers Expandidos de Ativação**
   - Palavras-chave ampliadas: "preço", "valor", "quanto custa", "orçamento", "custa quanto"
   - Validação contextual para evitar ativações incorretas
   - Mantida regra de não interferência quando gatilho não é ativado

#### Cenários Validados com Sucesso
1. **Cliente Novo Consultando Preço de Banho** - Score: 8.8/10
2. **Cliente Cadastrado Perguntando Valor da Tosa** - Score: 8.5/10  
3. **Consulta de Preços com Pet de Raça Específica** - Score: 8.9/10
4. **Cliente Assinante Solicitando Orçamento** - Score: 8.4/10
5. **Transição Natural para Agendamento** - Score: 8.4/10

#### Métricas Alcançadas
- **Score de Qualidade Médio:** 8.6/10 ✅
- **Naturalidade:** 9.0/10 ✅
- **Expertise Demonstrada:** 9.0/10 ✅
- **Personalização:** 8.5/10 ✅
- **Transição para Agendamento:** 8.5/10 ✅
- **Empatia:** 9.0/10 ✅

#### Sistema 4 Agentes Auxiliares - Eficácia Comprovada
- **Tempo total do ciclo:** ~4 horas
- **Agents utilizados:** Architect → Builder → Validator → Writer
- **Taxa de aprovação:** 100% (5/5 cenários aprovados)
- **Processo totalmente autônomo:** Sem intervenção humana necessária

#### Próximas Otimizações Sugeridas
1. **Agente Agendamento** - Prioridade: Alta (Score estimado atual: 7.2/10)
2. **Agente FAQ** - Prioridade: Média (Score estimado atual: 7.8/10)  
3. **Agente Franquia** - Prioridade: Média (Score estimado atual: 7.5/10)