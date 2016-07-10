from __future__ import print_function
from .Util import idenR

class GeneralValue:

    def __init__(self, name, to_string, map_f, reduce_f, post_map_f, post_reduce_f):
        self.name = name
        self.map_f = map_f
        self.reduce_f = reduce_f
        self.to_string = to_string
        self.post_map_f = post_map_f
        self.post_reduce_f = post_reduce_f


class Value(GeneralValue):

    def __init__(self, name, column, *, to_string=str, map_f=idenR,
                 reduce_f=idenR, post_map_f=idenR, post_reduce_f=idenR):
        GeneralValue.__init__(self, name, to_string, map_f, reduce_f, post_map_f, post_reduce_f)
        self.column = column

class StateValue(GeneralValue):

    def __init__(self, name, state_name, *, to_string=str, map_f=idenR,
                 reduce_f=idenR, post_map_f=idenR, post_reduce_f=idenR):
        GeneralValue.__init__(self, name, to_string,  map_f, reduce_f, post_map_f, post_reduce_f)
        self.state_name = state_name
