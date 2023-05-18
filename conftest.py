import pytest


@pytest.fixture()
def case1():
    request = {
        "cart": {"total": 800},
        "customer": {"country": "US", "tier": "gold"},
    }
    result = {"fees": {"flat": 25}}
    return request, result


@pytest.fixture()
def case2():
    request = {
        "cart": {"total": 2000},
        "customer": {"country": "GB", "tier": "normal"},
    }
    result = {"fees": {"percentage": 15}}
    return request, result


@pytest.fixture()
def case3():
    request = {
        "cart": {"total": 1800},
        "customer": {"country": "US", "tier": "gold"},
    }
    result = {"fees": {"percentage": 2}}
    return request, result


@pytest.fixture()
def case4():
    request = {
        "cart": {"total": 1200},
        "customer": {"country": "US", "tier": "normal"},
    }
    result = {"fees": {"percentage": 3}}
    return request, result


@pytest.fixture()
def case5():
    request = {
        "cart": {"total": 1200},
        "customer": {"country": "MX", "tier": "normal"},
    }
    result = {"fees": {"percentage": 5}}
    return request, result


@pytest.fixture()
def case6():
    request = {
        "cart": {"total": 100},
        "customer": {"country": "CA", "tier": "normal"},
    }
    result = {"fees": {"flat": 50}}
    return request, result


@pytest.fixture()
def case7():
    request = {
        "cart": {"total": 2200},
        "customer": {"country": "DE", "tier": "normal"},
    }
    result = {"fees": {"percentage": 10}}
    return request, result


@pytest.fixture()
def case8():
    request = {
        "cart": {"total": 200},
        "customer": {"country": "IE", "tier": "normal"},
    }
    result = {"fees": {"flat": 100}}
    return request, result


@pytest.fixture()
def case9():
    request = {
        "cart": {"total": 200},
        "customer": {"country": "GB", "tier": "normal"},
    }
    result = {"fees": {"flat": 150}}
    return request, result
