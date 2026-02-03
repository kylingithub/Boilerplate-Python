from loguru import logger
import pytest
counter = 0
counter_module = 0
@pytest.fixture(scope="function")
def func_fixture():
    logger.info("func_fixture")
    
    global counter
    counter += 1
    return f"func_fixture{counter}"

@pytest.fixture(scope="module")
def module_fixture():
    logger.info("module_fixture")
    global counter_module
    counter_module += 1
    return f"module_fixture{counter_module}"

@pytest.fixture
def module_fixture_with_yield():
    logger.info("module_fixture_with_yield begin")
    yield "module_fixture_with_yield"
    logger.info("teardown module_fixture_with_yield")
    