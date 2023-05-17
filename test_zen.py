import json

import pytest
import zen
from pytest_lazyfixture import lazy_fixture


@pytest.fixture()
def shipping_fees_json():
    return json.dumps(
        {
            "contentType": "application/vnd.gorules.decision",
            "edges": [
                {
                    "id": "04b0252c-9ba4-4c54-aaa2-ea062c974283",
                    "sourceId": "d0e72f75-15fd-4dec-bac4-63f9a68f5f2d",
                    "type": "edge",
                    "targetId": "c83952f3-c0ce-472a-9273-9dec7d6d3a45",
                },
                {
                    "id": "7bace0c3-c9d9-4d78-a0ad-0b353ac0e9af",
                    "sourceId": "c83952f3-c0ce-472a-9273-9dec7d6d3a45",
                    "type": "edge",
                    "targetId": "07468fa0-92c9-408a-a248-b1aa603d577f",
                },
            ],
            "nodes": [
                {
                    "id": "d0e72f75-15fd-4dec-bac4-63f9a68f5f2d",
                    "type": "inputNode",
                    "position": {"x": 200, "y": 200},
                    "name": "Request",
                },
                {
                    "id": "c83952f3-c0ce-472a-9273-9dec7d6d3a45",
                    "type": "decisionTableNode",
                    "position": {"x": 600, "y": 200},
                    "name": "Shipping Fees",
                    "content": {
                        "hitPolicy": "first",
                        "inputs": [
                            {
                                "field": "cart.total",
                                "id": "pMDaURmDrZ",
                                "name": "Cart Total",
                                "type": "expression",
                            },
                            {
                                "id": "D6SDwLBY-s",
                                "type": "expression",
                                "field": "customer.country",
                                "name": "Customer Country",
                            },
                            {
                                "id": "tjXrz6ncdr",
                                "type": "expression",
                                "field": "customer.tier",
                                "name": "Customer Tier",
                            },
                        ],
                        "outputs": [
                            {
                                "field": "fees.flat",
                                "id": "5XawM86q6b",
                                "name": "Fees Flat ($)",
                                "type": "expression",
                            },
                            {
                                "id": "HUa7FUD0u6",
                                "type": "expression",
                                "field": "fees.percentage",
                                "name": "Fees Percentage (%)",
                            },
                        ],
                        "rules": [
                            {
                                "_id": "mEUce2OilH",
                                "pMDaURmDrZ": ">1000",
                                "D6SDwLBY-s": '"US"',
                                "tjXrz6ncdr": '"gold"',
                                "5XawM86q6b": "",
                                "HUa7FUD0u6": "2",
                            },
                            {
                                "_id": "H43QXybz3O",
                                "pMDaURmDrZ": ">1000",
                                "D6SDwLBY-s": '"US"',
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "",
                                "HUa7FUD0u6": "3",
                            },
                            {
                                "_id": "jNp1Y5eBbz",
                                "pMDaURmDrZ": "",
                                "D6SDwLBY-s": '"US"',
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "25",
                                "HUa7FUD0u6": "",
                            },
                            {
                                "_id": "Wa8rfdr6Sv",
                                "pMDaURmDrZ": ">1000",
                                "D6SDwLBY-s": '"CA","MX"',
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "",
                                "HUa7FUD0u6": "5",
                            },
                            {
                                "_id": "eOUwesbLOT",
                                "pMDaURmDrZ": "",
                                "D6SDwLBY-s": '"CA","MX"',
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "50",
                                "HUa7FUD0u6": "",
                            },
                            {
                                "_id": "daeUTxVkvp",
                                "pMDaURmDrZ": ">1000",
                                "D6SDwLBY-s": '"IE","UK","FR","DE"',
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "",
                                "HUa7FUD0u6": "10",
                            },
                            {
                                "_id": "0WoWh9isak",
                                "pMDaURmDrZ": "",
                                "D6SDwLBY-s": '"IE","UK","FR","DE"',
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "100",
                                "HUa7FUD0u6": "",
                            },
                            {
                                "_id": "Rn-kepDJ6z",
                                "pMDaURmDrZ": ">1000",
                                "D6SDwLBY-s": "",
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "",
                                "HUa7FUD0u6": "15",
                            },
                            {
                                "_id": "Tt1N1jhKfo",
                                "pMDaURmDrZ": "",
                                "D6SDwLBY-s": "",
                                "tjXrz6ncdr": "",
                                "5XawM86q6b": "150",
                                "HUa7FUD0u6": "",
                            },
                        ],
                    },
                },
                {
                    "id": "07468fa0-92c9-408a-a248-b1aa603d577f",
                    "type": "outputNode",
                    "position": {"x": 1000, "y": 200},
                    "name": "Response",
                },
            ],
        }
    )


@pytest.mark.parametrize(
    "case",
    [
        lazy_fixture("shipping_fees_case1"),
        lazy_fixture("shipping_fees_case2"),
    ],
)
def test_zen_engine_for_shipping_fees(benchmark, shipping_fees_json, case):
    request, expected = case
    engine = zen.ZenEngine()

    decision = engine.create_decision(shipping_fees_json)
    result = benchmark(decision.evaluate, request)
    assert result["result"] == expected
