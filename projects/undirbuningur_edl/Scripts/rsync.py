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

import os, sys, getopt, subprocess
import common

def do(config):
    """
    Effectively run the rsync steps once all the checks have been done
    """

    # Check that all required variables are defined.
    common.var_check(config,
                     ['publish_src_folder', 'publish_dst_folder'])

    command = [
        'rsync', 
        '-avz', 
        '--exclude', 
        '*~']
 
    # Get the value stored in  extra args and check it is a list
    extra_args = config.get('publish_extra_args')
    if extra_args != None:
        if not isinstance(extra_args, list):
            print 'ERROR: Variable publish_extra_args must have a list'
            sys.exit(1)
        # Append to end of command
        command.extend(extra_args)
        
    # Append the rest of options.
    command.extend([
        config['publish_src_folder'],
        config['publish_dst_folder']
    ])
                   
    if config['debug']:
        print 'Executing command', ' '.join(command)
    subprocess.check_call(command)

sub_commands = {
    __name__: do
}

def main():
    """
    Script to push the content of the build folder to a publishing site using
    rsync. The tool is assued to be installed in the system.

    Config variables:

    publish_src_folder: source folder to publish (Rsync notation)
    publish_dst_folder: destination folder to publish (Rsync notation)
    """

    # Check that rsync exists and can be executed
    if common.which('rsync') == None:
        print 'This script requires the application rsync to be installed and'
        print 'available in your system.'
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
