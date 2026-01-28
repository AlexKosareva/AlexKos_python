import pytest
from api_client import ProjectPage

@pytest.fixture
def api():
    # ДАННЫЕ ДЛЯ НАСТАВНИКА:
    token = "ВАШ_ТОКЕН"
    base_url = "https://ru.yougile.com"
    return ProjectPage(base_url, token)

@pytest.fixture
def company_id():
    # ДАННЫЕ ДЛЯ НАСТАВНИКА:
    return "ВАШ_COMPANY_ID" 
