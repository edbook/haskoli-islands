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
import os, sys, getopt
from sphinx.util.tags import Tags

def find_conf_dir(start_dir, conf_file = 'conf.py'):
    """
    Traverse directories upward to find the configuration file.
    
    return the directory where the file is found or None
    """
    current_dir = os.path.abspath(start_dir)

    while (os.path.splitdrive(current_dir)[1] != os.sep) and \
            (not os.path.exists(os.path.join(current_dir, conf_file))):
        current_dir = os.path.abspath(os.path.join(current_dir, ".."))

    # If nothing found, return the given None
    if not os.path.exists(os.path.join(current_dir, conf_file)):
        return None

    return current_dir


def load_config_file(dirname = '.', filename = 'conf.py', cmd_args = ''):
    """
    Function that loads the values defined in the configuration file parses the
    options given, and returns
    a dictionary with the appropriate variables.
    """

    # Search for conf.py in the ancestors of the current directory
    dirname = find_conf_dir(dirname)
    if dirname == None:
        print 'ERROR: Configuration file', filename, 'could not be found.',
        print 'Check the location of this script.'
        sys.exit(1)

    tags = []
    eval_strs = []
    debug = False
    # Swallow the options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "dt:D:", [])
    except getopt.GetoptError:
        print >> sys.stderr, 'Incorrect option.'
        print >> sys.stderr, main.__doc__
        sys.exit(2)

    # Parse the options
    for optstr, value in opts:
        # Debug option
        if optstr == "-d":
            debug = True
        if optstr == "-t":
            tags.append(value)
        if optstr == "-D":
            eval_strs.append(value)

    current_dir = os.getcwd()
    tags = Tags(tags)
    os.chdir(dirname)
    exec(open(filename).read())

    # Evaluate the remaining strings
    for value in eval_strs:
        parts = value.split('=')
        if len(parts) != 2:
            print 'ERROR: Invalid syntax in option', value
            sys.exit(1)
        exec(parts[0] + "='" + parts[1] + "'")

    del eval_strs
    return (locals(), args)

def var_check(config, varnames):
    """
    Check if a set of variables exists in the config file.
    """

    for varname in varnames: 
        tmp = config.get(varname)
        if tmp == None or tmp == '':
            print 'Script needs the variable', varname, 'defined in config file'
            sys.exit(1)

    return

def which(program):
    """
    Function to search for an executable in a path.
    Taken from http://stackoverflow.com/a/377028
    """

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None



