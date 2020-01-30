
def read_preconfig():
    file = open('preconfig.txt', 'r')
    copy0 = file.readline()
    print(copy0)
    file.close()
    return copy0


def write_preconfig_default():
    file = open('preconfig.txt','x')
    file.write('pic/')
    copy0 = file.readline()
    print(copy0)
    file.close()
    return copy0
