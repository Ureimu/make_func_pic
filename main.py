import matplotlib.style as mplstyle
from gifconfig import *
from func_input import *
from gifmaker import *
from movefile import *
from history import *
import time

mplstyle.use('fast')

'''
在这里注明一下用到的模块:
numpy,moviepy,matplotlib,...
'''

if __name__ == '__main__':
    try:
        configdict = gif_config()  # 对gif进行设置
        fig, ax1 = draw_fig(configdict['xl'], configdict['xm'], configdict['yl'],
                            configdict['ym'], configdict['sizex'], configdict['sizey'])  # 生成图片基本格式
        funclist = getfunctions()  # 接受用户输入的函数
        recvfunlist = funclist[0]+funclist[1]
    except:
        print('An error has occured, you can get it in historylog.txt.')
        update_log_error()  # 在日志中记录错误
        time.sleep(10)
    print('update log...')
    update_log_fun(configdict,recvfunlist)  # 更新日志
    print('finish')
    try:
        t0,tl0 = get_time()  # 开始计时
        funclist[0], funclist[1] = makefunlist(funclist[0], funclist[1], configdict)  # 制作每一帧对应的函数表
        make_gif(fig, ax1, funclist, configdict)  # 编译函数表并制作gif
        mymovefile(configdict['gifname'], 'pic/'+configdict['gifname'])  # 把文件移动到根目录下的\pic\中
        t1,tl1 = get_time()  # 计时结束
        print('%ss' % (t1-t0))  # 输出制作花费时间
        update_log_time(tl0,tl1)  # 更新日志
    except:
        print('An error has occured, you can get it in historylog.txt.')
        update_log_error()  # 在日志中记录错误
        time.sleep(10)
    else:
        print('finish')

