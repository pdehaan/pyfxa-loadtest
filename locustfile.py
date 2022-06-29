import logging

from fxa.core import Client
from fxa.errors import ClientError
from fxa.tests.utils import TestEmailAccount

from locust import User, task, TaskSet, between, events

# client = Client(api_server)

# class FxAUser(User):
#     """
#     docstring
#     """

#     abstract = True

#     def __init__(self, environment):
#         super().__init__(environment)
#         print("Creating FxAUser...")
#         self.client = Client(self.api_server)

class FxATaskSet(TaskSet):
    api_server = "https://api-accounts.stage.mozaws.net/"
    default_fxa_password = "MySecretPassword"
    client = Client(api_server)

    wait_time = between(1, 2)

    def on_start(self):
        logging.info("starting task...")
        self.acct = TestEmailAccount()
        self.fxa_password = default_fxa_password
    
    def on_stop(self):
        logging.info("stopping test...")
        self.acct.clear()
        client.destroy_account(self.acct.email, self.fxa_password)

    @task
    def create_account(self):
        client.create_account(self.acct.email, self.fxa_password)
        logging.info("create_account: ") # + self.acct.email)

    @task
    def verify_account(self):
        logging.info("verify_account ") # + self.acct.email)

    @task
    def thing(self):
        # logging.info("thing")
        client.create_account(self.acct.email, default_fxa_password)
        client.login(self.acct.email, default_fxa_password)
        

class LoadUser(User):
    tasks = [FxATaskSet]
    host = ""



@events.quitting.add_listener
def _(environment, **kw):
    # if environment.stats.total.fail_ratio > 0.01:
    #     logging.error("Test failed due to failure ratio > 1%")
    #     environment.process_exit_code = 1
    # elif environment.stats.total.avg_response_time > 200:
    #     logging.error("Test failed due to average response time ratio > 200 ms")
    #     environment.process_exit_code = 1
    # elif environment.stats.total.get_response_time_percentile(0.95) > 800:
    #     logging.error("Test failed due to 95th percentile response time > 800 ms")
    #     environment.process_exit_code = 1
    # else:
        logging.info("[HANDLE THE CSV LOGS HERE?]")
        environment.process_exit_code = 0
