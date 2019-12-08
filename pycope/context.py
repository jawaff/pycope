# Copyright 2019 Jake Waffle. Subject to the Apache2 license.

import immutables

class Context(object):
    """
    A context is what keeps track of the Context-Oriented layers
    that are being entered/exited (hopefully with a 'with' statement.
    
    Warning Note: While the Context is thread-safe, it should be used
    in only one thread at a time. If multiple threads are both 
    introducing layers, then the context will be in an indeterministic
    state.
    """
    INSTANCE = None
    @staticmethod
    def shared_instance():
        """
        This is the default context for the library. It probably works for 
        most use cases.
        :returns: The shared context instance.
        """
        if not Context.INSTANCE:
            Context.INSTANCE = Context()
        return Context.INSTANCE
    
    def __init__(self):
        self._fields = [immutables.Map()]
        
    def peek_layer(self):
        """
        Used to check the valid fields for the current layer.
        :returns: An immutable mapping of the field names to the field values.
        """
        return self._fields[-1]
        
    def push_layer(self, fields_to_add={}, fields_to_remove=[]):
        """
        Pushes a layer of fields into the context's stack.
        :param fields_to_add: A mapping of name to value pairs for the fields to add
            to the new layer.
        :param fields_to_remove: A list of keys for the fields to remove in the
            new layer.
        """
        # We will mutate the current layer in order to create the new layer.
        with self.peek_layer().mutate() as mutation:
            for key, value in fields_to_add.items():
                mutation[key] = value
            
            for key in fields_to_remove:
                del mutation[key]
            
            # Adds the updated map to the top of the field stack.
            self._fields.append(mutation.finish())
            
    def pop_layer(self):
        """Pops the top layer of fields in the context's stack."""
        del self._fields[-1]
        
    def elect_strategy(self, strategies, is_strict=True):
        """
        Retrieves the best strategy for the top layer's valid fields.
        Only one of the given strategies will be elected. Each strategy
        can determine a priority value based on the current fields.
        The priority values are then used to determine winner.
        :param strategies: The candidate strategies for the election.
        :param is_strict: A boolean specifying whether the election algorithm
            is strict. If two or more strategies have the same, max priority, 
            then an error is thrown. (Default True)
        """
        fields = self.peek_layer()
        if len(strategies) > 0:
            votes = list(map(lambda strategy: strategy.get_priority(fields), strategies))
            if is_strict:
                max_votes = max(votes)
                assert(votes.count(max_votes) == 1)
                elected_choice = strategies[votes.index(max_votes)]
            else:
                elected_choice = strategies[votes.index(max(votes))]
            return elected_choice
        else:
            raise ValueError("At least one strategy is required for elections.")
    