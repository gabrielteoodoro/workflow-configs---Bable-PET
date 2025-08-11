# Protocolo de Validação de Prompts - Sistema Integrado Bable Pet

> **🔍 VALIDAÇÃO RIGOROSA**: Protocolo completo para validação de prompts otimizados antes da aplicação no n8n

---

## 🎯 **VISÃO GERAL DO PROTOCOLO**

### Objetivos da Validação
1. **Garantia de Qualidade**: Score mínimo de 8/10 em todas as métricas
2. **Segurança**: Nenhuma regressão em funcionalidades críticas
3. **Consistência**: Manutenção da persona e regras do Bable Pet
4. **Performance**: Melhorias mensuráveis e significativas
5. **Rollback Prevention**: Identificar problemas antes da aplicação

### Processo de Validação Multi-Layer
```
🔍 LAYER 1: Validação Estrutural
├── Sintaxe e formato
├── Campos obrigatórios
└── Compatibilidade n8n

🧪 LAYER 2: Validação Funcional  
├── Cenários de teste
├── Fluxos críticos
└── Edge cases

🎭 LAYER 3: Validação de Qualidade
├── Score humano
├── Naturalidade
└── Expertise demonstrada

📊 LAYER 4: Validação de Performance
├── Tempo de resposta
├── Taxa de sucesso
└── Eficiência de tokens

🔒 LAYER 5: Validação de Segurança
├── Não-regressão
├── Consistência de dados
└── Integridade do sistema
```

---

## 📋 **CHECKLIST DE VALIDAÇÃO ESTRUTURAL**

### ✅ **Layer 1: Validação Estrutural**

#### Prompt Structure Validation
```json
{
  "structural_validation": {
    "required_elements": [
      {
        "element": "persona_definition",
        "check": "Identidade do agente claramente definida",
        "critical": true
      },
      {
        "element": "tools_declaration", 
        "check": "Ferramentas necessárias listadas e descritas",
        "critical": true
      },
      {
        "element": "output_format",
        "check": "Formato de resposta JSON especificado",
        "critical": true
      },
      {
        "element": "business_rules",
        "check": "Regras de negócio do Bable Pet incluídas",
        "critical": true
      },
      {
        "element": "error_handling",
        "check": "Tratamento de erros e casos edge",
        "critical": false
      }
    ],
    "formatting_checks": [
      {
        "check": "markdown_formatting",
        "description": "Formatação markdown correta"
      },
      {
        "check": "json_schema_validity", 
        "description": "Schemas JSON válidos"
      },
      {
        "check": "character_encoding",
        "description": "Encoding UTF-8 sem caracteres especiais"
      }
    ]
  }
}
```

#### N8N Compatibility Check
```bash
# Validação de compatibilidade n8n
python validate_n8n_compatibility.py --prompt-file="prompt_otimizado.md" --workflow-id="DUOuKlAbIvwd9c3v"

# Verificações realizadas:
# ✓ Tamanho do prompt dentro dos limites
# ✓ Caracteres especiais compatíveis  
# ✓ Formato de entrada/saída correto
# ✓ Referências a ferramentas válidas
```

### 🔍 **Critérios de Aprovação - Layer 1**
```json
{
  "layer_1_approval": {
    "minimum_requirements": {
      "all_critical_elements_present": true,
      "n8n_compatibility_score": 1.0,
      "formatting_score": 0.95,
      "character_limit_compliance": true
    },
    "blocker_conditions": [
      "missing_persona_definition",
      "invalid_json_schema", 
      "n8n_incompatible_format",
      "critical_business_rules_missing"
    ]
  }
}
```

---

## 🧪 **PROTOCOLO DE VALIDAÇÃO FUNCIONAL**

### ✅ **Layer 2: Validação Funcional**

