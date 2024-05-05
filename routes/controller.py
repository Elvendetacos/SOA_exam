from fastapi import APIRouter, Depends
from entities.models import Student, Tutor, Course
from sqlalchemy.orm import Session
from config.db import SessionLocal
from schemas.request.tutor_request import TutorRequest
from schemas.request.student_request import StudentRequest
from schemas.request.course_request import CourseRequest

controller = APIRouter()

base_url = "/api/v1/"


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@controller.get(base_url + "students")
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students


@controller.post(base_url + "students/create")
def create_student(student: StudentRequest, db: Session = Depends(get_db)):
    student_db = Student(name=student.name, lastname=student.lastname, age=student.age, email=student.email, tutor_id=student.tutor_id)
    if student.courses is not None:
        for id in student.courses:
            course = db.query(Course).filter(Course.id == id).first()
            if course is not None:
                student_db.courses.append(course)
    db.add(student_db)
    db.commit()
    db.refresh(student_db)
    return student_db


@controller.get(base_url + "tutors")
def get_tutors(db: Session = Depends(get_db)):
    tutors = db.query(Tutor).all()
    return tutors


@controller.get(base_url + "tutors/{tutor_id}/students")
def get_tutor_students(tutor_id: int, db: Session = Depends(get_db)):
    students = db.query(Student).filter(Student.tutor_id == tutor_id).all()
    return students


@controller.post(base_url + "tutors/create")
def create_tutor(tutor: TutorRequest, db: Session = Depends(get_db)):
    tutor = Tutor(name=tutor.name, lastname=tutor.lastname, age=tutor.age, email=tutor.email)
    db.add(tutor)
    db.commit()
    db.refresh(tutor)
    return tutor


@controller.get(base_url + "courses")
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return courses


@controller.post(base_url + "courses/create")
def create_course(course: CourseRequest, db: Session = Depends(get_db)):
    course = Course(name=course.name)
    db.add(course)
    db.commit()
    db.refresh(course)
    return course


@controller.get(base_url + "students/{student_id}/courses")
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        return {"error": "Student not found"}
    return [course.name for course in student.courses]


@controller.put(base_url + "students/{student_id}/assign_tutor/{tutor_id}")
def assign_tutor_to_student(student_id: int, tutor_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        return {"error": "Student not found"}
    tutor = db.query(Tutor).filter(Tutor.id == tutor_id).first()
    if tutor is None:
        return {"error": "Tutor not found"}
    student.tutor_id = tutor.id
    db.commit()
    return {"message": "Tutor assigned to student successfully"}


@controller.put(base_url + "students/{student_id}/assign_course/{course_id}")
def assign_course_to_student(student_id: int, course_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        return {"error": "Student not found"}
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        return {"error": "Course not found"}
    student.courses.append(course)
    db.commit()
    return {"message": "Course assigned to student successfully"}
