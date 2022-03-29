import threading
from tkinter import ttk
import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox  # 弹窗
from tkinter import filedialog
import openpyxl
import sqlite3
import os


def check_sql():
    pdir = os.path.expanduser("~/sql/")
    isdir = os.path.exists(pdir)

    if not isdir:
        os.makedirs(pdir)
        conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
        c = conn.cursor()
        c.execute('''CREATE TABLE COMPANY
            (ID            INT     NOT NULL,
               NAME           TEXT    DEFAULT NULL,
               GENDER         INT     DEFAULT NULL,
               AGE            TEXT    DEFAULT NULL,
               UNIT           TEXT    DEFAULT NULL,
               PRICE          INT     DEFAULT NULL,
               PRIMARY KEY (`ID`));''')
        conn.commit()
        conn.close()


# 商品信息操作界面
def open_window():
    root = tk.Tk()
    root.withdraw()


class AdminPage:
    def __init__(self, parent_window):
        self.row_info = None
        self.row = None
        parent_window.update()
        parent_window.destroy()  # 自动销毁上一个界面
        check_sql()
        self.window = Tk()  # 初始框的声明
        self.window.title('管理面板')
        self.window.geometry("700x630+300+0")  # 初始窗口在屏幕中的位置
        self.frame_left_top = tk.Frame(width=300, height=200)  # 指定框架，在窗口上可以显示，这里指定四个框架
        self.frame_right_top = tk.Frame(width=300, height=280)
        self.frame_center = tk.Frame(width=750, height=200)
        self.frame_bottom = tk.Frame(width=800, height=50)

        menubar = Menu(self.window, tearoff=0)
        menu1 = Menu(self.window, tearoff=0)
        menu1.add_command(label='从Excel文件导入', command=self.read_excel, font=('Verdana', 15))
        menubar.add_cascade(label="文件", menu=menu1)
        menu1.add_command(label='导出到Excel', command=self.save_excel, font=('Verdana', 15))
        self.window['menu'] = menubar

        # 定义下方中心列表区域
        self.columns = ("商品id", "名称", "余货量", "型号", "单位", "单价")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=8, columns=self.columns)
        # 添加竖直滚动条
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 定义id1为修改id时的暂存变量，这个是为了更新信息而设计的
        self.id1 = 0
        # 表格的标题
        self.tree.column("商品id", width=100, anchor='center')
        self.tree.column("名称", width=150, anchor='center')
        self.tree.column("余货量", width=100, anchor='center')
        self.tree.column("型号", width=100, anchor='center')
        self.tree.column("单位", width=100, anchor='center')
        self.tree.column("单价", width=100, anchor='center')

        # grid方法将tree和vbar进行布局
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)

        # 定义几个数组，为中间的那个大表格做一些准备

        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.unit = []
        self.price = []
        # 打开数据库连接
        conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
        c = conn.cursor()
        cursor = c.execute("SELECT *  from COMPANY")
        results = cursor.fetchall()
        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.gender.append(row[2])
            self.age.append(row[3])
            self.unit.append(row[4])
            self.price.append(row[5])
        conn.close()

        print("test***********************")
        for i in range(min(len(self.id), len(self.name), len(self.gender), len(self.age),
                           len(self.unit), len(self.price))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i], self.age[i],
                                            self.unit[i], self.price[i]))

        for col in self.columns:  # 绑定函数，使表头可排序(这里的command=lambda _col=col还不是太懂)
            self.tree.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义左上方区域
        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明学号
        self.var_name = StringVar()  # 声明姓名
        self.var_gender = StringVar()  # 声明性别
        self.var_age = StringVar()  # 声明年龄
        self.var_unit = StringVar()  # 声明性别
        self.var_price = StringVar()  # 声明年龄
        # 商品id
        self.right_top_id_label = Label(self.frame_left_top, text="商品id： ", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id, font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)
        self.right_top_id_entry.grid(row=1, column=1)
        # 商品名称
        self.right_top_name_label = Label(self.frame_left_top, text="名称：", font=('Verdana', 15))
        self.right_top_name_entry = Entry(self.frame_left_top, textvariable=self.var_name, font=('Verdana', 15))
        self.right_top_name_label.grid(row=2, column=0)  # 位置设置
        self.right_top_name_entry.grid(row=2, column=1)
        # 商品价格
        self.right_top_gender_label = Label(self.frame_left_top, text="余货量：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_gender, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=3, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=3, column=1)
        # 销售数量
        self.right_top_gender_label = Label(self.frame_left_top, text="型号：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_age, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=4, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=4, column=1)

        self.right_top_gender_label = Label(self.frame_left_top, text="单位：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_unit, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=5, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=5, column=1)

        self.right_top_gender_label = Label(self.frame_left_top, text="单价：", font=('Verdana', 15))
        self.right_top_gender_entry = Entry(self.frame_left_top, textvariable=self.var_price, font=('Verdana', 15))
        self.right_top_gender_label.grid(row=6, column=0)  # 位置设置
        self.right_top_gender_entry.grid(row=6, column=1)

        # 定义右上方区域
        # self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 15))
        self.tree.bind('<Button-1>', self.click)  # 左键获取位置(tree.bind可以绑定一系列的事件，可以搜索ttk相关参数查看)
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建商品信息',
                                            width=20, command=self.new_row, padding=5)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中商品信息',
                                            width=20, command=self.update_row, padding=5)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中商品信息',
                                            width=20, command=self.del_row, padding=5)
        self.right_top_button3.bind_all('<Delete>', self.eventhandler)
        self.edit = StringVar()
        self.right_title = Label(self.frame_right_top, text="售出数量：", font=('Verdana', 15))
        self.right_entry = Entry(self.frame_right_top, textvariable=self.edit, font=('Verdana', 10))
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='修改商品库存',
                                            width=20, command=self.edit_num, padding=5)

        # 定义下方区域，查询功能块
        self.search = StringVar()
        self.right_bottom_gender_entry = Entry(self.frame_bottom, textvariable=self.search, font=('Verdana', 15))
        self.right_bottom_button = ttk.Button(self.frame_bottom, text='商品名称查询', width=20, command=self.put_data)
        self.right_bottom_button.grid(row=0, column=1, padx=20, pady=20)  # 位置设置
        self.right_bottom_gender_entry.grid(row=0, column=0, padx=20, pady=20)

        self.right_bottom_button1 = ttk.Button(self.frame_bottom, text='清除查询结果', width=20, command=self.clean_search)
        self.right_bottom_button1.grid(row=0, column=2, padx=20, pady=20)

        # 右上角按钮的位置设置
        self.right_top_button1.grid(row=2, column=0, padx=5, pady=5)
        self.right_top_button2.grid(row=3, column=0, padx=5, pady=5)
        self.right_top_button3.grid(row=4, column=0, padx=5, pady=5)
        self.right_top_button3.bind_all('Delete', self.del_row)
        self.right_title.grid(row=5, column=0, pady=5)
        self.right_entry.grid(row=6, column=0, padx=5, pady=5)
        self.right_top_button4.grid(row=7, column=0, padx=5, pady=5)

        # 整体区域定位，利用了Frame和grid进行布局
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=30)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        # 设置固定组件，(0)就是将组件进行了固定
        self.frame_left_top.grid_propagate(False)
        self.frame_right_top.grid_propagate(False)
        self.frame_center.grid_propagate(False)
        self.frame_bottom.grid_propagate(False)

        self.frame_left_top.tkraise()  # 开始显示主菜单，tkraise()提高z轴的顺序（不太懂）
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击，执行back方法
        self.window.mainloop()  # 进入消息循环

    def clean_search(self):
        self.search.set('')
        self.put_data()

    # 将查到的信息放到中间的表格中
    def put_data(self):
        self.del_button()  # 先将表格内的内容全部清空
        # 打开数据库连接，准备查找指定的信息
        conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
        d = self.search.get()
        e = conn.cursor().execute("SELECT * FROM COMPANY WHERE name like '%" + d + "%'")
        results = e.fetchall()
        self.id = []
        self.name = []
        self.gender = []
        self.age = []
        self.unit = []
        self.price = []
        # 向表格中插入数据
        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.gender.append(row[2])
            self.age.append(row[3])
            self.unit.append(row[4])
            self.price.append(row[5])

        print("进行数据的插入")
        for i in range(min(len(self.id), len(self.name), len(self.gender),
                           len(self.age), len(self.unit), len(self.price))):  # 写入数据
            self.tree.insert('', i, values=(self.id[i], self.name[i], self.gender[i],
                                            self.age[i], self.unit[i], self.price[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

    # 清空表格中的所有信息
    def del_button(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

    # 在表格上的点击事件，这里是作用就是一点击表格就可以将信息直接写到左上角的框框中
    def click(self, event):
        if not self.tree.identify_row(event.y):
            return
        self.row = self.tree.identify_row(event.y)  # 行
        self.row_info = self.tree.item(self.row, "values")
        print(self.row_info)
        self.var_id.set(self.row_info[0])
        self.id1 = self.var_id.get()
        self.var_name.set(self.row_info[1])
        self.var_gender.set(self.row_info[2])
        self.var_age.set(self.row_info[3])
        self.var_unit.set(self.row_info[4])
        self.var_price.set(self.row_info[5])
        self.right_top_id_entry = Entry(self.frame_left_top, state='disabled', textvariable=self.var_id,
                                        font=('Verdana', 15))

    # 点击中间的表格的表头，可以将那一列进行排序
    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        m = [(tv.set(k, col), k) for k in tv.get_children('')]
        m.sort(reverse=reverse)  # 排序方式
        for index, (val, k) in enumerate(m):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, text=col, command=lambda _col=col: self.tree_sort_column(tv, _col, not reverse))

    def new_row(self):
        if self.var_id.get() == '' or self.var_name.get() == '' or self.var_gender.get() == '' \
                or self.var_age.get() == '' or self.var_name.get() == '' or self.var_gender.get() == '':
            messagebox.showinfo('警告！', '请填写商品信息')
        else:
            if str(self.var_id.get()) in self.id:
                messagebox.showinfo('警告！', '该商品已存在！')
            else:
                # 打开数据库连接
                conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
                c = conn.cursor()
                sql = "INSERT INTO COMPANY (ID,NAME,GENDER,AGE,UNIT,PRICE) \
                           VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
                      (self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                       self.var_age.get(), self.var_unit.get(), self.var_price.get())
                try:
                    sqlerror = "0"
                    c.execute(sql)  # 执行sql语句
                    conn.commit()  # 提交到数据库执行
                except sqlite3.IntegrityError:
                    sqlerror = "1"
                    messagebox.showinfo('警告！', '该商品id已存在！')
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    sqlerror = "1"
                    conn.rollback()
                    messagebox.showinfo('警告！', '插入失败，数据库写入操作失败！')
                conn.close()
                if sqlerror == "0":
                    self.id.append(self.var_id.get())
                    self.name.append(self.var_name.get())
                    self.gender.append(self.var_gender.get())
                    self.age.append(self.var_age.get())
                    self.unit.append(self.var_unit.get())
                    self.price.append(self.var_price.get())
                    self.tree.insert('', len(self.id) - 1, values=(
                        self.id[len(self.id) - 1], self.name[len(self.id) - 1], self.gender[len(self.id) - 1],
                        self.age[len(self.id) - 1], self.unit[len(self.id) - 1], self.price[len(self.id) - 1]))
                    self.tree.update()
                    messagebox.showinfo('提示！', '插入成功！')

    def update_row(self):
        if self.var_id.get() == '':
            messagebox.showinfo('警告！', '请点击要更新的项目！')
        else:
            if self.var_id.get() == '' or self.var_name.get() == '' or self.var_gender.get() == '' \
                    or self.var_age.get() == '' or self.var_name.get() == '' or self.var_gender.get() == '':
                messagebox.showinfo('警告！', '请填写商品信息')
            else:
                res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
                if res:
                    # 打开数据库连接
                    conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
                    c = conn.cursor()
                    sql = "UPDATE COMPANY set ID = '%s', NAME = '%s', GENDER = '%s', AGE='%s' ," \
                          " UNIT = '%s', PRICE='%s' where ID='%s'" % \
                          (self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                           self.var_age.get(), self.var_unit.get(), self.var_price.get(), self.id1)
                    try:
                        sqlerror = "0"
                        c.execute(sql)
                        conn.commit()
                    except sqlite3.IntegrityError:
                        sqlerror = "1"
                        messagebox.showinfo('警告！', '该商品id已存在！')
                    except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                        sqlerror = "1"
                        conn.rollback()
                        messagebox.showinfo('警告！', '更新失败，数据库写入操作失败！')
                    conn.close()
                    if sqlerror == "0":
                        self.tree.item(self.tree.selection()[0], values=(
                            self.var_id.get(), self.var_name.get(), self.var_gender.get(),
                            self.var_age.get(), self.var_unit.get(), self.var_price.get()))

    def eventhandler(self, event):
        if event.keysym == 'Delete':
            self.del_row()

    # 删除行
    def del_row(self):
        if self.var_id.get() == '':
            messagebox.showinfo('警告！', '请点击要删除的项目！')
        else:
            res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
            if res:
                # 打开数据库连接
                conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
                c = conn.cursor()
                sql = "DELETE from COMPANY where ID='%s'" % (self.row_info[0])
                try:
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    messagebox.showinfo('警告！', '删除失败，数据库删除操作失败！')
                else:
                    conn.close()
                    self.tree.delete(self.tree.selection()[0])  # 删除所选行
                    self.clean_info()
                    messagebox.showinfo('提示！', '删除成功！')

    def clean_info(self):
        self.var_id.set('')
        self.var_name.set('')
        self.var_gender.set('')
        self.var_age.set('')
        self.var_unit.set('')
        self.var_price.set('')

    def clean_input(self):
        self.edit.set('')

    def edit_num(self):
        try:
            self.row_info = self.tree.item(self.row, "values")
        except AttributeError:
            messagebox.showinfo('警告！', '请选择要修改的项目')
            return FALSE
        self.id1 = self.var_id.get()
        d = self.edit.get()
        m = self.row_info[2]
        try:
            d1 = int(d)
        except ValueError:
            messagebox.showinfo('警告！', '请输入纯数字')
            self.clean_input()
            return FALSE
        m1 = int(m)
        print(type(d1))
        if d1 <= 0:
            messagebox.showinfo('警告！', '请输入大于0的数')
            self.clean_input()
            return FALSE
        k = m1 - d1
        if k >= 0:
            res = messagebox.askyesnocancel('警告！', '是否更新余货量？')
            if res:
                # 打开数据库连接
                conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
                c = conn.cursor()
                sql = "UPDATE COMPANY set GENDER = '%s' where ID='%s'" % \
                      (k, self.id1)
                try:
                    sqlerror = "0"
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    sqlerror = "1"
                    conn.rollback()
                    messagebox.showinfo('警告！', '更新失败，数据库写入操作失败！')
                conn.close()
                if sqlerror == "0":
                    self.tree.item(self.tree.selection()[0], values=(
                        self.var_id.get(), self.var_name.get(), k,
                        self.var_age.get(), self.var_unit.get(), self.var_price.get()))
                    k1 = str(k)
                    self.var_gender.set(k1)
                    messagebox.showinfo('提示！', '更新成功！')
        else:
            messagebox.showinfo('警告！', '更新失败，余货量不能为负数！')
        self.clean_input()

    def read_excel(self):
        # 打开文件
        td = threading.Thread(target=open_window)
        td.Daemon = True
        td.start()
        path = filedialog.askopenfilename()
        if not path:
            return
        workbook = openpyxl.load_workbook(path)
        m = workbook.active
        column = m.max_column
        row = m.max_row
        values = []
        conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
        c = conn.cursor()
        try:
            for i in range(2, (row + 1)):
                for j in range(1, (column + 1)):
                    values.append(m.cell(row=i, column=j).value)
                sql = "INSERT INTO COMPANY (ID,NAME,GENDER,AGE,UNIT,PRICE) \
                                        VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
                      (values[0], values[1], values[2], values[3], values[4], values[5])
                c.execute(sql)  # 执行sql语句
                del values[:]
        except sqlite3.IntegrityError:
            messagebox.showinfo('警告！', '导入失败，请检查商品id是否重复！')
        else:
            conn.commit()
            messagebox.showinfo('提示！', '导入成功！')
            self.clean_search()

    def save_excel(self):
        # 打开文件
        td = threading.Thread(target=open_window)
        td.Daemon = True
        td.start()
        path = filedialog.asksaveasfilename(title=u'保存文件', initialfile='导出表单.xlsx',
                                            filetypes=(("Excel files", "*.xlsx"),))
        if not path:
            return
        str1 = path.split(sep=".", maxsplit=-1)
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Sheet 1"
        conn = sqlite3.connect(os.path.expanduser("~/sql/list.db"))
        c = conn.cursor()
        cursor = c.execute("SELECT *  from COMPANY")
        cursor.execute("SELECT * FROM COMPANY WHERE name like '%'")
        results = cursor.fetchall()
        self.id1 = []
        self.name = []
        self.gender = []
        self.age = []
        self.unit = []
        self.price = []
        # 向表格中插入数据
        for row in results:
            self.id1.append(row[0])
            self.name.append(row[1])
            self.gender.append(row[2])
            self.age.append(row[3])
            self.unit.append(row[4])
            self.price.append(row[5])
        n = 0
        title = ['商品id', '名称', '余货量', '型号', '单位', '单价']
        ws.append(title)
        for var in [self.id1, self.name, self.gender, self.age, self.unit, self.price]:
            m = var[:]
            n = n + 1
            for i in range(len(m)):
                ws.cell(i + 2, n).value = m[i]
        try:
            wb.save(str1[0] + '.xlsx')
        except PermissionError:
            messagebox.showinfo('警告！', '导出失败，请检查文件是否被占用！')
        else:
            messagebox.showinfo('提示！', '导出成功！')

    def back(self):
        self.window.destroy()  # 进入管理员子菜单操作界面


if __name__ == '__main__':
    # 实例化Application
    window = tk.Tk()
    AdminPage(window)
