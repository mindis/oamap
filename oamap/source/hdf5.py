#!/usr/bin/env python

# Copyright (c) 2017, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

try:
    import h5py
except ImportError:
    pass
else:
    def oamap(group):
        return OAMapGroup(group._id)

    h5py._hl.group.Group.oamap = property(oamap)

    class OAMapGroup(h5py._hl.group.Group):
        def __init__(self, id):
            self._id = id

        def __repr__(self):
            return "<OAMap HDF5 group \"{0}\" ({1} members)>".format(self.name, len(self))

        def __str__(self):
            return __repr__(self)

        def __contains__(self, name):
            raise NotImplementedError

        def __len__(self):
            raise NotImplementedError

        def __getitem__(self, name):
            raise NotImplementedError

        def __setitem__(self, name, value):
            raise NotImplementedError

        def __delitem__(self, name):
            raise NotImplementedError

        def keys(self):
            raise NotImplementedError

        def values(self):
            return (self[n] for n in self.keys())

        def items(self):
            return ((n, self[n]) for n in self.keys())

        def __iter__(self):
            return self.keys()

        def __dict__(self):
            return dict(self.items())

        def setdefault(self, key, default=None):
            if key not in self:
                self[key] = default
            return self[key]

        def pop(self, **args):
            return self.popitem(**args)[1]

        def popitem(self, **args):
            if len(args) == 0:
                if len(self) > 0:
                    key, = self.keys()
                else:
                    raise IndexError("pop from empty OAMapGroup")
            elif len(args) == 1:
                key, = args
            elif len(args) == 2:
                key, default = args
            else:
                raise TypeError("popitem expected at most 2 arguments, got {0}".format(len(args)))

            if key in self:
                out = (key, self[key])
                del self[key]
                return out
            elif len(args) == 2:
                return default
            else:
                raise KeyError(repr(key))

        def update(self, other):
            for n, x in other.items():
                self[n] = x
