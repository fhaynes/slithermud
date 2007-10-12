### Okay!  I am going to attempt to write a Copyover function!
 ## Let's hope this works.
 ##
 ## I am looking at others' code to determine the best way to do this
 ## for Slither.  With that said, the sources of this inspiration
 ## are:
 ##  http://www.elifulkerson.com/projects/python-dynamically-reload-module.php
 ##   The old "autoreload" module from the original Slither at:
 ##  http://www.koders.com/python/fid0ED630D4D3CB6646D902AF763043839F4285D787.aspx?s=twisted
 ##   And of course, the Python.org documentation available at:
 ##  http://www.python.org
 ##
 ## Adam "Vopisk" Dean 10-12-2007

# Okay, so for this, we're going to need several different steps.
# I imagine these will be the following:
#  1. First, we need to get a complete list of the modules that we are currently using
#  2. Then we need to check those modules to determine whether or not they've changed
#  3. Then we need to make sure that the new modules will load without crashing everything
#  4. Then we'll go ahead and reload the modules

import sys, os
import string
import imp
from traceback import print_exc, format_exception

import MudCommand
import MudConst

class cmdCopyover(MudCommand.MudCommand):
    def __init__(self):
        MudCommand.MudCommand.__init__(self)
        self.info['cmdName']    = "Copyover"
        self.info['helpText']   = "A command to check and reload any code changes dynamically, rather than having \
                                    to reboot the entire MUD."
        self.info['useExample'] = "copyover"

    def process(self, player, args=''):
        '''Here's the good stuff, where we're going to walk through our steps and see if we can make it work!'''

        # Step 1:  Get a complete list of all the modules we are currently using
        #  We want to ignore the modules that are used by Python because they will
        #  add unnecessary time to the checks for updates.

        # A list to hold all of our Slither-specific modules:
        slitherModules = []
        # A list to hold all of our files that have been changed and need to be updated
        dirtyList = []
        
        for module in sys.modules.values():
            # First, we check to make sure the module is actually a file, for some reason
            # sys.modules.values() returns a lot of None's that we don't want to try and
            # mess with.
            if not hasattr(module, '__file__'):
                continue
            # We also have to bypass the __main__ file of the program (I think this should be
            # start.py) because if we reload it, we'll just start up the MUD again and weird
            # things might happen in that case.
            elif module.__name__ == '__main__':
                continue
            elif module.__name__ == 'cmdCopyover':
                continue
            else:
                # Here, we know that we have files that we're working with, so we split the path
                # and check it against our home directory as defined in MudConst.py, if the file
                # resides within our home directory, we know it's one we care about.
                path, file = os.path.split(module.__file__)
                if path.find(MudConst.homeDir) >= 0:
                    slitherModules.append(module)
            ### Step 1 Complete! ###

        # Step 2:  Now we need to check the modules to see if they have changed at all.  We don't
        #  want to waste time reloading modules that haven't changed.
        #
        #  First we need a variable to hold the suffix for files that have been compiled into python
        #  byte-code.  This is usually just .pyc, but we want to use the imp module just to be sure.
        #  imp.get_suffixes() returns a list of tuples, so we'll iterate over it until we get what we
        #  are looking for.
        for ext, mode, type in imp.get_suffixes():
            if type == imp.PY_COMPILED:
                COMPILED_EXT = ext

        # In this loop, we're going to break the files down, take the source files that we have references to
        #  and change their extension to the compiled byte-code extension, then perform a comparison against the
        #  source file to see if any changes have been made.  If they have, we'll add them to the dirtyList,
        #  if there are no changes, we'll just continue on our merry way.
        for module in slitherModules:
            file = module.__file__
            path, ext = os.path.splitext(file)

            if ext.lower() == '.py':
                ext = COMPILED_EXT
                file = path + COMPILED_EXT

            if ext != COMPILED_EXT:
                continue

            # Here we're doing the comparison... We use a try/except block here, because some files, like __init__.py
            #  files never get compiled to byte-code, thus, the attempted comparison will throw an OSError if we try
            #  and stat() a non-existant file, in this case, we just want to bow out(continue) gracefully.  Modifying of
            #  __init__.py files will require a restart to update changes.
            try:
                if os.stat(file[:-1])[8] <= os.stat(file)[8]:
                    continue
                else:
                    # Our comparison failed, the file is out-of-date, add it to the "dirtyList" to mark it for reloading...
                    dirtyList.append(module)
            except:
                continue
            ### Step 2 complete!! ###

        # Step 3:  Here we're going to do error-checking to make sure that our newly modified files will load without throwing
        #  any errors.  If they won't, we'll disregard them.  If everything checks out, we'll move on to the next step of
        #  reloading the files.
        
        for module in dirtyList:
            ### Step 3a: Check to see that the module can be imported at all... ###
            try:
                tmp = __import__(module.__name__)
            except:
                print "Could not import: " + module.__name__

            ### Step 3b: Check to see if we can open the module as a file... ###
            try:
                code = open(module.__file__, 'rU').read()
            except:
                print "Error opening file: " + module.__file__ + ". It doesn't exist?"

            ### Step 3c: See if the file that we opened can compile... If it cannot compile
            ### the import will fail.
            try:
                compile(code, module.__name__, "exec")
            except:
                print "Error in compilation: " + str(sys.exc_info()[0]) + "\r\n" + listf(format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
            else:
                ### The module compiled properly, but will it execute cleanly? ###
                try:
                    execfile(module.__file__)
                except:
                    print "Error in execution: " + str(sys.exc_info()[0]) + "\r\n" + listf(format_exception(sys.exc_type, sys.exc_value, sys.exc_traceback))
                else:
                    ### The code has both compiled and run without error. Now it's time to load it up
                    ### replacing the original code.
                    print "Attempting reload!  Hold on to your butts!"
                    reload( sys.modules[module.__name__] )
        print "Copyover complete!"
        return

def listf(data):
    buffer = ""
    for line in data:
        buffer = buffer + line + "\n"
    return buffer
        