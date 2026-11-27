"""Se encarga de gestionar el almacenamiento de los datos en memoria."""

from models.task import Task


class TaskRepository:
    # Simula mi base de datos
    _tasks: list[Task] = [
        Task("Estudiar POO", "Repasar clases y objetos"),
        Task("Practicar Tkinter", "Crear una interfaz con Treeview"),
    ]

    def find_all(self) -> list[Task]:
        """Retorna todas las tareas registradas."""
        return self._tasks

    def create_one(self, task: Task):
        self._tasks.append(task)
