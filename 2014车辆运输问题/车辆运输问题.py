from pulp import *

gg1 = [19, 2.7, 2.7]
gg2 = [24.3, 2.7, 3.7]
gg3 = []
c1 = [4.61, 1.7, 1.51]
c2 = [3.615, 1.605, 1.394]
c3 = [4.63, 1.785, 1.77]


def maxcar(long):
    car1 = LpVariable("car1", 0, None, LpInteger)
    car2 = LpVariable("car2", 0, None, LpInteger)
    car3 = LpVariable("car2", 0, None, LpInteger)
    prob2 = LpProblem("problem1", LpMaximize)

    # 优化目标
    prob2 += 4.61 * car1 + 3.615 * car2 + 0.1 * (car1 + car2 - 1)

    # 约束条件
    prob2 += 4.61 * car1 + 3.615 * car2 + 0.1 * (car1 + car2 - 1) <= long

    # 求解
    status = prob2.solve()

    print(status)
    print(LpStatus[status])
    print(value(prob2.objective))  # 计算结果
    for v in prob2.variables():
        print(v.name, "=", v.varValue)


def problem1():
    number = [100, 68, 0]

    g1 = LpVariable("g1", 0, None, LpInteger)
    g2 = LpVariable("g2", 0, None, LpInteger)
    g3 = LpVariable("g3", 0, None, LpInteger)
    g4 = LpVariable("g4", 0, None, LpInteger)
    g5 = LpVariable("g5", 0, None, LpInteger)
    g6 = LpVariable("g6", 0, None, LpInteger)
    g7 = LpVariable("g7", 0, None, LpInteger)
    g8 = LpVariable("g8", 0, None, LpInteger)
    g9 = LpVariable("g9", 0, None, LpInteger)
    g10 = LpVariable("g10", 0, None, LpInteger)
    g11 = LpVariable("g11", 0, None, LpInteger)

    prob1 = LpProblem("problem1", LpMinimize)

    # 优化目标
    prob1 += g1 + g2 + g3 + g4 + g5 + 1.000002 * (g6 + g7 + g8 + g9 + g10 + g11)

    # 约束条件
    prob1 += 8 * g1 + 6 * g2 + 4 * g3 + 2 * g4 + 0 * g5 + \
             15 * g6 + 12 * g7 + 9 * g8 + 6 * g9 + 3 * g10 + 0 * g11 >= number[0]
    prob1 += 0 * g1 + 2 * g2 + 4 * g3 + 6 * g4 + 10 * g5 + \
             0 * g6 + 3 * g7 + 6 * g8 + 12 * g9 + 15 * g10 + 18 * g11 >= number[1]
    prob1 += g6 + g7 + g8 + g9 + g10 + g11 <= 0.2 * (g1 + g2 + g3 + g4 + g5)
    # 求解
    status = prob1.solve()

    print(status)
    print(LpStatus[status])
    print(value(prob1.objective))  # 计算结果
    for v in prob1.variables():
        print(v.name, "=", v.varValue)


if __name__ == '__main__':
    # maxcar(19)
    # maxcar(24.3)
    problem1()
    print(1 * 1.000002)
    print(1 * 1.001)
