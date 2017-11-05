import sys

# sys.path.remove()


def curpaths():
    return(sys.path)


def setpaths():
    src = "c:\\dev\\SellaShepha\\src"
    sys.path.append(src + "\\IQFeeder")
    sys.path.append(src + "\\packages\\IQFeed-master")
    sys.path.append(src + "\\tests")
    sys.path.append(src + "\\utils")


