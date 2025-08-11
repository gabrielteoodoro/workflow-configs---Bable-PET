# 🧪 TESTES WORKFLOW INTEGRADO - Bable Pet
*Validação Completa dos Agentes em Produção*

## 🎯 OBJETIVO

Testar o **workflow completo** via trigger "When Executed by Another Workflow" para validar:

1. **Agente Orquestrador** - Identificação de intenções
2. **Agente Comercial REV2** - Humanização e contextualização  
3. **Agente Agendamento REV01** - Fluxo sequencial
4. **Agente Mestre** - Resposta final ao cliente

---

## 📋 CENÁRIOS DE TESTE

### **TESTE 1: Comercial - Primeira Cotação com Contextualização**
```json
{
  "testId": "TI001_comercial_contextualizacao",
  "description": "Validar contextualização por raça + oferta clube",
  "endpoint": "https://n8n.synapseautointeligente.com.br/webhook/DUOuKlAbIvwd9c3v",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511999888777"
          }
        },
        "id": 12345,
        "messages": [
          {
            "processed_message_content": "Quanto custa o banho e tosa para minha Poodle Lila?"
          }
        ]
      },
      "sender": {
        "name": "Maria Silva"
      },
      "account": {
        "id": 1
      },
      "content": "Quanto custa o banho e tosa para minha Poodle Lila?",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "orquestrador_should_detect": ["COMERCIAL", "AGENDAMENTO"],
    "comercial_should_trigger": true,
    "comercial_should_contextualize": "Poodle",
    "comercial_should_offer_club": true,
    "mestre_should_include": [
      "Lila",
      "Poodle", 
      "pelagem",
      "R$",
      "clube"
    ]
  },
  "success_criteria": {
    "response_time": "<5s",
    "personalization": "Nome pet + raça mencionados",
    "expertise": "Conhecimento específico Poodle",
    "offer": "Clube mencionado com economia",
    "transition": "Ponte para agendamento"
  }
}
```

### **TESTE 2: Agendamento - Cliente Novo Completo**
```json
{
  "testId": "TI002_agendamento_cliente_novo",
  "description": "Validar fluxo completo de agendamento cliente novo",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511987654321"
          }
        },
        "id": 23456,
        "messages": [
          {
            "processed_message_content": "Quero agendar um banho para meu cachorro"
          }
        ]
      },
      "sender": {
        "name": "João Santos"  
      },
      "account": {
        "id": 1
      },
      "content": "Quero agendar um banho para meu cachorro",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "orquestrador_should_detect": ["AGENDAMENTO"],
    "agendamento_should_start": "COLETAR_NOME_TUTOR",
    "mestre_should_ask": "nome do tutor"
  },
  "success_criteria": {
    "detects_new_customer": true,
    "starts_data_collection": true,
    "friendly_tone": true
  }
}
```

### **TESTE 3: Comercial - Gatilho NÃO Ativado** 
```json
{
  "testId": "TI003_comercial_nao_gatilho",
  "description": "Validar que comercial NÃO interfere sem palavra-chave preço",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511999111222"
          }
        },
        "id": 34567,
        "messages": [
          {
            "processed_message_content": "Vocês atendem Yorkshire Terrier?"
          }
        ]
      },
      "sender": {
        "name": "Ana Costa"
      },
      "account": {
        "id": 1
      },
      "content": "Vocês atendem Yorkshire Terrier?",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "orquestrador_should_detect": ["FAQ", "COMERCIAL"],
    "comercial_should_NOT_trigger": true,
    "faq_should_respond": true
  },
  "success_criteria": {
    "comercial_does_not_interfere": true,
    "appropriate_agent_responds": true
  }
}
```

