.PHONY: test test-agent test-node test-graph test-optimize test-all

# --- Agent Tests ---
test-agent:
	PYTHONPATH=src uv run test/ai/agent/test_general_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_declarative_general_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_schedule_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_declarative_schedule_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_task_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_declarative_task_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_trip_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_declarative_trip_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_supervisor_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_evaluation_agent.py
	PYTHONPATH=src uv run test/ai/agent/test_declarative_evaluation_agent.py

# --- Node Tests ---
test-node:
	PYTHONPATH=src uv run test/ai/node/test_general_node.py
	PYTHONPATH=src uv run test/ai/node/test_declarative_general_node.py
	PYTHONPATH=src uv run test/ai/node/test_schedule_node.py
	PYTHONPATH=src uv run test/ai/node/test_declarative_schedule_node.py
	PYTHONPATH=src uv run test/ai/node/test_task_node.py
	PYTHONPATH=src uv run test/ai/node/test_declarative_task_node.py
	PYTHONPATH=src uv run test/ai/node/test_trip_node.py
	PYTHONPATH=src uv run test/ai/node/test_declarative_trip_node.py
	PYTHONPATH=src uv run test/ai/node/test_optimize_node.py
	PYTHONPATH=src uv run test/ai/node/test_supervisor_node.py
	PYTHONPATH=src uv run test/ai/node/test_evaluate_node.py

# --- Graph Tests ---
test-graph:
	PYTHONPATH=src uv run test/ai/graph/test_tourist_agent_graph.py

# --- Optimization Tests ---
# takes about 15 minutes
# need to run docker compose up
test-optimize:
	PYTHONPATH=src uv run test/ai/graph/test_self_improve_graph.py
