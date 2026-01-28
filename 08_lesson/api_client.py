import requests

class ProjectPage:
    def __init__(self, url, token):
        self.url = f"{url}/api-v2/projects"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, company_id=None): # добавили =None для совместимости
        body = {"title": title} # Оставляем только title
        return requests.post(self.url, json=body, headers=self.headers)

    def get_project(self, project_id):
        return requests.get(f"{self.url}/{project_id}", headers=self.headers)

    def update_project(self, project_id, new_title):
        body = {"title": new_title}
        return requests.put(f"{self.url}/{project_id}", json=body, headers=self.headers)
