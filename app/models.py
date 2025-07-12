from typing import List
from datetime import date

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .db import Base


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    students: Mapped[List['Student']] = relationship(back_populates="group")

class Student(Base):
    __tablename__ = 'students'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]
    group_id: Mapped[int] = mapped_column(ForeignKey("groups.id"))
    group: Mapped['Group'] = relationship(back_populates="students")
    grades: Mapped[List['Grade']] = relationship(back_populates='student')
    
    
class Grade(Base):
    __tablename__ = 'grades'
    id: Mapped[int] = mapped_column(primary_key=True)
    grade: Mapped[int]
    date: Mapped[date] 
    student_id: Mapped[int] = mapped_column(ForeignKey('students.id'))
    subject_id: Mapped[int] = mapped_column(ForeignKey('subjects.id'))
    student: Mapped['Student'] = relationship(back_populates='grades')
    subject: Mapped['Subject'] = relationship(back_populates='grades')
    
    
class Subject(Base):
    __tablename__ = 'subjects'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] 
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id'))
    teacher: Mapped['Teacher'] = relationship(back_populates='subjects')
    grades: Mapped[List['Grade']] = relationship(back_populates='subject')
    
    
class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    subjects: Mapped[List['Subject']] = relationship(back_populates='teacher')
    
