from loguru import logger
from src.proj.func import func, cal_add, create_test_model
from src.proj.model import TestModel
from tests.fixtures import func_fixture, module_fixture, module_fixture_with_yield
use_fixtures = [func_fixture, module_fixture, module_fixture_with_yield]

def test_func():
    func()

def test_cal_add():
    assert cal_add(1, 2) == 3

def test_create_test_model():
    entity = create_test_model("John", 20)
    assert entity.name == "John"
    assert entity.age == 20
    assert entity.is_active == True

def test_func_fixture1(func_fixture):
    assert func_fixture == "func_fixture1"

def test_func_fixture2(func_fixture):
    logger.warning("Func fixture will be executed again")
    assert func_fixture == "func_fixture2"

def test_module_fixture1(module_fixture):
    assert module_fixture == "module_fixture1"

def test_module_fixture2(module_fixture):
    logger.warning("Module fixture will not be executed again")
    assert module_fixture == "module_fixture1"

def test_module_fixture_with_yield(module_fixture_with_yield):
    assert module_fixture_with_yield == "module_fixture_with_yield"
    logger.warning("you could do more things here , it will be executed after the test and")