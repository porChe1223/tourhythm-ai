import os
import dspy
from typing import Optional, Dict, Any
from dspy.teleprompt import MIPROv2

from ai.agent.schedule.schedule_agent import DeclarativeScheduleAgent
from ai.agent.task.task_agent import DeclarativeTaskAgent
from ai.agent.trip.trip_agent import DeclarativeTripAgent
from ai.node.states import GraphState
from ai.service import get_message_pairs_by_assignee, create_agent_valset
from ai.agent._shared import dspy_openai
from ai.node.optimize.metric import metric


class OptimizeNode:
    """
    Optimization Node
    -----------------
    Optimize agents using MIPROv2 based on messages from database and validation data.
    """
    def __init__(self, output_dir: str = "optimized_models"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
    

    def prepare_training_data(self, agent_type: str):
        print(f"\n[TrainSet準備] {agent_type}Agent...")
        
        message_pairs = get_message_pairs_by_assignee(agent_type)
        print(f"  - Number of message pairs retrieved: {len(message_pairs)}")
        
        # Log detailed message pair information
        for i, (human_msg, agent_msg) in enumerate(message_pairs, 1):
            print(f"\n  Pair {i}:")
            print(f"    [Human Input]")
            print(f"      - ID: {human_msg.id}")
            print(f"      - Assignee: {human_msg.assignee}")
            print(f"      - Message: {human_msg.message[:100]}..." if len(human_msg.message) > 100 else f"      - Message: {human_msg.message}")
            print(f"    [Agent Response]")
            print(f"      - ID: {agent_msg.id}")
            print(f"      - Assignee: {agent_msg.assignee}")
            print(f"      - Message: {agent_msg.message[:100]}..." if len(agent_msg.message) > 100 else f"      - Message: {agent_msg.message}")
            print(f"      - Score: {agent_msg.score}")
        
        # Make Datasets with proper input-output pairs
        train_examples = []
        for human_msg, agent_msg in message_pairs:
            if human_msg.message and agent_msg.message and \
               len(human_msg.message.strip()) > 0 and len(agent_msg.message.strip()) > 0:
                example = dspy.Example(
                    input=human_msg.message,
                    output=agent_msg.message
                ).with_inputs("input")
                train_examples.append(example)
        
        print(f"\n  - TrainSet: {len(train_examples)}件（有効なペアのみ）")
        return train_examples
    

    def optimize_agent(
        self,
        agent_type: str,
        agent_instance: Any,
        num_threads: int = 4,
        verbose: bool = True, # Log optimization process
    ) -> Optional[Any]:
        print(f"\n{'=' * 60}")
        print(f"Optimization started for {agent_type}Agent")
        print('=' * 60)
        
        # Train Data
        trainset = self.prepare_training_data(agent_type)

        # Validation Data
        valset = create_agent_valset(agent_type)
        
        # Configure Language Model
        lm = dspy_openai()
        dspy.configure(lm=lm)
        
        # MIPROv2 Optimizer
        print(f"\n[MIPROv2 Settings]")
        print(f"  - Number of parallel threads: {num_threads}")
        
        optimizer = MIPROv2(
            metric=metric,
            prompt_model=lm,
            task_model=lm,
            init_temperature=1.0,
            num_threads=num_threads,
            verbose=verbose
        )
        
        # Optimize
        print(f"\n[Optimization in progress...]")
        print(f"  This process may take approximately 15-30 minutes.")
        
        try:
            optimized_agent = optimizer.compile(
                student=agent_instance,
                trainset=trainset,
                valset=valset
            )
            
            # 5. 保存
            output_path = os.path.join(
                self.output_dir,
                f"{agent_type.lower()}_agent_miprov2.json"
            )
            optimized_agent.save(output_path)
            
            print(f"\n✅ 最適化完了!")
            print(f"  - 保存先: {output_path}")
            
            return optimized_agent
            
        except Exception as e:
            print(f"\n❌ 最適化エラー: {e}")
            import traceback
            traceback.print_exc()
            return None
    

    def process(self, state: GraphState, agent_type: str) -> Dict[str, Optional[Any]]:
        """Process optimization for Trip agent only. State parameter required by LangGraph."""
        print("\n" + "=" * 60)
        print(f"MIPROv2による {agent_type}Agent 最適化")

        print("=" * 60)
        
        if agent_type == 'Schedule':
            agent_instance = DeclarativeScheduleAgent()
        elif agent_type == 'Task':
            agent_instance = DeclarativeTaskAgent()
        elif agent_type == 'Trip':
            agent_instance = DeclarativeTripAgent()
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        result = self.optimize_agent(agent_type, agent_instance)
        
        # Summary
        print("\n" + "=" * 60)
        print("最適化完了")
        print("=" * 60)
        
        if result is not None:
            print(f"\n✅ {agent_type}Agent: 成功")

        else:
            print(f"\n❌ {agent_type}Agent: 失敗")

        return {"status": "success" if result is not None else "failed"}
