# Volatility
#
# Authors:
# Michael Cohen <scudette@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

"""Tests for the modules plugins."""

from volatility import testlib


class TestModules(testlib.VolatilityBaseUnitTestCase):
    """Test the Modules module."""

    PARAMETERS = dict(commandline="modules")

    def testModules(self):
        """Test the modules plugin."""
        previous = self.baseline['output']
        current = self.current['output']

        # The following can be out of order due to Volatility NG's list
        # traversal algorithm being different from Volatility trunks.

        # Compare virtual addresses.
        self.assertIntegerListEqual(
            sorted(self.ExtractColumn(current, 0, 2)),
            sorted(self.ExtractColumn(previous, 0, 2)))

        # Compare filenames.
        self.assertListEqual(
            sorted(self.ExtractColumn(previous, 1, 2)),
            sorted(self.ExtractColumn(current, 1, 2)))

        # Compare paths.
        self.assertListEqual(
            sorted(self.ExtractColumn(previous, 4, 2)),
            sorted(self.ExtractColumn(current, 4, 2)))

        # Compare base virtual addresses.
        self.assertIntegerListEqual(
            sorted(self.ExtractColumn(previous, 2, 2)),
            sorted(self.ExtractColumn(current, 2, 2)))
