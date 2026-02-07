"""
Cliente para interagir com a Agent API
Facilita o uso da API sem precisa de cURL ou Postman
"""

import requests
from typing import Optional, List, Dict, Any
import json


class AgentAPIClient:
    """Cliente para a Agent API"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
    
    def _make_request(self, method: str, endpoint: str, data: Dict = None) -> Dict[str, Any]:
        """Faz uma requisição HTTP"""
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method == "GET":
                response = self.session.get(url)
            elif method == "POST":
                response = self.session.post(url, json=data)
            elif method == "DELETE":
                response = self.session.delete(url)
            else:
                raise ValueError(f"Método HTTP não suportado: {method}")
            
            response.raise_for_status()
            return response.json()
        
        except requests.exceptions.ConnectionError:
            return {"error": "Não foi possível conectar à API. Certifique-se de que o servidor está rodando."}
        except requests.exceptions.HTTPError as e:
            return {"error": f"Erro HTTP: {e.response.status_code} - {e.response.text}"}
        except Exception as e:
            return {"error": f"Erro: {str(e)}"}
    
    # ==================== GERENCIAMENTO DE AGENTES ====================
    
    def create_agent(self, agent_name: str) -> Dict[str, Any]:
        """Cria um novo agente"""
        data = {"agent_name": agent_name}
        return self._make_request("POST", "/agent/create", data)
    
    def list_agents(self) -> Dict[str, Any]:
        """Lista todos os agentes"""
        return self._make_request("GET", "/agent/list")
    
    def get_agent_info(self, agent_name: str) -> Dict[str, Any]:
        """Retorna informações de um agente"""
        return self._make_request("GET", f"/agent/{agent_name}")
    
    def delete_agent(self, agent_name: str) -> Dict[str, Any]:
        """Deleta um agente"""
        return self._make_request("DELETE", f"/agent/{agent_name}")
    
    # ==================== MODOS DE OPERAÇÃO ====================
    
    def ask(self, agent_name: str, prompt: str) -> Dict[str, Any]:
        """
        Modo ASK: Pergunta ao agente
        
        Args:
            agent_name: Nome do agente
            prompt: A pergunta
        
        Returns:
            Resposta do agente
        """
        data = {"prompt": prompt}
        return self._make_request("POST", f"/agent/{agent_name}/ask", data)
    
    def study(self, agent_name: str, prompt: str, context: Optional[str] = None) -> Dict[str, Any]:
        """
        Modo STUDY: Análise profunda
        
        Args:
            agent_name: Nome do agente
            prompt: O tópico para análise
            context: Contexto opcional
        
        Returns:
            Análise do agente
        """
        data = {"prompt": prompt, "context": context}
        return self._make_request("POST", f"/agent/{agent_name}/study", data)
    
    def plan(self, agent_name: str, prompt: str, goals: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Modo PLAN: Plano de ação
        
        Args:
            agent_name: Nome do agente
            prompt: O objetivo principal
            goals: Lista de metas específicas
        
        Returns:
            Plano do agente
        """
        data = {"prompt": prompt, "goals": goals}
        return self._make_request("POST", f"/agent/{agent_name}/plan", data)
    
    # ==================== HISTÓRICO ====================
    
    def get_history(self, agent_name: str) -> Dict[str, Any]:
        """Retorna o histórico de um agente"""
        return self._make_request("GET", f"/agent/{agent_name}/history")
    
    def clear_history(self, agent_name: str) -> Dict[str, Any]:
        """Limpa o histórico de um agente"""
        return self._make_request("DELETE", f"/agent/{agent_name}/history")
    
    # ==================== UTILIDADE ====================
    
    def health_check(self) -> Dict[str, Any]:
        """Verifica o status da API"""
        return self._make_request("GET", "/health")
    
    def get_api_info(self) -> Dict[str, Any]:
        """Retorna informações da API"""
        return self._make_request("GET", "/")


def print_response(response: Dict[str, Any]):
    """Imprime uma resposta de forma legível"""
    print(json.dumps(response, indent=2, ensure_ascii=False))


def main():
    """Exemplo de uso do cliente"""
    print("="*70)
    print("🤖 CLIENTE AGENT API")
    print("="*70)
    
    # Criar cliente
    client = AgentAPIClient()
    
    # Verificar status da API
    print("\n📡 Verificando status da API...")
    health = client.health_check()
    if "error" in health:
        print(f"❌ Erro: {health['error']}")
        print("\nCertifique-se de que o servidor está rodando:")
        print("  python app.py")
        return
    print("✅ API está funcionando!")
    
    # Criar agente
    agent_name = "meu_agente"
    print(f"\n🤖 Criando agente '{agent_name}'...")
    response = client.create_agent(agent_name)
    print_response(response)
    
    # Modo ASK
    print("\n📌 MODO ASK")
    print("-"*70)
    response = client.ask(agent_name, "Qual é a capital do Brasil?")
    print_response(response)
    
    # Modo STUDY
    print("\n📌 MODO STUDY")
    print("-"*70)
    response = client.study(
        agent_name,
        "Explique como funciona inteligência artificial",
        context="para iniciantes"
    )
    print_response(response)
    
    # Modo PLAN
    print("\n📌 MODO PLAN")
    print("-"*70)
    response = client.plan(
        agent_name,
        "Aprender Python",
        goals=["Sintaxe básica", "POO", "Criar projetos"]
    )
    print_response(response)
    
    # Histórico
    print("\n📚 HISTÓRICO")
    print("-"*70)
    response = client.get_history(agent_name)
    print_response(response)
    
    # Listar agentes
    print("\n📋 LISTAR AGENTES")
    print("-"*70)
    response = client.list_agents()
    print_response(response)
    
    # Info da API
    print("\n📊 INFO DA API")
    print("-"*70)
    response = client.get_api_info()
    print_response(response)


if __name__ == "__main__":
    main()
