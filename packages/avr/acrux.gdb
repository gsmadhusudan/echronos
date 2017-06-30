#
# eChronos Real-Time Operating System
# Copyright (C) 2016 National ICT Australia Limited (NICTA), ABN 62 102 206 173.
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

# gdb --batch <SYSTEM_BINARY> -x <THIS_FILE>
# Don't prompt for terminal input
set height 0
target remote localhost:1212
load
b debug_println
b main
b tick_irq
display rtos_internal_current_task
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
c
# First tick
echo Tick 1-1
c
c
c
c
# Second tick
echo Tick 1-2
c
c
c
c
# Third tick
echo Tick 1-3
c
c
c
c
# Fourth tick
echo Tick 1-4
c
c
c
c
# Fifth tick - b wakes up and does some things
echo Tick 1-5
c
c
c
c
c
c
c
c
c
c
# First tick
echo Tick 2-1
c
c
c
c
# Second tick
echo Tick 2-2
c
c
c
c
# Third tick
echo Tick 2-3
c
c
c
c
# Fourth tick
echo Tick 2-4
c
c
c
c
# Fifth tick - b wakes up and does some things
echo Tick 2-5
c
c
c
c
c
c
c
c
c
c
# Let it tick one more time, then finish up
echo Tick 3, Done.
quit
y