#### Test Scenario Execution
```python
# Validação funcional por cenários
class FunctionalValidation:
    def __init__(self, agent_id, optimized_prompt):
        self.agent_id = agent_id
        self.prompt = optimized_prompt
        self.test_results = []
    
    def run_core_scenarios(self):
        """Executa cenários críticos para o agente"""
        scenarios = self.get_agent_scenarios()
        
        for scenario in scenarios:
            result = self.execute_scenario(scenario)
            self.test_results.append({
                'scenario_id': scenario['id'],
                'input': scenario['input'],
                'expected': scenario['expected'],
                'actual': result['actual'],
                'success': result['success'],
                'score': result['score'],
                'issues': result.get('issues', [])
            })
    
    def validate_critical_flows(self):
        """Valida fluxos críticos do agente"""
        critical_flows = {
            'orquestrador': ['intention_identification', 'json_output', 'think_tool_usage'],
            'saudacao': ['data_retrieval', 'delegation', 'store_status'],
            'comercial': ['price_lookup', 'breed_mapping', 'subscription_offer'],
            'agendamento': ['calendar_integration', 'data_collection', 'ficha_creation'],
            'franquia': ['interest_detection', 'info_accuracy', 'handoff'],
            'faq': ['query_resolution', 'scope_recognition', 'standby_behavior']
        }
        
        flows = critical_flows.get(self.agent_id, [])
        for flow in flows:
            success = self.test_critical_flow(flow)
            if not success:
                raise ValidationError(f"Critical flow {flow} failed validation")
```

#### Specific Agent Validations
```json
{
  "agent_specific_validations": {
    "orquestrador": {
      "required_tests": [
        "single_intention_identification",
        "multiple_intentions_handling", 
        "ambiguous_message_detection",
        "json_format_compliance",
        "think1_tool_mandatory_usage"
      ],
      "critical_success_rate": 0.95
    },
    "saudacao": {
      "required_tests": [
        "new_customer_detection",
        "existing_customer_recognition",
        "store_hours_validation",
        "delegation_accuracy",
        "data_propagation_integrity"
      ],
      "critical_success_rate": 0.90
    },
    "comercial": {
      "required_tests": [
        "price_accuracy_validation",
        "breed_to_group_mapping",
        "unknown_breed_handling",
        "subscription_offer_trigger",
        "commercial_keyword_precision"
      ],
      "critical_success_rate": 0.90
    },
    "agendamento": {
      "required_tests": [
        "appointment_flow_completion",
        "calendar_integration_success",
        "ficha_atendimento_creation",
        "cria_atendimento_after_evento",
        "data_collection_completeness"
      ],
      "critical_success_rate": 0.90
    },
    "franquia": {
      "required_tests": [
        "franchise_interest_detection",
        "investment_info_accuracy",
        "handoff_to_specialist",
        "scope_boundary_respect"
      ],
      "critical_success_rate": 0.85
    },
    "faq": {
      "required_tests": [
        "general_query_resolution",
        "company_info_accuracy",
        "out_of_scope_recognition",
        "standby_state_handling"
      ],
      "critical_success_rate": 0.85
    }
  }
}
```

### 🔍 **Critérios de Aprovação - Layer 2**
```json
{
  "layer_2_approval": {
    "minimum_requirements": {
      "core_scenarios_success_rate": 0.90,
      "critical_flows_success_rate": 0.95,
      "edge_cases_handled": 0.80,
      "no_regression_detected": true
    },
    "blocker_conditions": [
      "critical_flow_failure",
      "success_rate_below_threshold",
      "major_functionality_regression",
      "data_integrity_compromised"
    ]
  }
}
```

---

## 🎭 **VALIDAÇÃO DE QUALIDADE HUMANA**

### ✅ **Layer 3: Validação de Qualidade**

#### Human-like Interaction Assessment
```python
class HumanQualityValidator:
    def __init__(self):
        self.quality_dimensions = [
            'naturalness',
            'empathy', 
            'clarity',
            'expertise',
            'proactivity'
        ]
    
    def assess_response_quality(self, scenario_input, agent_response):
        """Avalia qualidade humana da resposta"""
        scores = {}
        
        # Naturalidade (1-10)
        scores['naturalness'] = self.evaluate_naturalness(agent_response)
        
        # Empatia (1-10)
        scores['empathy'] = self.evaluate_empathy(scenario_input, agent_response)
        
        # Clareza (1-10)
        scores['clarity'] = self.evaluate_clarity(agent_response)
        
        # Expertise (1-10)
        scores['expertise'] = self.evaluate_expertise(agent_response)
        
        # Proatividade (1-10)
        scores['proactivity'] = self.evaluate_proactivity(agent_response)
        
        # Score geral ponderado
        weights = {'naturalness': 0.25, 'empathy': 0.20, 'clarity': 0.20, 'expertise': 0.20, 'proactivity': 0.15}
        overall_score = sum(scores[dim] * weights[dim] for dim in self.quality_dimensions)
        
        return {
            'individual_scores': scores,
            'overall_score': overall_score,
            'meets_threshold': overall_score >= 8.0
        }
    
    def evaluate_naturalness(self, response):
        """Avalia naturalidade da linguagem (1-10)"""
        indicators = {
            'robotic_phrases': -2.0,  # "Processando solicitação..."
            'natural_greetings': +1.0,  # "Oi! Como posso ajudar?"
            'conversational_tone': +1.5,
            'appropriate_emojis': +0.5,
            'human_expressions': +1.0  # "Que bom que você entrou em contato!"
        }
        
        score = 7.0  # Base score
        for indicator, impact in indicators.items():
            if self.detect_indicator(response, indicator):
                score += impact
        
        return max(1.0, min(10.0, score))
```

