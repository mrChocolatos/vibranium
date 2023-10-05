import time
import pytest


def pytest_addoption(parser):
    """PyTest's method for adding custom parameters."""

    parser.addoption("--dog_endpoint",
                     action="store",
                     type=str,
                     required=True,
                     help="Set dog api endpoint")


@pytest.fixture(scope="session")
def dog_endpoint(request):
    """Handler for --dog_endpoint parameter."""

    return request.config.getoption("--dog_endpoint")
