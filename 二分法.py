# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-10
# @FileName: 二分法.py
"""
二分法的用途：
1.  有序列表的搜索：二分法可以在有序列表中高效地查找特定元素，因为每次可以排除一半的元素，从而快速缩小搜索范围。

2.  寻找最大值或最小值：在有序列表中，二分法可以用于寻找最大值或最小值，因为最大值或最小值通常位于列表的两端。

3.  近似解的计算：二分法可以用于计算方程或函数的近似解，因为二分法可以将搜索范围缩小到足够小的范围。

4.  分箱算法：在机器学习和数据科学中，二分法可以用于分箱算法，以将连续的数值型变量转换为离散的分类变量。
"""
from typing import List


# def binary_search(arr: List[int], target: int) -> int:
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] < target:
#             left = mid + 1
#         elif arr[mid] > target:
#             right = mid - 1
#         else:
#             return mid
#     return -1
#
#
# arr = [2, 3, 4, 10, 40]
# target = 10
#
# result = binary_search(arr, target)
#
# if result != -1:
#     print(f'元素{target}在数组中的下标为{result}')
# else:
#     print('数组中不存在该元素')


def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        #  计算中间位置
        mid = (left + right) // 2
        if arr[mid] < target:
            #  更新左边界
            left = mid + 1
        elif arr[mid] > target:
            #  更新右边界
            right = mid - 1
        else:
            return mid
    return -1


arr = [2, 3, 4, 10, 40]
target = 10

result = binary_search(arr, target)

if result != -1:
    print(f'元素{target}在数组中的下标为{result}')
else:
    print('数组中不存在该元素')