#### Quality Benchmarking
```json
{
  "quality_benchmarks": {
    "response_examples": {
      "excellent_10": {
        "example": "Oi! Que bom falar com você! 😊 Para o banho do seu Golden, que é um amorzinho de porte grande, o valor fica R$ 124,00. E olha, se você se tornar membro do nosso Clube Bable, esse mesmo banho sai por apenas R$ 99,20! Vale super a pena. Posso te explicar mais sobre o clube?",
        "scores": {
          "naturalness": 10,
          "empathy": 9,
          "clarity": 10,
          "expertise": 9,
          "proactivity": 10
        }
      },
      "good_8": {
        "example": "Olá! Para o banho do seu Golden Retriever, o preço é R$ 124,00 pois ele está no grupo G4 (porte grande). Temos também nosso clube de assinatura que oferece 20% de desconto. Gostaria de saber mais?",
        "scores": {
          "naturalness": 8,
          "empathy": 7,
          "clarity": 9,
          "expertise": 8,
          "proactivity": 8
        }
      },
      "poor_6": {
        "example": "Golden Retriever grupo G4. Banho R$ 124,00. Assinatura disponível com desconto 20%.",
        "scores": {
          "naturalness": 5,
          "empathy": 4,
          "clarity": 7,
          "expertise": 7,
          "proactivity": 6
        }
      },
      "unacceptable_3": {
        "example": "Processando consulta. Raça identificada: GOLDEN_RETRIEVER. Grupo: G4. Preço consulta realizada. Valor retornado: 124.00 BRL. Oferta assinatura: TRUE.",
        "scores": {
          "naturalness": 1,
          "empathy": 1,
          "clarity": 4,
          "expertise": 3,
          "proactivity": 3
        }
      }
    }
  }
}
```

### 🔍 **Critérios de Aprovação - Layer 3**
```json
{
  "layer_3_approval": {
    "minimum_requirements": {
      "overall_human_score": 8.0,
      "individual_dimension_minimum": 7.0,
      "naturalness_score": 8.0,
      "consistency_across_scenarios": 0.90
    },
    "excellence_indicators": [
      "conversational_tone_maintained",
      "appropriate_empathy_shown",
      "proactive_suggestions_provided",
      "expertise_clearly_demonstrated"
    ],
    "failure_indicators": [
      "robotic_language_detected",
      "inappropriate_tone_for_context",
      "generic_responses_without_context",
      "lack_of_domain_expertise"
    ]
  }
}
```

---

## 📊 **VALIDAÇÃO DE PERFORMANCE**

### ✅ **Layer 4: Validação de Performance**

