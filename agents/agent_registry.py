"""
Agent Registry for managing and coordinating agents.
"""

from typing import Dict, List, Any, Optional
from .base_agent import BaseAgent


class AgentRegistry:
    """Registry for managing all agents in the system."""
    
    def __init__(self):
        """Initialize the agent registry."""
        self._agents: Dict[str, BaseAgent] = {}
        self._execution_history: List[Dict[str, Any]] = []
    
    def register(self, agent: BaseAgent) -> str:
        """
        Register an agent.
        
        Args:
            agent: Agent instance to register
            
        Returns:
            Agent ID
        """
        self._agents[agent.id] = agent
        return agent.id
    
    def unregister(self, agent_id: str) -> bool:
        """
        Unregister an agent.
        
        Args:
            agent_id: ID of agent to unregister
            
        Returns:
            True if successful, False if agent not found
        """
        if agent_id in self._agents:
            del self._agents[agent_id]
            return True
        return False
    
    def get_agent(self, agent_id: str) -> Optional[BaseAgent]:
        """
        Get an agent by ID.
        
        Args:
            agent_id: Agent ID
            
        Returns:
            Agent instance or None if not found
        """
        return self._agents.get(agent_id)
    
    def get_all_agents(self) -> List[BaseAgent]:
        """Get all registered agents."""
        return list(self._agents.values())
    
    def get_agent_by_name(self, name: str) -> Optional[BaseAgent]:
        """Get an agent by name."""
        for agent in self._agents.values():
            if agent.name == name:
                return agent
        return None
    
    def execute_agent_task(self, agent_id: str, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a task on an agent.
        
        Args:
            agent_id: ID of agent to execute task on
            task: Task to execute
            
        Returns:
            Execution result
        """
        agent = self.get_agent(agent_id)
        if not agent:
            return {"success": False, "error": f"Agent {agent_id} not found"}
        
        try:
            agent.status = "running"
            result = agent.execute(task)
            agent.status = "idle"
            
            # Record execution
            execution_record = {
                "agent_id": agent_id,
                "agent_name": agent.name,
                "task": task,
                "result": result,
                "success": True
            }
            self._execution_history.append(execution_record)
            
            return {"success": True, "result": result}
        except Exception as e:
            agent.status = "error"
            error_msg = str(e)
            agent.log_event("error", f"Task execution failed: {error_msg}")
            
            return {"success": False, "error": error_msg}
    
    def get_execution_history(self, agent_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get execution history.
        
        Args:
            agent_id: Optional agent ID to filter history
            
        Returns:
            List of execution records
        """
        if agent_id:
            return [rec for rec in self._execution_history if rec["agent_id"] == agent_id]
        return self._execution_history
    
    def get_registry_status(self) -> Dict[str, Any]:
        """Get overall registry status."""
        return {
            "total_agents": len(self._agents),
            "agents": [agent.get_status() for agent in self._agents.values()],
            "execution_count": len(self._execution_history)
        }
