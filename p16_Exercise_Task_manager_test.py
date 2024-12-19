"""Správa úkolů (OOP)
Vytvořte třídu Task s atributy description (popis úkolu) a completed (boolean určující, zda je úkol dokončen).
Vytvořte třídu TaskManager, která umožňuje přidávat úkoly, označovat úkoly jako dokončené
a vracet seznam dokončených a nedokončených úkolů.
"""
import pytest
from p16_Exercise_task_manager import Task, TaskManager


def test_task_creation():
    task = Task("Complete assignment")
    assert task.description == "Complete assignment"
    assert task.completed is False


def test_task_manager():
    manager = TaskManager()
    task1 = Task("Complete assignment")
    task2 = Task("Read book")
    manager.add_task(task1)
    manager.add_task(task2)

    assert len(manager.tasks) == 2
    assert manager.get_completed_tasks() == []
    assert manager.get_incomplete_tasks() == [task1, task2]

    task1.mark_completed()
    assert manager.get_completed_tasks() == [task1]
    assert manager.get_incomplete_tasks() == [task2]


def test_task_exception():
    with pytest.raises(TypeError):
        Task("Task1", "False")


if __name__ == "__main__":
    pytest.main()
