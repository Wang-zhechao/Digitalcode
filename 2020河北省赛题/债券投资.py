from pulp import *
profit = [[1.0445, 1.3989, 3.3211],
          [1.0800, 1.5827, 4.0054],
          [1.1255, 2.8009, 3.3211],
          [1.1255, 1.3989, 3.0612],
          [1.0445, 1.1877, 3.0612]]
tax = [1.00, 0.80, 1.00, 0.90, 0.70]
risk = [5, 2, 4, 3, 1]


def problem1():
    medicine2 = LpVariable("medicine2", 0, None, LpContinuous)
    medicine9 = LpVariable("medicine9", 0, None, LpContinuous)
    medicine20 = LpVariable("medicine20", 0, None, LpContinuous)

    traffic3 = LpVariable("traffic3", 0, None, LpContinuous)
    traffic12 = LpVariable("traffic12", 0, None, LpContinuous)
    traffic25 = LpVariable("traffic25", 0, None, LpContinuous)

    technology4 = LpVariable("technology4", 0, None, LpContinuous)
    technology15 = LpVariable("technology15", 0, None, LpContinuous)
    technology20 = LpVariable("technology20", 0, None, LpContinuous)

    equipment4 = LpVariable("equipment4", 0, None, LpContinuous)
    equipment9 = LpVariable("equipment9", 0, None, LpContinuous)
    equipment18 = LpVariable("equipment18", 0, None, LpContinuous)

    welfare2 = LpVariable("welfare2", 0, None, LpContinuous)
    welfare5 = LpVariable("welfare5", 0, None, LpContinuous)
    welfare18 = LpVariable("welfare18", 0, None, LpContinuous)

    prob1 = LpProblem("problem1", LpMaximize)

    # 优化目标
    prob1 += medicine2 * profit[0][0] * tax[0] + medicine9 * profit[0][1] * tax[0] + medicine20 * profit[0][2] * tax[0] \
             + traffic3 * profit[1][0] * tax[1] + traffic12 * profit[1][1] * tax[1] + traffic25 * profit[1][2] * tax[1] \
             + technology4 * profit[2][0] * tax[2] + technology15 * profit[2][1] * tax[2] + technology20 * profit[2][2] * tax[2] \
             + equipment4 * profit[3][0] * tax[3] + equipment9 * profit[3][1] * tax[3] + equipment18 * profit[3][2] * tax[3] \
             + welfare2 * profit[4][0] * tax[4] + welfare5 * profit[4][1] * tax[4] + welfare18 * profit[4][2] * tax[4]

    # 约束条件
    prob1 += medicine2 + medicine9 + medicine20 + traffic3 + traffic12 + traffic25 + technology4 + technology15 + \
             technology20 + equipment4 + equipment9 + equipment18 + welfare2 + welfare5 + welfare18 <= 8000

    prob1 += medicine2 + medicine9 + medicine20 >= 1600

    prob1 += (medicine2 + medicine9 + medicine20) * risk[0] + (traffic3 + traffic12 + traffic25) * risk[1] + \
             (technology4 + technology15 + technology20) * risk[2] + (equipment4 + equipment9 + equipment18) * risk[3] + \
             (welfare2 + welfare5 + welfare18) * risk[4] >= 2.5 * 8000

    prob1 += traffic3 + traffic12 + traffic25 >= 800
    prob1 += technology4 + technology15 + technology20 >= 800
    prob1 += equipment4 + equipment9 + equipment18 >= 800
    prob1 += welfare2 + welfare5 + welfare18 >= 800

    prob1 += medicine2 * 2 + medicine9 * 9 + medicine20 * 20 \
             + traffic3 * 3 + traffic12 * 12 + traffic25 * 25 \
             + technology4 * 4 + technology15 * 15 + technology20 * 20 \
             + equipment4 * 4 + equipment9 * 9 + equipment18 * 18 \
             + welfare2 * 2 + welfare5 * 5 + welfare18 * 18 <= 10 * 8000

    # 求解
    status = prob1.solve()

    print(status)
    print(LpStatus[status])
    print(value(prob1.objective))  # 计算结果
    for v in prob1.variables():
        print(v.name, "=", v.varValue)


