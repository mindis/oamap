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

import unittest

from oamap.fillable import *

class TestFillable(unittest.TestCase):
    def runTest(self):
        pass

    def test_FillableArray1(self):
        data = [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        a = FillableArray("f8", chunksize=10)
        self.assertEqual(a[:].tolist(), [])
        a.append(data[0])
        self.assertEqual(a[:].tolist(), [])
        a.append(data[1])
        a.append(data[2])
        a.append(data[3])
        a.update()
        self.assertEqual(a[:].tolist(), data[:4])
        for x in data[4:]:
            a.append(x)
        a.update()
        self.assertEqual(len(a._data), 1)
        self.assertEqual(a[:].tolist(), data)
        self.assertEqual(a[1:].tolist(), data[1:])
        self.assertEqual(a[2:].tolist(), data[2:])
        self.assertEqual(a[:9].tolist(), data[:9])
        self.assertEqual(a[:8].tolist(), data[:8])
        self.assertEqual(a[-10:].tolist(), data[-10:])
        self.assertEqual(a[-9:].tolist(), data[-9:])
        self.assertEqual(a[:-1].tolist(), data[:-1])
        self.assertEqual(a[:-2].tolist(), data[:-2])
        self.assertEqual(a[::2].tolist(), data[::2])
        self.assertEqual(a[1::2].tolist(), data[1::2])
        self.assertEqual(a[2::3].tolist(), data[2::3])
        self.assertEqual(a[3::3].tolist(), data[3::3])
        self.assertEqual(a[::-2].tolist(), data[::-2])
        self.assertEqual(a[1::-2].tolist(), data[1::-2])
        self.assertEqual(a[2::-2].tolist(), data[2::-2])
        self.assertEqual(a[9::-2].tolist(), data[9::-2])
        self.assertEqual(a[8::-2].tolist(), data[8::-2])
        self.assertEqual(a[:1:-2].tolist(), data[:1:-2])
        self.assertEqual(a[:2:-2].tolist(), data[:2:-2])
        self.assertEqual(a[:9:-2].tolist(), data[:9:-2])
        self.assertEqual(a[:8:-2].tolist(), data[:8:-2])
        self.assertEqual(a[8:2:-2].tolist(), data[8:2:-2])
        self.assertEqual(a[8:1:-2].tolist(), data[8:1:-2])
        self.assertEqual(a[7:2:-2].tolist(), data[7:2:-2])
        self.assertEqual(a[7:1:-2].tolist(), data[7:1:-2])

    def test_FillableArray2(self):
        data = [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        a = FillableArray("f8", chunksize=5)
        self.assertEqual(a[:].tolist(), [])
        a.append(data[0])
        self.assertEqual(a[:].tolist(), [])
        a.append(data[1])
        a.append(data[2])
        a.append(data[3])
        a.update()
        self.assertEqual(a[:].tolist(), data[:4])
        for x in data[4:]:
            a.append(x)
        a.update()
        self.assertEqual(len(a._data), 2)
        self.assertEqual(a[:].tolist(), data)
        self.assertEqual(a[1:].tolist(), data[1:])
        self.assertEqual(a[2:].tolist(), data[2:])
        self.assertEqual(a[:9].tolist(), data[:9])
        self.assertEqual(a[:8].tolist(), data[:8])
        self.assertEqual(a[-10:].tolist(), data[-10:])
        self.assertEqual(a[-9:].tolist(), data[-9:])
        self.assertEqual(a[:-1].tolist(), data[:-1])
        self.assertEqual(a[:-2].tolist(), data[:-2])
        self.assertEqual(a[::2].tolist(), data[::2])
        self.assertEqual(a[1::2].tolist(), data[1::2])
        self.assertEqual(a[2::3].tolist(), data[2::3])
        self.assertEqual(a[3::3].tolist(), data[3::3])
        self.assertEqual(a[::-2].tolist(), data[::-2])
        self.assertEqual(a[1::-2].tolist(), data[1::-2])
        self.assertEqual(a[2::-2].tolist(), data[2::-2])
        self.assertEqual(a[9::-2].tolist(), data[9::-2])
        self.assertEqual(a[8::-2].tolist(), data[8::-2])
        self.assertEqual(a[:1:-2].tolist(), data[:1:-2])
        self.assertEqual(a[:2:-2].tolist(), data[:2:-2])
        self.assertEqual(a[:9:-2].tolist(), data[:9:-2])
        self.assertEqual(a[:8:-2].tolist(), data[:8:-2])
        self.assertEqual(a[8:2:-2].tolist(), data[8:2:-2])
        self.assertEqual(a[8:1:-2].tolist(), data[8:1:-2])
        self.assertEqual(a[7:2:-2].tolist(), data[7:2:-2])
        self.assertEqual(a[7:1:-2].tolist(), data[7:1:-2])

    def test_FillableArray3(self):
        data = [0.0, 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
        a = FillableArray("f8", chunksize=3)
        self.assertEqual(a[:].tolist(), [])
        a.append(data[0])
        self.assertEqual(a[:].tolist(), [])
        a.append(data[1])
        a.append(data[2])
        a.append(data[3])
        a.update()
        self.assertEqual(a[:].tolist(), data[:4])
        for x in data[4:]:
            a.append(x)
        a.update()
        self.assertEqual(len(a._data), 4)
        self.assertEqual(a[:].tolist(), data)
        self.assertEqual(a[1:].tolist(), data[1:])
        self.assertEqual(a[2:].tolist(), data[2:])
        self.assertEqual(a[:9].tolist(), data[:9])
        self.assertEqual(a[:8].tolist(), data[:8])
        self.assertEqual(a[-10:].tolist(), data[-10:])
        self.assertEqual(a[-9:].tolist(), data[-9:])
        self.assertEqual(a[:-1].tolist(), data[:-1])
        self.assertEqual(a[:-2].tolist(), data[:-2])
        self.assertEqual(a[::2].tolist(), data[::2])
        self.assertEqual(a[1::2].tolist(), data[1::2])
        self.assertEqual(a[2::3].tolist(), data[2::3])
        self.assertEqual(a[3::3].tolist(), data[3::3])
        self.assertEqual(a[::-2].tolist(), data[::-2])
        self.assertEqual(a[1::-2].tolist(), data[1::-2])
        self.assertEqual(a[2::-2].tolist(), data[2::-2])
        self.assertEqual(a[9::-2].tolist(), data[9::-2])
        self.assertEqual(a[8::-2].tolist(), data[8::-2])
        self.assertEqual(a[:1:-2].tolist(), data[:1:-2])
        self.assertEqual(a[:2:-2].tolist(), data[:2:-2])
        self.assertEqual(a[:9:-2].tolist(), data[:9:-2])
        self.assertEqual(a[:8:-2].tolist(), data[:8:-2])
        self.assertEqual(a[8:2:-2].tolist(), data[8:2:-2])
        self.assertEqual(a[8:1:-2].tolist(), data[8:1:-2])
        self.assertEqual(a[7:2:-2].tolist(), data[7:2:-2])
        self.assertEqual(a[7:1:-2].tolist(), data[7:1:-2])