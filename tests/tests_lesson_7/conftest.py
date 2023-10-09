import pytest


def pytest_addoption(parser):
    """PyTest's method for adding custom parameters."""

    parser.addoption("--dog_endpoint",
                     action="store",
                     type=str,
                     required=True,
                     help="Set dog api endpoint")

    parser.addoption("--brewery_endpoint",
                     action="store",
                     type=str,
                     required=True,
                     help="Set brewery api endpoint")

    parser.addoption("--json_placeholder_endpoint",
                     action="store",
                     type=str,
                     required=True,
                     help="Set json placeholder api endpoint")

    parser.addoption("--url",
                     action="store",
                     default="https://ya.ru",
                     type=str,
                     help="Set url")

@pytest.fixture(scope="session")
def dog_endpoint(request):
    """Handler for --dog_endpoint parameter."""

    return request.config.getoption("--dog_endpoint")


@pytest.fixture(scope="session")
def brewery_endpoint(request):
    """Handler for --brewery_endpoint parameter."""

    return request.config.getoption("--brewery_endpoint")


@pytest.fixture(scope="session")
def json_placeholder_endpoint(request):
    """Handler for --json_placeholder_endpoint parameter."""

    return request.config.getoption("--json_placeholder_endpoint")


@pytest.fixture(scope="session")
def url(request):
    """Handler for --yandex_endpoint parameter."""

    return request.config.getoption("--url")
