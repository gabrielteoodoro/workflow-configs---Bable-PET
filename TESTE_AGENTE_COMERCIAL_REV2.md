# 🧪 Bateria de Testes - Agente Comercial REV2
*Validação Completa das Funcionalidades Humanizadas*

## 📋 CENÁRIOS DE TESTE

### **TESTE 1: Contextualização por Raça + Primeira Cotação**
```json
{
  "testId": "TC001_contextualizacao_poodle",
  "input": {
    "chatInput": "Quanto custa o banho e tosa?",
    "feedback_saudacao": {
      "dados_cliente": {
        "sessionId": "teste001",
        "cliente_nome": "Maria",
        "pet_nome": "Fifi",
        "pet_raca": "Poodle"
      }
    },
    "chatHistory": ["Olá", "Preciso agendar para minha Poodle Fifi"]
  },
  "expectedBehavior": {
    "should_trigger": true,
    "must_use_racas_e_grupos": true,
    "must_contextualize_breed": true,
    "must_call_precos_e_servicos": true,
    "must_check_buscaAssinantes": true,
    "contextualizacao_example": "Que fofinha! Poodles têm uma pelagem linda que precisa de cuidados especiais"
  },
  "expectedOutput": {
    "script_id_sugerido": "INFORMAR_PRECO_COM_OFERTA_CLUBE_HUMANIZADO",
    "ficha_comercial": {
      "cliente_nome": "Maria",
      "pet_nome": "Fifi",
      "pet_raca": "Poodle", 
      "pet_tamanho": "G2 - Pequeno",
      "servico": "banho e tosa",
      "contextualizacao_raca": "string_with_breed_info"
    },
    "status_operacao": {
      "contextualizacao_aplicada": true,
      "expertise_demonstrada": true,
      "transicao_agendamento": true,
      "personalizacao_ativa": true
    }
  }
}
```

### **TESTE 2: Cliente Sem Raça Definida**
```json
{
  "testId": "TC002_solicitar_raca_humanizado",
  "input": {
    "chatInput": "Qual o valor do banho?",
    "feedback_saudacao": {
      "dados_cliente": {
        "sessionId": "teste002",
        "cliente_nome": "João",
        "pet_nome": "Rex"
      }
    }
  },
  "expectedBehavior": {
    "should_trigger": true,
    "should_request_breed": true,
    "must_be_empathetic": true
  },
  "expectedOutput": {
    "script_id_sugerido": "SOLICITAR_RACA_HUMANIZADO",
    "script_sugerido": "contains: 'Que amor! Para te dar o melhor preço'",
    "ficha_comercial": {
      "cliente_nome": "João",
      "pet_nome": "Rex",
      "pet_raca": null,
      "servico": "banho"
    }
  }
}
```

### **TESTE 3: Cliente Assinante VIP**
```json
{
  "testId": "TC003_assinante_vip_golden",
  "input": {
    "chatInput": "Quanto fica a tosa para meu Golden?",
    "feedback_saudacao": {
      "dados_cliente": {
        "sessionId": "assinante_vip_001",
        "cliente_nome": "Ana",
        "pet_nome": "Buddy",
        "pet_raca": "Golden Retriever"
      }
    }
  },
  "mock_responses": {
    "buscaAssinantes": {
      "is_member": true,
      "plan": "Premium"
    }
  },
  "expectedBehavior": {
    "must_contextualize_golden": true,
    "must_recognize_vip_status": true,
    "must_show_member_price": true
  },
  "expectedOutput": {
    "script_id_sugerido": "INFORMAR_PRECO_ASSINANTE_VIP",
    "script_sugerido": "contains: ['Goldens são lindos', 'status VIP', 'membro do clube']",
    "ficha_comercial": {
      "pet_raca": "Golden Retriever",
      "pet_tamanho": "G4 - Grande",
      "contextualizacao_raca": "contains: Golden"
    },
    "status_operacao": {
      "contextualizacao_aplicada": true,
      "personalizacao_ativa": true
    }
  }
}
```

### **TESTE 4: Gatilho NÃO Ativado (Falso Positivo)**
```json
{
  "testId": "TC004_gatilho_nao_ativado",
  "input": {
    "chatInput": "Vocês atendem Yorkshire?",
    "intencoes": ["COMERCIAL", "FAQ"]
  },
  "expectedBehavior": {
    "should_trigger": false,
    "should_not_interfere": true,
    "should_update_ficha_only": true
  },
  "expectedOutput": {
    "script_id_sugerido": null,
    "script_sugerido": null,
    "ficha_comercial": {
      "pet_raca": "Yorkshire",
      "updated": true
    },
    "analise": "contains: 'aguardando'"
  }
}
```

