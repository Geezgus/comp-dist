from locust import HttpUser, TaskSet, task, between


class UserTasks(TaskSet):
    @task
    def img_large(self):
        self.client.get("/large-image")

    @task
    def img_medium(self):
        self.client.get("/medium-image")

    @task
    def txt_large(self):
        self.client.get("/large-text")


class WebsiteUser(HttpUser):
    tasks = [UserTasks]
    wait_time = between(1, 5)
