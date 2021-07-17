#!/usr/bin/env python
#
# Copyright (C) 2014 The University of Sydney
# This file is part of the Reauthoring toolkit

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor
# Boston, MA  02110-1301, USA.
#
# Author: Abelardo Pardo (abelardo.pardo@sydney.edu.au)
#
import sys, os, getopt
import common, rsync, sanity_check, link_checker, git_operations
import version_tag

command_index = dict(
    rsync.sub_commands.items() +
    sanity_check.sub_commands.items() +
    link_checker.sub_commands.items() +
    git_operations.sub_commands.items() +
    version_tag.sub_commands.items()
)

def main(command_index):
    """
    Script to bundle the execution of multiple steps corresponding with other
    scripts.

    command_index is a dictionary with names to functions to execute.
    """

    (config, args) = common.load_config_file(cmd_args = sys.argv[1:])

    if args == []:
        print 'Script must have one or more of the following keys:'
        print ' ', '\n  '.join(sorted(command_index.keys()))

    # Loop over the command names given
    for name in args:
        if command_index.get(name) == None:
            print 'Command', name, 'not found. Ignoring.'
            continue

        command_index[name](config)

# Execution as script
if __name__ == "__main__":
    main(command_index)

