from locust import User, task, between

from locust import events
from locust.runners import MasterRunner

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if isinstance(environment.runner, MasterRunner):
        print("I'm on master node")
    else:
        print("I'm on a worker or standalone node")

class MyUser(User):
    @task
    def my_task(self):
        print("executing my_task")
        return True

    wait_time = between(0.5, 1)
