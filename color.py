colors = {
    'Black': '\x1b[1;30m',
    'Blue': '\x1b[1;94m',
    'Green': '\x1b[1;92m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[0;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Dark Gray': '\x1b[1;30m',
    'Light Blue': '\x1b[1;34m',
    'Light Cyan': '\x1b[1;36m',
    'Light Red': '\x1b[1;31m',
    'Light Purple': '\x1b[1;35m',
    'Yellow': '\x1b[1;33m',
    'White': '\x1b[1;37m'
}


def getcolor(charac, x, y):

    if charac in [":", ")", "|", "}", "^", "M"]:
        color = "White"
    elif charac == "-":
        color = "Blue"
    elif charac == "#" and x < 36:
        color = "Green"
    elif charac == "#" and x >= 36:
        color = "Red"
        return('\x1b[0;30;41m' + colors[color] + charac + '\x1b[0m')
    elif charac == "+":
        color = "Yellow"
    elif charac in ["H", "$", '@', 'O']:
        color = "Yellow"
    else:
        color = "White"

    return('\x1b[0;30;45m' + colors[color] + charac + '\x1b[0m')
