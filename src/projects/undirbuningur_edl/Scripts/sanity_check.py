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
    Effectively run the sanity check once all the checks have been done
    """

    # Check that all required variables are defined.
    common.var_check(config,
                     ['sanity_src_folder', 'sanity_files', 'sanity_detect'])

    # Detect all files that match the filter
    matches = []
    for root, dirnames, filenames in os.walk(config['sanity_src_folder']):
        for filename in fnmatch.filter(filenames, config['sanity_files']):
            matches.append(os.path.join(root, filename))

    # Print the number of files to be processed
    if config['debug']:
        print "{:,}".format(len(matches)), 'files to be processed'
        print "{:,}".format(len(config['sanity_detect'])),
        print 'expressions to be tested'

    # Loop over all detected file names
    total_lines = 0
    for filename in matches:
        with open(filename) as f:
            line_number = 1
            # Loop over all lines in a file
            for line in f:
                # Loop over all the given regular expressions
                for expression in config['sanity_detect']:
                    if re.search(expression, line) != None:
                        print 'Incorrect expression detected in file',
                        print filename, 'line', line_number
                line_number += 1
            f.close()
            total_lines += line_number

    if config['debug']:
        print "{:,}".format(total_lines), 'text lines inspected.'
        print "{:,}".format(total_lines * len(matches) * 
                            len(config['sanity_detect'])), 'checks.'
               
    return

sub_commands = {
    __name__: do
}

def main():
    """
    Script to search for a given set of expressions in files contained in a
    folder (or subfolder).
    """
    
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
