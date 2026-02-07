"""
Exemplo de uso dos agentes
Execute este arquivo para testar a funcionalidade dos agentes
"""

from agent import SimpleAgent, AgentMode


def example_simple_agent():
    """Exemplo com SimpleAgent (sem API OpenAI)"""
    print("=" * 60)
    print("EXEMPLO COM SimpleAgent")
    print("=" * 60)
    
    # Criar agente
    agent = SimpleAgent(name="Assistente", description="Agente de demonstração")
    
    # ===== MODO ASK =====
    print("\n📌 MODO ASK (Resposta Direta)")
    print("-" * 60)
    ask_response = agent.ask("Qual é a capital do Brasil?")
    print(f"Pergunta: {ask_response.prompt}")
    print(f"Resposta:\n{ask_response.response}\n")
    
    # ===== MODO STUDY =====
    print("\n📌 MODO STUDY (Análise Profunda)")
    print("-" * 60)
    study_response = agent.study(
        "Explique como funciona machine learning",
        context="Para iniciantes em programação"
    )
    print(f"Tema: {study_response.prompt}")
    print(f"Análise:\n{study_response.response}\n")
    
    # ===== MODO PLAN =====
    print("\n📌 MODO PLAN (Plano de Ação)")
    print("-" * 60)
    plan_response = agent.plan(
        "Aprender Python do zero",
        goals=[
            "Dominar sintaxe básica",
            "Aprender POO",
            "Criar projetos reais"
        ]
    )
    print(f"Objetivo: {plan_response.prompt}")
    print(f"Plano:\n{plan_response.response}\n")
    
    # ===== HISTÓRICO =====
    print("\n📌 HISTÓRICO DE CONVERSAÇÕES")
    print("-" * 60)
    history = agent.get_history()
    print(f"Total de interações: {len(history)}")
    for i, entry in enumerate(history, 1):
        print(f"\n{i}. Modo: {entry['mode']}")
        print(f"   Pergunta: {entry['prompt'][:50]}...")


def example_with_api():
    """Exemplo de como usar com a API"""
    print("\n" + "=" * 60)
    print("COMO USAR COM A API")
    print("=" * 60)
    
    print("\n1. INICIE O SERVIDOR:")
    print("   python app.py")
    
    print("\n2. CRIE UM AGENTE (POST):")
    print('   curl -X POST http://localhost:8000/agent/create \\')
    print('     -H "Content-Type: application/json" \\')
    print('     -d \'{"agent_name": "meu_agente"}\'')
    
    print("\n3. USE O MODO ASK (POST):")
    print('   curl -X POST http://localhost:8000/agent/meu_agente/ask \\')
    print('     -H "Content-Type: application/json" \\')
    print('     -d \'{"prompt": "Qual é a capital do Brasil?"}\'')
    
    print("\n4. USE O MODO STUDY (POST):")
    print('   curl -X POST http://localhost:8000/agent/meu_agente/study \\')
    print('     -H "Content-Type: application/json" \\')
    print('     -d \'{"prompt": "Explique machine learning", "context": "para iniciantes"}\'')
    
    print("\n5. USE O MODO PLAN (POST):")
    print('   curl -X POST http://localhost:8000/agent/meu_agente/plan \\')
    print('     -H "Content-Type: application/json" \\')
    print('     -d \'{"prompt": "Aprender Python", "goals": ["sintaxe", "POO", "projetos"]}\'')
    
    print("\n6. VEJA O HISTÓRICO (GET):")
    print('   curl http://localhost:8000/agent/meu_agente/history')
    
    print("\n7. ACESSE A DOCUMENTAÇÃO INTERATIVA:")
    print("   http://localhost:8000/docs")


if __name__ == "__main__":
    # Executar exemplo com SimpleAgent
    example_simple_agent()
    
    # Mostrar informações sobre como usar a API
    example_with_api()
    
    print("\n" + "=" * 60)
    print("✅ Exemplos concluídos!")
    print("=" * 60)
