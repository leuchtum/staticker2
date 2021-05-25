import pytest


def pytest_addoption(parser):
    """Set flag for CLI use
    """
    parser.addoption("--db-tests", action="store_true")


@pytest.fixture(scope='session')
def dbtests(request):
    doit = request.config.getoption("--db-tests")

    if doit is False:
        # Skip every tests with: test_xy(dbtests)
        pass# pytest.skip("Need --db-tests to run")
            
