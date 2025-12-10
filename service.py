from models import Course, Enrollment
from datetime import datetime
from typing import List

class SchoolCMSService:
    def __init__(self):
        self.courses: List[Course] = []
        self.enrollments: List[Enrollment] = []
        self._course_counter = 1
        self._enroll_counter = 1

    def add_course(self, title: str, instructor: str, section: str) -> Course:
        new_course = Course(
            id=self._course_counter,
            title=title,
            instructor=instructor,
            section=section
        )
        self._course_counter += 1
        self.courses.append(new_course)
        return new_course

    def get_all_courses(self):
        return list(self.courses)

    def enroll_student(self, course_id: int, student_name: str, student_id: str) -> bool:
        course = next((c for c in self.courses if c.id == course_id), None)
        if not course:
            return False
        already = any(e.course_id == course_id and e.student_id == student_id for e in self.enrollments)
        if already:
            # duplicate
            return False
        enrolled = Enrollment(
            id=self._enroll_counter,
            course_id=course_id,
            student_name=student_name,
            student_id=student_id,
            enrolled_date=datetime.now().strftime("%Y-%m-%d")
        )
        self._enroll_counter += 1
        self.enrollments.append(enrolled)
        return True

    def get_enrollments_by_course(self, course_id: int):
        return [e for e in self.enrollments if e.course_id == course_id]

    def delete_course(self, course_id: int) -> bool:
        initial_len = len(self.courses)
        self.courses = [c for c in self.courses if c.id != course_id]
        self.enrollments = [e for e in self.enrollments if e.course_id != course_id]
        return len(self.courses) < initial_len
