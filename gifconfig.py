from typing import Dict, Any, Union

import numpy as np
import matplotlib.pyplot as plt


def draw_fig(xl=-5, xm=5, yl=-5, ym=5):
    fig, ax1 = plt.subplots(1, figsize=(6, 6), facecolor='white')
    ax1.set_title("Elevation in y=0")
    ax1.set_ylim(yl, ym)
    ax1.set_xlim(xl, xm)  # x least,x most
    return fig, ax1


def gif_config():
    """Get a config for this gif.

    It is a config,including name,fps,duration,the length of the picture and sth about math.
    """
    xl, xm, yl, ym = -5, 5, -5, 5
    xlfw, xmfw = xl, xm
    jd = 0.01
    # gif属性设置
    gifname = input('输入gif名称:') + '.gif'
    print('输入fps值:')
    fps = int(input())
    print('输入持续时间(s):')
    duration = int(input())
    # 独立设置
    logic1 = input('输入y进行高级设置,否则继续')
    logic2 = 0
    if logic1 == 'y':
        lixy = ((input('设置图像框大小,定义域与值域')).split())
        xl, xm, yl, ym, xlfw, xmfw = float(lixy[0]), float(lixy[1]), float(lixy[2]), float(lixy[3]), float(
            lixy[4]), float(lixy[5])
        logic2 = input('输入y以保留函数运动轨迹,输入y0来使用列表绘制多个方程,列表参量为m0,函数应传入xt和yt')
        jd = float(input('设置函数精度'))
        m = np.arange(xlfw, xmfw, jd)
    else:
        m = np.arange(xlfw, xmfw, jd)
    configdict: Dict[Union[str, Any], Union[Union[str, int, float], Any]] = {'gifname': gifname,
                                                                             'fps': fps,
                                                                             'duration': duration,
                                                                             'logic2': logic2,
                                                                             'xl': xl,
                                                                             'xm': xm,
                                                                             'yl': yl,
                                                                             'ym': ym,
                                                                             'xlfw': xlfw,
                                                                             'xmfw': xmfw,
                                                                             'jd': jd,
                                                                             'm': m,

                                                                             }
    return configdict
