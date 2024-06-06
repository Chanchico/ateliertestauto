# EXERCICE 7

from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(5, 9)
    host = "http://127.0.0.1:5000"

    @task
    def access_website(self):
        self.client.get("/books")