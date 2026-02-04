import os
import sys
import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Исправляем кодировку консоли для Windows
if sys.platform == "win32":
    os.environ['PGCLIENTENCODING'] = 'utf8'

# Используем проверенный пароль
DB_URL = "postgresql+psycopg://postgres:1234@localhost:5432/postgres"

Base = declarative_base()
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    """Создание таблиц перед началом тестов"""
    Base.metadata.create_all(engine)


@pytest.fixture
def db_session():
    """Фикстура для сессии БД с откатом изменений"""
    session = Session()
    yield session
    session.rollback()
    session.close()


def test_add_student(db_session):
    """Тест добавления"""
    new_id = 101
    db_session.query(Student).filter_by(id=new_id).delete()
    new_student = Student(id=new_id, name="Ivan")
    db_session.add(new_student)
    db_session.commit()
    student = db_session.query(Student).filter_by(id=new_id).first()
    assert student is not None
    assert student.name == "Ivan"
    db_session.delete(student)
    db_session.commit()


def test_update_student(db_session):
    """Тест изменения"""
    new_id = 102
    db_session.query(Student).filter_by(id=new_id).delete()
    student = Student(id=new_id, name="Old Name")
    db_session.add(student)
    db_session.commit()
    student.name = "New Name"
    db_session.commit()
    updated = db_session.query(Student).filter_by(id=new_id).first()
    assert updated.name == "New Name"
    db_session.delete(updated)
    db_session.commit()


def test_delete_student(db_session):
    """Тест удаления"""
    new_id = 103
    db_session.query(Student).filter_by(id=new_id).delete()
    student = Student(id=new_id, name="To Delete")
    db_session.add(student)
    db_session.commit()
    db_session.delete(student)
    db_session.commit()
    deleted = db_session.query(Student).filter_by(id=new_id).first()
    assert deleted is None
