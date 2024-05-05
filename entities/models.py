from sqlalchemy import String, Column, Table, Integer, ForeignKey
from config.db import Base, engine, meta
from sqlalchemy.orm import relationship

student_course = Table('student_course', Base.metadata,
                       Column('student_id', Integer, ForeignKey('students.id')),
                       Column('course_id', Integer, ForeignKey('courses.id'))
                       )


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    lastname = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    tutor_id = Column(Integer, ForeignKey('tutors.id'))
    tutors = relationship("Tutor", back_populates="students")
    courses = relationship("Course", secondary=student_course, back_populates="students")


class Tutor(Base):
    __tablename__ = 'tutors'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    lastname = Column(String(100))
    age = Column(Integer)
    email = Column(String(100))
    students = relationship("Student", back_populates="tutors")


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    students = relationship("Student", secondary=student_course, back_populates="courses")


Base.metadata.create_all(engine)
