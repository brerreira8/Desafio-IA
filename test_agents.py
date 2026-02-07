"""
Teste de validação dos agentes
Execute: python test_agents.py
"""

import sys
from agent import SimpleAgent, AgentMode


def test_simple_agent():
    """Testa o SimpleAgent em todos os três modos"""
    print("\n" + "="*70)
    print("🧪 TESTE: SimpleAgent")
    print("="*70)
    
    agent = SimpleAgent(name="TestAgent")
    
    # Teste 1: ASK
    print("\n✓ Testando Modo ASK...")
    ask_response = agent.ask("Teste de pergunta simples")
    assert ask_response.mode == AgentMode.ASK
    assert ask_response.prompt == "Teste de pergunta simples"
    assert len(ask_response.response) > 0
    print(f"  ✅ Resposta gerada: {len(ask_response.response)} caracteres")
    
    # Teste 2: STUDY
    print("\n✓ Testando Modo STUDY...")
    study_response = agent.study("Teste de análise", context="contexto teste")
    assert study_response.mode == AgentMode.STUDY
    assert study_response.prompt == "Teste de análise"
    assert len(study_response.response) > 0
    assert study_response.metadata["context_provided"] == True
    print(f"  ✅ Análise gerada: {len(study_response.response)} caracteres")
    
    # Teste 3: PLAN
    print("\n✓ Testando Modo PLAN...")
    goals = ["Meta 1", "Meta 2", "Meta 3"]
    plan_response = agent.plan("Teste de plano", goals=goals)
    assert plan_response.mode == AgentMode.PLAN
    assert plan_response.prompt == "Teste de plano"
    assert len(plan_response.response) > 0
    assert plan_response.metadata["goals_count"] == 3
    print(f"  ✅ Plano gerado: {len(plan_response.response)} caracteres")
    
    # Teste 4: Histórico
    print("\n✓ Testando Histórico...")
    history = agent.get_history()
    assert len(history) == 3
    assert history[0]["mode"] == "ask"
    assert history[1]["mode"] == "study"
    assert history[2]["mode"] == "plan"
    print(f"  ✅ Histórico com {len(history)} entradas")
    
    # Teste 5: Limpar histórico
    print("\n✓ Testando Limpeza de Histórico...")
    agent.clear_history()
    history = agent.get_history()
    assert len(history) == 0
    print(f"  ✅ Histórico limpo com sucesso")
    
    print("\n✅ Todos os testes do SimpleAgent passaram!")
    return True


def test_agent_modes():
    """Testa o enum AgentMode"""
    print("\n" + "="*70)
    print("🧪 TESTE: AgentMode Enum")
    print("="*70)
    
    # Teste dos valores enum
    print("\n✓ Testando valores de AgentMode...")
    assert AgentMode.ASK.value == "ask"
    assert AgentMode.STUDY.value == "study"
    assert AgentMode.PLAN.value == "plan"
    print(f"  ✅ AgentMode.ASK = {AgentMode.ASK.value}")
    print(f"  ✅ AgentMode.STUDY = {AgentMode.STUDY.value}")
    print(f"  ✅ AgentMode.PLAN = {AgentMode.PLAN.value}")
    
    print("\n✅ Testes de AgentMode passaram!")
    return True


def test_response_structure():
    """Testa a estrutura de resposta"""
    print("\n" + "="*70)
    print("🧪 TESTE: Estrutura de Resposta")
    print("="*70)
    
    print("\n✓ Testando estrutura de resposta...")
    agent = SimpleAgent()
    response = agent.ask("Teste")
    
    response_dict = response.to_dict()
    assert "mode" in response_dict
    assert "prompt" in response_dict
    assert "response" in response_dict
    assert "metadata" in response_dict
    
    print(f"  ✅ Campos da resposta: {list(response_dict.keys())}")
    print(f"  ✅ Resposta em dict convertida com sucesso")
    
    print("\n✅ Testes de estrutura passaram!")
    return True


def test_multiple_agents():
    """Testa múltiplos agentes independentes"""
    print("\n" + "="*70)
    print("🧪 TESTE: Múltiplos Agentes")
    print("="*70)
    
    print("\n✓ Criando múltiplos agentes...")
    agent1 = SimpleAgent(name="Agent1")
    agent2 = SimpleAgent(name="Agent2")
    agent3 = SimpleAgent(name="Agent3")
    
    # Cada agente deve ter histórico independente
    agent1.ask("Pergunta 1")
    agent2.ask("Pergunta 2")
    agent2.ask("Pergunta 3")
    agent3.ask("Pergunta 4")
    
    assert len(agent1.get_history()) == 1
    assert len(agent2.get_history()) == 2
    assert len(agent3.get_history()) == 1
    
    print(f"  ✅ Agent1 com {len(agent1.get_history())} entrada")
    print(f"  ✅ Agent2 com {len(agent2.get_history())} entradas")
    print(f"  ✅ Agent3 com {len(agent3.get_history())} entrada")
    print(f"  ✅ Agentes independentes funcionam corretamente")
    
    print("\n✅ Testes de múltiplos agentes passaram!")
    return True


def run_all_tests():
    """Executa todos os testes"""
    print("\n")
    print("╔" + "="*68 + "╗")
    print("║" + " "*68 + "║")
    print("║" + "  🧪  EXECUTANDO TESTES DO AGENT  ".center(68) + "║")
    print("║" + " "*68 + "║")
    print("╚" + "="*68 + "╝")
    
    tests = [
        test_agent_modes,
        test_simple_agent,
        test_response_structure,
        test_multiple_agents
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            failed += 1
            print(f"\n❌ Teste falhou: {test.__name__}")
            print(f"   Erro: {str(e)}")
    
    print("\n" + "="*70)
    print("📊 RESULTADO DOS TESTES")
    print("="*70)
    print(f"✅ Testes aprovados: {passed}")
    print(f"❌ Testes falhados: {failed}")
    print(f"📈 Total de testes: {passed + failed}")
    
    if failed == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM COM SUCESSO! 🎉")
        return True
    else:
        print(f"\n⚠️  {failed} teste(s) falharam")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
