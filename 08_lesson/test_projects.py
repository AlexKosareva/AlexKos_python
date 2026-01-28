import pytest
import uuid

def test_create_project_positive(api, company_id):
    title = f"Test Project {uuid.uuid4()}"
    response = api.create_project(title, company_id)
    print(response.json()) # <--- Добавьте эту строку
    assert response.status_code == 201


def test_create_project_negative(api, company_id):
    # Пустое название проекта
    response = api.create_project("", company_id)
    assert response.status_code == 400

def test_get_project_positive(api, company_id):
    # Создаем проект, чтобы его получить
    title = "To be fetched"
    project_id = api.create_project(title, company_id).json()["id"]
    
    response = api.get_project(project_id)
    assert response.status_code == 200
    assert response.json()["title"] == title

def test_get_project_negative(api):
    # Несуществующий ID
    response = api.get_project(str(uuid.uuid4()))
    assert response.status_code == 404

def test_update_project_positive(api, company_id):
    project_id = api.create_project("Old Title", company_id).json()["id"]
    new_title = "Updated Title"
    
    response = api.update_project(project_id, new_title)
    assert response.status_code == 200
    
    # Проверяем через GET, что имя реально изменилось
    check = api.get_project(project_id).json()
    assert check["title"] == new_title

def test_update_project_negative(api):
    # Обновление без ID (или невалидный ID)
    response = api.update_project("invalid-id", "New Title")
    assert response.status_code in [400, 404]
