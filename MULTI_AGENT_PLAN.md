# MULTI_AGENT_PLAN.md - Planejamento Compartilhado Bable Pet

> **Documento de coordenação entre Agent 1 (Architect), Agent 2 (Builder), Agent 3 (Validator) e Agent 4 (Writer)**
> 
> **Última Atualização Geral**: 2025-01-08 15:30 por Claude Code

---

## 🎯 OBJETIVO ATUAL DO PROJETO
**Otimização e Manutenção do Sistema Multi-Agente Bable Pet**

### Escopo Atual
- Sistema com 7 agentes especializados (Orquestrador, Saudação, Agendamento, Comercial, Franquia, FAQ, Mestre)
- Integração N8N + ChatWoot + Evolution API
- Fluxos de atendimento automatizado para pet shop

---

## 📋 TAREFAS ATIVAS

### Tarefa: Análise Arquitetural do Sistema Atual
- **Atribuído a**: Agent 1 (Architect)
- **Status**: Pronto para Iniciar
- **Prioridade**: Alta
- **Descrição**: Mapear estado atual do sistema, identificar pontos de melhoria e criar roadmap de otimizações
- **Observações**: Foco em interações entre agentes e performance dos workflows N8N
- **Última Atualização**: 2025-01-08 15:30 por Claude Code

### Tarefa: Implementação de Melhorias Identificadas
- **Atribuído a**: Agent 2 (Builder)  
- **Status**: Aguardando Dependências
- **Prioridade**: Alta
- **Dependências**: Aguardando análise completa do Agent 1 (Architect)
- **Descrição**: Implementar modificações nos prompts, workflows e integrações conforme especificações
- **Última Atualização**: 2025-01-08 15:30 por Claude Code

### Tarefa: Validação de Sistema e Testes
- **Atribuído a**: Agent 3 (Validator)
- **Status**: Aguardando Dependências  
- **Prioridade**: Alta
- **Dependências**: Aguardando implementações do Agent 2 (Builder)
- **Descrição**: Executar testes completos de agentes individuais, fluxos integrados e cenários de negócio
- **Observações**: Incluir testes de performance e casos extremos
- **Última Atualização**: 2025-01-08 15:30 por Claude Code

### Tarefa: Atualização da Documentação
- **Atribuído a**: Agent 4 (Writer)
- **Status**: Em Progresso Contínuo
- **Prioridade**: Média
- **Descrição**: Manter documentação atualizada com todas as modificações e criar guias de uso
- **Observações**: Documentar padrões descobertos e melhores práticas
- **Última Atualização**: 2025-01-08 15:30 por Claude Code

---

## 🔄 FLUXO DE TRABALHO ESTABELECIDO

### Sequência Padrão
1. **Architect** → Analisa e planeja
2. **Builder** → Implementa baseado no plano
3. **Validator** → Testa e valida implementação
4. **Writer** → Documenta e refina

### Comunicação Entre Agentes
- **Architect → Builder**: Especificações técnicas detalhadas
- **Builder → Validator**: Implementações para teste e critérios de validação
- **Validator → Writer**: Resultados de teste e issues encontrados
- **Writer → Architect**: Feedback de documentação e sugestões de melhoria

---

## 📊 STATUS GERAL DO PROJETO

### Métricas de Progresso
- **Análise Arquitetural**: 0% (Não iniciado)
- **Implementação**: 0% (Aguardando)
- **Validação**: 0% (Aguardando)
- **Documentação**: 15% (CLAUDE.md criado, agents definidos)

### Riscos Identificados
- *Nenhum risco crítico identificado no momento*

### Próximas Reuniões/Reviews
- **Review Arquitetural**: Após conclusão da análise pelo Agent 1
- **Review de Implementação**: Após conclusão das implementações pelo Agent 2
- **Review de Qualidade**: Após validação completa pelo Agent 3

---

## 🎯 OBJETIVOS ESPECÍFICOS POR SPRINT

### Sprint Atual: Análise e Planejamento
**Duração**: Até definição completa do roadmap
**Objetivos**:
- [x] Criar estrutura de 4 agentes especializados
- [ ] Mapear estado atual do sistema Bable Pet
- [ ] Identificar oportunidades de melhoria
- [ ] Definir plano de implementação

### Próxima Sprint: Implementação
**Objetivos Planejados**:
- [ ] Implementar melhorias prioritárias
- [ ] Atualizar prompts conforme necessário
- [ ] Modificar workflows N8N
- [ ] Testar integrações

---

## 📝 NOTAS E OBSERVAÇÕES COMPARTILHADAS

### Decisões Arquiteturais
- Manter estrutura de 7 agentes Bable Pet existente
- Preservar compatibilidade com N8N workflows
- Focar em otimização sem quebrar integrações existentes

### Padrões Estabelecidos
- Versionamento de prompts: `_revXX`
- Formato de resposta JSON padrão para todos os agentes
- Uso obrigatório de `think1` para raciocínio
- Estrutura de "Fichas" para gerenciamento de estado

### Lições Aprendidas
- *A ser preenchido conforme progresso do projeto*

---

## ⚡ AÇÕES RÁPIDAS NECESSÁRIAS

### Pendências Críticas
- [ ] **Agent 1**: Iniciar análise arquitetural completa
- [ ] **Agent 4**: Completar documentação dos 4 agentes criados

### Bloqueadores Atuais
- *Nenhum bloqueador crítico identificado*

---

## 📞 PROTOCOLOS DE COMUNICAÇÃO

### Para Adicionar Nova Tarefa
1. Definir título, responsável, prioridade
2. Especificar dependências se houver
3. Adicionar descrição clara
4. Atualizar timestamp e autor

### Para Atualizar Status
1. Modificar campo Status
2. Adicionar observações relevantes
3. Atualizar timestamp e autor
4. Notificar dependentes se necessário

### Para Escalação de Issues
1. Marcar como alta prioridade
2. Adicionar na seção de bloqueadores
3. Notificar todos os agents relevantes
4. Definir plano de resolução

---

## 🔧 CONFIGURAÇÕES DO PROJETO

### Ferramentas Compartilhadas
- **Claude Code**: Ambiente de desenvolvimento
- **N8N**: Orquestração de workflows
- **ChatWoot + Evolution API**: Integração de mensagens
- **Git**: Controle de versão (se aplicável)

### Ambientes
- **Desenvolvimento**: Ambiente local de testes
- **Produção**: Sistema Bable Pet ativo

---

*Este documento é atualizado continuamente pelos 4 agentes. Sempre verificar timestamp da última atualização antes de fazer modificações.*