### **TESTE 4: Múltiplas Intenções - Saudação + Comercial**
```json
{
  "testId": "TI004_multiplas_intencoes",
  "description": "Validar detecção múltiplas intenções em uma mensagem",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511888777666"
          }
        },
        "id": 45678,
        "messages": [
          {
            "processed_message_content": "Oi! Gostaria de saber o preço do banho para Golden Retriever"
          }
        ]
      },
      "sender": {
        "name": "Carlos Lima"
      },
      "account": {
        "id": 1
      },
      "content": "Oi! Gostaria de saber o preço do banho para Golden Retriever",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "orquestrador_should_detect": ["SAUDACAO", "COMERCIAL", "AGENDAMENTO"],
    "saudacao_should_delegate": "comercial",
    "comercial_should_contextualize": "Golden Retriever",
    "size_should_be": "G4 - Grande"
  },
  "success_criteria": {
    "greeting_acknowledged": true,
    "price_provided": true,
    "breed_expertise": "Golden characteristics mentioned",
    "size_calculated": "Large dog pricing"
  }
}
```

### **TESTE 5: Cliente VIP - Reconhecimento Status**
```json
{
  "testId": "TI005_cliente_vip",
  "description": "Validar reconhecimento de cliente assinante VIP",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511777555333"
          }
        },
        "id": 56789,
        "messages": [
          {
            "processed_message_content": "Qual o valor da tosa para meu Bulldog Francês Thor?"
          }
        ]
      },
      "sender": {
        "name": "Patricia Oliveira"
      },
      "account": {
        "id": 1
      },
      "content": "Qual o valor da tosa para meu Bulldog Francês Thor?",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "customer_lookup": "existing customer",
    "vip_status": "should recognize if member",
    "pricing": "member vs non-member",
    "personalization": "Thor + Bulldog mentioned"
  },
  "success_criteria": {
    "status_recognition": true,
    "appropriate_pricing": true,
    "breed_context": "Bulldog characteristics"
  }
}
```

### **TESTE 6: Agendamento - Remarcação**
```json
{
  "testId": "TI006_remarcacao",
  "description": "Validar fluxo de remarcação de agendamento existente",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511666444222"
          }
        },
        "id": 67890,
        "messages": [
          {
            "processed_message_content": "Preciso remarcar o agendamento da Mel"
          }
        ]
      },
      "sender": {
        "name": "Fernanda Alves"
      },
      "account": {
        "id": 1
      },
      "content": "Preciso remarcar o agendamento da Mel",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "orquestrador_should_detect": ["AGENDAMENTO"],
    "agendamento_task": "TAREFA_B",
    "should_search_existing": true,
    "should_use_buscaIDAtendimento": true
  },
  "success_criteria": {
    "detects_remark_request": true,
    "searches_existing_appointment": true,
    "provides_remark_options": true
  }
}
```

### **TESTE 7: Franquia - Interesse**
```json
{
  "testId": "TI007_franquia",
  "description": "Validar detecção e resposta para interesse em franquia",
  "payload": {
    "body": {
      "conversation": {
        "meta": {
          "sender": {
            "phone_number": "+5511555333111"
          }
        },
        "id": 78901,
        "messages": [
          {
            "processed_message_content": "Tenho interesse em abrir uma franquia da Bable Pet"
          }
        ]
      },
      "sender": {
        "name": "Roberto Mendes"
      },
      "account": {
        "id": 1
      },
      "content": "Tenho interesse em abrir uma franquia da Bable Pet",
      "message_type": "incoming"
    }
  },
  "expectedBehavior": {
    "orquestrador_should_detect": ["FRANQUIA"],
    "franquia_agent_activation": true,
    "should_use_buscarInfoFranquia": true
  },
  "success_criteria": {
    "franchise_info_provided": true,
    "investment_details": true,
    "next_steps_clear": true
  }
}
```

---

## 🔧 SCRIPTS DE TESTE

