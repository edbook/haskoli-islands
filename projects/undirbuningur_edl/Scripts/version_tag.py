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
    Refresh a version number in a given file.
    """

    # Check that all required variables are defined.
    common.var_check(config, ['version_file', 'version_re', 'version_tag'])

    if not os.path.exists(config['version_file']) or \
       not os.path.isfile(config['version_file']):
        print 'ERROR:', config['version_file'], 'is not a correct file'
        sys.exit(1)

    new_content = '' # New file content
    matched = False  # To detect if a match occurs
    with open(config['version_file']) as f:
        for line in f:
            match = re.match(config['version_re'], line)
            # If there was a match, treat the line specially
            if match != None:
                # Leave a mark that the line was detected
                matched = True
                value = match.groupdict().get('tag')
                # If the match has not a number field, terminate.
                if value == None:
                    print 'Regular expression in version_re must contain a',
                    print 'field named <tag>.'
                    sys.exit(1)
                # Replace the tag with a new one.
                if config['debug']:
                    print 'Replacing', value, 'with', config['version_tag'],
                    print 'in file', config['version_file']
                    
                line = line.replace(value, config['version_tag'])
            new_content += line
        f.close()

    # If there was a match, update the file.
    if matched:
        with open(config['version_file'], 'w') as f:
            f.write(new_content)
            f.close()
    # If no match was detected, warn
    else:
        print 'WARNING: No line matched the given regular expression',
        print '(var version_re in the conf file)'
        print 'No changes done to the file.'

    return

sub_commands = {
    __name__: do
}

def main():
    """
    Script to change a line in a file and update its value with a new date/time
    tag. 
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
