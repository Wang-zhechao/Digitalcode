from bas.rbas import RBAS
import numpy as np


# 使用前请安装文件
# pip install pybas
# 确保版本号大于0.0.1

# 求 z = -cos(x) - sin(y)(x in [1, 2*pi], y in [1, 2*pi]) 的最大值

def fun(vars):
    # 评价函数
    x, y = vars
    # if 0 <= x <= 2 * np.pi and 0 <= y <= 2 * np.pi:
    return -np.cos(x) - np.sin(y) + 10
    # else:
    #     return -10  # 返回一个达不到的小值

bas = RBAS(fitness_function=fun, dim=2)
bas.run()
print(bas.gbest)