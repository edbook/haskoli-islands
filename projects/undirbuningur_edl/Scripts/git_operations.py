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

import os, sys, getopt, git
import common

def check_branch(config):
    """
    Effectively run the sanity check once all the checks have been done
    """

    # Check that all required variables are defined.
    common.var_check(config, ['git_root_folder'])
    
    repo_dir = config['git_root_folder']
    repo = git.Repo(repo_dir)
    assert not repo.bare
    
    if repo.head.ref.name != 'master':
        print 'Repository in', repo_dir, 'not in master branch.'
        print 'Terminating'
        sys.exit(1)

    if config['debug']:
        print 'Repository in master branch'

    return

def commit(config):
    """
    Not written yet. Commit the changes to the main branch
    """
    print 'Function not implemented yet'

def datetime_tag(config):
    """
    Tag with date time
    """
    print 'Function not implemented yet'

sub_commands = {
    'git_check_branch': check_branch
}

def main():
    """
    Script to .....
    """
    
    # Load config and arguments
    (config, args) = common.load_config_file(cmd_args = sys.argv[1:])

    # This script does not need any additional arguments
    if len(args) != 1:
        print 'WARNING: Script needs one of the following arguments:'
        print ' ', '\n  '.join(sorted(sub_functions.keys()))
        sys.exit(1)

    sub_commands[args[0]](config)

# Execution as script
if __name__ == "__main__":
    main()
