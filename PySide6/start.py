import datetime
import os
import shutil
import sqlite3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QGuiApplication
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Side, Border, colors, Font

from need.mainwindow import *

desktop_path = os.path.join(os.path.expanduser('~'), "Desktop")
sql_dir = os.path.join(os.path.expanduser('~'), "sql")
sql_file = os.path.join(os.path.expanduser(sql_dir), "list.db")
backup_dir = os.path.join(os.path.expanduser(sql_dir), "backup")

border_set = Border(left=Side(style='thin', color=colors.BLACK),
                    right=Side(style='thin', color=colors.BLACK),
                    top=Side(style='thin', color=colors.BLACK),
                    bottom=Side(style='thin', color=colors.BLACK))


def backup():
    is_backup_dir = os.path.exists(backup_dir)
    if not is_backup_dir:
        os.makedirs(backup_dir)
    i = datetime.datetime.now()
    date1 = "%s-%s-%s" % (i.year, i.month, i.day)
    ppdir = backup_dir + '/' + date1
    isdir = os.path.exists(ppdir)
    if not isdir:
        os.makedirs(ppdir)
        shutil.copyfile(sql_file, ppdir + '/' + 'list.db')


def check_sql():
    isdir = os.path.exists(sql_dir)
    if not isdir:
        os.makedirs(sql_dir)
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        c.execute('''CREATE TABLE COMPANY
            (ID            INT     NOT NULL,
               NAME           TEXT    DEFAULT NULL,
               REMINDER       INT     DEFAULT NULL,
               MODEL          TEXT    DEFAULT NULL,
               UNIT           TEXT    DEFAULT NULL,
               COST           INT     DEFAULT NULL,
               PRICE          INT     DEFAULT NULL,
               PRIMARY KEY (`ID`));''')
        conn.commit()
        c.execute('''CREATE TABLE SALE
                (DATE             TEXT    NOT NULL,
                   ID             INT     NOT NULL,
                   NAME           TEXT    DEFAULT NULL,
                   MODEL          TEXT    DEFAULT NULL,
                   UNIT           TEXT    DEFAULT NULL,
                   COST           INT     DEFAULT NULL,
                   PRICE          INT     DEFAULT NULL,
                   NUM            INT     DEFAULT NULL,
                   COST_SUM       INT     DEFAULT NULL,
                   SUM            INT     DEFAULT NULL,
                   GET            INT     DEFAULT NULL);''')
        conn.commit()
        c.execute('''CREATE TABLE SELL
                        (ID             INT     NOT NULL,
                           NAME           TEXT    DEFAULT NULL,
                           MODEL          TEXT    DEFAULT NULL,
                           UNIT           TEXT    DEFAULT NULL,
                           NUM            INT     DEFAULT NULL,
                           PRICE          INT     DEFAULT NULL,
                           SUM            INT     DEFAULT NULL,
                           PRIMARY KEY (`ID`));''')
        conn.commit()
        c.execute('''CREATE TABLE GOODS
                  (DATE           TEXT    NOT NULL,
                   ID             INT     NOT NULL,
                   NAME           TEXT    DEFAULT NULL,
                   MODEL          TEXT    DEFAULT NULL,
                   UNIT           TEXT    DEFAULT NULL,
                   COST           INT     DEFAULT NULL,
                   NUM            INT     DEFAULT NULL,
                   COST_SUM       INT     DEFAULT NULL);''')
        conn.commit()
        c.execute('''CREATE TABLE INFO
                          (NAME           TEXT    NOT NULL,
                           LOCALE         TEXT    NOT NULL,
                           NUMBER         TEXT    NOT NULL);''')
        conn.commit()
        c.execute("INSERT INTO INFO (NAME,LOCALE,NUMBER) VALUES ('', '', '')")
        conn.commit()
        conn.close()


class FirstWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FirstWindow, self).__init__()
        self.setupUi(self)
        check_sql()
        backup()
        self.date = []
        self.id = []
        self.name = []
        self.reminder = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        self.num = []
        self.cost_sum = []
        self.sum = []
        self.get = []
        self.row1 = None
        self.col1 = None
        self.all_rows = None

        self.put_goods_data()
        self.put_sale_data()
        self.put_stock_data()
        self.put_prepare_goods_data()
        self.put_sell_out_data()
        self.put_setting_data()

        self.table_goods.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table_goods.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_goods.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_goods.cellPressed.connect(self.get_click)
        self.table_goods.verticalHeader().setVisible(False)

        self.table_new_goods.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.table_sale.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table_sale.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sale.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sale.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sale.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sale.horizontalHeader().setSectionResizeMode(7, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sale.verticalHeader().setVisible(False)
        self.table_sale.cellPressed.connect(self.get_sale_click)

        self.table_stock.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table_stock.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_stock.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_stock.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_stock.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_stock.horizontalHeader().setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_stock.verticalHeader().setVisible(False)
        self.table_stock.cellPressed.connect(self.get_stock_click)

        self.table_prepare_goods.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table_prepare_goods.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_prepare_goods.horizontalHeader().setSectionResizeMode(
            4, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_prepare_goods.cellPressed.connect(self.get_prepare_goods_click)
        self.table_prepare_goods.verticalHeader().setVisible(False)

        self.table_sell_out.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.table_sell_out.horizontalHeader().setSectionResizeMode(0,
                                                                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sell_out.horizontalHeader().setSectionResizeMode(4,
                                                                    QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
        self.table_sell_out.cellPressed.connect(self.get_sell_out_click)
        self.table_sell_out.verticalHeader().setVisible(False)

        self.btn_new_goods_1.clicked.connect(lambda: self.table_new_goods.insertRow(self.table_new_goods.rowCount()))
        self.btn_new_goods_2.clicked.connect(
            lambda: self.table_new_goods.removeRow(self.table_new_goods.rowCount() - 1))
        self.btn_new_goods_3.clicked.connect(self.merge_new_goods_table)

        self.btn_goods_1.clicked.connect(lambda: self.search_goods_by('name'))
        self.btn_goods_2.clicked.connect(lambda: self.search_goods_by('id'))
        self.btn_goods_3.clicked.connect(self.clean_goods_search)
        self.btn_goods_4.clicked.connect(self.del_goods_row)
        self.btn_goods_5.clicked.connect(self.update_goods_reminder)

        self.btn_sale_1.clicked.connect(lambda: self.search_sale_by('name'))
        self.btn_sale_2.clicked.connect(lambda: self.search_sale_by('date'))
        self.btn_sale_3.clicked.connect(self.clean_sale_search)
        self.btn_sale_4.clicked.connect(self.sale_rollback)
        self.btn_sale_5.clicked.connect(self.del_sale_row)

        self.btn_stock_1.clicked.connect(lambda: self.search_stock_by('name'))
        self.btn_stock_2.clicked.connect(lambda: self.search_stock_by('date'))
        self.btn_stock_3.clicked.connect(self.clean_stock_search)
        self.btn_stock_4.clicked.connect(self.del_stock_row)

        self.btn_sell_1.clicked.connect(self.sell_goods)
        self.btn_sell_2.clicked.connect(self.del_sell_out_row)
        self.btn_sell_3.clicked.connect(self.sell_out)
        self.btn_sell_4.clicked.connect(lambda: self.search_prepare_goods_by('name'))
        self.btn_sell_5.clicked.connect(lambda: self.search_prepare_goods_by('id'))
        self.btn_sell_6.clicked.connect(self.clean_prepare_goods_search)

        self.btn_settings_1.clicked.connect(self.settings)

        self.action.triggered.connect(self.excel_template)
        self.action_Excel.triggered.connect(self.read_excel)
        self.action_Excel_2.triggered.connect(self.save_excel)
        self.action_Excel_3.triggered.connect(self.save_sellout_excel_by_time)
        self.action_Excel_4.triggered.connect(self.save_sellout_excel)

    def merge_new_goods_table(self):
        row = self.table_new_goods.rowCount()
        if row == 0:
            return
        value = []
        error_flag = 0
        merge_flag = 0
        err = []
        values = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        for i in range(row):
            for m in range(7):
                try:
                    value.append(self.table_new_goods.item(i, m).text())
                except AttributeError:
                    error_flag = 1
                    break
            if value.count('') == 0 and value and len(value) == 7:
                sql = "INSERT INTO COMPANY (ID,NAME,REMINDER,MODEL,UNIT,COST,PRICE) \
                                           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                      (value[0], value[1], value[2], value[3], value[4], value[5], value[6])
                try:
                    c.execute(sql)
                    conn.commit()
                except sqlite3.IntegrityError:
                    err.append('id_err')
                    error_flag = 1
                else:
                    merge_flag = 1
                    values.append(i)
            else:
                err.append('value_err')
            value = []
        conn.close()
        self.clean_goods_search()
        self.clean_prepare_goods_search()
        for i in reversed(values):
            self.table_new_goods.removeRow(i)
        k = 0
        for i in err:
            k = k + 1
            if i == 'id_err':
                QtWidgets.QMessageBox.warning(self, '警告！', '合并失败，第 ' + str(k) + ' 行商品id冲突！')
            else:
                QtWidgets.QMessageBox.warning(self, '警告！', '合并失败，第 ' + str(k) + ' 行信息有错误！')
        if merge_flag == 1 and error_flag == 1:
            QtWidgets.QMessageBox.information(self, '提示！', '正确的数据合并成功！')
        elif merge_flag == 1 and error_flag == 0:
            QtWidgets.QMessageBox.information(self, '提示！', '合并成功！')

    def get_click(self, row, col):
        self.table_goods.item(row, col).text()
        self.row1 = row

    def click(self, q):
        pp = self.table_goods.item(self.table_goods.currentRow(), q).text()
        return pp

    def del_goods_row(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '提示！', '请点击要删除的项目！')
        else:
            reply = QtWidgets.QMessageBox.question(self, '警告', '是否删除所选数据？')
            if reply == QMessageBox.Yes:
                del_id = self.click(0)
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                sql = "DELETE from COMPANY where ID='%s'" % del_id
                try:
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '提示', '删除失败，数据库删除操作失败！')
                else:
                    conn.close()
                    self.table_goods.removeRow(self.table_goods.currentRow())
                    QtWidgets.QMessageBox.information(self, '提示', '删除成功！')
            self.row1 = None

    def update_goods_reminder(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '警告！', '请点击要更新的项目！')
        else:
            self.id = self.click(0)
            self.name = self.click(1)
            self.reminder = self.click(2)
            self.model = self.click(3)
            self.unit = self.click(4)
            self.cost = self.click(5)
            self.price = self.click(6)
            num, ok = QtWidgets.QInputDialog.getInt(self, '输入框', '输入数字')
            if ok is False:
                self.row1 = None
                return
            elif ok is True and num <= 0:
                QtWidgets.QMessageBox.information(self, '提示！', '请输入一个大于 0 的数！')
            else:
                self.sum = num + int(self.reminder)
                self.cost_sum = num * int(self.cost)
                self.num = num
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                sql = "UPDATE COMPANY set REMINDER = '%s' where ID='%s'" % \
                      (self.sum, self.click(0))
                try:
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，数据库写入操作失败！')
                else:
                    self.table_goods.item(int(self.row1), 2).setText(str(self.sum))
                i = datetime.datetime.now()
                date1 = "%s/%s/%s %s:%s:%s" % (i.year, i.month, i.day, i.hour, i.minute, i.second)
                sql1 = "INSERT INTO GOODS (DATE,ID,NAME,MODEL,UNIT,COST,NUM,COST_SUM) \
                       VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                       (date1, self.id, self.name, self.model, self.unit,
                        self.cost, self.num, self.cost_sum)
                try:
                    c.execute(sql1)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，数据库写入操作失败！')
                conn.close()
                self.clean_prepare_goods_search()
                self.clean_stock_search()
                QtWidgets.QMessageBox.information(self, '提示！', '更新成功！')
                self.row1 = None

    def clean_goods_search(self):
        self.text_1.clear()
        self.search_goods_by('name')

    def search_goods_by(self, var):
        self.row1 = None
        self.id = []
        self.name = []
        self.reminder = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        if var == 'date':
            d = self.text_1.text().replace('.', '/')
        else:
            d = self.text_1.text()
        if not d:
            m = self.table_goods.rowCount()
            for i in range(m):
                self.table_goods.removeRow(0)
            self.put_goods_data()
        else:
            results = c.execute("SELECT * FROM COMPANY WHERE " + var + " like '%" + d + "%'").fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.reminder.append(row[2])
                self.model.append(row[3])
                self.unit.append(row[4])
                self.cost.append(row[5])
                self.price.append(row[6])
            rows = min(len(self.id), len(self.name), len(self.reminder), len(self.model), len(self.unit),
                       len(self.cost),
                       len(self.price))
            m = self.table_goods.rowCount()
            for i in range(m):
                self.table_goods.removeRow(0)
            self.table_goods.setRowCount(rows)
            for i in range(rows):
                for m in range(7):
                    value = [self.id[i], self.name[i], self.reminder[i], self.model[i], self.unit[i], self.cost[i],
                             self.price[i]]
                    item = QtWidgets.QTableWidgetItem()
                    self.table_goods.setItem(i, m, item)
                    item_add = self.table_goods.item(i, m)
                    item_add.setText(str(value[m]))
                    item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def put_goods_data(self):
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("select * from COMPANY order by id")
        results = cursor.fetchall()
        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.reminder.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.cost.append(row[5])
            self.price.append(row[6])
        conn.close()
        rows = min(len(self.id), len(self.name), len(self.reminder), len(self.model), len(self.unit), len(self.cost),
                   len(self.price))
        self.all_rows = rows
        self.table_goods.setRowCount(rows)
        for row in range(rows):
            item = QtWidgets.QTableWidgetItem()
            self.table_goods.setVerticalHeaderItem(row, item)
            item = self.table_goods.verticalHeaderItem(row)
            item.setText('')
        for i in range(rows):
            for m in range(7):
                value = [self.id[i], self.name[i], self.reminder[i], self.model[i], self.unit[i], self.cost[i],
                         self.price[i]]
                item = QtWidgets.QTableWidgetItem()
                self.table_goods.setItem(i, m, item)
                item_add = self.table_goods.item(i, m)
                item_add.setText(str(value[m]))
                item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def put_sale_data(self):
        self.date = []
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        self.num = []
        self.cost_sum = []
        self.sum = []
        self.get = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("SELECT *  from SALE")
        results = cursor.fetchall()
        for row in results:
            self.date.append(row[0])
            self.id.append(row[1])
            self.name.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.cost.append(row[5])
            self.price.append(row[6])
            self.num.append(row[7])
            self.cost_sum.append(row[8])
            self.sum.append(row[9])
            self.get.append(row[10])
        conn.close()
        rows = min(len(self.date), len(self.id), len(self.name), len(self.model),
                   len(self.unit), len(self.cost), len(self.price), len(self.num), len(self.cost_sum),
                   len(self.sum), len(self.get))
        self.all_rows = rows
        self.table_sale.setRowCount(rows)
        for row in range(rows):
            item = QtWidgets.QTableWidgetItem()
            self.table_sale.setVerticalHeaderItem(row, item)
            item = self.table_sale.verticalHeaderItem(row)
            item.setText('')
        for i in range(rows):
            for m in range(11):
                value = [self.date[i], self.id[i], self.name[i], self.model[i], self.unit[i], self.cost[i],
                         self.price[i], self.num[i], self.cost_sum[i], self.sum[i], self.get[i]]
                item = QtWidgets.QTableWidgetItem()
                self.table_sale.setItem(i, m, item)
                item_add = self.table_sale.item(i, m)
                item_add.setText(str(value[m]))
                item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def clean_sale_search(self):
        self.text_sale_1.clear()
        self.search_sale_by('name')

    def search_sale_by(self, var):
        self.row1 = None
        self.date = []
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        self.num = []
        self.cost_sum = []
        self.sum = []
        self.get = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        if var == 'date':
            d = self.text_sale_1.text().replace('.', '/')
        else:
            d = self.text_sale_1.text()
        if not d:
            m = self.table_sale.rowCount()
            for i in range(m):
                self.table_sale.removeRow(0)
            self.put_sale_data()
        else:
            results = c.execute("SELECT * FROM SALE WHERE " + var + " like '%" + d + "%'").fetchall()
            for row in results:
                self.date.append(row[0])
                self.id.append(row[1])
                self.name.append(row[2])
                self.model.append(row[3])
                self.unit.append(row[4])
                self.cost.append(row[5])
                self.price.append(row[6])
                self.num.append(row[7])
                self.cost_sum.append(row[8])
                self.sum.append(row[9])
                self.get.append(row[10])
            rows = min(len(self.date), len(self.id), len(self.name), len(self.model),
                       len(self.unit), len(self.cost), len(self.price), len(self.num), len(self.cost_sum),
                       len(self.sum), len(self.get))
            m = self.table_sale.rowCount()
            for i in range(m):
                self.table_sale.removeRow(0)
            self.table_sale.setRowCount(rows)
            for i in range(rows):
                for m in range(11):
                    value = [self.date[i], self.id[i], self.name[i], self.model[i],
                             self.unit[i], self.cost[i], self.price[i], self.num[i], self.cost_sum[i],
                             self.sum[i], self.get[i]]
                    item = QtWidgets.QTableWidgetItem()
                    self.table_sale.setItem(i, m, item)
                    item_add = self.table_sale.item(i, m)
                    item_add.setText(str(value[m]))
                    item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def get_sale_click(self, row, col):
        self.table_sale.item(row, col).text()
        self.row1 = row

    def sale_click(self, q):
        pp = self.table_sale.item(self.table_sale.currentRow(), q).text()
        return pp

    def del_sale_row(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '提示！', '请点击要删除的项目！')
        else:
            reply = QtWidgets.QMessageBox.question(self, '警告', '是否删除所选数据？')
            if reply == QMessageBox.Yes:
                del_date = self.sale_click(0)
                del_id = self.sale_click(1)
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                sql = "DELETE from SALE where DATE='%s' and ID='%s'" % (del_date, del_id)
                try:
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '提示', '删除失败，数据库删除操作失败！')
                else:
                    conn.close()
                    self.table_sale.removeRow(self.table_sale.currentRow())
                    QtWidgets.QMessageBox.information(self, '提示', '删除成功！')
            self.row1 = None

    def sale_rollback(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '提示！', '请点击要退货的项目！')
        else:
            num, ok = QtWidgets.QInputDialog.getInt(self, '退货数量', '输入数字')
            if ok is False:
                self.row1 = None
                return
            elif ok is True and num <= 0:
                QtWidgets.QMessageBox.information(self, '提示！', '请输入一个大于 0 的数！')
            else:
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                e = c.execute(
                    "SELECT * FROM SALE WHERE date = '%s' and id = '%s'" % (
                        self.sale_click(0), self.sale_click(1))).fetchall()
                results = e[0]
                after_num = int(results[7]) - int(num)
                if after_num == 0:
                    sql = "DELETE from SALE where DATE='%s' and ID='%s'" % (self.sale_click(0), self.sale_click(1))
                    try:
                        c.execute(sql)
                        conn.commit()
                    except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                        conn.rollback()
                        QtWidgets.QMessageBox.warning(self, '警告！', '删除失败，数据库删除操作失败！')
                    else:
                        self.table_sale.removeRow(self.table_sale.currentRow())
                elif after_num < 0:
                    QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，退货数量不能大于售出数量！')
                    return
                else:
                    after_cost_sum = after_num * int(self.sale_click(5))
                    after_price_sum = after_num * int(self.sale_click(6))
                    after_get = after_price_sum - after_cost_sum
                    try:
                        c.execute(
                            "UPDATE SALE set NUM='%s', COST_SUM='%s',SUM='%s',GET='%s' where DATE = '%s' and ID = '%s'"
                            % (after_num, after_cost_sum, after_price_sum, after_get, self.sale_click(0),
                               self.sale_click(1)))
                        conn.commit()
                    except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                        conn.rollback()
                        QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，数据库写入操作失败！')
                    else:
                        self.table_sale.item(int(self.row1), 7).setText(str(after_num))
                        self.table_sale.item(int(self.row1), 8).setText(str(after_cost_sum))
                        self.table_sale.item(int(self.row1), 9).setText(str(after_price_sum))
                        self.table_sale.item(int(self.row1), 10).setText(str(after_get))
                try:
                    goods_reminder = c.execute(
                        "SELECT REMINDER from COMPANY  where ID='%s'" % self.sale_click(1)).fetchall()
                    goods_reminder1 = goods_reminder[0]
                    goods_reminder2 = int(goods_reminder1[0]) + int(num)
                    sql = "UPDATE COMPANY set REMINDER = '%s' where ID='%s'" % \
                          (goods_reminder2, self.sale_click(1))
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，数据库写入操作失败！')
                else:
                    self.clean_goods_search()
                    self.clean_prepare_goods_search()
                    QtWidgets.QMessageBox.information(self, '提示！', '更新成功！')
                self.row1 = None
                conn.close()

    def put_stock_data(self):
        self.date = []
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.cost = []
        self.num = []
        self.sum = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("SELECT *  from GOODS")
        results = cursor.fetchall()
        for row in results:
            self.date.append(row[0])
            self.id.append(row[1])
            self.name.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.cost.append(row[5])
            self.num.append(row[6])
            self.sum.append(row[7])
        conn.close()
        rows = min(len(self.date), len(self.id), len(self.name), len(self.model),
                   len(self.unit), len(self.cost), len(self.num), len(self.sum))
        self.all_rows = rows
        self.table_stock.setRowCount(rows)
        for row in range(rows):
            item = QtWidgets.QTableWidgetItem()
            self.table_stock.setVerticalHeaderItem(row, item)
            item = self.table_stock.verticalHeaderItem(row)
            item.setText('')
        for i in range(rows):
            for m in range(8):
                value = [self.date[i], self.id[i], self.name[i], self.model[i],
                         self.unit[i], self.cost[i], self.num[i], self.sum[i]]
                item = QtWidgets.QTableWidgetItem()
                self.table_stock.setItem(i, m, item)
                item_add = self.table_stock.item(i, m)
                item_add.setText(str(value[m]))
                item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def clean_stock_search(self):
        self.text_stock_1.clear()
        self.search_stock_by('name')

    def search_stock_by(self, var):
        self.row1 = None
        self.date = []
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.cost = []
        self.num = []
        self.sum = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        if var == 'date':
            d = self.text_stock_1.text().replace('.', '/')
        else:
            d = self.text_stock_1.text()
        if not d:
            m = self.table_stock.rowCount()
            for i in range(m):
                self.table_stock.removeRow(0)
            self.put_stock_data()
        else:
            results = c.execute("SELECT * FROM GOODS WHERE " + var + " like '%" + d + "%'").fetchall()
            for row in results:
                self.date.append(row[0])
                self.id.append(row[1])
                self.name.append(row[2])
                self.model.append(row[3])
                self.unit.append(row[4])
                self.cost.append(row[5])
                self.num.append(row[6])
                self.sum.append(row[7])
            rows = min(len(self.date), len(self.id), len(self.name), len(self.model),
                       len(self.unit), len(self.cost), len(self.num), len(self.sum))
            m = self.table_stock.rowCount()
            for i in range(m):
                self.table_stock.removeRow(0)
            self.table_stock.setRowCount(rows)
            for i in range(rows):
                for m in range(8):
                    value = [self.date[i], self.id[i], self.name[i], self.model[i],
                             self.unit[i], self.cost[i], self.num[i], self.sum[i]]
                    item = QtWidgets.QTableWidgetItem()
                    self.table_stock.setItem(i, m, item)
                    item_add = self.table_stock.item(i, m)
                    item_add.setText(str(value[m]))
                    item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def get_stock_click(self, row, col):
        self.table_stock.item(row, col).text()
        self.row1 = row

    def stock_click(self, q):
        pp = self.table_stock.item(self.table_stock.currentRow(), q).text()
        return pp

    def del_stock_row(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '提示！', '请点击要删除的项目！')
        else:
            reply = QtWidgets.QMessageBox.question(self, '警告', '是否删除所选数据？')
            if reply == QMessageBox.Yes:
                del_date = self.stock_click(0)
                del_id = self.stock_click(1)
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                sql = "DELETE from GOODS where DATE='%s' and ID='%s'" % (del_date, del_id)
                try:
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '提示', '删除失败，数据库删除操作失败！')
                else:
                    conn.close()
                    self.table_stock.removeRow(self.table_stock.currentRow())
                    QtWidgets.QMessageBox.information(self, '提示', '删除成功！')
            self.row1 = None

    def put_prepare_goods_data(self):
        self.id = []
        self.name = []
        self.reminder = []
        self.model = []
        self.unit = []
        self.price = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("select * from COMPANY order by id")
        results = cursor.fetchall()
        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.reminder.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.price.append(row[6])
        conn.close()
        rows = min(len(self.id), len(self.name), len(self.reminder), len(self.model), len(self.unit), len(self.price))
        self.all_rows = rows
        self.table_prepare_goods.setRowCount(rows)
        for row in range(rows):
            item = QtWidgets.QTableWidgetItem()
            self.table_prepare_goods.setVerticalHeaderItem(row, item)
            item = self.table_prepare_goods.verticalHeaderItem(row)
            item.setText('')
        for i in range(rows):
            for m in range(6):
                value = [self.id[i], self.name[i], self.reminder[i], self.model[i], self.unit[i], self.price[i]]
                item = QtWidgets.QTableWidgetItem()
                self.table_prepare_goods.setItem(i, m, item)
                item_add = self.table_prepare_goods.item(i, m)
                item_add.setText(str(value[m]))
                item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def clean_prepare_goods_search(self):
        self.text_sell.clear()
        self.search_prepare_goods_by('name')

    def search_prepare_goods_by(self, var):
        self.row1 = None
        self.id = []
        self.name = []
        self.reminder = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        if var == 'date':
            d = self.text_sell.text().replace('.', '/')
        else:
            d = self.text_sell.text()
        if not d:
            m = self.table_prepare_goods.rowCount()
            for i in range(m):
                self.table_prepare_goods.removeRow(0)
            self.put_prepare_goods_data()
        else:
            results = c.execute("SELECT * FROM COMPANY WHERE " + var + " like '%" + d + "%'").fetchall()
            for row in results:
                self.id.append(row[0])
                self.name.append(row[1])
                self.reminder.append(row[2])
                self.model.append(row[3])
                self.unit.append(row[4])
                self.price.append(row[6])
            rows = min(len(self.id), len(self.name), len(self.reminder),
                       len(self.model), len(self.unit), len(self.price))
            m = self.table_prepare_goods.rowCount()
            for i in range(m):
                self.table_prepare_goods.removeRow(0)
            self.table_prepare_goods.setRowCount(rows)
            for i in range(rows):
                for m in range(6):
                    value = [self.id[i], self.name[i], self.reminder[i], self.model[i], self.unit[i], self.price[i]]
                    item = QtWidgets.QTableWidgetItem()
                    self.table_prepare_goods.setItem(i, m, item)
                    item_add = self.table_prepare_goods.item(i, m)
                    item_add.setText(str(value[m]))
                    item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def get_prepare_goods_click(self, row, col):
        self.table_prepare_goods.item(row, col).text()
        self.row1 = row

    def prepare_goods_click(self, q):
        pp = self.table_prepare_goods.item(self.table_prepare_goods.currentRow(), q).text()
        return pp

    def sell_goods(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '警告！', '请点击要更新的项目！')
        else:
            self.id = self.prepare_goods_click(0)
            self.name = self.prepare_goods_click(1)
            self.reminder = self.prepare_goods_click(2)
            self.model = self.prepare_goods_click(3)
            self.unit = self.prepare_goods_click(4)
            self.price = self.prepare_goods_click(5)
            ok = bool()
            num, ok = QtWidgets.QInputDialog.getInt(self, '输入框', '输入数字', ok)
            if ok is False:
                self.row1 = None
                return
            elif ok is True and num <= 0:
                QtWidgets.QMessageBox.information(self, '提示！', '请输入一个大于 0 的数！')
            else:
                after_num = int(self.reminder) - num
                self.sum = num * int(self.price)
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                sql1 = "INSERT INTO SELL (ID,NAME,MODEL,UNIT,NUM,PRICE,SUM) \
                                           VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                       (self.id, self.name, self.model, self.unit,
                        num, self.price, self.sum)
                try:
                    c.execute(sql1)
                    conn.commit()
                except sqlite3.IntegrityError:
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，请勿重复出售相同的商品！')
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，数据库写入操作失败！')
                else:
                    sql = "UPDATE COMPANY set REMINDER = '%s' where ID='%s'" % \
                          (after_num, self.prepare_goods_click(0))
                    try:
                        c.execute(sql)
                        conn.commit()
                    except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                        conn.rollback()
                        QtWidgets.QMessageBox.warning(self, '警告！', '更新失败，数据库写入操作失败！')
                    else:
                        self.table_prepare_goods.item(int(self.row1), 2).setText(str(after_num))
                        self.clean_goods_search()
                        self.put_sell_out_data()
                        conn.close()
                        QtWidgets.QMessageBox.information(self, '提示！', '更新成功！')
                self.row1 = None

    def put_sell_out_data(self):
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.num = []
        self.price = []
        self.sum = []
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        results = c.execute("SELECT * FROM SELL").fetchall()
        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.model.append(row[2])
            self.unit.append(row[3])
            self.num.append(row[4])
            self.price.append(row[5])
            self.sum.append(row[6])
        rows = min(len(self.id), len(self.name), len(self.model),
                   len(self.unit), len(self.num), len(self.price), len(self.sum))
        m = self.table_sell_out.rowCount()
        for i in range(m):
            self.table_sell_out.removeRow(0)
        self.table_sell_out.setRowCount(rows)
        for i in range(rows):
            for m in range(7):
                value = [self.id[i], self.name[i], self.model[i], self.unit[i], self.num[i], self.price[i], self.sum[i]]
                item = QtWidgets.QTableWidgetItem()
                self.table_sell_out.setItem(i, m, item)
                item_add = self.table_sell_out.item(i, m)
                item_add.setText(str(value[m]))
                item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def get_sell_out_click(self, row, col):
        self.table_sell_out.item(row, col).text()
        self.row1 = row

    def sell_out_click(self, q):
        pp = self.table_sell_out.item(self.table_sell_out.currentRow(), q).text()
        return pp

    def del_sell_out_row(self):
        if not self.row1 and self.row1 != 0:
            QtWidgets.QMessageBox.warning(self, '提示！', '请点击要删除的项目！')
        else:
            reply = QtWidgets.QMessageBox.question(self, '警告', '是否删除所选数据？')
            if reply == QMessageBox.Yes:
                del_id = self.sell_out_click(0)
                conn = sqlite3.connect(sql_file)
                c = conn.cursor()
                sql = "DELETE from SELL where ID='%s'" % del_id
                try:
                    c.execute(sql)
                    conn.commit()
                except (sqlite3.ProgrammingError, sqlite3.OperationalError):
                    conn.rollback()
                    QtWidgets.QMessageBox.warning(self, '提示', '删除失败，数据库删除操作失败！')
                else:
                    sql = "SELECT REMINDER from COMPANY where ID='%s'" % del_id
                    cursor = c.execute(sql)
                    results = cursor.fetchall()
                    m = max(results[0])
                    k = m + int(self.sell_out_click(4))
                    sql = "UPDATE COMPANY set REMINDER = '%s' where ID='%s'" % (k, del_id)
                    c.execute(sql)
                    conn.commit()
                    conn.close()
                    self.clean_goods_search()
                    self.clean_prepare_goods_search()
                    self.table_sell_out.removeRow(self.table_sell_out.currentRow())
                    QtWidgets.QMessageBox.information(self, '提示', '删除成功！')
            self.row1 = None

    def sell_out(self):
        if self.table_sell_out.rowCount() == 0:
            return
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', desktop_path + '/出货单.xlsx', "Excel (*.xlsx)")
        if ok == '':
            return
        i = datetime.datetime.now()
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet 1"
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("SELECT *  from SELL")
        results = cursor.fetchall()
        self.name = []
        self.model = []
        self.unit = []
        self.num = []
        self.price = []
        self.sum = []
        for row in results:
            self.name.append(row[1])
            self.model.append(row[2])
            self.unit.append(row[3])
            self.num.append(row[4])
            self.price.append(row[5])
            self.sum.append(row[6])
        cursor = c.execute("SELECT *  from INFO").fetchall()
        get_info = cursor[0]
        name = get_info[0]
        locale = get_info[1]
        number = get_info[2]
        if name == '' or locale == '' or number == '':
            QtWidgets.QMessageBox.information(self, '提示！', '未填写Excel信息！')
        ws.cell(1, 2).value = name
        ws.cell(1, 2).font = Font(size="16")
        ws.cell(2, 1).value = '客户：'
        ws.cell(2, 5).value = str(i.year) + '年' + str(i.month) + '月' + str(i.day) + '日'
        n = 0
        var = ['序号', '名称', '型号', '单位', '数量', '单价', '总价']
        for i in range(7):
            n = n + 1
            ws.cell(3, n).value = var[i]
            ws.cell(3, n).border = border_set
        n = 0
        for var in [self.name, self.model, self.unit, self.num, self.price, self.sum]:
            m = var[:]
            n = n + 1
            for i in range(len(m)):
                try:
                    float(m[i])
                except ValueError:
                    ws.cell(i + 4, n + 1).value = m[i]
                    ws.cell(i + 4, n + 1).border = border_set
                else:
                    ws.cell(i + 4, n + 1).value = m[i]
                    ws.cell(i + 4, n + 1).border = border_set
                    ws.cell(i + 4, n + 1).data_type = "int"
        n = 0
        for i in range(len(m)):
            n = n + 1
            ws.cell(i + 4, 1).value = n
            ws.cell(i + 4, 1).border = border_set
        mm = str(len(m) + 3)
        if int(mm) == 4:
            bbc = '=G4'
        else:
            bbc = '=SUM(G4:G' + mm + ')'
        mm = str(int(mm) + 1)
        bb = '=TEXT(SUBSTITUTE(IF(G' + mm + '="","",IF(MOD(G' + mm + ',1)=0,TEXT(INT(G' + mm + \
             '),"[DBNum2][$-804]G/通用格式元整"),(TEXT(INT(G' + mm + '),"[DBNum2][$-804]G/通用格式元")&TEXT((INT(G' + mm + \
             '*10)-INT(G' + mm + ')*10),"[DBNum2][$-804]G/通用格式角")&TEXT((INT(G' + mm + '*100)-INT(G' + mm + \
             '*10)*10),"[DBNum2][$-804]G/通用格式分")))),"零角","零"),)'
        var = [' ', '大写', bb, ' ', ' ', ' ', bbc]
        n = 0
        for i in range(7):
            n = n + 1
            ws.cell(len(m) + 4, n).value = var[i]
            ws.cell(len(m) + 4, n).border = border_set
        var = [locale, '电话', number]
        n = 0
        for i in range(3):
            n = n + 1
            ws.cell(len(m) + 6, n + 2).value = var[i]
        ws.column_dimensions['B'].width = 20.0
        ws.column_dimensions['C'].width = 20.0
        ws.merge_cells('E2:F2')
        merge_tel = 'E' + str(len(m) + 6) + ':' + 'F' + str(len(m) + 6)
        ws.merge_cells(merge_tel)
        try:
            wb.save(path)
        except PermissionError:
            QtWidgets.QMessageBox.warning(self, '警告！', '导出失败，请检查文件是否被占用！')
        else:
            self.put_sale()
            self.clean_sale()

            QtWidgets.QMessageBox.information(self, '提示！', '导出成功！')

    def put_sale(self):
        i = datetime.datetime.now()
        date1 = "%s/%s/%s %s:%s:%s" % (i.year, i.month, i.day, i.hour, i.minute, i.second)
        conn = sqlite3.connect(sql_file)
        e = conn.cursor().execute("SELECT * FROM SELL")
        result1 = e.fetchall()
        for i in range(len(result1)):
            value1 = result1[i]
            sql1 = "select * from COMPANY order by id where ID='%s'" % value1[0]
            e = conn.cursor().execute(sql1)
            result2 = e.fetchall()
            value2 = result2[0]
            cost_sum = value2[5] * value1[4]
            price = value2[6] * value1[4]
            get = price - cost_sum
            sql2 = "INSERT INTO SALE (DATE,ID,NAME,MODEL,UNIT,COST,PRICE,NUM,COST_SUM,SUM,GET) \
                                      VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                   (date1, value2[0], value2[1], value2[3], value2[4], value2[5], value2[6], value1[4], cost_sum,
                    price, get)
            try:
                conn.cursor().execute(sql2)
                conn.commit()
            except Warning:
                conn.rollback()
                conn.close()
                QtWidgets.QMessageBox.warning(self, '警告！', '数据库写入操作失败！')
            else:
                self.clean_sale_search()

    def clean_sale(self):
        m = self.table_sell_out.rowCount()
        for n in range(m):
            self.table_sell_out.removeRow(0)
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        c.execute('''DROP TABLE SELL''')
        conn.commit()
        c.execute('''CREATE TABLE SELL
                                    (ID             INT     NOT NULL,
                                       NAME           TEXT    DEFAULT NULL,
                                       MODEL          TEXT    DEFAULT NULL,
                                       UNIT           TEXT    DEFAULT NULL,
                                       NUM            INT     DEFAULT NULL,
                                       PRICE          INT     DEFAULT NULL,
                                       SUM            INT     DEFAULT NULL,
                                       PRIMARY KEY (`ID`));''')
        conn.commit()
        conn.close()

    def put_setting_data(self):
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        result = c.execute("SELECT *  from INFO").fetchall()
        info = result[0]
        name = info[0]
        locale = info[1]
        number = info[2]
        conn.close()
        self.text_settings_1.setText(name)
        self.text_settings_2.setText(locale)
        self.text_settings_3.setText(number)

    def settings(self):
        name = self.text_settings_1.text()
        locale = self.text_settings_2.text()
        number = self.text_settings_3.text()
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        sql = "UPDATE INFO set NAME = '%s',LOCALE = '%s',NUMBER = '%s'" % \
              (name, locale, number)
        try:
            c.execute(sql)
            conn.commit()
        except (sqlite3.ProgrammingError, sqlite3.OperationalError):
            conn.rollback()
            QtWidgets.QMessageBox.warning(self, '警告！', '数据库写入操作失败！')
        else:
            QtWidgets.QMessageBox.information(self, '提示！', '更新成功！')
        conn.close()

    def excel_template(self):
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', desktop_path + '/模板文件.xlsx', "Excel 文件(*.xlsx)")
        if ok == '':
            return
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet 1"
        title = ['商品id', '名称', '余货量', '型号', '单位', '成本价', '单价']
        ws.append(title)
        ws.cell(2, 1).value = 1
        ws.cell(3, 1).value = 2
        try:
            wb.save(path)
        except PermissionError:
            QtWidgets.QMessageBox.warning(self, '警告！', '导出失败，请检查文件是否被占用！')
        else:
            QtWidgets.QMessageBox.information(self, '提示！', '导出成功！')

    def read_excel(self):
        path, ok = QtWidgets.QFileDialog.getOpenFileName(self, '读取文件', desktop_path, "Excel 文件(*.xlsx)")
        if ok == '':
            return
        workbook = load_workbook(path)
        ws = workbook.active
        row = ws.max_row
        cell = []
        k = self.table_new_goods.rowCount()
        for i in range(k):
            self.table_new_goods.removeRow(0)
        self.table_new_goods.setRowCount(row - 1)
        for n in range(row - 1):
            for m in range(7):
                cell.append(ws.cell(n + 2, m + 1).value)
                item = QtWidgets.QTableWidgetItem()
                self.table_new_goods.setItem(n, m, item)
                item_add = self.table_new_goods.item(n, m)
                item_add.setText(str(cell[m]))
                item_add.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            cell = []
        self.tabWidget.setCurrentIndex(1)

    def save_excel(self):
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', desktop_path + '/商品清单.xlsx', "Excel 文件(*.xlsx)")
        if ok == '':
            return
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet 1"
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("SELECT *  from COMPANY")
        results = cursor.fetchall()
        self.id = []
        self.name = []
        self.reminder = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        for row in results:
            self.id.append(row[0])
            self.name.append(row[1])
            self.reminder.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.cost.append(row[5])
            self.price.append(row[6])
        n = 0
        title = ['商品id', '名称', '余货量', '型号', '单位', '成本价', '单价']
        ws.append(title)
        for var in [self.id, self.name, self.reminder, self.model, self.unit, self.cost, self.price]:
            m = var[:]
            n = n + 1
            for i in range(len(m)):
                ws.cell(i + 2, n).value = m[i]
        try:
            wb.save(path)
        except PermissionError:
            QtWidgets.QMessageBox.warning(self, '警告！', '导出失败，请检查文件是否被占用！')
        else:
            QtWidgets.QMessageBox.information(self, '提示！', '导出成功！')

    def save_sellout_excel_by_time(self):
        text, ok = QtWidgets.QInputDialog.getText(self, '导出记录时间', '例如：导出某一年：2022   导出某一月：2022.4   导出某一天：2022.4.1')
        if not ok:
            return
        date = text.split(sep='.', maxsplit=3)
        if len(date) == 0:
            QtWidgets.QMessageBox.warning(self, '警告！', '请输入导出记录的时间！')
            return
        elif len(date) == 1:
            d = date[0]
        elif len(date) == 2:
            d = '%s/%s' % (date[0], date[1])
        elif len(date) == 3:
            d = '%s/%s/%s' % (date[0], date[1], date[2])
        else:
            QtWidgets.QMessageBox.warning(self, '警告！', '请输入正确的时间！')
            return
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', desktop_path + '/' + text + '-销售记录.xlsx',
                                                         "Excel 文件(*.xlsx)")
        if ok == '':
            return
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet 1"
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("SELECT * FROM SALE WHERE date like '%" + d + "%'")
        results = cursor.fetchall()
        self.date = []
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        self.num = []
        self.cost_sum = []
        self.sum = []
        self.get = []
        for row in results:
            self.date.append(row[0])
            self.id.append(row[1])
            self.name.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.cost.append(row[5])
            self.price.append(row[6])
            self.num.append(row[7])
            self.cost_sum.append(row[8])
            self.sum.append(row[9])
            self.get.append(row[10])
        n = 0
        title = ['日期', '商品id', '名称', '型号', '单位', '成本价', '单价', '售出数量', '总成本价', '总销售额', '利润']
        ws.append(title)
        for var in [self.date, self.id, self.name, self.model, self.unit, self.cost, self.price, self.num,
                    self.cost_sum, self.sum, self.get]:
            m = var[:]
            n = n + 1
            for i in range(len(m)):
                ws.cell(i + 2, n).value = m[i]
        row1 = ws.max_row
        row = ws.max_row + 1
        ws.cell(row, 8).value = '合计'
        ws.cell(row, 9).value = '=SUM(I2:I' + str(row1) + ')'
        ws.cell(row, 10).value = '=SUM(J2:J' + str(row1) + ')'
        ws.cell(row, 11).value = '=SUM(K2:K' + str(row1) + ')'
        try:
            wb.save(path)
        except PermissionError:
            QtWidgets.QMessageBox.warning(self, '警告！', '导出失败，请检查文件是否被占用！')
        else:
            QtWidgets.QMessageBox.information(self, '提示！', '导出成功！')

    def save_sellout_excel(self):
        path, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存文件', desktop_path + '/销售记录.xlsx', "Excel 文件(*.xlsx)")
        if ok == '':
            return
        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet 1"
        conn = sqlite3.connect(sql_file)
        c = conn.cursor()
        cursor = c.execute("SELECT *  from SALE")
        results = cursor.fetchall()
        self.date = []
        self.id = []
        self.name = []
        self.model = []
        self.unit = []
        self.cost = []
        self.price = []
        self.num = []
        self.cost_sum = []
        self.sum = []
        self.get = []
        for row in results:
            self.date.append(row[0])
            self.id.append(row[1])
            self.name.append(row[2])
            self.model.append(row[3])
            self.unit.append(row[4])
            self.cost.append(row[5])
            self.price.append(row[6])
            self.num.append(row[7])
            self.cost_sum.append(row[8])
            self.sum.append(row[9])
            self.get.append(row[10])
        n = 0
        title = ['日期', '商品id', '名称', '型号', '单位', '成本价', '单价', '售出数量', '总成本价', '总销售额', '利润']
        ws.append(title)
        for var in [self.date, self.id, self.name, self.model, self.unit, self.cost, self.price, self.num,
                    self.cost_sum, self.sum, self.get]:
            m = var[:]
            n = n + 1
            for i in range(len(m)):
                ws.cell(i + 2, n).value = m[i]
        row1 = ws.max_row
        row = ws.max_row + 1
        ws.cell(row, 8).value = '合计'
        ws.cell(row, 9).value = '=SUM(I2:I' + str(row1) + ')'
        ws.cell(row, 10).value = '=SUM(J2:J' + str(row1) + ')'
        ws.cell(row, 11).value = '=SUM(K2:K' + str(row1) + ')'
        try:
            wb.save(path)
        except PermissionError:
            QtWidgets.QMessageBox.warning(self, '警告！', '导出失败，请检查文件是否被占用！')
        else:
            QtWidgets.QMessageBox.information(self, '提示！', '导出成功！')


if __name__ == "__main__":
    import sys

    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.Floor)
    app = QtWidgets.QApplication(sys.argv)
    w = FirstWindow()
    w.show()
    sys.exit(app.exec())
