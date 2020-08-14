from pulp import *

profit = {
    '医药2': 1.0445, '医药9': 1.3989, '医药20': 3.3211,
    '交通3': 1.0800, '交通12': 1.5827, '交通25': 4.0054,
    '科技4': 1.1255, '科技15': 2.8009, '科技20': 3.3211,
    '装备4': 1.1255, '装备9': 1.3989, '装备18': 3.0612,
    '国民2': 1.0445, '国民5': 1.1877, '国民18': 3.0612
}

tax = {
    '医药2': 1.00, '医药9': 1.00, '医药20': 1.00,
    '交通3': 0.80, '交通12': 0.80, '交通25': 0.80,
    '科技4': 1.00, '科技15': 1.00, '科技20': 1.00,
    '装备4': 0.90, '装备9': 0.90, '装备18': 0.90,
    '国民2': 0.70, '国民5': 0.70, '国民18': 0.70
}

risk = {
    '医药2': 5, '医药9': 5, '医药20': 5,
    '交通3': 2, '交通12': 2, '交通25': 2,
    '科技4': 4, '科技15': 4, '科技20': 4,
    '装备4': 3, '装备9': 3, '装备18': 3,
    '国民2': 1, '国民5': 1, '国民18': 1
}

year = {
    '医药2': 2, '医药9': 9, '医药20': 20,
    '交通3': 3, '交通12': 12, '交通25': 25,
    '科技4': 4, '科技15': 15, '科技20': 20,
    '装备4': 4, '装备9': 9, '装备18': 18,
    '国民2': 2, '国民5': 5, '国民18': 18
}

plan = {
    '方案1': ['科技20', '科技4', '科技4', '医药2'],
    '方案2': ['科技20', '科技4', '科技4', '国民2'],
    '方案3': ['科技20', '装备4', '装备4', '医药2'],
    '方案4': ['科技20', '装备4', '装备4', '国民2'],
    '方案5': ['科技20', '科技4', '装备4', '国民2'],
    '方案6': ['科技20', '科技4', '装备4', '国民2'],
    '方案7': ['科技20', '装备4', '科技4', '国民2'],
    '方案8': ['科技20', '装备4', '科技4', '国民2'],
    '方案9': ['科技20', '国民5', '国民5'],
    '方案10': ['科技20', '科技4', '交通3'],
    '方案11': ['科技20', '装备4', '交通3'],

    '方案12': ['医药20', '科技4', '科技4', '医药2'],
    '方案13': ['医药20', '科技4', '科技4', '国民2'],
    '方案14': ['医药20', '装备4', '装备4', '医药2'],
    '方案15': ['医药20', '装备4', '装备4', '国民2'],
    '方案16': ['医药20', '科技4', '装备4', '国民2'],
    '方案17': ['医药20', '科技4', '装备4', '国民2'],
    '方案18': ['医药20', '装备4', '科技4', '国民2'],
    '方案19': ['医药20', '装备4', '科技4', '国民2'],
    '方案20': ['医药20', '国民5', '国民5'],
    '方案21': ['医药20', '科技4', '交通3'],
    '方案22': ['医药20', '装备4', '交通3'],

    '方案23': ['装备18', '交通12'],
    '方案24': ['装备18', '医药9', '交通3'],
    '方案25': ['装备18', '装备9', '交通3'],
    '方案26': ['装备18', '国民5', '国民5', '医药2'],
    '方案27': ['装备18', '国民5', '国民5', '国民2'],
    '方案28': ['装备18', '科技4', '科技4', '医药2'],
    '方案29': ['装备18', '科技4', '科技4', '国民2'],
    '方案30': ['装备18', '装备4', '装备4', '医药2'],
    '方案31': ['装备18', '装备4', '装备4', '国民2'],
    '方案32': ['装备18', '科技4', '装备4', '医药2'],
    '方案33': ['装备18', '科技4', '装备4', '国民2'],
    '方案34': ['装备18', '装备4', '科技4', '医药2'],
    '方案35': ['装备18', '装备4', '科技4', '国民2'],
    '方案36': ['装备18', '交通3', '交通3', '交通3', '交通3'],

    '方案37': ['国民18', '交通12'],
    '方案38': ['国民18', '医药9', '交通3'],
    '方案39': ['国民18', '装备9', '交通3'],
    '方案40': ['国民18', '国民5', '国民5', '医药2'],
    '方案41': ['国民18', '国民5', '国民5', '国民2'],
    '方案42': ['国民18', '科技4', '科技4', '医药2'],
    '方案43': ['国民18', '科技4', '科技4', '国民2'],
    '方案44': ['国民18', '装备4', '装备4', '医药2'],
    '方案45': ['国民18', '装备4', '装备4', '国民2'],
    '方案46': ['国民18', '科技4', '装备4', '医药2'],
    '方案47': ['国民18', '科技4', '装备4', '国民2'],
    '方案48': ['国民18', '装备4', '科技4', '医药2'],
    '方案49': ['国民18', '装备4', '科技4', '国民2'],
    '方案50': ['国民18', '交通3', '交通3', '交通3', '交通3'],

    '方案51': ['交通25', '国民5'],
    '方案52': ['交通25', '交通3', '国民2'],
    '方案53': ['交通25', '交通3', '医药2'],
}


