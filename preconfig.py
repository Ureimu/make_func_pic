
def read_preconfig():  # 读取用户的preconfig文件
    file = open('preconfig.txt', 'r')
    copy0 = file.readline()
    print(copy0)
    file.close()
    return copy0


def write_preconfig_default():  #　创建一个默认的preconfig文件
    file = open('preconfig.txt','x')
    file.write('pic/')
    copy0 = file.readline()
    print(copy0)
    file.close()
    return copy0
