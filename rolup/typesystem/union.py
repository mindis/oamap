#!/usr/bin/env python

# Copyright 2017 DIANA-HEP
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rolup.util import *
from rolup.typesystem.type import Type

class Union(Type):
    def __init__(self, *of):
        def flatten(x):
            while isinstance(x, Union):
                x = x.of
            return x
        self.of = tuple(map(flatten, of))
        super(Union, self).__init__()

    @property
    def args(self):
        return self.of

    def __contains__(self, element):
        return any(element in x for x in self.of)

    def issubtype(self, supertype):
        # Type.issubtype(supertype) handles the inverse case (supertype is a Union and self isn't); all other Types try that first

        if isinstance(supertype, Union) and self.rtname == supertype.rtname:
            # supertype is a Union; everything that we have must fit into one of its possibilities
            for tpe in self.of:
                if not any(tpe.issubtype(x) for x in supertype.of):
                    return False
            return True

        elif self.rtname == supertype.rtname:
            # supertype is not a Union; everything that we have must fit into it
            for tpe in self.of:
                if not tpe.issubtype(supertype):
                    return False
            return True

        else:
            return False

    def toJson(self):
        return {"union": [x.toJson() for x in self.of]}