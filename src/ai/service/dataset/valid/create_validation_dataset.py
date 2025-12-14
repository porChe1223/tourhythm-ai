import dspy

from ai.service.dataset.valid.schedule_validation_dataset import (
    SCHEDULE_VALIDATION_INPUT1,
    SCHEDULE_VALIDATION_OUTPUT1,
    SCHEDULE_VALIDATION_INPUT2,
    SCHEDULE_VALIDATION_OUTPUT2,
    SCHEDULE_VALIDATION_INPUT3,
    SCHEDULE_VALIDATION_OUTPUT3,
    SCHEDULE_VALIDATION_INPUT4,
    SCHEDULE_VALIDATION_OUTPUT4,
    SCHEDULE_VALIDATION_INPUT5,
    SCHEDULE_VALIDATION_OUTPUT5,
)
from ai.service.dataset.valid.task_validation_dataset import (
    TASK_VALIDATION_INPUT1,
    TASK_VALIDATION_OUTPUT1,
    TASK_VALIDATION_INPUT2,
    TASK_VALIDATION_OUTPUT2,
    TASK_VALIDATION_INPUT3,
    TASK_VALIDATION_OUTPUT3,
    TASK_VALIDATION_INPUT4,
    TASK_VALIDATION_OUTPUT4,
    TASK_VALIDATION_INPUT5,
    TASK_VALIDATION_OUTPUT5,
)
from ai.service.dataset.valid.trip_validation_dataset import (
    TRIP_VALIDATION_INPUT1,
    TRIP_VALIDATION_OUTPUT1,
    TRIP_VALIDATION_INPUT2,
    TRIP_VALIDATION_OUTPUT2,
    TRIP_VALIDATION_INPUT3,
    TRIP_VALIDATION_OUTPUT3,
    TRIP_VALIDATION_INPUT4,
    TRIP_VALIDATION_OUTPUT4,
    TRIP_VALIDATION_INPUT5,
    TRIP_VALIDATION_OUTPUT5,
)


def create_agent_valset(agent_type: str):
    if agent_type == "Trip":
        return create_trip_valset()
    elif agent_type == "Schedule":
        return create_schedule_valset()
    elif agent_type == "Task":
        return create_task_valset()
    else:
        raise ValueError(f"Unknown agent type: {agent_type}")
    

def create_trip_valset():
    return [
        dspy.Example(
            input=TRIP_VALIDATION_INPUT1,
            output=TRIP_VALIDATION_OUTPUT1
        ).with_inputs("input"),
        dspy.Example(
            input=TRIP_VALIDATION_INPUT2,
            output=TRIP_VALIDATION_OUTPUT2
        ).with_inputs("input"),
        dspy.Example(
            input=TRIP_VALIDATION_INPUT3,
            output=TRIP_VALIDATION_OUTPUT3
        ).with_inputs("input"),
        dspy.Example(
            input=TRIP_VALIDATION_INPUT4,
            output=TRIP_VALIDATION_OUTPUT4
        ).with_inputs("input"),
        dspy.Example(
            input=TRIP_VALIDATION_INPUT5,
            output=TRIP_VALIDATION_OUTPUT5
        ).with_inputs("input"),
    ]


def create_schedule_valset():
    return [
        dspy.Example(
            input=SCHEDULE_VALIDATION_INPUT1,
            output=SCHEDULE_VALIDATION_OUTPUT1
        ).with_inputs("input"),
        dspy.Example(
            input=SCHEDULE_VALIDATION_INPUT2,
            output=SCHEDULE_VALIDATION_OUTPUT2
        ).with_inputs("input"),
        dspy.Example(
            input=SCHEDULE_VALIDATION_INPUT3,
            output=SCHEDULE_VALIDATION_OUTPUT3
        ).with_inputs("input"),
        dspy.Example(
            input=SCHEDULE_VALIDATION_INPUT4,
            output=SCHEDULE_VALIDATION_OUTPUT4
        ).with_inputs("input"),
        dspy.Example(
            input=SCHEDULE_VALIDATION_INPUT5,
            output=SCHEDULE_VALIDATION_OUTPUT5
        ).with_inputs("input"),
    ]


def create_task_valset():
    return [
        dspy.Example(
            input=TASK_VALIDATION_INPUT1,
            output=TASK_VALIDATION_OUTPUT1
        ).with_inputs("input"),
        dspy.Example(
            input=TASK_VALIDATION_INPUT2,
            output=TASK_VALIDATION_OUTPUT2
        ).with_inputs("input"),
        dspy.Example(
            input=TASK_VALIDATION_INPUT3,
            output=TASK_VALIDATION_OUTPUT3
        ).with_inputs("input"),
        dspy.Example(
            input=TASK_VALIDATION_INPUT4,
            output=TASK_VALIDATION_OUTPUT4
        ).with_inputs("input"),
        dspy.Example(
            input=TASK_VALIDATION_INPUT5,
            output=TASK_VALIDATION_OUTPUT5
        ).with_inputs("input"),
    ]
