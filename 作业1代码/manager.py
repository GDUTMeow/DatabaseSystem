import atexit
import csv
import os

# 学号,姓名,性别,宿舍,电话号码
DATAFILE = '作业1代码/data.csv'
data: list[list[int | str]] = []
numbers: list[int] = []
MENU = '''
========== 同学录 ==========
1. 添加
2. 删除
3. 查找
4. 修改
0. 退出
============================'''

@atexit.register
def save_data():
    with open(DATAFILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

if os.path.exists(DATAFILE):
    with open(DATAFILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        for row in data:
            numbers.append(int(row[0]))
        
if __name__ == '__main__':
    print(MENU)
    while True:
        choice = input('\n请选择操作: ')
        if choice == '1':
            student_id = input('请输入学号: ')
            name = input('请输入姓名: ')
            gender = input('请输入性别: ')
            dormitory = input('请输入宿舍: ')
            phone = input('请输入电话号码: ')
            if student_id in [row[0] for row in data]:
                print('学号已存在')
                continue
            data.append([student_id, name, gender, dormitory, phone])
            numbers.append(int(student_id))
        elif choice == '3':
            student_id = input('请输入要查找的学号: ')
            for row in data:
                if row[0] == student_id:
                    print(f'学号: {row[0]}, 姓名: {row[1]}, 性别: {row[2]}, 宿舍: {row[3]}, 电话号码: {row[4]}')
                    break
            else:
                print('未找到')
        elif choice == '4':
            student_id = input('请输入要修改的学号: ')
            for row in data:
                if row[0] == student_id:
                    name = input(f'请输入新的姓名（当前: {row[1]}）: ')
                    gender = input(f'请输入新的性别（当前: {row[2]}）: ')
                    dormitory = input(f'请输入新的宿舍（当前: {row[3]}）: ')
                    phone = input(f'请输入新的电话号码（当前: {row[4]}）: ')
                    row[1] = name if name else row[1]
                    row[2] = gender if gender else row[2]
                    row[3] = dormitory if dormitory else row[3]
                    row[4] = phone if phone else row[4]
                    break
            else:
                print('未找到')
        elif choice == '0':
            break