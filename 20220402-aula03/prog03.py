"""
Composição

Quando uma classe compõe ou é composta por outra. Composição é diferente de Herança

"""

from typing import List, NoReturn
from datetime import datetime


class Student:
    def __init__(self, name):
        self._name = name


class CourseClass:
    def __init__(self, name: str, initial_date: datetime, final_date: datetime, students: List[Student] = []):
        self._name = name
        self._initial_date = initial_date
        self._final_date = final_date
        self._students = students.copy()


class Course:
    def __init__(self, name: str, price: float, _class: List = [CourseClass]) -> NoReturn:
        self._name = name
        self._price = price
        self._class = _class