def problem1():
    ingredients = ['医药2', '医药9', '医药20',
                   '交通3', '交通12', '交通25',
                   '科技4', '科技15', '科技20',
                   '装备4', '装备9', '装备18',
                   '国民2', '国民5', '国民18']

    ingMass = LpVariable.dicts("Ingr", ingredients, 0, None, cat=LpContinuous)
    prob = LpProblem("第一问", LpMaximize)

    # # 优化目标
    prob += lpSum([ingMass[item] * profit[item] * tax[item]] for item in ingredients)

    # ------------约束条件---------------------
    # 投资总额小于8000
    prob += lpSum([ingMass[item]] for item in ingredients) <= 8000
    # 医药占比大于20%
    prob += lpSum([ingMass[item]] for item in ingredients[0:3]) >= 0.2 * lpSum([ingMass[item]] for item in ingredients)
    # 交通占比大于10%
    prob += lpSum([ingMass[item]] for item in ingredients[3:6]) >= 0.1 * lpSum([ingMass[item]] for item in ingredients)
    # 科技占比大于10%
    prob += lpSum([ingMass[item]] for item in ingredients[6:9]) >= 0.1 * lpSum([ingMass[item]] for item in ingredients)
    # 装备占比大于10%
    prob += lpSum([ingMass[item]] for item in ingredients[9:12]) >= 0.1 * lpSum([ingMass[item]] for item in ingredients)
    # 国民占比大于10%'
    prob += lpSum([ingMass[item]] for item in ingredients[12:15]) >= 0.1 * lpSum([ingMass[item]] for item in ingredients)
    # 平均风险等级大于2.5
    prob += lpSum([ingMass[item] * risk[item]] for item in ingredients) >= 2.5 * lpSum([ingMass[item]] for item in ingredients)
    # 平均年限小于10
    prob += lpSum([ingMass[item] * year[item]] for item in ingredients) <= 10 * lpSum([ingMass[item]] for item in ingredients)

    status = prob.solve()

    # print(prob)
    print(status)
    print(LpStatus[status])
    print(value(prob.objective))  # 计算结果
    for v in prob.variables():
        print(v.name, "=", v.varValue)


def problem2():
    ingredients = ['方案{}'.format(i) for i in range(1, 54)]

    ingMass = LpVariable.dicts("Ingr", ingredients, 0, None, cat=LpContinuous)
    prob = LpProblem("第二问", LpMaximize)

    # # 收益字典
    # profit_plan = {}
    # for i in ingredients:
    #     p = 1
    #     for e in plan[i]:
    #         p = p * profit[e] * tax[e]
    #     profit_plan[i] = p

    # 收益字典
    profit_plan = {}
    for i in ingredients:
        p = 1
        list1 = [1]
        for e in plan[i]:
            p = p * profit[e] * tax[e]
            list1.append(p)
        profit_plan[i] = list1


    # 风险字典
    risk_plan = {}
    for i in ingredients:
        r = 0
        p = 1
        z = 0
        for e in plan[i]:
            r = r + risk[e] * p
            z = z + p
            p = p * profit[e] * tax[e]
        risk_plan[i] = r / z

    # 年限字典
    year_plan = {}
    for i in ingredients:
        y = 0
        p = 1
        z = 0
        for e in plan[i]:
            y = y + year[e] * p
            z = z + p
            p = p * profit[e] * tax[e]
        year_plan[i] = y / z

    # 总投资的钱
    zong = None
    for pl in plan:
        for p in profit_plan[pl][: -1]:
            zong += ingMass[pl] * p

    # 医药投资的钱
    yiyao = None
    for pl in plan:
        for num, e in enumerate(plan[pl]):
            if risk[e] == 5:
                yiyao += ingMass[pl] * profit_plan[pl][num]

    # 交通投资的钱
    jiaotong = None
    for pl in plan:
        for num, e in enumerate(plan[pl]):
            if risk[e] == 2:
                jiaotong += ingMass[pl] * profit_plan[pl][num]

    # 科技投资的钱
    keji = None
    for pl in plan:
        for num, e in enumerate(plan[pl]):
            if risk[e] == 4:
                keji += ingMass[pl] * profit_plan[pl][num]

    # 装备投资的钱
    zhuangbei = None
    for pl in plan:
        for num, e in enumerate(plan[pl]):
            if risk[e] == 3:
                zhuangbei += ingMass[pl] * profit_plan[pl][num]

    # 国民投资的钱
    guomin = None
    for pl in plan:
        for num, e in enumerate(plan[pl]):
            if risk[e] == 1:
                guomin += ingMass[pl] * profit_plan[pl][num]

    # ------------优化目标--------------------
    prob += lpSum([ingMass[item] * profit_plan[item][-1]] for item in ingredients)

    # ------------约束条件---------------------
    # 投资总额小于8000
    prob += lpSum([ingMass[item]] for item in ingredients) <= 8000
    # 投资风险等级大于2.5
    prob += lpSum([ingMass[item] * risk_plan[item]] for item in ingredients) >= 3 * lpSum([ingMass[item]] for item in ingredients)
    # 投资风险年限小于10
    prob += lpSum([ingMass[item] * year_plan[item]] for item in ingredients) <= 10 * lpSum([ingMass[item]] for item in ingredients)
    # 医药大于20%
    prob += yiyao >= 0.2 * zong
    # 交通大于10%
    prob += jiaotong >= 0.1 * zong
    # 科技大于10%
    prob += keji >= 0.1 * zong
    # 装备大于10%
    prob += zhuangbei >= 0.1 * zong
    # 国民大于10%
    prob += guomin >= 0.1 * zong

    # -------------求解---------------------
    status = prob.solve()

    # print(prob)
    print(status)
    print(LpStatus[status])
    print(value(prob.objective))  # 计算结果
    for v in prob.variables():
        print(v.name, "=", v.varValue)

    # for e in year_plan:
    #     if year_plan[e] > 10:
    #         print(e, year_plan[e])
    #
    # for e in risk_plan:
    #     if risk_plan[e] < 2.6:
    #         print(e, risk_plan[e])


if __name__ == '__main__':
    problem2()

