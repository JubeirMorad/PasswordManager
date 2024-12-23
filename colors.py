
""" the coloring process may not work on the command prompt or power shell , 
We will solve this problem in the next versions ..."""
#################################################################################
normal = "\033[0;00m"
gray = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
pink = "\033[0;35m"
skyblue = "\033[0;36m"
white = "\033[0;37m"
lgray = "\033[1;30m" # Lite Gray
lred = "\033[1;31m" # Lite Red
lgreen = "\033[1;32m" # Lite Green
lyellow = "\033[1;33m" # Lite Yellow
lblue = "\033[1;34m" # Lite Blue
lpink = "\033[1;35m" # Lite Pink
lskyblue = "\033[1;36m" # Lite SkyBlue
lwhite = "\033[1;37m" # Lite White

def ToGray(string):
    str_ = gray+str(string)+normal
    return str_

def ToLGray(string):
    str_ = lgray+str(string)+normal
    return str_

def ToRed(string):
    str_ = red+str(string)+normal
    return str_

def ToLRed(string):
    str_ = lred+str(string)+normal
    return str_

def ToGreen(string):
    str_ = green+str(string)+normal
    return str_

def ToLGreen(string):
    str_ = lgreen+str(string)+normal
    return str_

def ToYellow(string):
    str_ = yellow+str(string)+normal
    return str_

def ToLYellow(string):
    str_ = lyellow+str(string)+normal
    return str_

def ToBlue(string):
    str_ = blue+str(string)+normal
    return str_

def ToLBlue(string):
    str_ = lblue+str(string)+normal
    return str_

def ToPink(string):
    str_ = pink+str(string)+normal
    return str_

def ToLPink(string):
    str_ = lpink+str(string)+normal
    return str_

def ToSkyBlue(string):
    str_ = skyblue+str(string)+normal
    return str_

def ToLSkyBlue(string):
    str_ = lskyblue+str(string)+normal
    return str_

def ToWhite(string):
    str_ = white+str(string)+normal
    return str_

def ToLWhite(string):
    str_ = lwhite+str(string)+normal
    return str_

