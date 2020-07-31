from locust import HttpUser, between, TaskSet, task

class MetricsTaskSet(TaskSet):
    @task(1)
    def login(self):
        self.client.post("/predict", {"age":"21", "sex":"male", "bmi":"18", "children":"0", "smoker":"no", "region":"southwest"})

class MyLoadTest(HttpUser):
  tasks = MetricsTaskSet
  wait_time = between(5, 15)