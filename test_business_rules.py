from dataclasses import dataclass, field
from typing import Any, Dict, List

import pytest
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC
from business_rules.variables import (
    BaseVariables,
    numeric_rule_variable,
    string_rule_variable,
)
from pytest_lazyfixture import lazy_fixture


@dataclass
class ShippingFeeVars(BaseVariables):
    inputs: Any

    @numeric_rule_variable()
    def cart_total(self):
        return self.inputs["cart"]["total"]

    @string_rule_variable()
    def customer_country(self):
        return self.inputs["customer"]["country"]

    @string_rule_variable()
    def customer_tier(self):
        return self.inputs["customer"]["tier"]


@dataclass
class ShippingFeeActions(BaseActions):
    result: Dict[str, int] = field(default_factory=dict)

    @rule_action(params={"value": FIELD_NUMERIC})
    def set_fees_flat(self, value: int):
        self.result["fees"] = {"flat": value}

    @rule_action(params={"value": FIELD_NUMERIC})
    def set_fees_percentage(self, value: int):
        self.result["fees"] = {"percentage": value}


@dataclass
class ShippingFeeEngine:
    rules: List[Any]

    def evaluate(self, inputs: Any) -> Any:
        vars = ShippingFeeVars(inputs=inputs)
        actions = ShippingFeeActions()

        run_all(
            rule_list=self.rules,
            defined_variables=vars,
            defined_actions=actions,
            stop_on_first_trigger=True,
        )

        return actions.result


@pytest.fixture()
def shipping_fees_rules():
    return [
        {
            "conditions": {
                "all": [
                    {
                        "name": "cart_total",
                        "operator": "greater_than",
                        "value": 1000,
                    },
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "US",
                    },
                    {
                        "name": "customer_tier",
                        "operator": "equal_to",
                        "value": "gold",
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_percentage",
                    "params": {"value": 2},
                },
            ],
        },
        {
            "conditions": {
                "all": [
                    {
                        "name": "cart_total",
                        "operator": "greater_than",
                        "value": 1000,
                    },
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "US",
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_percentage",
                    "params": {"value": 3},
                },
            ],
        },
        {
            "conditions": {
                "all": [
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "US",
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_flat",
                    "params": {"value": 25},
                },
            ],
        },
        {
            "conditions": {
                "all": [
                    {
                        "name": "cart_total",
                        "operator": "greater_than",
                        "value": 1000,
                    },
                    {
                        "any": [
                            {
                                "name": "customer_country",
                                "operator": "equal_to",
                                "value": "CA",
                            },
                            {
                                "name": "customer_country",
                                "operator": "equal_to",
                                "value": "MX",
                            },
                        ]
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_percentage",
                    "params": {"value": 5},
                },
            ],
        },
        {
            "conditions": {
                "any": [
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "CA",
                    },
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "MX",
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_flat",
                    "params": {"value": 50},
                },
            ],
        },
        {
            "conditions": {
                "all": [
                    {
                        "name": "cart_total",
                        "operator": "greater_than",
                        "value": 1000,
                    },
                    {
                        "any": [
                            {
                                "name": "customer_country",
                                "operator": "equal_to",
                                "value": "IE",
                            },
                            {
                                "name": "customer_country",
                                "operator": "equal_to",
                                "value": "UK",
                            },
                            {
                                "name": "customer_country",
                                "operator": "equal_to",
                                "value": "FR",
                            },
                            {
                                "name": "customer_country",
                                "operator": "equal_to",
                                "value": "DE",
                            },
                        ]
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_percentage",
                    "params": {"value": 10},
                },
            ],
        },
        {
            "conditions": {
                "any": [
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "IE",
                    },
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "UK",
                    },
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "FR",
                    },
                    {
                        "name": "customer_country",
                        "operator": "equal_to",
                        "value": "DE",
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_flat",
                    "params": {"value": 100},
                },
            ],
        },
        {
            "conditions": {
                "all": [
                    {
                        "name": "cart_total",
                        "operator": "greater_than",
                        "value": 1000,
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_percentage",
                    "params": {"value": 15},
                },
            ],
        },
        {
            "conditions": {
                "all": [
                    {
                        "name": "cart_total",
                        "operator": "less_than_or_equal_to",
                        "value": 1000,
                    },
                ]
            },
            "actions": [
                {
                    "name": "set_fees_flat",
                    "params": {"value": 150},
                },
            ],
        },
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
def test_business_rules(benchmark, shipping_fees_rules, case):
    request, expected = case
    engine = ShippingFeeEngine(shipping_fees_rules)
    result = benchmark(engine.evaluate, request)
    assert result == expected
