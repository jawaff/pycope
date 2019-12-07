import prioritizers

def test_contains_key():
    checker = prioritizers.contains_key("key")
    assert checker({"key": "value"}) == 1
    assert checker({"key": "diffValue"}) == 1
    assert checker({"diffKey": "value"}) == 0
    assert checker({"diffKey": "diffValue"}) == 0

def test_contains_field():
    checker = prioritizers.contains_field("key", "value")
    assert checker({"key": "value"}) == 1
    assert checker({"diffKey": "value"}) == 0
    assert checker({"key": "diffValue"}) == 0
    assert checker({"diffKey": "diffValue"}) == 0