#### Performance Benchmarking
```python
class PerformanceValidator:
    def __init__(self, baseline_metrics):
        self.baseline = baseline_metrics
        self.performance_tests = []
    
    def run_performance_validation(self, optimized_prompt, test_scenarios):
        """Executa validação de performance completa"""
        results = {
            'response_times': [],
            'success_rates': [],
            'token_usage': [],
            'error_counts': []
        }
        
        for scenario in test_scenarios:
            start_time = time.time()
            
            # Executa cenário
            response = self.execute_scenario(optimized_prompt, scenario)
            
            # Coleta métricas
            response_time = (time.time() - start_time) * 1000  # ms
            success = self.evaluate_success(response, scenario.expected)
            tokens = self.count_tokens(response)
            
            results['response_times'].append(response_time)
            results['success_rates'].append(1.0 if success else 0.0)
            results['token_usage'].append(tokens)
            
        return self.analyze_performance_results(results)
    
    def analyze_performance_results(self, results):
        """Analisa resultados de performance"""
        metrics = {
            'avg_response_time': np.mean(results['response_times']),
            'success_rate': np.mean(results['success_rates']),
            'avg_token_usage': np.mean(results['token_usage']),
            'response_time_p95': np.percentile(results['response_times'], 95)
        }
        
        # Compara com baseline
        improvements = {
            'response_time_improvement': (self.baseline['avg_response_time'] - metrics['avg_response_time']) / self.baseline['avg_response_time'],
            'success_rate_improvement': metrics['success_rate'] - self.baseline['success_rate'],
            'token_efficiency_improvement': (self.baseline['avg_token_usage'] - metrics['avg_token_usage']) / self.baseline['avg_token_usage']
        }
        
        return {
            'current_metrics': metrics,
            'improvements': improvements,
            'meets_performance_threshold': self.meets_threshold(improvements)
        }
```

#### Performance Thresholds
```json
{
  "performance_thresholds": {
    "response_time": {
      "excellent": {"max_ms": 1000, "p95_max_ms": 1500},
      "acceptable": {"max_ms": 2000, "p95_max_ms": 3000},
      "poor": {"max_ms": 3000, "p95_max_ms": 5000}
    },
    "success_rate": {
      "excellent": 0.95,
      "acceptable": 0.90,
      "poor": 0.85
    },
    "token_efficiency": {
      "excellent": 0.20,  # 20% melhoria
      "acceptable": 0.10,
      "poor": 0.00
    },
    "improvement_requirements": {
      "minimum_overall_improvement": 0.05,
      "human_score_minimum_gain": 0.5,
      "no_regression_tolerance": -0.02
    }
  }
}
```

### 🔍 **Critérios de Aprovação - Layer 4**
```json
{
  "layer_4_approval": {
    "minimum_requirements": {
      "response_time_acceptable": true,
      "success_rate_maintained": true,
      "overall_improvement_positive": true,
      "no_significant_regression": true
    },
    "performance_gates": [
      {
        "metric": "avg_response_time",
        "threshold": 2000,
        "critical": true
      },
      {
        "metric": "success_rate", 
        "threshold": 0.85,
        "critical": true
      },
      {
        "metric": "human_score_improvement",
        "threshold": 0.3,
        "critical": false
      }
    ]
  }
}
```

---

## 🔒 **VALIDAÇÃO DE SEGURANÇA**

### ✅ **Layer 5: Validação de Segurança**

#### Regression Prevention
```python
class SecurityValidator:
    def __init__(self, production_baseline):
        self.baseline = production_baseline
        self.critical_functionalities = [
            'data_integrity',
            'business_rule_compliance', 
            'integration_stability',
            'error_handling_robustness'
        ]
    
    def validate_no_regression(self, optimized_results):
        """Valida que não há regressão em funcionalidades críticas"""
        regressions = []
        
        for functionality in self.critical_functionalities:
            baseline_score = self.baseline[functionality]
            current_score = optimized_results[functionality]
            
            regression_threshold = -0.05  # 5% de tolerância
            regression = (current_score - baseline_score) / baseline_score
            
            if regression < regression_threshold:
                regressions.append({
                    'functionality': functionality,
                    'baseline_score': baseline_score,
                    'current_score': current_score,
                    'regression_percentage': regression * 100
                })
        
        return {
            'regressions_detected': len(regressions) > 0,
            'regressions': regressions,
            'safe_to_deploy': len(regressions) == 0
        }
    
    def validate_data_integrity(self, test_results):
        """Valida integridade de dados entre agentes"""
        integrity_checks = [
            'customer_data_consistency',
            'appointment_data_completeness',
            'pricing_data_accuracy',
            'handoff_data_preservation'
        ]
        
        integrity_scores = {}
        for check in integrity_checks:
            integrity_scores[check] = self.run_integrity_check(check, test_results)
        
        overall_integrity = np.mean(list(integrity_scores.values()))
        
        return {
            'individual_scores': integrity_scores,
            'overall_integrity_score': overall_integrity,
            'integrity_validated': overall_integrity >= 0.95
        }
```

