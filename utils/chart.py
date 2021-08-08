# -*- coding: utf-8 -*-
"""
@Author: llf
@File: chart.py
@IDE: Pycharm
@Time: 2021-08-08
"""
import random


def random_data(length=8):
    data = []
    for _ in range(length):
        data.append(random.randint(0, 100000))
    return data


if __name__ == '__main__':
    data = random_data()
    print(data)
