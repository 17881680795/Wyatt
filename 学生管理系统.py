class SqList:
    def __init__(self):
        self.init_capacity = 1
        self.capacity = self.init_capacity
        self.data = [None] * self.capacity
        self.size = 0

    def student(self, number, name, course, grade):
        self.number = number
        self.name = name
        self.course = course
        self.grade = grade
        return f'学号为{self.number}，名字为{self.name}，课程为{self.course}，成绩为{self.grade}'

    def resize(self, new_capacity):
        assert new_capacity >= 0
        old_data = self.data
        self.data = [None] * new_capacity
        self.capacity = new_capacity
        for i in range(self.size):
            self.data[i] = old_data[i]

    def add_to(self, data):
        if self.size == self.capacity:
            self.resize(2 * self.size)
        self.data[self.size] = data
        self.size += 1

    def add_stu(self):
        if self.size == self.capacity:
            self.resize(2 * self.size)
        number_stu, name_stu, course_stu, grade_stu = input("输入学号，姓名，科目，成绩：(以空格为间)").split(" ")
        self.add_to(number_stu)
        self.add_to(name_stu)
        self.add_to(course_stu)
        self.add_to(grade_stu)
        print("添加成功")

    def all_stu(self):
        if self.data == [None]:
            print("暂时无学生的信息")
        else:
            stu = 0
            for i in range(self.size // 4):
                print(self.student(self.data[stu], self.data[stu + 1], self.data[stu + 2], self.data[stu + 3]))
                stu += 4
            # print(self.datasets)
            # print(self.size)

    def pop_number(self, op):
        num = 0
        while num < self.size and self.data[num] != op:
            num += 1
        for j in range(num + 4, self.size):
            self.data[j - 4] = self.data[j]
        self.size -= 4
        if self.capacity > self.init_capacity and self.size <= self.capacity / 4:
            self.resize(self.capacity // 2)

    def pop_course(self, pop):
        num = 0
        while num < self.size and self.data[num] != pop:
            num += 1
        for j in range(num + 4, self.size):
            self.data[j - 4] = self.data[j]
        self.size -= 4

    def delete_stu(self):
        select = int(input("请选择删除方式(python package.学号删除，2.课程删除):"))
        if select == 1:
            id_stu = str(input("输入需要删除的学生的学号："))
            if id_stu in self.data:
                self.pop_number(id_stu)
            else:
                print("无此学生信息")
        elif select == 2:
            course_in = str(input("输入要删除的学生的对应课程："))
            if course_in in self.data:
                self.pop_course(course_in)
            else:
                print("无此课程")
        else:
            print("请输入正确指令")

    def sort_number(self):
        for i in range(self.size // 4):
            exchange = False
            for j in range(self.size - 4, 0, -4):
                if int(self.data[j]) > int(self.data[j - 4]):
                    number, name, course, grade = self.data[j], self.data[j - 1], self.data[j - 2], self.data[j - 3]
                    self.data[j], self.data[j - 1], self.data[j - 2], self.data[j - 3] = self.data[j - 4], self.data[
                        j - 5], self.data[j - 6], self.data[j - 7]
                    self.data[j - 4], self.data[j - 5], self.data[j - 6], self.data[j - 7] = number, name, course, grade
                    exchange = True
            if exchange == False: return

    def sort_grade(self):
        for i in range(self.size // 4):
            exchange = False
            for j in range(self.size - 4, 4, -4):
                if int(self.data[j]) < int(self.data[j - 4]):
                    number, name, course, grade = self.data[j], self.data[j - 1], self.data[j - 2], self.data[j - 3]
                    self.data[j], self.data[j - 1], self.data[j - 2], self.data[j - 3] = self.data[j - 4], self.data[
                        j - 5], self.data[j - 6], self.data[j - 7]
                    self.data[j - 4], self.data[j - 5], self.data[j - 6], self.data[j - 7] = number, name, course, grade
            if exchange == False: return

    def menu_stu(self):
        try:
            while True:
                print("-----------欢迎登录学生管理系统--------")
                print('python package.显示学生记录\n2.添加一个学生信息\n3.输入学号或课程删除学生记录\n4.按学号递减排序输出学生记录\n5.递减查看学生成绩\n6.退出系统\n')
                select = int(input("输入对应功能数字："))
                if select == 1:
                    self.all_stu()
                if select == 2:
                    self.add_stu()
                if select == 3:
                    self.delete_stu()
                if select == 4:
                    self.sort_number()
                if select == 5:
                    self.sort_grade()
                if select == 6:
                    print("欢迎下一次使用")
                    break
        except ValueError:
            print("输入有效内容，please！")


use = SqList()
use.menu_stu()
