from typing import Optional, Dict, Any
from enum import Enum
from abc import ABC, abstractmethod
import json


class AgentMode(str, Enum):
    """Modos de operação do agente"""
    ASK = "ask"
    STUDY = "study"
    PLAN = "plan"


class AgentResponse:
    """Estrutura de resposta do agente"""
    def __init__(self, mode: AgentMode, prompt: str, response: str, metadata: Dict[str, Any] = None):
        self.mode = mode
        self.prompt = prompt
        self.response = response
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "mode": self.mode.value,
            "prompt": self.prompt,
            "response": self.response,
            "metadata": self.metadata
        }


class BaseAgent(ABC):
    """Classe base para agentes"""
    
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description
        self.conversation_history = []

    @abstractmethod
    def ask(self, prompt: str) -> AgentResponse:
        """
        Modo ASK: Responde perguntas diretamente
        Ideal para respostas rápidas e diretas
        """
        pass

    @abstractmethod
    def study(self, prompt: str, context: Optional[str] = None) -> AgentResponse:
        """
        Modo STUDY: Analisa profundamente um tópico
        Retorna análise detalhada com explicações
        """
        pass

    @abstractmethod
    def plan(self, prompt: str, goals: Optional[list] = None) -> AgentResponse:
        """
        Modo PLAN: Cria um plano de ação
        Retorna passos estruturados para atingir um objetivo
        """
        pass

    def add_to_history(self, mode: AgentMode, prompt: str, response: str):
        """Adiciona à história de conversação"""
        self.conversation_history.append({
            "mode": mode.value,
            "prompt": prompt,
            "response": response
        })

    def get_history(self) -> list:
        """Retorna histórico de conversações"""
        return self.conversation_history

    def clear_history(self):
        """Limpa o histórico"""
        self.conversation_history = []


class SimpleAgent(BaseAgent):
    """
    Implementação simples de um agente
    Pode ser estendida com integração de LLM real
    """

    # Prompts específicos para cada modo
    PROMPTS_TEMPLATES = {
        AgentMode.ASK: "Responda diretamente e concisamente: {prompt}",
        AgentMode.STUDY: "Analise profundamente este tópico. Forneça explicações detalhadas, exemplos e insights: {prompt}",
        AgentMode.PLAN: "Crie um plano de ação estruturado com passos claros para: {prompt}"
    }

    def __init__(self, name: str = "SimpleAgent", description: str = "Agente simples de demonstração"):
        super().__init__(name, description)

    def ask(self, prompt: str) -> AgentResponse:
        """
        Modo ASK: Resposta direta
        """
        # Aqui você pode integrar com um LLM real
        response_text = f"Resposta para: {prompt}\n\nEste é um exemplo de resposta rápida e direta ao seu questionamento."
        
        agent_response = AgentResponse(
            mode=AgentMode.ASK,
            prompt=prompt,
            response=response_text,
            metadata={"processed": True}
        )
        
        self.add_to_history(AgentMode.ASK, prompt, response_text)
        return agent_response

    def study(self, prompt: str, context: Optional[str] = None) -> AgentResponse:
        """
        Modo STUDY: Análise profunda
        """
        response_text = f"Análise profunda sobre: {prompt}\n\n"
        response_text += "1. CONTEXTO:\n   - Este é um tópico importante para compreensão.\n\n"
        response_text += "2. ANÁLISE DETALHADA:\n   - Primeiro aspecto: Explicação detalhada.\n   - Segundo aspecto: Insights relevantes.\n\n"
        response_text += "3. EXEMPLOS:\n   - Exemplo prático do conceito.\n\n"
        response_text += "4. CONCLUSÕES:\n   - Resumo das aprendizagens principais."
        
        if context:
            response_text += f"\n\nCONTEXTO FORNECIDO: {context}"
        
        agent_response = AgentResponse(
            mode=AgentMode.STUDY,
            prompt=prompt,
            response=response_text,
            metadata={"depth": "detailed", "context_provided": context is not None}
        )
        
        self.add_to_history(AgentMode.STUDY, prompt, response_text)
        return agent_response

    def plan(self, prompt: str, goals: Optional[list] = None) -> AgentResponse:
        """
        Modo PLAN: Criação de plano
        """
        response_text = f"Plano de ação para: {prompt}\n\n"
        response_text += "OBJETIVO PRINCIPAL:\n   - " + prompt + "\n\n"
        
        if goals:
            response_text += "METAS ESPECÍFICAS:\n"
            for i, goal in enumerate(goals, 1):
                response_text += f"   {i}. {goal}\n"
            response_text += "\n"
        
        response_text += "PASSOS DE EXECUÇÃO:\n"
        response_text += "   1. Preparação e análise\n"
        response_text += "   2. Planejamento detalhado\n"
        response_text += "   3. Implementação\n"
        response_text += "   4. Monitoramento\n"
        response_text += "   5. Avaliação e ajustes\n\n"
        response_text += "TIMELINE ESTIMADA:\n"
        response_text += "   - Curto prazo: 1-2 semanas\n"
        response_text += "   - Médio prazo: 1-3 meses\n"
        response_text += "   - Longo prazo: 3-6 meses"
        
        agent_response = AgentResponse(
            mode=AgentMode.PLAN,
            prompt=prompt,
            response=response_text,
            metadata={"goals_count": len(goals) if goals else 0}
        )
        
        self.add_to_history(AgentMode.PLAN, prompt, response_text)
        return agent_response