#### Safety Gates
```json
{
  "safety_gates": {
    "mandatory_checks": [
      {
        "name": "business_rules_preserved",
        "description": "Regras de negócio mantidas",
        "critical": true,
        "validation_method": "rule_compliance_test"
      },
      {
        "name": "data_flow_integrity", 
        "description": "Integridade do fluxo de dados",
        "critical": true,
        "validation_method": "data_consistency_check"
      },
      {
        "name": "error_handling_robust",
        "description": "Tratamento de erros robusto",
        "critical": true,
        "validation_method": "error_injection_test"
      },
      {
        "name": "integration_points_stable",
        "description": "Pontos de integração estáveis",
        "critical": true,
        "validation_method": "integration_stability_test"
      }
    ],
    "rollback_triggers": [
      "critical_functionality_regression",
      "data_integrity_compromised",
      "business_rules_violated",
      "integration_failures_increased"
    ]
  }
}
```

### 🔍 **Critérios de Aprovação - Layer 5**
```json
{
  "layer_5_approval": {
    "minimum_requirements": {
      "no_critical_regressions": true,
      "data_integrity_score": 0.95,
      "business_rules_compliance": 1.0,
      "integration_stability": 0.98
    },
    "safety_certification": {
      "all_safety_gates_passed": true,
      "rollback_plan_validated": true,
      "monitoring_configured": true,
      "emergency_procedures_documented": true
    }
  }
}
```

---

## 📋 **CHECKLIST FINAL DE VALIDAÇÃO**

### Approval Checklist Completo
```json
{
  "final_validation_checklist": {
    "structural_validation": {
      "required_elements_present": false,
      "n8n_compatibility_verified": false,
      "formatting_correct": false,
      "status": "pending"
    },
    "functional_validation": {
      "core_scenarios_passed": false,
      "critical_flows_validated": false,
      "edge_cases_handled": false,
      "status": "pending"
    },
    "quality_validation": {
      "human_score_acceptable": false,
      "naturalness_validated": false,
      "expertise_demonstrated": false,
      "status": "pending"
    },
    "performance_validation": {
      "response_time_acceptable": false,
      "success_rate_maintained": false,
      "improvements_significant": false,
      "status": "pending"
    },
    "security_validation": {
      "no_regressions_detected": false,
      "data_integrity_preserved": false,
      "safety_gates_passed": false,
      "status": "pending"
    },
    "overall_approval": {
      "ready_for_deployment": false,
      "approval_timestamp": null,
      "approved_by": null,
      "rollback_plan_confirmed": false
    }
  }
}
```

### Automated Validation Pipeline
```bash
#!/bin/bash
# validation_pipeline.sh - Pipeline completa de validação

AGENT_ID=$1
OPTIMIZED_PROMPT=$2

echo "🔍 Iniciando validação completa para $AGENT_ID"

# Layer 1: Structural Validation
echo "📋 Layer 1: Validação Estrutural"
python validators/structural_validator.py --agent-id=$AGENT_ID --prompt-file=$OPTIMIZED_PROMPT
if [ $? -ne 0 ]; then
    echo "❌ Layer 1 falhou - parando validação"
    exit 1
fi
echo "✅ Layer 1: Aprovado"

# Layer 2: Functional Validation  
echo "🧪 Layer 2: Validação Funcional"
python validators/functional_validator.py --agent-id=$AGENT_ID --prompt-file=$OPTIMIZED_PROMPT
if [ $? -ne 0 ]; then
    echo "❌ Layer 2 falhou - parando validação"
    exit 1
fi
echo "✅ Layer 2: Aprovado"

# Layer 3: Quality Validation
echo "🎭 Layer 3: Validação de Qualidade"
python validators/quality_validator.py --agent-id=$AGENT_ID --prompt-file=$OPTIMIZED_PROMPT
QUALITY_SCORE=$(python validators/get_quality_score.py --agent-id=$AGENT_ID)
if (( $(echo "$QUALITY_SCORE < 8.0" | bc -l) )); then
    echo "❌ Layer 3 falhou - score: $QUALITY_SCORE (mínimo: 8.0)"
    exit 1
fi
echo "✅ Layer 3: Aprovado (Score: $QUALITY_SCORE)"

# Layer 4: Performance Validation
echo "📊 Layer 4: Validação de Performance"
python validators/performance_validator.py --agent-id=$AGENT_ID --prompt-file=$OPTIMIZED_PROMPT
if [ $? -ne 0 ]; then
    echo "❌ Layer 4 falhou - performance insuficiente"
    exit 1
fi
echo "✅ Layer 4: Aprovado"

# Layer 5: Security Validation
echo "🔒 Layer 5: Validação de Segurança"
python validators/security_validator.py --agent-id=$AGENT_ID --prompt-file=$OPTIMIZED_PROMPT
if [ $? -ne 0 ]; then
    echo "❌ Layer 5 falhou - regressão detectada"
    exit 1
fi
echo "✅ Layer 5: Aprovado"

# Final Approval
echo "🎉 Validação completa aprovada para $AGENT_ID"
python validators/generate_approval_certificate.py --agent-id=$AGENT_ID --prompt-file=$OPTIMIZED_PROMPT

echo "📄 Certificado de aprovação gerado"
echo "🚀 Prompt otimizado pronto para aplicação no n8n"
```

