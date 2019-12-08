# Copyright 2019 Jake Waffle. Subject to the Apache2 license.

import context
import layer
import strategy

class Executable(object):
    """
    This is a contextual executable. Depending on the state of the context,
    it will proxy executions to different strategies.
    """
    def __init__(self, ctx, strategies = []):
        """
        :param ctx: The context that the executable will use.
        :param strategies: The possible strategies available for the contextual 
            execution. This must be a list of functions that have the same signature
            (i.e. same parameters and return types).
        """
        self._ctx = ctx
        self._strategies = strategies

    def get_context(self):
        """
        :returns: The current context for this executable.
        """
        return self._ctx
        
    def set_context(self, ctx):
        """
        :param ctx: The new context for this executable.
        """
        self._ctx = ctx
    
    def new_layer(self, fields_to_add={}, fields_to_remove=[]):
        """
        Creates a new layer for this executable's context.
        :param fields_to_add: A mapping of field names to field values. They will
            be added to the layer.
        :param fields_to_remove: Field names that should be removed from the layer.
        """
        return layer.Layer(self._ctx, fields_to_add, fields_to_remove)

    def elect_strategy(self, is_strict=True):
        """
        Retrieves the best strategy for the top layer's valid fields.
        Only one of the given strategies will be elected. Each strategy
        can determine a priority value based on the current fields.
        The priority values are then used to determine winner.
        :param is_strict: A boolean specifying whether the election algorithm
            is strict. If two or more strategies have the same, max priority, 
            then an error is thrown. (Default True)
        """
        return self._ctx.elect_strategy(self._strategies, is_strict=is_strict)
        
    def execute(self, *args, **kwargs):
        """
        First a strategy is elected and then it is executed with the provided 
        arguments.

        Note: Arguments and the return value are propagated to the executed 
        strategy.

        :param is_strict: A boolean specifying whether the election algorithm
            is strict. If two or more strategies have the same, max priority, 
            then an error is thrown. (Default True) (This argument is not passed
            to the strategy's execute.)
        """
        is_strict = kwargs.pop("is_strict", True)
        return self.elect_strategy(is_strict=is_strict).execute(*args, **kwargs)

        