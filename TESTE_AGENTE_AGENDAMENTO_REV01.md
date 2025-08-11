# 🧪 Bateria de Testes - Agente Agendamento REV01
*Validação Completa do Fluxo de Agendamento*

## 📋 CENÁRIOS DE TESTE

### **TESTE 1: Cliente Novo - Fluxo Completo (Crítico)**
```json
{
  "testId": "TA001_cliente_novo_completo",
  "input": {
    "chatInput": "Quero agendar um banho para meu cachorro",
    "relatorio_saudacao": {
      "dados_cliente": {
        "sessionId": "11987654321",
        "status": "NOVO",
        "cliente_nome": null,
        "pet_nome": null
      }
    },
    "prioridade_mestre": "agendamento"
  },
  "expectedBehavior": {
    "must_use_think1": true,
    "should_initialize_ficha": true,
    "should_detect_new_client": true,
    "expected_task": "TAREFA_C",
    "expected_entry_point": "cliente novo"
  },
  "expectedOutput": {
    "id_script_sugerido": "COLETAR_NOME_TUTOR",
    "script_sugerido": "contains: 'nome do tutor'",
    "ficha_atendimento": {
      "cliente_nome": null,
      "pet_nome": null,
      "ddd_telefone": "11987654321"
    },
    "analise": "contains: 'cliente novo'",
    "status_operacao": "iniciando_coleta_dados"
  }
}
```

### **TESTE 2: Cliente Cadastrado - Confirmar Pet**
```json
{
  "testId": "TA002_cliente_cadastrado_confirmar",
  "input": {
    "chatInput": "Preciso agendar para minha Yorkshire",
    "relatorio_saudacao": {
      "dados_cliente": {
        "sessionId": "11999888777",
        "status": "CADASTRADO",
        "cliente_nome": "Ana Silva",
        "pet_nome": "Mel",
        "pet_raca": "Yorkshire"
      }
    }
  },
  "expectedBehavior": {
    "should_detect_existing_pet": true,
    "expected_task": "TAREFA_C",
    "expected_entry_point": "cliente cadastrado"
  },
  "expectedOutput": {
    "id_script_sugerido": "CONFIRMAR_PET_CADASTRADO",
    "ficha_atendimento": {
      "cliente_nome": "Ana Silva",
      "pet_nome": "Mel",
      "pet_raca": "Yorkshire"
    },
    "analise": "contains: 'confirmação do pet cadastrado'"
  }
}
```

### **TESTE 3: Solicitação de Serviço Específico**
```json
{
  "testId": "TA003_servico_especifico",
  "input": {
    "chatInput": "Sim, é a Mel mesmo",
    "relatorio_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Ana Silva",
        "pet_nome": "Mel"
      }
    },
    "chatHistory": [
      "Agente: É para a Mel mesmo, sua Yorkshire?",
      "Cliente: Sim, é a Mel mesmo"
    ]
  },
  "expectedBehavior": {
    "should_identify_pet_confirmed": true,
    "should_proceed_to_service": true,
    "initial_request_was": "banho"
  },
  "expectedOutput": {
    "id_script_sugerido": "SOLICITAR_TIPO_BANHO",
    "ficha_atendimento": {
      "pet_confirmado": true,
      "servico": "banho"
    },
    "analise": "contains: 'pet confirmado, solicitando tipo de serviço'"
  }
}
```

### **TESTE 4: Coleta de Data + Verificação Calendário**
```json
{
  "testId": "TA004_coleta_data_calendario",
  "input": {
    "chatInput": "Queria para próxima terça-feira",
    "data_referencia": "2025-01-15",
    "data_solicitada": "2025-01-21",
    "relatorio_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Ana Silva",
        "pet_nome": "Mel"
      }
    },
    "chatHistory": [
      "Agente: Que tipo de banho para a Mel?",
      "Cliente: Banho completo com tosa",
      "Agente: Para que data gostaria de agendar?",
      "Cliente: Queria para próxima terça-feira"
    ]
  },
  "expectedBehavior": {
    "must_update_ficha_with_service": true,
    "must_update_ficha_with_date": true,
    "expected_next_step": "periodo"
  },
  "expectedOutput": {
    "id_script_sugerido": "SOLICITAR_PERIODO_DIA",
    "ficha_atendimento": {
      "servico": "banho completo com tosa",
      "data_agendamento": "2025-01-21"
    },
    "analise": "contains: 'data definida'"
  }
}
```

