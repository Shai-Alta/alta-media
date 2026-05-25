# Agent & Dashboard System

A modular Python framework for building agent-based systems with monitoring dashboards.

## 📋 Features

- **Flexible Agent System**: Abstract base class for creating custom agents
- **Agent Registry**: Centralized management of agents with task execution
- **Monitoring Dashboard**: Real-time system monitoring and analytics
- **Event Logging**: Built-in event logging for all agents
- **Execution Tracking**: Complete history of all agent executions
- **Example Implementations**: Pre-built agents for data processing, analytics, and notifications

## 🏗️ Architecture

```
alta-media/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py          # Abstract base class
│   ├── agent_registry.py      # Central coordinator
│   └── example_agents.py      # Example implementations
├── dashboard/
│   ├── __init__.py
│   └── dashboard.py           # Monitoring dashboard
├── main.py                    # Demo entry point
├── requirements.txt           # Dependencies
└── README.md                  # This file
```

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Shai-Alta/alta-media.git
cd alta-media

# Install dependencies
pip install -r requirements.txt
```

### Running the Demo

```bash
python main.py
```

This will:
1. Create 3 example agents
2. Register them in the system
3. Execute sample tasks
4. Display the monitoring dashboard
5. Print a full system report

## 📚 Usage Guide

### Creating a Custom Agent

```python
from agents import BaseAgent

class MyCustomAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="MyAgent",
            description="Description of what my agent does"
        )
    
    def execute(self, task: Dict[str, Any]) -> Dict[str, Any]:
        # Implement your agent logic here
        self.log_event("info", "Task started")
        
        result = {
            "status": "completed",
            "data": "your_result_here"
        }
        
        return result
```

### Using the Registry

```python
from agents import AgentRegistry
from agents.example_agents import DataProcessorAgent

# Initialize registry
registry = AgentRegistry()

# Create and register agent
agent = DataProcessorAgent()
agent_id = registry.register(agent)

# Execute a task
task = {"data": [1, 2, 3]}
result = registry.execute_agent_task(agent_id, task)

# Get system status
status = registry.get_registry_status()
```

### Using the Dashboard

```python
from dashboard import Dashboard

# Create dashboard
dashboard = Dashboard(registry)

# Get system overview
overview = dashboard.get_system_overview()

# Print interactive dashboard
dashboard.print_dashboard()

# Get full report
report = dashboard.get_full_report()
```

## 📊 Included Agents

### DataProcessorAgent
Processes and validates incoming data.

```python
task = {
    "data_type": "user_metrics",
    "data": [1, 2, 3, 4, 5]
}
```

### AnalyticsAgent
Generates analytics and reports.

```python
task = {
    "metric": "user_engagement"
}
```

### NotificationAgent
Sends notifications and alerts.

```python
task = {
    "message": "System health check completed",
    "channel": "slack"
}
```

## 🔄 System Flow

```
1. Create Agents
   ↓
2. Register with AgentRegistry
   ↓
3. Execute Tasks via Registry
   ↓
4. Monitor with Dashboard
   ↓
5. Review Execution History & Analytics
```

## 🛠️ Development Roadmap

- [ ] REST API endpoints for agent management
- [ ] GraphQL interface
- [ ] Web-based dashboard UI
- [ ] Database persistence (SQLAlchemy)
- [ ] Advanced agent scheduling
- [ ] Inter-agent communication
- [ ] Agent state persistence
- [ ] Performance metrics
- [ ] Docker containerization

## 💡 Next Steps

This is a foundation ready for extension. You can:

1. **Add specialized agents** - Create domain-specific agents (ContentAgent, AnalyticsAgent, etc.)
2. **Build APIs** - Add REST or GraphQL endpoints
3. **Create web UI** - Build a React/Vue dashboard
4. **Add persistence** - Connect to a database
5. **Implement scheduling** - Add task scheduling with APScheduler
6. **Advanced monitoring** - Add metrics collection and alerting

## 📝 License

MIT

## 👤 Author

Shai-Alta (shai@alta-media.net)
