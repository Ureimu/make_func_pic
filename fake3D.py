str1 = input('put in a function')
str2 = ''
logic0 = input('choose one to use:+ x n')
if logic0 == '+':
    m = int(input('i'))
    for i in range(m):
        str2 += str1 + '+%d'%(i) + '\n'
        str2 += str1 + '-%d'%(i) + '\n'
    print(str2)
elif logic0 == 'x':
    m = int(input('i'))
    for i in range(m):
        str2 += str1 + '*%d'%(i) + '\n'
        str2 += str1 + '*1/%d'%(i) + '\n'
    print(str2)
elif logic0 == 'n':
    m = int(input('i'))
    for i in range(m):
        str2 += str1+ '\n'
    print(str2)
else:
    end
