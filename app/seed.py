import faker
import random
from app.models import Student, Subject, Grade, Teacher, Group
from app.db import session

fake = faker.Faker()

groups = ['A', 'B', 'C']
teachers = [fake.name() for _ in range(4)]
subjects = ["Math", "Physics", "History", "Foreign language", "Literature"]

def fill_groups():
    for i in groups:
        group = Group(name=i)
        session.add(group)
    session.commit()
    
def fill_teachers():
    for _ in range(4):
        session.add(Teacher(name=fake.name()))
    session.commit()
    
def fill_subjects():
    for i in subjects:
        session.add(Subject(name=i, teacher_id=random.randint(1,4)))
    session.commit()
    
def fill_students():
    for _ in range(40):
        session.add(Student(name=fake.name(), age=random.randint(17,30), group_id=random.randint(1,3)))
    session.commit()
        
def fill_grades():
    for i in range(1,40):
            for _ in range(random.randint(10,20)):
                session.add(Grade(student_id=i, subject_id=random.randint(1,5), grade=random.randint(1,20), date=fake.date_this_year()))
    session.commit()
    
if __name__ == "__main__":
    fill_groups()
    fill_teachers()
    fill_subjects()
    fill_students()
    fill_grades()


    


