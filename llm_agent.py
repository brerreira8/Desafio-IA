"""
Agente integrado com OpenAI GPT
Para usar, configure sua API key no .env
"""

from typing import Optional, Dict, Any
import openai
from config import API_KEY, MODEL_DEFAULT, TEMPERATURE, MAX_TOKENS
from agent import BaseAgent, AgentMode, AgentResponse


class GPTAgent(BaseAgent):
    """
    Agente integrado com OpenAI GPT
    Fornece respostas reais usando o modelo GPT
    """

    # Prompts específicos para cada modo
    SYSTEM_PROMPTS = {
        AgentMode.ASK: """Você é um assistente inteligente e útil.
        Responda às perguntas de forma direta, concisa e clara.
        Vá direto ao ponto.""",

        AgentMode.STUDY: """Você é um professor e pesquisador experiente.
        Quando solicitado, forneça análises profundas e detalhadas.
        Inclua contexto, exemplos práticos e insights importantes.
        Estruture suas respostas de forma clara e organizada.""",

        AgentMode.PLAN: """Você é um estrategista e planejador experiente.
        Quando solicitado, crie planos de ação estruturados e viáveis.
        Inclua passos claros, metas, timeline e recursos necessários.
        Seja prático e objetivo."""
    }

    def __init__(self, name: str = "GPTAgent", description: str = "Agente inteligente baseado em GPT"):
        super().__init__(name, description)
        openai.api_key = API_KEY
        self.model = MODEL_DEFAULT

    def _call_gpt(self, system_prompt: str, user_prompt: str) -> str:
        """
        Chama a API OpenAI GPT
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=TEMPERATURE,
                max_tokens=MAX_TOKENS
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao chamar GPT: {str(e)}"

    def ask(self, prompt: str) -> AgentResponse:
        """
        Modo ASK: Resposta direta via GPT
        """
        system_prompt = self.SYSTEM_PROMPTS[AgentMode.ASK]
        response_text = self._call_gpt(system_prompt, prompt)
        
        agent_response = AgentResponse(
            mode=AgentMode.ASK,
            prompt=prompt,
            response=response_text,
            metadata={"model": self.model}
        )
        
        self.add_to_history(AgentMode.ASK, prompt, response_text)
        return agent_response

    def study(self, prompt: str, context: Optional[str] = None) -> AgentResponse:
        """
        Modo STUDY: Análise profunda via GPT
        """
        system_prompt = self.SYSTEM_PROMPTS[AgentMode.STUDY]
        
        study_prompt = prompt
        if context:
            study_prompt = f"Contexto: {context}\n\nAnálise: {prompt}"
        
        response_text = self._call_gpt(system_prompt, study_prompt)
        
        agent_response = AgentResponse(
            mode=AgentMode.STUDY,
            prompt=prompt,
            response=response_text,
            metadata={"model": self.model, "context_provided": context is not None}
        )
        
        self.add_to_history(AgentMode.STUDY, prompt, response_text)
        return agent_response

    def plan(self, prompt: str, goals: Optional[list] = None) -> AgentResponse:
        """
        Modo PLAN: Plano de ação via GPT
        """
        system_prompt = self.SYSTEM_PROMPTS[AgentMode.PLAN]
        
        plan_prompt = prompt
        if goals:
            goals_text = "\n".join([f"- {goal}" for goal in goals])
            plan_prompt = f"Objetivo: {prompt}\n\nMetas específicas:\n{goals_text}\n\nCrie um plano detalhado."
        
        response_text = self._call_gpt(system_prompt, plan_prompt)
        
        agent_response = AgentResponse(
            mode=AgentMode.PLAN,
            prompt=prompt,
            response=response_text,
            metadata={"model": self.model, "goals_count": len(goals) if goals else 0}
        )
        
        self.add_to_history(AgentMode.PLAN, prompt, response_text)
        return agent_response
