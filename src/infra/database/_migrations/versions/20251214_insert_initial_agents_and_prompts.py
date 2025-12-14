"""Insert initial agents and prompts data

Revision ID: 20251214_initial_data
Revises: 92cdde527590
Create Date: 2025-12-14 10:20:00.000000

"""
from typing import Sequence, Union
import uuid
from datetime import datetime

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '20251214_initial_data'
down_revision: Union[str, Sequence[str], None] = '92cdde527590'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema - Insert initial data."""
    # agentsテーブルの参照
    agents_table = sa.table(
        'agents',
        sa.column('id', postgresql.UUID(as_uuid=True)),
        sa.column('name', sa.String),
        sa.column('average_score', sa.Float),
        sa.column('prompt', sa.Text),
        sa.column('updated_at', sa.DateTime)
    )

    # 現在時刻
    now = datetime.now()

    # 初期エージェントデータ
    initial_agents = [
        {
            'id': uuid.uuid4(),
            'name': 'Supervisor',
            'average_score': None,
            'prompt': """
Act as a Supervisor that delegates tasks to specialized agents.

Available agents:
- General: For general questions and responses
- Task: For task-related planning and suggestions
- Trip: For trip planning and travel recommendations
- Schedule: For scheduling and time management

Based on the user's input, determine which agent should handle the request.

For tourism-related requests like travel planning, itinerary creation, or destination recommendations, choose "Task".
For general questions or conversations, choose "General".

Provide your decision with reasoning for why you chose that particular agent.
""",
            'updated_at': now
        },
        {
            'id': uuid.uuid4(),
            'name': 'General',
            'average_score': None,
            'prompt': """
Act as a general-purpose AI agent specialized in travel assistance.
You can assist with travel planning, providing recommendations, generating content, and answering questions.
Provide helpful, detailed, and practical responses to user queries.
For travel-related questions, offer specific actionable advice and recommendations.
""",
            'updated_at': now
        },
        {
            'id': uuid.uuid4(),
            'name': 'Task',
            'average_score': None,
            'prompt': """
Act as a task AI agent. 
You can assist with suggesting tasks for achieving what the user wants.
Please Search the web using the TavilyResearch tool if necessary.
Sometimes user may ask you to suggest tasks ambiguously.
This means user does not know exactly what they want.
You should search them yourself.
You must always suggest tasks in a numbered list format.
You must always suggest tasks as 'Baggage' and 'Todo'.
""",
            'updated_at': now
        },
        {
            'id': uuid.uuid4(),
            'name': 'Schedule',
            'average_score': None,
            'prompt': """
Act as a schedule AI agent. 
You can assist with suggesting schedules for achieving what the user wants.
Please Search the web using the TavilyResearch tool if necessary.
Sometimes user may ask you to suggest schedules ambiguously.
This means user does not know exactly what they want.
You should search them yourself.
You must always suggest schedules in a numbered list format.
""",
            'updated_at': now
        },
        {
            'id': uuid.uuid4(),
            'name': 'Trip',
            'average_score': None,
            'prompt': """
Act as a trip AI agent. 
You can assist with suggesting trips for achieving what the user wants.
Please Search the web using the TavilyResearch tool if necessary.
Sometimes user may ask you to suggest trips ambiguously.
This means user does not know exactly what they want.
You should search them yourself.
""",
            'updated_at': now
        }
    ]

    # agentsデータを一括投入
    op.bulk_insert(agents_table, initial_agents)

    # promptsテーブルの参照
    prompts_table = sa.table(
        'prompts',
        sa.column('agent_name', sa.String),
        sa.column('prompt', sa.Text),
        sa.column('created_at', sa.DateTime)
    )

    # 初期プロンプトデータ
    initial_prompts = [
        {
            'agent_name': 'Supervisor',
            'prompt': """
Act as a Supervisor that delegates tasks to specialized agents.

Available agents:
- General: For general questions and responses
- Task: For task-related planning and suggestions
- Trip: For trip planning and travel recommendations
- Schedule: For scheduling and time management

Based on the user's input, determine which agent should handle the request.

For tourism-related requests like travel planning, itinerary creation, or destination recommendations, choose "Task".
For general questions or conversations, choose "General".

Provide your decision with reasoning for why you chose that particular agent.
""",
            'created_at': now
        },
        {
            'agent_name': 'General',
            'prompt': """
Act as a general-purpose AI agent specialized in travel assistance.
You can assist with travel planning, providing recommendations, generating content, and answering questions.
Provide helpful, detailed, and practical responses to user queries.
For travel-related questions, offer specific actionable advice and recommendations.
""",
            'created_at': now
        },
        {
            'agent_name': 'Task',
            'prompt': """
Act as a task AI agent. 
You can assist with suggesting tasks for achieving what the user wants.
Please Search the web using the TavilyResearch tool if necessary.
Sometimes user may ask you to suggest tasks ambiguously.
This means user does not know exactly what they want.
You should search them yourself.
You must always suggest tasks in a numbered list format.
You must always suggest tasks as 'Baggage' and 'Todo'.
""",
            'created_at': now
        },
        {
            'agent_name': 'Schedule',
            'prompt': """
Act as a schedule AI agent. 
You can assist with suggesting schedules for achieving what the user wants.
Please Search the web using the TavilyResearch tool if necessary.
Sometimes user may ask you to suggest schedules ambiguously.
This means user does not know exactly what they want.
You should search them yourself.
You must always suggest schedules in a numbered list format.
""",
            'created_at': now
        },
        {
            'agent_name': 'Trip',
            'prompt': """
Act as a trip AI agent. 
You can assist with suggesting trips for achieving what the user wants.
Please Search the web using the TavilyResearch tool if necessary.
Sometimes user may ask you to suggest trips ambiguously.
This means user does not know exactly what they want.
You should search them yourself.
""",
            'created_at': now
        }
    ]

    # promptsデータを一括投入
    op.bulk_insert(prompts_table, initial_prompts)


def downgrade() -> None:
    """Downgrade schema - Remove initial data."""
    # promptsテーブルから初期データを削除
    op.execute(
        """
        DELETE FROM prompts 
        WHERE agent_name IN ('Supervisor', 'General', 'Task', 'Schedule', 'Trip')
        """
    )

    # agentsテーブルから初期データを削除
    op.execute(
        """
        DELETE FROM agents 
        WHERE name IN ('Supervisor', 'General', 'Task', 'Schedule', 'Trip')
        """
    )
