#
# eChronos Real-Time Operating System
# Copyright (C) 2015  National ICT Australia Limited (NICTA), ABN 62 102 206 173.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, version 3, provided that these additional
# terms apply under section 7:
#
#   No right, title or interest in or to any trade mark, service mark, logo or
#   trade name of of National ICT Australia Limited, ABN 62 102 206 173
#   ("NICTA") or its licensors is granted. Modified versions of the Program
#   must be plainly marked as such, and must not be distributed using
#   "eChronos" as a trade mark or product name, or misrepresented as being the
#   original Program.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# @TAG(NICTA_AGPL)
#

import ctypes
import os
import random
import sys
import unittest

from pylib.utils import get_executable_extension, base_path


class TestSimple(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # pylint: disable=invalid-name
        result = os.system("{} {} build posix.unittest.simple"
                           .format(sys.executable, base_path('prj', 'app', 'prj.py')))
        system = "out/posix/unittest/simple/system" + get_executable_extension()
        assert result == 0
        cls.simple = ctypes.CDLL(system)

    def test_foo(self):
        assert self.simple.foo() == 37

    def test_bar(self):
        rand = random.Random()
        rand.seed(37)

        for _ in range(20):
            int_x = rand.randint(0, 5000)
            int_y = rand.randint(0, 5000)
            self.assertEqual(int_x + int_y, self.simple.add(int_x, int_y))
