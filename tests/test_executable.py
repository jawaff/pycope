# Copyright 2019 Jake Waffle. Subject to the Apache2 license.

import context
import strategy
import prioritizers
import executable

def test_executable():
    ctx = context.Context()
    strategies = [strategy.Strategy(lambda x: "{}_1".format(x), [prioritizers.contains_key("name1")]),
                  strategy.Strategy(lambda x: "{}_2".format(x), [prioritizers.contains_key("name2")])]

    string_appender = executable.Executable(ctx, strategies)
    
    with string_appender.new_layer({"name1":"value1"}, []) as layer1:
        strategy1 = string_appender.elect_strategy()
        assert strategy1.execute("entering layer1") == "entering layer1_1"
        assert string_appender.execute("implied election execute test") == "implied election execute test_1"

        with string_appender.new_layer({"name2":"value2"}, ["name1"]) as layer2:
            strategy2 = string_appender.elect_strategy()
            assert strategy2.execute("entering layer2") == "entering layer2_2"
            assert string_appender.execute("implied election execute test") == "implied election execute test_2"
        
        strategy3 = string_appender.elect_strategy()
        assert strategy3.execute("back in layer1") == "back in layer1_1"
        assert string_appender.execute("implied election execute test") == "implied election execute test_1"
        
