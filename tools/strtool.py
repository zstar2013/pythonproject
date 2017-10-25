
def containsAny(allstr, childstr):
    for item in filter(childstr.__contains__, allstr):  # python3里直接使用filter
        return True
    return False

def containsAnyOr(allstr, childstrlist):
    for childstr in childstrlist:
        for item in filter(childstr.__contains__, allstr):  # python3里直接使用filter
            return True
    return False

def contains(allstr, childstr):
    return childstr in allstr

def lowercase(string):
    return string.lower()

def uppercase(string):
    return string.upper()