### **TESTE 5: Apresentar Vagas Disponíveis**
```json
{
  "testId": "TA005_apresentar_vagas",
  "input": {
    "chatInput": "Prefiro de manhã",
    "relatorio_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Ana Silva",
        "pet_nome": "Mel"
      }
    },
    "chatHistory": ["Agente: Prefere manhã, tarde ou qualquer horário?", "Cliente: Prefiro de manhã"]
  },
  "mock_responses": {
    "listarEvento": {
      "timeMin": "2025-01-21T08:00:00",
      "timeMax": "2025-01-21T12:00:00",
      "events": [
        {
          "start": "2025-01-21T09:00:00",
          "end": "2025-01-21T10:00:00",
          "summary": "Ocupado"
        }
      ]
    }
  },
  "expectedBehavior": {
    "must_call_listarEvento": true,
    "must_use_calculator": true,
    "should_filter_available_slots": true,
    "expected_available": ["08:00", "08:30", "10:00", "10:30", "11:00", "11:30"]
  },
  "expectedOutput": {
    "id_script_sugerido": "APRESENTAR_VAGAS",
    "script_sugerido": "contains: ['08:00', '08:30', '10:00']",
    "ficha_atendimento": {
      "periodo_preferido": "manhã"
    },
    "analise": "contains: 'vagas calculadas'"
  }
}
```

### **TESTE 6: Finalização - Criar Evento + Atendimento**
```json
{
  "testId": "TA006_finalizar_agendamento",
  "input": {
    "chatInput": "Quero às 10:30",
    "relatorio_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Ana Silva",
        "email": "ana@email.com",
        "pet_nome": "Mel"
      }
    },
    "chatHistory": [
      "Agente: Horários disponíveis: 08:00, 08:30, 10:00, 10:30...",
      "Cliente: Quero às 10:30"
    ]
  },
  "expectedBehavior": {
    "must_create_personalized_summary": true,
    "must_call_criarEvento": true,
    "must_call_criaAtendimento_after": true,
    "expected_summary": "banho completo com tosa - Mel (Ana Silva)"
  },
  "mock_responses": {
    "criarEvento": {
      "id": "evento_12345",
      "start": "2025-01-21T10:30:00",
      "end": "2025-01-21T11:30:00"
    },
    "criaAtendimento": {
      "id": "atend_67890",
      "status": "criado"
    }
  },
  "expectedOutput": {
    "id_script_sugerido": "CONFIRMACAO_AGENDAMENTO",
    "ficha_atendimento": {
      "hora_agendamento": "10:30",
      "id_evento_calendar": "evento_12345",
      "id_atendimento_planilha": "atend_67890",
      "status": "confirmado"
    },
    "variaveis": {
      "data_formatada": "terça-feira, 21/01",
      "hora_formatada": "10h30",
      "servico_completo": "banho completo com tosa"
    }
  }
}
```

### **TESTE 7: Remarcação de Agendamento**
```json
{
  "testId": "TA007_remarcacao",
  "input": {
    "chatInput": "Preciso remarcar o agendamento da Mel",
    "relatorio_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Ana Silva",
        "pet_nome": "Mel"
      }
    }
  },
  "expectedBehavior": {
    "should_detect_remark_request": true,
    "expected_task": "TAREFA_B",
    "must_call_buscaIDAtendimento": true
  },
  "mock_responses": {
    "buscaIDAtendimento": {
      "found": true,
      "id_evento": "evento_12345",
      "data_atual": "2025-01-21T10:30:00"
    }
  },
  "expectedOutput": {
    "id_script_sugerido": "CONFIRMAR_REMARCACAO",
    "ficha_atendimento": {
      "operacao": "remarcacao",
      "id_evento_original": "evento_12345"
    },
    "analise": "contains: 'agendamento encontrado'"
  }
}
```