### **TESTE 5: Economia para Não-Assinante**
```json
{
  "testId": "TC005_economia_clube_calculada",
  "input": {
    "chatInput": "Preço do banho completo para Bulldog?",
    "feedback_saudacao": {
      "dados_cliente": {
        "sessionId": "nao_assinante_001",
        "cliente_nome": "Carlos",
        "pet_nome": "Thor",
        "pet_raca": "Bulldog Francês"
      }
    }
  },
  "mock_responses": {
    "buscaAssinantes": {
      "is_member": false
    },
    "precos_e_servicos": {
      "preco": "R$ 120,00"
    },
    "precosAssinatura": {
      "preco_mensal": "R$ 89,90",
      "desconto": "20%"
    }
  },
  "expectedBehavior": {
    "must_contextualize_bulldog": true,
    "must_calculate_economy": true,
    "must_show_club_benefits": true
  },
  "expectedOutput": {
    "variaveis": {
      "preco_servico": "R$ 120,00",
      "economia_clube": "R$ 24,00 (20% de desconto)",
      "contexto_raca": "contains: Bulldog",
      "transicao_agendamento": "contains: agendar"
    },
    "status_operacao": {
      "contextualizacao_aplicada": true,
      "expertise_demonstrada": true,
      "transicao_agendamento": true
    }
  }
}
```

### **TESTE 6: Serviço Genérico - Detalhamento Necessário**
```json
{
  "testId": "TC006_detalhar_servico_generico",
  "input": {
    "chatInput": "Quanto custa para cuidar do meu Shih Tzu?",
    "feedback_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Patricia",
        "pet_nome": "Mel",
        "pet_raca": "Shih Tzu"
      }
    }
  },
  "expectedBehavior": {
    "must_contextualize_shihtzu": true,
    "must_detail_services": true,
    "should_offer_options": true
  },
  "expectedOutput": {
    "script_id_sugerido": "DETALHAR_SERVICO_HUMANIZADO",
    "script_sugerido": "contains: ['Shih Tzu', 'banho simples', 'banho e tosa', 'pacote completo']",
    "ficha_comercial": {
      "pet_raca": "Shih Tzu",
      "servico": "cuidados gerais",
      "contextualizacao_raca": "contains: Shih Tzu"
    }
  }
}
```

## 🎯 CRITÉRIOS DE VALIDAÇÃO

### **Métricas de Qualidade (Target ≥8.5/10)**

1. **Naturalidade (9/10)**
   - ✅ Linguagem fluida e calorosa
   - ✅ Sem robotização
   - ✅ Uso frequente dos nomes (pet + cliente)

2. **Expertise (9/10)** 
   - ✅ Conhecimento específico por raça
   - ✅ Conexão características → cuidados
   - ✅ Vocabulário técnico adequado

3. **Personalização (8.5/10)**
   - ✅ Contextualização antes do preço
   - ✅ Ofertas adequadas ao perfil
   - ✅ Cálculos de economia personalizados

4. **Transição (8.5/10)**
   - ✅ Ponte natural para agendamento
   - ✅ Call-to-action específico
   - ✅ Continuidade da jornada

5. **Empatia (9/10)**
   - ✅ Conexão emocional pet-dono
   - ✅ Tom consultivo vs vendedor
   - ✅ Reconhecimento de status (VIP)

### **Validações Técnicas**

1. **Formato JSON**
   - ✅ Estrutura `feedback_comercial` válida
   - ✅ Campos obrigatórios preenchidos
   - ✅ Tipos de dados corretos

2. **Lógica de Gatilho**
   - ✅ Ativa apenas com palavras-chave de preço
   - ✅ Não interfere sem trigger
   - ✅ Atualiza ficha passivamente sempre

3. **Fluxo de Ferramentas**
   - ✅ `think1` sempre primeiro
   - ✅ `racas_e_grupos` quando necessário
   - ✅ `precos_e_servicos` para cotações
   - ✅ `buscaAssinantes` para personalização

4. **Campos da Ficha**
   - ✅ `contextualizacao_raca` preenchido
   - ✅ `pet_tamanho` determinado corretamente
   - ✅ Dados persistidos entre execuções

## 📊 RESULTADOS ESPERADOS

### **Taxa de Sucesso por Cenário:**
- TC001: 100% (funcionalidade core)
- TC002: 100% (fallback humanizado)  
- TC003: 100% (experiência VIP)
- TC004: 100% (precisão do gatilho)
- TC005: 100% (cálculo de valor)
- TC006: 100% (detalhamento consultivo)

### **Score Médio Esperado:** ≥8.7/10

### **Comportamentos Críticos:**
- ❌ **Zero** interferência sem palavra-chave de preço
- ✅ **100%** contextualização por raça antes do preço
- ✅ **100%** transição para agendamento
- ✅ **100%** personalização baseada em status do cliente

## 🚀 PRÓXIMOS PASSOS

1. **Executar Testes**: Rodar cada cenário individualmente
2. **Validar Métricas**: Verificar scores de qualidade
3. **Ajustar Prompts**: Corrigir comportamentos abaixo do esperado  
4. **Integrar**: Deployar REV2 no sistema principal
5. **Monitorar**: Acompanhar performance em produção

---
*Testes criados para validar as melhorias de humanização e contextualização da REV2*