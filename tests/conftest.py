import pytest
from utils.config_loader import load_config
from utils.data_loader import load_test_data

@pytest.fixture(scope="session", autouse=True)
def config():
    return load_config()

@pytest.fixture(scope="session")
def test_data():
    return load_test_data()
