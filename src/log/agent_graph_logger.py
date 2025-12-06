import json
from datetime import datetime
from typing import Dict, Any


class AgentGraphLogger:
    """
    AgentGraphLogger
    ----------------
    - Logs Tool, Agent, Node, Graph executions
    - Logs to stdout
    """
    def log_to_stdout(self, log_type: str, data: Dict[str, Any]):
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "type": log_type,
            "data": data
        }
        print(f"[LOG] {json.dumps(log_entry, ensure_ascii=False, indent=2)}")

    
    def log_tool(
        self,
        tool_name: str,
        input_data,
        output_data = None,
        error: Exception = None,
        execution_time: float = None
    ):
        log_data = {
            "tool_name": tool_name,
            "input": str(input_data) | None,
            "output": str(output_data) | None,
            "error": str(error) | None,
            "execution_time": execution_time
        }
        
        self.log_to_stdout("tool_execution", log_data)


    # def log_agent(
    #     self, 
    #     agent_name: str,
    #     input_data: Any, 
    #     output_data: Any = None,
    #     error: Exception = None,
    #     execution_time: float = None,
    #     metadata: Dict[str, Any] = None
    # ):
    #     log_data = {
    #         "agent_name": agent_name,
    #         "input": self.make_serializable(input_data),
    #         "output": self.make_serializable(output_data),
    #         "error": str(error) | None,
    #         "execution_time": execution_time,
    #         "metadata": metadata
    #     }
        
    #     self.log_to_stdout("agent_execution", log_data)
    

    # def log_node(
    #     self, 
    #     node_name: str,
    #     input_data: Any, 
    #     output_data: Any = None,
    #     error: Exception = None, 
    #     execution_time: float = None
    # ):
    #     log_data = {
    #         "node_name": node_name,
    #         "input": self.make_serializable(input_data),
    #         "output": self.make_serializable(output_data),
    #         "error": str(error) | None,
    #         "execution_time": execution_time
    #     }
        
    #     self.log_to_stdout("node_execution", log_data)


    def log_graph(
        self, 
        input_data, 
        output_data = None,
        error: Exception = None, 
        execution_time: float = None
    ):
        log_data = {
            "input_data": self.make_serializable(input_data),
            "output_data": self.make_serializable(output_data),
            "error": str(error) if error else None,
            "execution_time": execution_time
        }
        
        self.log_to_stdout("graph_execution", log_data)
    

    def make_serializable(self, obj: Any) -> Dict[str, Any]:
        if isinstance(obj, dict):
            # Handle dict
            result = {}
            for key, value in obj.items():
                try:
                    result[key] = [self.make_serializable(item) for item in value]
                except (TypeError, ValueError):
                    result[key] = str(value)
            return result
        
        elif isinstance(obj, list):
            # Handle list
            return [self.make_serializable(item) for item in obj]
        
        else:
            # Convert to string
            return {"input": str(obj)}
