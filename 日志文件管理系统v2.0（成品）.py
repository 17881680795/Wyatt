# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-17
# @FileName: 日志文件管理系统v2.0（成品）.py
"""
1.  添加操作提示信息：在执行每个操作之前，请添加适当的提示信息，以便用户知道当前正在执行的操作。例如，在执行删除日志行的操作之前，请添加一个提示信息，询问用户要删除哪一行。
2.更好的输入方式：在输入操作系统密码之前，请添加一个提示信息，告诉用户何时可以输入。在输入命令之前，请使用一个循环，并在每个循环迭代之前打印一条提示信息。这样用户就可以更方便地在一次会话中执行多个命令。
3.异常处理：需要添加适当的异常处理机制，以便在发生错误或异常情况时提供足够的信息和处理方法，例如在文件读写时处理文件不存在或无法读取的情况等。
4.格式化输出：可以使用更好的格式化输出方法，例如使用  f-string，使输出更易于阅读和理解。
5.添加可选参数选项：您可以添加一些可选参数选项，例如日期范围、日志级别、输出格式等，以便更方便地搜索、过滤和分析日志文件。
6.日志文件检索：支持根据关键字、日期、日志级别等多种条件对日志文件进行检索，以满足用户对数据的查询和分析需求。
7.监控告警：可以配置告警规则，及时识别和处理故障和异常情况，为用户提供及时的告警和异常处理服务。
8.高可用性和扩展性：确保系统具备高可用性和良好的扩展性，可以处理大量的数据和高并发访问。"""
import pymysql
import time

#  连接数据库
conn = pymysql.connect(
    host="localhost",  # 数据库所在主机地址
    user="root",  # 数据库用户名
    password="123456",  # 数据库用户密码
    db="iciba",  # 数据库名称
    charset='utf8'  # 数据库字符集
)
# 获取数据库游标
cursor = conn.cursor()

#  创建日志表
cursor.execute('''CREATE  TABLE  IF  NOT  EXISTS  日志文件管理系统v2  (
    id  INTEGER  PRIMARY  KEY  AUTO_INCREMENT,
    title  VARCHAR(255)  NOT  NULL,
    content  TEXT,
    timestamp  INTEGER
)''')
# 提交事务
conn.commit()


# 定义一个查询类
class Query:
    # 初始化类，设定关键字，开始时间，结束时间，排序方法和排序顺序
    def __init__(self, keyword=None, start_time=None, end_time=None, sort_by=None, sort_order='ASC'):
        self.keyword = keyword
        self.start_time = start_time
        self.end_time = end_time
        self.sort_by = sort_by
        self.sort_order = sort_order


#  新增数据
def add_data(title, content):
    cursor.execute('INSERT  INTO  日志文件管理系统v2  (title,  content,  timestamp)  VALUES  (%s,  %s,  %s)',
                   (title, content, round(time.time())))
    # 提交事务
    conn.commit()


#  删除数据
def delete_data(id):
    cursor.execute('DELETE  FROM  日志文件管理系统v2  WHERE  id=%s', (id,))
    # 提交事务
    conn.commit()


#  修改数据
def update_data(id, title, content):
    cursor.execute('UPDATE  日志文件管理系统v2  SET  title=%s,  content=%s,  timestamp=%s  WHERE  id=%s',
                   (title, content, round(time.time()), id))
    # 提交事务
    conn.commit()


#  查询数据
def query_data(query):
    sql = 'SELECT  *  FROM  日志文件管理系统v2  WHERE  1=1'  # 定义SQL语句，查询log表中所有记录
    # 如果查询关键字不为空，添加查询条件
    if query.keyword:
        sql += "  AND  (title  LIKE  '%" + query.keyword + "%'  OR  content  LIKE  '%" + query.keyword + "%')"
    # 如果查询起始时间不为空，添加查询条件
    if query.start_time:
        sql += '  AND  timestamp  >=  ' + str(query.start_time)
    # 如果查询结束时间不为空，添加查询条件
    if query.end_time:
        sql += '  AND  timestamp  <=  ' + str(query.end_time)
    # 如果需要按照某个字段排序，添加排序添加
    if query.sort_by:
        sql += '  ORDER  BY  ' + query.sort_by + '  ' + query.sort_order
    # 执行SQL语句查询语句
    cursor.execute(sql)
    # 获取查询结果
    result = cursor.fetchall()
    # 返回查询结果
    return result


#  数据校验
def validate_data(title, content):
    # 如果标题或内容不存在
    if not title or not content:
        return False
    return True


#  展示查询结果
def show_results(results):
    for result in results:
        print('ID：', result[0])  # 输出id字段
        print('标题：', result[1])  # 输出标题字段
        print('内容：', result[2])  # 输出内容字段
        print('时间戳：', result[3])  # 输出时间戳字段
        print('-' * 20)


#  程序入口
while True:
    # 输出操作提示
    print('请输入操作序号：\n1.  新增日志2.  删除日志3.  修改日志4.  查询日志0.  退出程序')
    # 接受用户输入
    choice = input('请选择：')
    if choice == '1':  # 如果用户选择新增数据
        # 获取标题和内容
        title = input('请输入标题：')
        content = input('请输入内容（可选）：')
        # 验证数据是否有效
        if validate_data(title, content):
            # 如果数据有效，添加数据
            add_data(title, content)
            print('添加成功！')
        else:
            # 如果数据无效，提示用户重新输入
            print('无效数据，请重新输入！')
    elif choice == '2':  # 如果用户选择删除数据
        # 获取要删除的数据的ID
        id = input('请输入要删除的日志ID：')
        # 删除数据
        delete_data(id)
        print('删除成功！')
    elif choice == '3':  # 如果用户选择修改数据
        # 获取要需改的数据的ID、新的标题和新的内容
        id = input('请输入要修改的日志ID：')
        title = input('请输入新标题：')
        content = input('请输入新内容：')
        # 验证数据是否有效
        if validate_data(title, content):
            # 如果数据有效，更新数据
            update_data(id, title, content)
            print('修改成功！')
        else:
            # 如果数据无效，提示用户重新输入
            print('无效数据，请重新输入！')
    elif choice == '4':  # 如果用户选择查询数据
        # 获取查询条件
        keyword = input('请输入关键词（可选）：')
        start_time = input('请输入起始时间戳（可选）：')
        end_time = input('请输入结束时间戳（可选）：')
        sort_by = input('请输入排序字段（可选）：')
        sort_order = input('请输入排序方式（ASC/DESC，默认ASC）：')
        # 构造查询对象
        query = Query(keyword, start_time, end_time, sort_by, sort_order)
        # 查询数据
        results = query_data(query)
        if results:
            # 如果找到相关数据，展示查询结果
            show_results(results)
        else:
            # 如果未找到相关数据，提示用户
            print('没有找到相关日志！')
    elif choice == '0':  # 如果用户选择退出程序
        # 突出循环
        break
    else:
        # 如果用户输入无效操作，提示用户重新输入
        print('无效操作！')

#  关闭数据库连接
cursor.close()
conn.close()

# 用python脚本帮我写一段代码：要由增删改查功能；要由用户输入用户名和密码的功能（两次输入密码）；使用SHA加密算法；容错机制（当文件不存在时创建文件；如果存在则判断是否为重复内容，筛选重复的）；输入框具有详细的提示。