### **TESTE 8: Cancelamento de Agendamento**
```json
{
  "testId": "TA008_cancelamento",
  "input": {
    "chatInput": "Quero cancelar o agendamento",
    "relatorio_saudacao": {
      "dados_cliente": {
        "cliente_nome": "Ana Silva"
      }
    }
  },
  "expectedBehavior": {
    "should_detect_cancel_request": true,
    "expected_task": "TAREFA_B",
    "must_call_buscaIDAtendimento": true,
    "must_call_desmarcarEvento": true,
    "must_call_excluiAtendimento": true
  },
  "mock_responses": {
    "buscaIDAtendimento": {
      "found": true,
      "id_evento": "evento_12345"
    },
    "desmarcarEvento": {
      "success": true
    },
    "excluiAtendimento": {
      "success": true
    }
  },
  "expectedOutput": {
    "id_script_sugerido": "CONFIRMACAO_CANCELAMENTO",
    "ficha_atendimento": {
      "operacao": "cancelamento",
      "status": "cancelado"
    },
    "analise": "contains: 'cancelamento concluído'"
  }
}
```

### **TESTE 9: Ordem Direta da Saudação**
```json
{
  "testId": "TA009_ordem_direta",
  "input": {
    "chatInput": "João Silva",
    "relatorio_saudacao": {
      "id_script_sugerido": "CONFIRMAR_PET_CADASTRADO",
      "dados_cliente": {
        "pet_nome": "Thor"
      }
    }
  },
  "expectedBehavior": {
    "should_detect_direct_order": true,
    "expected_task": "TAREFA_A",
    "should_use_exact_script_from_saudacao": true
  },
  "expectedOutput": {
    "id_script_sugerido": "CONFIRMAR_PET_CADASTRADO",
    "script_sugerido": "contains: 'Thor'",
    "analise": "contains: 'executando ordem direta'"
  }
}
```

## 🎯 CRITÉRIOS DE VALIDAÇÃO

### **Fluxo Sequencial (Score: /10)**
1. **Inicialização (8/10)**: `think1` + Ficha preenchida
2. **Seleção de Tarefa (9/10)**: A, B ou C corretamente
3. **Execução Ordenada (8.5/10)**: Passos na sequência correta
4. **Validação Script (8/10)**: `buscarScript` sempre chamado
5. **Duplo Registro (10/10)**: `criarEvento` + `criaAtendimento`

### **Integração de Ferramentas (Score: /10)**
1. **Calendário (9/10)**: `listarEvento` antes de apresentar vagas
2. **Calculator (8/10)**: Intervalos de 30min calculados
3. **Busca (8.5/10)**: `buscaIDAtendimento` para remarcações
4. **Scripts (8/10)**: `buscarScript` com ID correto
5. **Persistência (9/10)**: Ficha atualizada a cada passo

### **Validações Técnicas**
1. **Formato JSON**: Estrutura `feedback_agendamento` válida
2. **Ficha Completa**: Todos os campos obrigatórios
3. **Ordem de Ferramentas**: Sequência lógica respeitada
4. **Error Handling**: Comportamento com falhas de API

### **Comportamentos Críticos**
- ✅ Cliente novo → `COLETAR_NOME_TUTOR`
- ✅ Cliente cadastrado → `CONFIRMAR_PET_CADASTRADO` 
- ✅ Finalização → `criarEvento` ANTES de `criaAtendimento`
- ✅ Remarcação → `buscaIDAtendimento` primeiro
- ✅ Cancelamento → `desmarcarEvento` + `excluiAtendimento`

## 📊 RESULTADOS ESPERADOS

### **Taxa de Sucesso por Cenário:**
- TA001: 100% (fluxo principal)
- TA002: 100% (cliente cadastrado)
- TA003: 100% (continuidade)
- TA004: 100% (integração calendário)
- TA005: 100% (cálculo vagas)
- TA006: 100% (finalização crítica)
- TA007: 100% (remarcação)
- TA008: 100% (cancelamento)
- TA009: 100% (ordem direta)

### **Score Médio Esperado:** ≥8.5/10

### **Tempo de Execução:** <3s por teste

## 🚀 PRÓXIMOS PASSOS

1. **Executar Cenários**: Testar cada fluxo individualmente
2. **Validar Integrações**: Verificar APIs de calendário e planilha
3. **Testar Error Cases**: Comportamento com falhas
4. **Performance**: Tempo de resposta por operação
5. **Deploy**: Integrar no sistema principal

---
*Testes criados para validar fluxo completo de agendamento do Bable Pet*