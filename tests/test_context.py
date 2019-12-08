import layer
import context
import strategy
import prioritizers

def test_context_init():
    assert context.Context()
    
def test_context_layers():
    ctx = context.Context()
    layer0 = ctx.peek_layer()
    assert len(layer0) == 0
    
    ctx.push_layer({"name1":"value1"}, [])
    layer1 = ctx.peek_layer()
    assert len(layer1) == 1
    assert "name1" in layer1
    assert layer1["name1"] == "value1"
    
    ctx.push_layer({"name2":"value2"}, ["name1"])
    layer2 = ctx.peek_layer()
    assert len(layer2) == 1
    assert "name2" in layer2
    assert layer2["name2"] == "value2"
    
    ctx.pop_layer()
    layer1_2 = ctx.peek_layer()
    assert len(layer1_2) == 1
    assert "name1" in layer1_2
    assert layer1_2["name1"] == "value1"
    
    ctx.pop_layer()
    layer0_2 = ctx.peek_layer()
    assert len(layer0_2) == 0

def test_context_elect_strategy():
    ctx = context.Context()
    strategies = [strategy.Strategy(lambda x: "{}_1".format(x), [prioritizers.contains_key("name1")]),
                  strategy.Strategy(lambda x: "{}_2".format(x), [prioritizers.contains_key("name2")])]
    
    with layer.Layer(ctx, {"name1":"value1"}, []) as layer1:
        strategy1 = ctx.elect_strategy(strategies)
        assert strategy1.execute("entering layer1") == "entering layer1_1"
        with layer.Layer(ctx, {"name2":"value2"}, ["name1"]) as layer2:
            strategy2 = ctx.elect_strategy(strategies)
            assert strategy2.execute("entering layer2") == "entering layer2_2"
        
        strategy2 = ctx.elect_strategy(strategies)
        assert strategy2.execute("back in layer1") == "back in layer1_1"

def test_context_shared_instance():
    ctx = context.Context.shared_instance()
    assert ctx
    assert len(ctx.peek_layer()) == 0
