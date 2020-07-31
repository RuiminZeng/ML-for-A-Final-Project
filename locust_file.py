from locust import HttpUser, between
import os

def my_task(self):
  self.client.post("/predict", {"age":"21", "sex":"male", "bmi":"18", "children":"0", "smoker":"no", "region":"southwest"})

class MyLoadTest(HttpUser):
  host = os.getenv("LOCUST_TARGET_HOST", "http://localhost:8080")
  tasks = [my_task]
  wait_time = between(5, 15)
