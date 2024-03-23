from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_comments(self):
        self.client.get("/comments")