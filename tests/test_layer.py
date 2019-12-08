# Copyright 2019 Jake Waffle. Subject to the Apache2 license.

import layer
import context

def test_layer_init():
    assert layer.Layer(context.Context(), {"name":"value"}, ["otherName"])
    
def test_layer_with():
    ctx = context.Context()
    cur_fields = ctx.peek_layer()
    assert len(cur_fields) == 0
    with layer.Layer(ctx , {"name1": "value1", "name2": "value2"}, []) as layer1:
        cur_fields = ctx.peek_layer()
        assert len(cur_fields) == 2
        assert "name1" in cur_fields
        assert "name2" in cur_fields
        assert cur_fields["name1"] == "value1"
        assert cur_fields["name2"] == "value2"
        with layer.Layer(ctx , {"name3": "value3"}, ["name1"]) as layer2:
            cur_fields = ctx.peek_layer()
            assert len(cur_fields) == 2
            assert "name3" in cur_fields
            assert "name2" in cur_fields
            assert cur_fields["name3"] == "value3"
            assert cur_fields["name2"] == "value2"
            with layer.Layer(ctx, {"name4": "value4"}, ["name2"]) as layer3:
                cur_fields = ctx.peek_layer()
                assert len(cur_fields) == 2
                assert "name3" in cur_fields
                assert "name4" in cur_fields
                assert cur_fields["name3"] == "value3"
                assert cur_fields["name4"] == "value4"
            cur_fields = ctx.peek_layer()
            assert len(cur_fields) == 2
            assert "name3" in cur_fields
            assert "name2" in cur_fields
            assert cur_fields["name3"] == "value3"
            assert cur_fields["name2"] == "value2"
        cur_fields = ctx.peek_layer()
        assert len(cur_fields) == 2 
        assert "name1" in cur_fields
        assert "name2" in cur_fields
        assert cur_fields["name1"] == "value1"
        assert cur_fields["name2"] == "value2"
    cur_fields = ctx.peek_layer()
    assert len(cur_fields) == 0
