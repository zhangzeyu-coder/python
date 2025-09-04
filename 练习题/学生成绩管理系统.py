def show_manue():
    print("\n--------学生成绩管理系统-----------")
    print("1. 添加学生成绩")
    print("2. 查看学生成绩")
    print("3. 显示所有学生成绩")
    print("4. 退出系统")
def addstudent(students):
    name = input("请输入学生姓名")
    if name in students:
        print(f"学生{name}已经存在,将更新成绩")
        