# Black And White
# (c) by Peter Rake 2018

import sys, os


def main():
    # figure out our directories
    global DATADIR, CODEDIR
    localpath = os.path.split(os.path.abspath(sys.argv[0]))[0]
    testdata = localpath
    testcode = os.path.join(localpath, 'code')
    if os.path.isdir(os.path.join(testdata, 'data')):
        DATADIR = testdata
    if os.path.isdir(testcode):
        CODEDIR = testcode

    # apply our directories and test environment
    os.chdir(DATADIR)
    sys.path.insert(0, CODEDIR)

    try:
        import game

    except ImportError:
        pass

        # run game and protect from exceptions
    try:
        import main, pygame
        main.main(sys.argv)
    except KeyboardInterrupt:
        print("Keyboard Interrupt (Control-C)...")


# call the main function, start up my_game
if __name__ == "__main__":
    main()
