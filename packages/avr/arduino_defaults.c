/*
 * eChronos Real-Time Operating System
 * Copyright (C) 2016 National ICT Australia Limited (NICTA), ABN 62 102 206 173.
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as published by
 * the Free Software Foundation, version 3, provided that these additional
 * terms apply under section 7:
 *
 *   No right, title or interest in or to any trade mark, service mark, logo
 *   or trade name of of National ICT Australia Limited, ABN 62 102 206 173
 *   ("NICTA") or its licensors is granted. Modified versions of the Program
 *   must be plainly marked as such, and must not be distributed using
 *   "eChronos" as a trade mark or product name, or misrepresented as being
 *   the original Program.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * @TAG(NICTA_AGPL)
 */
#pragma weak setup
void
setup(void)
{
    rtos_start();
}

#pragma weak loop
void
loop(void)
{
}

#pragma weak task_a
void
task_a(void)
{
    for (;;)
    {
        loop_a();
    }
}

#pragma weak task_b
void
task_b(void)
{
    for (;;)
    {
        loop_b();
    }
}

#pragma weak task_c
void
task_c(void)
{
    for (;;)
    {
        loop_c();
    }
}