def problem2():
    medicine2 = LpVariable("medicine2", 0, 0, LpContinuous)
    medicine9 = LpVariable("medicine9", 0, 0, LpContinuous)
    medicine20 = LpVariable("medicine20", 0, None, LpContinuous)

    traffic3 = LpVariable("traffic3", 0, 0, LpContinuous)
    traffic12 = LpVariable("traffic12", 0, 0, LpContinuous)
    traffic25 = LpVariable("traffic25", 0, None, LpContinuous)

    technology4 = LpVariable("technology4", 0, 0, LpContinuous)
    technology15 = LpVariable("technology15", 0, 0, LpContinuous)
    technology20 = LpVariable("technology20", 0, None, LpContinuous)

    equipment4 = LpVariable("equipment4", 0, 0, LpContinuous)
    equipment9 = LpVariable("equipment9", 0, 0, LpContinuous)
    equipment18 = LpVariable("equipment18", 0, None, LpContinuous)

    welfare2 = LpVariable("welfare2", 0, 0, LpContinuous)
    welfare5 = LpVariable("welfare5", 0, 0, LpContinuous)
    welfare18 = LpVariable("welfare18", 0, None, LpContinuous)

    prob1 = LpProblem("problem1", LpMaximize)

    # 优化目标
    prob1 += medicine2 * profit[0][0] * tax[0] + medicine9 * profit[0][1] * tax[0] + medicine20 * profit[0][2] * \
             tax[0] \
             + traffic3 * profit[1][0] * tax[1] + traffic12 * profit[1][1] * tax[1] + traffic25 * profit[1][2] * \
             tax[1] \
             + technology4 * profit[2][0] * tax[2] + technology15 * profit[2][1] * tax[2] + technology20 * \
             profit[2][2] * tax[2] \
             + equipment4 * profit[3][0] * tax[3] + equipment9 * profit[3][1] * tax[3] + equipment18 * profit[3][
                 2] * tax[3] \
             + welfare2 * profit[4][0] * tax[4] + welfare5 * profit[4][1] * tax[4] + welfare18 * profit[4][2] * tax[
                 4]

    # 约束条件
    prob1 += medicine2 + medicine9 + medicine20 + traffic3 + traffic12 + traffic25 + technology4 + technology15 + \
             technology20 + equipment4 + equipment9 + equipment18 + welfare2 + welfare5 + welfare18 <= 8000

    prob1 += medicine2 + medicine9 + medicine20 >= 1600

    prob1 += (medicine2 + medicine9 + medicine20) * risk[0] + (traffic3 + traffic12 + traffic25) * risk[1] + \
             (technology4 + technology15 + technology20) * risk[2] + (equipment4 + equipment9 + equipment18) * risk[
                 3] + \
             (welfare2 + welfare5 + welfare18) * risk[4] >= 2.5 * 8000

    prob1 += traffic3 + traffic12 + traffic25 >= 800
    prob1 += technology4 + technology15 + technology20 >= 800
    prob1 += equipment4 + equipment9 + equipment18 >= 800
    prob1 += welfare2 + welfare5 + welfare18 >= 800

    # prob1 += medicine2 * 2 + medicine9 * 9 + medicine20 * 20 \
    #          + traffic3 * 3 + traffic12 * 12 + traffic25 * 25 \
    #          + technology4 * 4 + technology15 * 15 + technology20 * 20 \
    #          + equipment4 * 4 + equipment9 * 9 + equipment18 * 18 \
    #          + welfare2 * 2 + welfare5 * 5 + welfare18 * 18 <= 10 * 8000

    # 求解
    status = prob1.solve()

    print(status)
    print(LpStatus[status])
    print(value(prob1.objective))  # 计算结果
    for v in prob1.variables():
        print(v.name, "=", v.varValue)

if __name__ == '__main__':
    problem1()