# -*- coding: utf-8 -*-
"""
BMI 计算器
我的第一个 Python 小程序，写在 helloworld 仓库里
"""


def calc_bmi(height_m: float, weight_kg: float) -> float:
    """按身高(米)和体重(公斤)算 BMI"""
    return weight_kg / (height_m ** 2)


def bmi_level(bmi: float) -> str:
    """按中国标准给 BMI 分级"""
    if bmi < 18.5:
        return "偏瘦"
    elif bmi < 24:
        return "正常"
    elif bmi < 28:
        return "偏胖"
    else:
        return "肥胖"


def main() -> None:
    print("=== BMI 计算器 ===")
    height = float(input("请输入身高(米)，例如 1.75: "))
    weight = float(input("请输入体重(公斤)，例如 65: "))

    bmi = calc_bmi(height, weight)
    level = bmi_level(bmi)

    print(f"你的 BMI 是 {bmi:.1f}，属于「{level}」")


if __name__ == "__main__":
    main()
