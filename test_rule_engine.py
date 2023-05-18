from dataclasses import dataclass, field
from typing import Any, List, Tuple

import pytest
from pytest_lazyfixture import lazy_fixture
from rule_engine import Rule


@dataclass
class SimpleEngine:
    rows: List[Tuple[Rule, Any]] = field(default_factory=list)

    def add_row(self, rule: str, output: Any):
        self.rows.append((Rule(rule), output))

    def evaluate(self, request: Any) -> Any:
        for rule, output in self.rows:
            if rule.matches(request):
                return output


@pytest.fixture()
def shipping_fees_rules():
    return [
        (
            (
                "cart.total>1000"
                " and customer.country=='US'"
                " and customer.tier=='gold'"
            ),
            {"fees": {"percentage": 2}},
        ),
        (
            "cart.total>1000 and customer.country=='US'",
            {"fees": {"percentage": 3}},
        ),
        (
            "customer.country=='US'",
            {"fees": {"flat": 25}},
        ),
        (
            "cart.total>1000 and customer.country in ['CA', 'MX']",
            {"fees": {"percentage": 5}},
        ),
        (
            "customer.country in ['CA', 'MX']",
            {"fees": {"flat": 50}},
        ),
        (
            "cart.total>1000 and customer.country in ['IE', 'UK', 'FR', 'DE']",
            {"fees": {"percentage": 10}},
        ),
        (
            "customer.country in ['IE', 'UK', 'FR', 'DE']",
            {"fees": {"flat": 100}},
        ),
        (
            "cart.total>1000",
            {"fees": {"percentage": 15}},
        ),
        (
            "cart.total<=1000",
            {"fees": {"flat": 150}},
        ),
    ]


@pytest.mark.parametrize(
    "case",
    [
        lazy_fixture("case1"),
        lazy_fixture("case2"),
        lazy_fixture("case3"),
        lazy_fixture("case4"),
        lazy_fixture("case5"),
        lazy_fixture("case6"),
        lazy_fixture("case7"),
        lazy_fixture("case8"),
        lazy_fixture("case9"),
    ],
)
def test_rule_engine(benchmark, shipping_fees_rules, case):
    engine = SimpleEngine()
    for rule, output in shipping_fees_rules:
        engine.add_row(rule, output)

    request, expected = case
    result = benchmark(engine.evaluate, request)
    assert result == expected
