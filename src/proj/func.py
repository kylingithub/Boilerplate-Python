from proj.model import TestModel
from proj.env import GLOBAL_VAR
from loguru import logger

def func():
    print(f"Hello, {GLOBAL_VAR}!")
    logger.info("Hello, info ")
    logger.warning("Hello, warning ")
    logger.error("Hello, error ")
    logger.critical("Hello, critical ")
    logger.debug("Hello, debug ")

def cal_add(a, b):
    logger.info(f"Adding {a} and {b}!")
    return a + b

def create_test_model(name: str, age: int):
    return TestModel(name=name, age=age, is_active=True)