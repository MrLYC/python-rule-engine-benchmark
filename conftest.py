import pytest


@pytest.fixture()
def shipping_fees_case1():
    request = {
        "cart": {"total": 800},
        "customer": {"country": "US", "tier": "gold"},
    }
    result = {"fees": {"flat": 25}}
    return request, result


@pytest.fixture()
def shipping_fees_case2():
    request = {
        "cart": {"total": 2000},
        "customer": {"country": "GB"},
    }
    result = {"fees": {"percentage": 15}}
    return request, result
