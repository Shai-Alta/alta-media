"""
Base Agent class for the agent system.
All agents inherit from this class.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List
from datetime import datetime
import uuid


class BaseAgent(ABC):
    """Abstract base class for all agents in the system."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize a base agent.
        
        Args:
            name: Agent name
            description: Agent description
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.status = "idle"
        self.logs: List[Dict[str, Any]] = []
    
    @abstractmethod
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a task. Must be implemented by subclasses.
        
        Args:
            task: Task dictionary containing task details
            
        Returns:
            Result dictionary
        """
        pass
    
    def log_event(self, event_type: str, message: str, data: Dict[str, Any] = None):
        """
        Log an event for this agent.
        
        Args:
            event_type: Type of event (e.g., 'info', 'error', 'warning')
            message: Event message
            data: Additional data to log
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "type": event_type,
            "message": message,
            "data": data or {}
        }
        self.logs.append(log_entry)
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status information."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat(),
            "log_count": len(self.logs)
        }
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: {self.name} (id={self.id})>"
