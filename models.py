import time
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Course:
    id: int
    title: str
    instructor: str
    section: str
    capacity: int = 30

@dataclass
class Enrollment:
    id: int
    course_id: int
    student_name: str
    student_id: str
    enrolled_date: str
