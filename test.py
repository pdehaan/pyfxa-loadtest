from fxa.core import Client
from fxa.errors import ClientError
from fxa.tests.utils import TestEmailAccount

# VIA https://wiki.mozilla.org/TestEngineering/Services/FxATestEnvironments
# api_server = "https://api.accounts.firefox.com"
api_server = "https://api-accounts.stage.mozaws.net/"

client = Client(api_server)

default_password = "MySecretPassword"


# NEW USER
try:
    # https://pypi.org/project/PyFxA/#testing-email-addresses
    acct = TestEmailAccount()
    client.create_account(acct.email, default_password)
    print("SUCCESS")
except ClientError as err:
    print("UH OH")
    print(err.details)


# LOGIN
try:
    acct = TestEmailAccount()
    client.create_account(acct.email, default_password)
    session = client.login(acct.email, default_password)
    print("SUCCESS")
except ClientError as err:
    print("UH OH")
    print(err.details)


# VERIFY ACCT
