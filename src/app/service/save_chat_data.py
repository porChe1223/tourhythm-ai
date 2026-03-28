import json
import uuid
from datetime import datetime
from typing import List, Any

from infra.database import ChatSession, ChatMessage, ChatRepository


def save_chat_data(messages: List[Any]):
    """
    Save chat data to database
    
    Args:
        user_message: The original user input
        messages: List of messages from TouristAgentGraph.execute()
    """
    # --- Format messages ---
    formatted_messages = []

    for order_index, message in enumerate(messages):
        message_type = type(message).__name__

        # Initialize variables
        content = ""
        assignee = None
        message_id = getattr(message, 'id', str(uuid.uuid4()))

        # Pick content and assignee
        if message_type in ['HumanMessage', 'AIMessage']:
            raw_content = getattr(message, 'content', '')
            try:
                parsed_content = json.loads(raw_content.strip())
                assignee = parsed_content.get('assignee')
                content = parsed_content.get('output', raw_content)
                    
            except json.JSONDecodeError:
                assignee = None
                content = raw_content
        else:
            content = str(message)
            assignee = None

        # Add processed message dict
        processed_message = {
            'id': message_id,
            'content': content,
            'assignee': assignee,
            'order_index': order_index
        }
        formatted_messages.append(processed_message)

    # --- Save to database ---
    try:
        chat_repo = ChatRepository()
        
        # Create new chat session
        session_id = uuid.uuid4()
        session = ChatSession(
            id=session_id,
            created_at=datetime.now()
        )
        
        saved_session = chat_repo.create_session(session)
        
        # Create ChatMessage objects
        chat_messages = []
        
        for msg_data in formatted_messages:
            chat_message = ChatMessage(
                id=msg_data['id'] if isinstance(msg_data['id'], str) else str(msg_data['id']),
                session_id=saved_session.id,
                message=msg_data['content'],
                assignee=msg_data['assignee'],
                order_index=msg_data['order_index'],
                score=None,
                created_at=datetime.now()
            )
            chat_messages.append(chat_message)
        
        # Save all messages in batch
        if chat_messages:
            chat_repo.add_messages(chat_messages)
        else:
            raise ValueError("No chat messages to save")
        
    except Exception as e:
        raise e
