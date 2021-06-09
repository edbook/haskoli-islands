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

import os, sys, getopt, subprocess, fnmatch, re, locale
import common

def do(config):
    """
    Effectively run the linkchecker from a folder.
    """

    # Check that all required variables are defined.
    common.var_check(config,
                     ['linkchecker_src_folder', 'linkchecker_ignore_urls'])

    command = [
        'linkchecker',
        '-a',
    ]

    command.extend(['--ignore-url=' + x 
                    for x in config['linkchecker_ignore_urls']])

    command.append(config['linkchecker_src_folder'])

    print 'Executing command', ' '.join(command)
    subprocess.check_call(command)

    return

sub_commands = {
    __name__: do
}

def main():
    """
    Script to run linkchecker in a folder. It expects the following variables:

    linkchecker_ignore_urls
    linkchecker_src_folder
    """
    
    # Check that rsync exists and can be executed
    if common.which('linkchecker') == None:
        print 'This script requires the application linkchecker to be',
        print 'installed and available in your system.'
        sys.exit(1)

    # Load config and arguments
    (config, args) = common.load_config_file(cmd_args = sys.argv[1:])

    # This script does not need any additional arguments
    if args != []:
        print 'WARNING: Script ignoring the following arguments:'
        print ' ', '\n  '.join(args)

    do(config)

# Execution as script
if __name__ == "__main__":
    main()
