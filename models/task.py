"""Esta clase modela los datos de una tarea"""
from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class Task:
    title: str
    description: str
    id: UUID = field(default_factory=uuid4)
