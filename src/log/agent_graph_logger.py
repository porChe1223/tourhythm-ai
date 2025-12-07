import json
import os
from datetime import datetime
from langchain_core.tracers import LangChainTracer
from langsmith import Client
from typing import Dict, Any

from config.settings import Setting


class AgentGraphLogger:
    """
    AgentGraphLogger
    ----------------
    - Logs Tool, Agent, Node, Graph executions
    - Uses LangSmith if configured
    - Otherwise logs to stdout
    """

    def __init__(self):
        self.langsmith_client = LangSmithClient()
    

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
        
        if self.langsmith_client.is_enabled:
            print(f"✅ LangSmith auto-tracing active for tool: {tool_name}")


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
        
    #     if self.langsmith_client.is_enabled:
    #         print(f"✅ LangSmith auto-tracing active for agent: {agent_name}")
    

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
        
    #     if self.langsmith_client.is_enabled:
    #         print(f"✅ LangSmith auto-tracing active for node: {node_name}"
    # )


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
        
        if not self.langsmith_client.is_enabled:
            self.log_to_stdout("graph_execution", log_data)

            return
        
        self.log_to_stdout("graph_execution", log_data)

        if self.langsmith_client.is_enabled:
            print("✅ LangSmith auto-tracing active for graph execution")
    

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


class LangSmithClient():
    """
    LangSmith Client
    ----------------
    - Extended from Setting
    - Manages LangSmith Client and Tracer
    """
    def __init__(self):
        setting = Setting()
        self.ENABLE_LANGSMITH = setting.ENABLE_LANGSMITH
        self.LANGCHAIN_TRACING_V2 = setting.LANGCHAIN_TRACING_V2.get_secret_value()
        self.LANGCHAIN_API_KEY = setting.LANGCHAIN_API_KEY.get_secret_value()
        self.LANGCHAIN_ENDPOINT = setting.LANGCHAIN_ENDPOINT.get_secret_value()
        self.LANGCHAIN_PROJECT = setting.LANGCHAIN_PROJECT.get_secret_value()
        self.client = None
        self.tracer = None
        self.enabled = False

        if not self.ENABLE_LANGSMITH:
            print("⚠️ LangSmith Logging is OFF.")

            return
        
        try:
            # Set Environment Variables in OS for LangSmith
            os.environ["LANGCHAIN_TRACING_V2"] = self.LANGCHAIN_TRACING_V2
            os.environ["LANGCHAIN_ENDPOINT"] = self.LANGCHAIN_ENDPOINT
            os.environ["LANGCHAIN_API_KEY"] = self.LANGCHAIN_API_KEY
            os.environ["LANGCHAIN_PROJECT"] = self.LANGCHAIN_PROJECT

            self.enabled = True

        except Exception as e:
            print(f"⚠️ Could not Start LangSmith Due to Environment Variables: {e}")

        try:
            # Get LangSmith Tracer URL
            self.client = Client(
                api_url=self.LANGCHAIN_ENDPOINT,
                api_key=self.LANGCHAIN_API_KEY
            )
            self.tracer = LangChainTracer(
                project_name=self.LANGCHAIN_PROJECT,
                client=self.client
            )
            projects = list(self.client.list_projects(name=self.LANGCHAIN_PROJECT))
            project_id = projects[0].id
            print("✅ LangSmith Tracing Started:")
            print(f"   https://smith.langchain.com/projects/p/{project_id}")

        except Exception as e:
            print(f"⚠️ Could not Find project URL: {e}")


    @property
    def is_enabled(self) -> bool:
        """
        You Must Check this property before use LangSmith.
        """
        if not self.enabled:
            print("⚠️ LangSmith Logging is OFF.")
        return self.enabled
