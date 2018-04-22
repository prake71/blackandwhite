#!/usr/bin/env python
# Black And White
# (c) by Peter Rake 2018

import sys, os

#these directories will be used if blackandwhite cannot find
#the directories in the location of the main program
if sys.platform == "win32":
    DATADIR = "C:\\Program Files\\BlackAndWhite"
    CODEDIR = "C:\\Program Files\\BlackAndWhite\\code"
else:
    DATADIR = "/usr/share/games/blackandwhite"
    CODEDIR = "/usr/lib/games/blackandwhite"

def main():
    # figure out our directories
    # create global variables in local context
    global DATADIR, CODEDIR
    # os.path.split:
    # Split the pathname path into a pair, (head, tail) where tail is the last pathname component and head is
    # everything leading up to that.
    # sys.argv[0]: full qualified name of current script
    # os.path.abspath: Return a normalized absolutized version of the pathname path.
    localpath = os.path.split(os.path.abspath(sys.argv[0]))[0]
    testdata = localpath
    # Join one or more path components intelligently.
    testcode = os.path.join(localpath, 'code')
    testdata = os.path.join(localpath, 'data')
    # Return True if path is an existing directory.
    if os.path.isdir(testdata):
        DATADIR = testdata
    if os.path.isdir(testcode):
        CODEDIR = testcode

    # apply our directories and test environment
    # changes the current working directory to the given path
    os.chdir(DATADIR)
    # putting CODEDIR as first entry in system path
    sys.path.insert(0, CODEDIR)
    print(DATADIR)

    # run game and protect from exceptions
    try:
        import main, pygame
        main.main(sys.argv)
    except KeyboardInterrupt:
        print("Keyboard Interrupt (Control-C)...")


# call the main function, start up my_game
if __name__ == "__main__":
    main()
