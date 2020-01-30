
def read_preconfig():
    file = open('preconfig.txt', 'r')
    copy0 = str(file)
    file.close()
    return copy0


def write_preconfig_default():
    file = open('preconfig.txt','x')
    file.write('pic/')
    copy0 = str(file)
    file.close()
    return copy0