---

## 📊 **RELATÓRIO DE VALIDAÇÃO**

### Template de Relatório
```markdown
# Relatório de Validação de Prompt Otimizado
**Agente**: {{agent_name}}
**Data**: {{validation_date}}
**Versão**: {{prompt_version}}

## 📊 Resumo Executivo
- **Status Geral**: {{overall_status}}
- **Score de Qualidade**: {{quality_score}}/10
- **Melhoria de Performance**: {{performance_improvement}}%
- **Recomendação**: {{recommendation}}

## 🔍 Validação por Layer

### Layer 1: Estrutural ✅
- Elementos obrigatórios: {{structural_completeness}}
- Compatibilidade n8n: {{n8n_compatibility}}
- Formatação: {{formatting_score}}

### Layer 2: Funcional ✅
- Cenários críticos: {{critical_scenarios_passed}}/{{total_critical_scenarios}}
- Taxa de sucesso: {{functional_success_rate}}%
- Fluxos validados: {{validated_flows}}

### Layer 3: Qualidade ✅
- Score humano: {{human_score}}/10
- Naturalidade: {{naturalness_score}}/10
- Expertise: {{expertise_score}}/10

### Layer 4: Performance ✅
- Tempo de resposta: {{avg_response_time}}ms
- Taxa de sucesso: {{success_rate}}%
- Melhoria de tokens: {{token_improvement}}%

### Layer 5: Segurança ✅
- Regressões detectadas: {{regressions_count}}
- Integridade de dados: {{data_integrity_score}}
- Gates de segurança: {{safety_gates_passed}}/{{total_safety_gates}}

## 🎯 Comparação Baseline vs Otimizado

| Métrica | Baseline | Otimizado | Melhoria |
|---------|----------|-----------|-----------|
| Score Humano | {{baseline_human_score}} | {{optimized_human_score}} | {{human_score_improvement}}% |
| Tempo Resposta | {{baseline_response_time}}ms | {{optimized_response_time}}ms | {{response_time_improvement}}% |
| Taxa Sucesso | {{baseline_success_rate}}% | {{optimized_success_rate}}% | {{success_rate_improvement}}% |
| Tokens Usados | {{baseline_tokens}} | {{optimized_tokens}} | {{token_efficiency}}% |

## ✅ Certificação de Aprovação
- **Validação Completa**: ✅ APROVADO
- **Certificado por**: Sistema de Validação Automático
- **Data/Hora**: {{approval_timestamp}}
- **Hash de Validação**: {{validation_hash}}

## 🚀 Próximos Passos
1. ✅ Aplicar prompt otimizado no n8n workflow {{workflow_id}}
2. 📊 Monitorar performance por 48 horas
3. 📝 Documentar resultados no histórico de otimizações
4. 🔄 Configurar monitoramento contínuo

---
*Relatório gerado automaticamente pelo Sistema de Validação de Prompts Bable Pet*
```

---

*Este protocolo garante validação rigorosa e sistemática de todos os prompts otimizados, assegurando qualidade, performance e segurança antes da aplicação no ambiente de produção.*