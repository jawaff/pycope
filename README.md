# PyCOPE [![Build Status](https://travis-ci.org/jawaff/pycope.svg?branch=master)](https://travis-ci.org/jawaff/pycope) [![codecov](https://codecov.io/gh/jawaff/pycope/branch/master/graph/badge.svg)](https://codecov.io/gh/jawaff/pycope)

This is a Context-Oriented Programming Extension for the Python language. It provides
that allow programmers to utilize Context-Oriented techniques in an Object-Oriented
manner. 

# Motivation
This library is the fruit of my Context-Oriented Programming (COP) research and experimentation.
My approach is a new take on COP that can potentially be implemented in any Object Oriented 
supported language. I'll be writing a paper on it soon.

# Installation
This library is available in Pypi. Execute the following command to istall it:
```
pip install pycope
```

# Description
To make this library work at minimum you need a context, a group of strategies with the same
method signature and layers.

## Context
It's unconventional, but the context is stored as a stack of dictionaries.
When you create a COP "layer" you are adding/removing to/from the context's dictionary stack.
Each item in the stack represents a layer's alterations to the previous item. This was made 
possible with a functional styled immutable dictionary, where a new dictionary is made after
each set of alterations.

On a side note with contexts, there should be at least one context foreach thread of execution.
They are thread-safe, but you will probably get unexpected results if multiple threads are 
applying layers to the same context.

## Layers
A 'with' statement must be used on a pycope layer. Layers effects are not permanent 
and must be reversed after the layer reaches the end of its execution scope.

## Strategies
A single group of strategies is used to define a contextual execution. The 
strategies specify their priority based on the available context's map of fields. The 
strategy with the highest priority is the one chosen for execution. This is essentially an 
advanced if/elif/else chain.

## Executable
An executable defines a single contextual executable. The main goal is to minimize 
boilerplate for the user whilst still allowing flexibility and power.

# Example
```python
import context
import strategy
import prioritizers
import executable

def is_red(red, green, blue):
    return red > 50 and green < 30 and blue < 30:
    
def is_green(red, green, blue):
    return red < 30 and green > 50 and blue < 30:

def is_blue(red, green, blue):
    return red < 30 and green < 30 and blue > 50:

color_ctx = context.Context()
color_strategies = [strategy.Strategy(is_red, [prioritizers.contains_field("color": "red")]),
                    strategy.Strategy(is_green, [prioritizers.contains_field("color": "green")]),
                    strategy.Strategy(is_blue, [prioritizers.contains_field("color": "blue")])]
color_tester = executable.Executable(color_ctx, color_strategies)

with color_tester.new_layer({"color":"red"}, []) as layer1:
    assert color_tester.execute(255, 0, 0)
    assert not color_tester.execute(0, 255, 0)
    assert not color_tester.execute(0, 0, 255)

    with color_tester.new_layer({"color":"blue"}, []) as layer2:
        assert not color_tester.execute(255, 0, 0)
        assert not color_tester.execute(0, 255, 0)
        assert color_tester.execute(0, 0, 255)

    assert color_tester.execute(255, 0, 0)
    assert not color_tester.execute(0, 255, 0)
    assert not color_tester.execute(0, 0, 255)
```