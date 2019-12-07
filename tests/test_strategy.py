import strategy

def test_strategy_init():
    assert(strategy.Strategy(lambda count: print("Count: {}".format(count)),
                             [lambda fields: 1]))

def test_strategy_priority():
    for i in range(10):
        key = "Key{}".format(i)
        strat = strategy.Strategy(lambda value: "{}_{}".format(key, value), 
                                  [lambda fields: 1 if key in fields else 0])
        priority = strat.get_priority({key : key})
        assert priority == 1
        priority = strat.get_priority({"diffKey" : "diffValue"})
        assert priority == 0
        priority = strat.get_priority({})
        assert priority == 0
    
def test_strategy_execution():
    for i in range(10):
        key = "Key{}".format(i)
        strat = strategy.Strategy(lambda value: "{}_{}".format(key, value))
        
        result = strat.execute(i)
        print(result)
        assert result == "{}_{}".format(key, i)
