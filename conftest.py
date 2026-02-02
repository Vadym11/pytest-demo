import pytest
from AOM.product import ProductAPI
from utils.api_handler import APIHandler

@pytest.fixture(scope='module')
def api_handler():
    api_handler = APIHandler()
    api_handler.authenticate()
    return api_handler

@pytest.fixture(scope='module')
def product_api(api_handler):
    product_api = ProductAPI(api_handler)
    return product_api