'''
Set up (system) path search for python imports
See: https://stackoverflow.com/questions/13793921/removing-path-from-python-search-module-path
'''
import sys

# sys.path.remove()


def curpaths():
    return(sys.path)


def setpaths():
    '''
    Sets paths for this project
    Note: it seems they don't accumulate from run to run
    '''
'''
    src = "c:\\dev\\SellaShepha\\src"
    sys.path.append(src + "\\IQFeeder")
    sys.path.append(src + "\\packages\\IQFeed-master")
    sys.path.append(src + "\\tests")
    sys.path.append(src + "\\utils")
'''