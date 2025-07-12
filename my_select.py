from app.models import *
from app.db import session
from sqlalchemy import desc, func, select

def select_1():
    result = session.query(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    print(result)

def select_2():
    result = session.execute(select(Student.name.label("sname"), func.avg(Grade.grade).label("avg_grade")).join(Grade.student).join(Grade.subject).where(Subject.name=='Math').group_by(Student.id).order_by(func.avg(Grade.grade).desc()).limit(1))    
    name, grade = result.first()
    print(name, grade)

def select_3():
    result = session.execute(select(func.avg(Grade.grade).label('avg_grade'), Group.name).join(Grade.student).join(Student.group).join(Grade.subject).where(Subject.name=='Math').group_by(Group.id, Subject.id))
    
    for avg_grade, group_name in result.all():
        print(group_name, round(avg_grade, 2))

def select_4():
    result = session.execute(select(func.avg(Grade.grade))).scalar_one()
    print(result)

def select_5():
    result = session.execute(select(Subject.name).join(Subject.teacher).where(Teacher.name=='Kenneth Barron'))
    print(result.scalars().all())

def select_6():
    result = session.execute(select(Student.name).where(Student.group_id==1)).all()
    print(result)
    

def select_7():
    result = session.execute(select(Group.name, Student.name, Grade.grade).join(Grade.student).join(Student.group).join(Grade.subject).where(Group.name=='A', Subject.name=='Math'))
    for group_name, student_name, grade in result.all():
        print(group_name, student_name, grade)
        
def select_8():
    result = session.execute(select(func.avg(Grade.grade)).join(Grade.subject).join(Subject.teacher).where(Teacher.name =='Kenneth Barron'))
    print(result.scalar_one())
    
def select_9():
    result = session.execute(select(Subject.name).join(Subject.grades).join(Grade.student).where(Student.name=='Michael Mccullough').distinct())
    print(result.scalars().all())

def select_10():
    result = session.execute(select(Subject.name).join(Grade.student).join(Grade.subject).join(Subject.teacher).where(Student.name == 'Michael Mccullough', Teacher.name == 'Lori Hill').distinct())
    print(result.scalars().all())

if __name__ == '__main__':
    select_2()