# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-03-23
# @FileName: 链表.py
# 定义节点类
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# 定义链表类
class LinkedList:
    def __init__(self):
        self.head = Node()

    # 添加节点
    def append(self, val):
        new_node = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # 获取链表长度
    def length(self):
        cnt = 0
        cur = self.head
        while cur.next:
            cnt += 1
            cur = cur.next
        return cnt

    # 遍历链表
    def display(self):
        elems = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elems.append(cur.val)
        print(elems)

    # 插入节点
    def insert(self, val, pos):
        if pos < 0 or pos > self.length():
            print("插入位置不合法")
            return
        new_node = Node(val)
        cur = self.head
        cur_pos = 0
        while cur_pos != pos:
            cur = cur.next
            cur_pos += 1
        new_node.next = cur.next
        cur.next = new_node

    # 删除节点
    def delete(self, val):
        cur = self.head
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.val == val:
                pre.next = cur.next
                del cur
                return
        print("节点不存在")

    # 查找链表中的重复数字
    def find_duplicates(self):
        cur = self.head
        elem_dict = {}
        while cur.next:
            cur = cur.next
            if cur.val in elem_dict:
                elem_dict[cur.val] += 1
            else:
                elem_dict[cur.val] = 1
        return [k for k, v in elem_dict.items() if v > 1]

    # 删除链表中的重复数字
    def remove_duplicates(self):
        cur = self.head
        elem_dict = {}
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.val in elem_dict:
                pre.next = cur.next
                del cur
                cur = pre
            else:
                elem_dict[cur.val] = 1


# 主函数
if __name__ == '__main__':
    # 初始化链表
    linked_list = LinkedList()
    # 添加节点
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(6)
    # 查看链表元素
    print("初始链表：")
    linked_list.display()
    # 查找链表中的重复数字
    duplicates = linked_list.find_duplicates()
    print("链表中的重复数字为：", duplicates)
    # 删除链表中的重复数字
    linked_list.remove_duplicates()
    # 查看删除重复数字后的链表元素
    print("删除重复数字后的链表：")
    linked_list.display()