### **Script Principal de Execução:**
```python
import requests
import json
import time
from datetime import datetime

class BablePetWorkflowTester:
    def __init__(self):
        self.base_url = "https://n8n.synapseautointeligente.com.br"
        self.workflow_id = "DUOuKlAbIvwd9c3v"
        self.results = []
    
    def execute_test(self, test_case):
        """Executa um caso de teste individual"""
        print(f"\n🧪 Executando: {test_case['testId']}")
        print(f"📝 {test_case['description']}")
        
        start_time = time.time()
        
        try:
            # Executar workflow
            response = requests.post(
                f"{self.base_url}/webhook/{self.workflow_id}",
                json=test_case['payload'],
                timeout=30
            )
            
            end_time = time.time()
            response_time = end_time - start_time
            
            # Analisar resultado
            result = {
                'test_id': test_case['testId'],
                'status': 'SUCCESS' if response.status_code == 200 else 'FAILED',
                'response_time': response_time,
                'response_data': response.text if response.status_code == 200 else None,
                'error': None if response.status_code == 200 else response.text,
                'timestamp': datetime.now().isoformat()
            }
            
            self.results.append(result)
            
            if response.status_code == 200:
                print(f"✅ Sucesso - Tempo: {response_time:.2f}s")
                print(f"📤 Resposta: {response.text[:200]}...")
            else:
                print(f"❌ Falha - Status: {response.status_code}")
                print(f"💬 Erro: {response.text}")
                
        except Exception as e:
            result = {
                'test_id': test_case['testId'],
                'status': 'ERROR',
                'response_time': 0,
                'response_data': None,
                'error': str(e),
                'timestamp': datetime.now().isoformat()
            }
            self.results.append(result)
            print(f"💥 Erro: {e}")
        
        return result
    
    def run_all_tests(self, test_cases):
        """Executa todos os casos de teste"""
        print("🚀 Iniciando Bateria de Testes do Workflow Bable Pet")
        print("=" * 60)
        
        for test_case in test_cases:
            self.execute_test(test_case)
            time.sleep(2)  # Pausa entre testes
        
        self.generate_report()
    
    def generate_report(self):
        """Gera relatório final"""
        total_tests = len(self.results)
        successful_tests = len([r for r in self.results if r['status'] == 'SUCCESS'])
        
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL")
        print("=" * 60)
        print(f"Total de Testes: {total_tests}")
        print(f"Sucessos: {successful_tests}")
        print(f"Falhas: {total_tests - successful_tests}")
        print(f"Taxa de Sucesso: {(successful_tests/total_tests)*100:.1f}%")
        
        if successful_tests > 0:
            avg_time = sum([r['response_time'] for r in self.results if r['status'] == 'SUCCESS']) / successful_tests
            print(f"Tempo Médio: {avg_time:.2f}s")

# Exemplo de uso:
if __name__ == "__main__":
    tester = BablePetWorkflowTester()
    
    # Carregar casos de teste
    test_cases = [
        # TI001, TI002, etc. definidos acima
    ]
    
    tester.run_all_tests(test_cases)
```

---

## ✅ CRITÉRIOS DE SUCESSO GERAL

### **Performance:**
- ⏱️ Tempo de resposta: <5s por teste
- 📈 Taxa de sucesso: >90%
- 🔄 Consistency: Mesma entrada = mesma saída

### **Funcionalidade:**
- 🎯 **Orquestrador**: Intenções corretas identificadas
- 🏪 **Comercial REV2**: Contextualização + humanização
- 📅 **Agendamento REV01**: Fluxo sequencial respeitado
- 👑 **Mestre**: Resposta final coerente e natural

### **Qualidade da Resposta:**
- 💬 Tom natural e empático
- 🎭 Personalização (nomes usados)
- 🧠 Expertise demonstrada
- 🔗 Transições adequadas entre agentes

---

## 🚀 PRÓXIMOS PASSOS

1. **Executar Testes**: Rodar todos os 7 cenários
2. **Analisar Respostas**: Validar qualidade das saídas do Mestre
3. **Ajustar se Necessário**: Corrigir comportamentos inadequados
4. **Documentar**: Registrar performance em produção
5. **Monitorar**: Estabelecer métricas contínuas

---

*Testes criados para validação completa do workflow integrado Bable Pet*