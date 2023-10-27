# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-17
# @FileName: 日志文件管理系统v1.0（成品）.py
import datetime

log_types = ['Tasks', 'Events', 'Important Matters']


def write_header(file):
    """
    写入日志文件头
    """
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    file.write(f'LOG FILE - CREATED: {current_time}\n')
    for index, log_type in enumerate(log_types):
        file.write(f'{index + 1}. {log_type}\n')
    file.write('\n')


class LogFile:
    def __init__(self, file_name):
        self.file_name = file_name
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                pass
        except FileNotFoundError:
            with open(file_name, 'w', encoding='utf-8') as file:
                write_header(file)

    def add_log(self, log_type, log_info):
        with open(self.file_name, 'a', encoding='utf-8') as file:
            type_number = str(log_types.index(log_type) + 1)
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log_string = f'[{type_number}] {current_time}: {log_info}\n'
            file.write(log_string)

    def delete_log(self, line_number):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(self.file_name, 'w', encoding='utf-8') as file:
            for i, line in enumerate(lines):
                if i != line_number - 1:
                    file.write(line)

    def edit_log(self, line_number, new_info):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        with open(self.file_name, 'w', encoding='utf-8') as file:
            for i, line in enumerate(lines):
                if i == line_number - 1:
                    type_number = line.split()[0][1:-1]
                    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    new_line = f'[{type_number}] {current_time}: {new_info}\n'
                    file.write(new_line)
                else:
                    file.write(line)

    def search_log(self, search_string):
        match_lines = []
        with open(self.file_name, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                if search_string in line:
                    match_lines.append((i + 1, line.strip()))
        return match_lines


if __name__ == '__main__':
    file_name = 'log.txt'
    log_file = LogFile(file_name)

    # 添加新日志信息
    log_file.add_log('Events', '5月13号报名英语四级考试')
    log_file.add_log('Events', '5月4号报名人工智能工程师（python）考试')
    log_file.add_log('Events', '参加学校举行的信息素养大赛')
    log_file.add_log('Tasks', '本周四参加1 X考试（模拟）')
    log_file.add_log('Tasks', '六月份参加科大讯飞1 X考试（正式）')
    log_file.add_log('Tasks', '每天刷英语四级训练题')
    log_file.add_log('Tasks', '每天学python')
    log_file.add_log('Tasks', '每天学数据分析及可视化')
    log_file.add_log('Tasks', '按时复习机器学习的内容')
    log_file.add_log('Tasks', '每周三次练习爬虫')
    print(f'日志文件 {file_name} 添加新日志信息成功！')

    # 删除日志信息
    line_number = 2
    log_file.delete_log(line_number)
    print(f'已删除第 {line_number} 行日志信息')

    # 修改日志信息
    line_number = 2
    new_log_info = 'Submit the final AI project.'
    log_file.edit_log(line_number, new_log_info)
    print(f'已修改第 {line_number} 行日志信息')

    # 搜索日志信息
    search_string = 'Friday'
    search_log_result = log_file.search_log(search_string)
    print(f'搜索结果:')
    if len(search_log_result) == 0:
        print(f'未找到包含 "{search_string}" 的日志信息。')
    else:
        for result in search_log_result:
            print(f'行号：{result[0]} 内容：{result[1]}')
