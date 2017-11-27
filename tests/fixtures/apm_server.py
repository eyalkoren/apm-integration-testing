import pytest
import os


@pytest.fixture(scope="session")
def apm_server(elasticsearch):
    class APMServer:
        def __init__(self, url, elasticsearch):
            self.url = url
            self.elasticsearch = elasticsearch

    return APMServer(os.environ['APM_SERVER_URL'], elasticsearch)