# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QAction, QFont, QIcon)
from PySide6.QtWidgets import (QAbstractItemView, QCheckBox, QComboBox,
                               QFrame, QGridLayout, QGroupBox, QHBoxLayout,
                               QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSizePolicy,
                               QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 865)
        MainWindow.setMinimumSize(QSize(1400, 865))
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_Excel = QAction(MainWindow)
        self.action_Excel.setObjectName(u"action_Excel")
        self.action_Excel_2 = QAction(MainWindow)
        self.action_Excel_2.setObjectName(u"action_Excel_2")
        self.action_Excel_3 = QAction(MainWindow)
        self.action_Excel_3.setObjectName(u"action_Excel_3")
        self.action_Excel_4 = QAction(MainWindow)
        self.action_Excel_4.setObjectName(u"action_Excel_4")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(Qt.StrongFocus)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.table_sell_out = QTableWidget(self.tab)
        if (self.table_sell_out.columnCount() < 7):
            self.table_sell_out.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_sell_out.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.table_sell_out.setObjectName(u"table_sell_out")
        font1 = QFont()
        font1.setPointSize(10)
        self.table_sell_out.setFont(font1)
        self.table_sell_out.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_sell_out.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_sell_out.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_sell_out.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_3.addWidget(self.table_sell_out)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.btn_sell_3 = QPushButton(self.tab)
        self.btn_sell_3.setObjectName(u"btn_sell_3")
        self.btn_sell_3.setMinimumSize(QSize(150, 75))
        self.btn_sell_3.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_sell_3)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_9)

        self.checkBox_1 = QCheckBox(self.tab)
        self.checkBox_1.setObjectName(u"checkBox_1")

        self.horizontalLayout_51.addWidget(self.checkBox_1)

        self.horizontalSpacer_10 = QSpacerItem(117, 4, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_51)

        self.btn_sell_2 = QPushButton(self.tab)
        self.btn_sell_2.setObjectName(u"btn_sell_2")
        self.btn_sell_2.setMinimumSize(QSize(150, 75))
        self.btn_sell_2.setFont(font)

        self.verticalLayout_2.addWidget(self.btn_sell_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.line_4 = QFrame(self.tab)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Raised)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.text_sell = QLineEdit(self.tab)
        self.text_sell.setObjectName(u"text_sell")
        self.text_sell.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.text_sell)

        self.btn_sell_4 = QPushButton(self.tab)
        self.btn_sell_4.setObjectName(u"btn_sell_4")
        self.btn_sell_4.setMinimumSize(QSize(200, 50))
        self.btn_sell_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_sell_4)

        self.btn_sell_5 = QPushButton(self.tab)
        self.btn_sell_5.setObjectName(u"btn_sell_5")
        self.btn_sell_5.setMinimumSize(QSize(200, 50))
        self.btn_sell_5.setFont(font)

        self.horizontalLayout_2.addWidget(self.btn_sell_5)

        self.horizontalSpacer = QSpacerItem(230, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_prepare_goods = QTableWidget(self.tab)
        if (self.table_prepare_goods.columnCount() < 6):
            self.table_prepare_goods.setColumnCount(6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_prepare_goods.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_prepare_goods.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_prepare_goods.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_prepare_goods.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_prepare_goods.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_prepare_goods.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        self.table_prepare_goods.setObjectName(u"table_prepare_goods")
        self.table_prepare_goods.setFont(font1)
        self.table_prepare_goods.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.table_prepare_goods.setAutoFillBackground(False)
        self.table_prepare_goods.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_prepare_goods.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_prepare_goods.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_prepare_goods.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout.addWidget(self.table_prepare_goods)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_sell_6 = QPushButton(self.tab)
        self.btn_sell_6.setObjectName(u"btn_sell_6")
        self.btn_sell_6.setMinimumSize(QSize(150, 75))
        self.btn_sell_6.setFont(font)

        self.verticalLayout.addWidget(self.btn_sell_6)

        self.btn_sell_1 = QPushButton(self.tab)
        self.btn_sell_1.setObjectName(u"btn_sell_1")
        self.btn_sell_1.setMinimumSize(QSize(150, 75))
        self.btn_sell_1.setFont(font)

        self.verticalLayout.addWidget(self.btn_sell_1)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_12 = QVBoxLayout(self.tab_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.table_goods = QTableWidget(self.tab_2)
        if (self.table_goods.columnCount() < 7):
            self.table_goods.setColumnCount(7)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_goods.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        self.table_goods.setObjectName(u"table_goods")
        self.table_goods.setFont(font1)
        self.table_goods.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_goods.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_goods.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_goods.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_6.addWidget(self.table_goods)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_goods_5 = QPushButton(self.tab_2)
        self.btn_goods_5.setObjectName(u"btn_goods_5")
        self.btn_goods_5.setMinimumSize(QSize(150, 75))

        self.verticalLayout_6.addWidget(self.btn_goods_5)

        self.btn_goods_4 = QPushButton(self.tab_2)
        self.btn_goods_4.setObjectName(u"btn_goods_4")
        self.btn_goods_4.setMinimumSize(QSize(150, 75))

        self.verticalLayout_6.addWidget(self.btn_goods_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.horizontalLayout_6.setStretch(0, 5)
        self.horizontalLayout_6.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.text_1 = QLineEdit(self.tab_2)
        self.text_1.setObjectName(u"text_1")
        self.text_1.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_4.addWidget(self.text_1)

        self.btn_goods_1 = QPushButton(self.tab_2)
        self.btn_goods_1.setObjectName(u"btn_goods_1")
        self.btn_goods_1.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_4.addWidget(self.btn_goods_1)

        self.btn_goods_2 = QPushButton(self.tab_2)
        self.btn_goods_2.setObjectName(u"btn_goods_2")
        self.btn_goods_2.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_4.addWidget(self.btn_goods_2)

        self.btn_goods_3 = QPushButton(self.tab_2)
        self.btn_goods_3.setObjectName(u"btn_goods_3")
        self.btn_goods_3.setMinimumSize(QSize(200, 50))

        self.horizontalLayout_4.addWidget(self.btn_goods_3)

        self.horizontalSpacer_2 = QSpacerItem(230, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)
        self.horizontalLayout_4.setStretch(4, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.line_3 = QFrame(self.tab_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.line_3)

        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.label.setFont(font2)

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.table_new_goods = QTableWidget(self.tab_2)
        if (self.table_new_goods.columnCount() < 7):
            self.table_new_goods.setColumnCount(7)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_new_goods.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        self.table_new_goods.setObjectName(u"table_new_goods")
        self.table_new_goods.setFont(font1)
        self.table_new_goods.setFocusPolicy(Qt.NoFocus)
        self.table_new_goods.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.table_new_goods.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_new_goods.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_5.addWidget(self.table_new_goods)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_new_goods_1 = QPushButton(self.tab_2)
        self.btn_new_goods_1.setObjectName(u"btn_new_goods_1")
        self.btn_new_goods_1.setMinimumSize(QSize(150, 50))

        self.verticalLayout_5.addWidget(self.btn_new_goods_1)

        self.btn_new_goods_2 = QPushButton(self.tab_2)
        self.btn_new_goods_2.setObjectName(u"btn_new_goods_2")
        self.btn_new_goods_2.setMinimumSize(QSize(150, 50))

        self.verticalLayout_5.addWidget(self.btn_new_goods_2)

        self.btn_new_goods_3 = QPushButton(self.tab_2)
        self.btn_new_goods_3.setObjectName(u"btn_new_goods_3")
        self.btn_new_goods_3.setMinimumSize(QSize(150, 50))

        self.verticalLayout_5.addWidget(self.btn_new_goods_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_9 = QVBoxLayout(self.tab_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.table_sale = QTableWidget(self.tab_3)
        if (self.table_sale.columnCount() < 11):
            self.table_sale.setColumnCount(11)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(7, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(8, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(9, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_sale.setHorizontalHeaderItem(10, __qtablewidgetitem37)
        self.table_sale.setObjectName(u"table_sale")
        self.table_sale.setFont(font1)
        self.table_sale.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_sale.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_sale.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_sale.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_sale.horizontalHeader().setDefaultSectionSize(122)

        self.verticalLayout_9.addWidget(self.table_sale)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.text_sale_1 = QLineEdit(self.tab_3)
        self.text_sale_1.setObjectName(u"text_sale_1")
        self.text_sale_1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_8.addWidget(self.text_sale_1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_sale_1 = QPushButton(self.tab_3)
        self.btn_sale_1.setObjectName(u"btn_sale_1")
        self.btn_sale_1.setMinimumSize(QSize(200, 50))
        self.btn_sale_1.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_8.addWidget(self.btn_sale_1)

        self.btn_sale_2 = QPushButton(self.tab_3)
        self.btn_sale_2.setObjectName(u"btn_sale_2")
        self.btn_sale_2.setMinimumSize(QSize(200, 50))
        self.btn_sale_2.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_8.addWidget(self.btn_sale_2)

        self.btn_sale_3 = QPushButton(self.tab_3)
        self.btn_sale_3.setObjectName(u"btn_sale_3")
        self.btn_sale_3.setMinimumSize(QSize(200, 50))
        self.btn_sale_3.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_8.addWidget(self.btn_sale_3)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_9.addLayout(self.verticalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.line = QFrame(self.tab_3)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_7.addWidget(self.line)

        self.btn_sale_4 = QPushButton(self.tab_3)
        self.btn_sale_4.setObjectName(u"btn_sale_4")
        self.btn_sale_4.setMinimumSize(QSize(200, 100))

        self.horizontalLayout_7.addWidget(self.btn_sale_4)

        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.btn_sale_5 = QPushButton(self.tab_3)
        self.btn_sale_5.setObjectName(u"btn_sale_5")
        self.btn_sale_5.setMinimumSize(QSize(250, 100))

        self.horizontalLayout_7.addWidget(self.btn_sale_5)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_9)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_11 = QVBoxLayout(self.tab_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.table_stock = QTableWidget(self.tab_4)
        if (self.table_stock.columnCount() < 8):
            self.table_stock.setColumnCount(8)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(6, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_stock.setHorizontalHeaderItem(7, __qtablewidgetitem45)
        self.table_stock.setObjectName(u"table_stock")
        self.table_stock.setFont(font1)
        self.table_stock.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_stock.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_stock.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.table_stock.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.verticalLayout_11.addWidget(self.table_stock)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.text_stock_1 = QLineEdit(self.tab_4)
        self.text_stock_1.setObjectName(u"text_stock_1")
        self.text_stock_1.setMinimumSize(QSize(0, 40))

        self.verticalLayout_10.addWidget(self.text_stock_1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_stock_1 = QPushButton(self.tab_4)
        self.btn_stock_1.setObjectName(u"btn_stock_1")
        self.btn_stock_1.setMinimumSize(QSize(200, 50))
        self.btn_stock_1.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_10.addWidget(self.btn_stock_1)

        self.btn_stock_2 = QPushButton(self.tab_4)
        self.btn_stock_2.setObjectName(u"btn_stock_2")
        self.btn_stock_2.setMinimumSize(QSize(200, 50))
        self.btn_stock_2.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_10.addWidget(self.btn_stock_2)

        self.btn_stock_3 = QPushButton(self.tab_4)
        self.btn_stock_3.setObjectName(u"btn_stock_3")
        self.btn_stock_3.setMinimumSize(QSize(200, 50))
        self.btn_stock_3.setMaximumSize(QSize(200, 50))

        self.horizontalLayout_10.addWidget(self.btn_stock_3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_10)

        self.line_2 = QFrame(self.tab_4)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setFrameShape(QFrame.VLine)

        self.horizontalLayout_11.addWidget(self.line_2)

        self.horizontalSpacer_4 = QSpacerItem(300, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.btn_stock_4 = QPushButton(self.tab_4)
        self.btn_stock_4.setObjectName(u"btn_stock_4")
        self.btn_stock_4.setMinimumSize(QSize(250, 100))

        self.horizontalLayout_11.addWidget(self.btn_stock_4)

        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 1)
        self.horizontalLayout_11.setStretch(2, 1)
        self.horizontalLayout_11.setStretch(3, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_33 = QVBoxLayout(self.tab_5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.text_cal_3 = QLineEdit(self.tab_5)
        self.text_cal_3.setObjectName(u"text_cal_3")
        self.text_cal_3.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.text_cal_3, 1, 4, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 1, 5, 1, 1)

        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 0))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 6, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.text_cal_4 = QLineEdit(self.tab_5)
        self.text_cal_4.setObjectName(u"text_cal_4")
        self.text_cal_4.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.text_cal_4, 1, 6, 1, 1)

        self.label_6 = QLabel(self.tab_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(70, 0))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(70, 0))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(500, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 1, 7, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 1, 1, 1, 1)

        self.text_cal_1 = QLineEdit(self.tab_5)
        self.text_cal_1.setObjectName(u"text_cal_1")
        self.text_cal_1.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.text_cal_1, 1, 0, 1, 1)

        self.label_8 = QLabel(self.tab_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(70, 0))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)

        self.text_cal_2 = QLineEdit(self.tab_5)
        self.text_cal_2.setObjectName(u"text_cal_2")
        self.text_cal_2.setMinimumSize(QSize(0, 40))

        self.gridLayout_2.addWidget(self.text_cal_2, 1, 2, 1, 1)


        self.verticalLayout_33.addLayout(self.gridLayout_2)

        self.tabWidget_2 = QTabWidget(self.tab_5)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_36 = QVBoxLayout(self.tab_7)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_22 = QGroupBox(self.tab_7)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setMinimumSize(QSize(200, 210))
        self.groupBox_22.setMaximumSize(QSize(200, 210))
        self.layoutWidget_15 = QWidget(self.groupBox_22)
        self.layoutWidget_15.setObjectName(u"layoutWidget_15")
        self.layoutWidget_15.setGeometry(QRect(20, 40, 171, 123))
        self.verticalLayout_26 = QVBoxLayout(self.layoutWidget_15)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_55 = QLabel(self.layoutWidget_15)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setMinimumSize(QSize(50, 20))
        self.label_55.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_52.addWidget(self.label_55)

        self.number_a1 = QLabel(self.layoutWidget_15)
        self.number_a1.setObjectName(u"number_a1")
        self.number_a1.setMinimumSize(QSize(40, 20))
        self.number_a1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.number_a1)


        self.verticalLayout_26.addLayout(self.horizontalLayout_52)

        self.line_41 = QFrame(self.layoutWidget_15)
        self.line_41.setObjectName(u"line_41")
        self.line_41.setFrameShape(QFrame.HLine)
        self.line_41.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_41)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_29 = QLabel(self.layoutWidget_15)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(50, 20))

        self.horizontalLayout_53.addWidget(self.label_29)

        self.text_a1 = QPushButton(self.layoutWidget_15)
        self.text_a1.setObjectName(u"text_a1")
        self.text_a1.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_53.addWidget(self.text_a1)


        self.verticalLayout_26.addLayout(self.horizontalLayout_53)

        self.line_42 = QFrame(self.layoutWidget_15)
        self.line_42.setObjectName(u"line_42")
        self.line_42.setFrameShape(QFrame.HLine)
        self.line_42.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_42)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_56 = QLabel(self.layoutWidget_15)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(50, 20))
        self.label_56.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_54.addWidget(self.label_56)

        self.price_a1 = QLabel(self.layoutWidget_15)
        self.price_a1.setObjectName(u"price_a1")
        self.price_a1.setMinimumSize(QSize(40, 20))
        self.price_a1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.price_a1)


        self.verticalLayout_26.addLayout(self.horizontalLayout_54)

        self.line_43 = QFrame(self.layoutWidget_15)
        self.line_43.setObjectName(u"line_43")
        self.line_43.setFrameShape(QFrame.HLine)
        self.line_43.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_26.addWidget(self.line_43)


        self.gridLayout_4.addWidget(self.groupBox_22, 0, 0, 1, 1)

        self.groupBox_23 = QGroupBox(self.tab_7)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setMinimumSize(QSize(200, 210))
        self.groupBox_23.setMaximumSize(QSize(200, 210))
        self.layoutWidget_16 = QWidget(self.groupBox_23)
        self.layoutWidget_16.setObjectName(u"layoutWidget_16")
        self.layoutWidget_16.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget_16)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_57 = QLabel(self.layoutWidget_16)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(50, 20))
        self.label_57.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_55.addWidget(self.label_57)

        self.number_a2 = QLabel(self.layoutWidget_16)
        self.number_a2.setObjectName(u"number_a2")
        self.number_a2.setMinimumSize(QSize(40, 20))
        self.number_a2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.number_a2)


        self.verticalLayout_27.addLayout(self.horizontalLayout_55)

        self.line_44 = QFrame(self.layoutWidget_16)
        self.line_44.setObjectName(u"line_44")
        self.line_44.setFrameShape(QFrame.HLine)
        self.line_44.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_44)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_30 = QLabel(self.layoutWidget_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_56.addWidget(self.label_30)

        self.text_a2 = QPushButton(self.layoutWidget_16)
        self.text_a2.setObjectName(u"text_a2")
        self.text_a2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_56.addWidget(self.text_a2)


        self.verticalLayout_27.addLayout(self.horizontalLayout_56)

        self.line_45 = QFrame(self.layoutWidget_16)
        self.line_45.setObjectName(u"line_45")
        self.line_45.setFrameShape(QFrame.HLine)
        self.line_45.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_45)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_58 = QLabel(self.layoutWidget_16)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(50, 20))
        self.label_58.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_57.addWidget(self.label_58)

        self.price_a2 = QLabel(self.layoutWidget_16)
        self.price_a2.setObjectName(u"price_a2")
        self.price_a2.setMinimumSize(QSize(40, 20))
        self.price_a2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.price_a2)


        self.verticalLayout_27.addLayout(self.horizontalLayout_57)

        self.line_46 = QFrame(self.layoutWidget_16)
        self.line_46.setObjectName(u"line_46")
        self.line_46.setFrameShape(QFrame.HLine)
        self.line_46.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_27.addWidget(self.line_46)


        self.gridLayout_4.addWidget(self.groupBox_23, 0, 1, 1, 1)

        self.groupBox_24 = QGroupBox(self.tab_7)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setMinimumSize(QSize(200, 210))
        self.groupBox_24.setMaximumSize(QSize(200, 210))
        self.layoutWidget_17 = QWidget(self.groupBox_24)
        self.layoutWidget_17.setObjectName(u"layoutWidget_17")
        self.layoutWidget_17.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_28 = QVBoxLayout(self.layoutWidget_17)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_59 = QLabel(self.layoutWidget_17)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(50, 20))
        self.label_59.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_58.addWidget(self.label_59)

        self.number_a3 = QLabel(self.layoutWidget_17)
        self.number_a3.setObjectName(u"number_a3")
        self.number_a3.setMinimumSize(QSize(40, 20))
        self.number_a3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.number_a3)


        self.verticalLayout_28.addLayout(self.horizontalLayout_58)

        self.line_47 = QFrame(self.layoutWidget_17)
        self.line_47.setObjectName(u"line_47")
        self.line_47.setFrameShape(QFrame.HLine)
        self.line_47.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_47)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_60 = QLabel(self.layoutWidget_17)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_59.addWidget(self.label_60)

        self.text_a3 = QPushButton(self.layoutWidget_17)
        self.text_a3.setObjectName(u"text_a3")
        self.text_a3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_59.addWidget(self.text_a3)


        self.verticalLayout_28.addLayout(self.horizontalLayout_59)

        self.line_48 = QFrame(self.layoutWidget_17)
        self.line_48.setObjectName(u"line_48")
        self.line_48.setFrameShape(QFrame.HLine)
        self.line_48.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_48)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_61 = QLabel(self.layoutWidget_17)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(50, 20))
        self.label_61.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_60.addWidget(self.label_61)

        self.price_a3 = QLabel(self.layoutWidget_17)
        self.price_a3.setObjectName(u"price_a3")
        self.price_a3.setMinimumSize(QSize(40, 20))
        self.price_a3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.price_a3)


        self.verticalLayout_28.addLayout(self.horizontalLayout_60)

        self.line_49 = QFrame(self.layoutWidget_17)
        self.line_49.setObjectName(u"line_49")
        self.line_49.setFrameShape(QFrame.HLine)
        self.line_49.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_28.addWidget(self.line_49)


        self.gridLayout_4.addWidget(self.groupBox_24, 0, 2, 1, 1)

        self.groupBox_25 = QGroupBox(self.tab_7)
        self.groupBox_25.setObjectName(u"groupBox_25")
        self.groupBox_25.setMinimumSize(QSize(200, 210))
        self.groupBox_25.setMaximumSize(QSize(200, 210))
        self.layoutWidget_18 = QWidget(self.groupBox_25)
        self.layoutWidget_18.setObjectName(u"layoutWidget_18")
        self.layoutWidget_18.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_29 = QVBoxLayout(self.layoutWidget_18)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_62 = QLabel(self.layoutWidget_18)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(50, 20))
        self.label_62.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_61.addWidget(self.label_62)

        self.number_a4 = QLabel(self.layoutWidget_18)
        self.number_a4.setObjectName(u"number_a4")
        self.number_a4.setMinimumSize(QSize(40, 20))
        self.number_a4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.number_a4)


        self.verticalLayout_29.addLayout(self.horizontalLayout_61)

        self.line_50 = QFrame(self.layoutWidget_18)
        self.line_50.setObjectName(u"line_50")
        self.line_50.setFrameShape(QFrame.HLine)
        self.line_50.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_29.addWidget(self.line_50)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_63 = QLabel(self.layoutWidget_18)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_62.addWidget(self.label_63)

        self.text_a4 = QPushButton(self.layoutWidget_18)
        self.text_a4.setObjectName(u"text_a4")
        self.text_a4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_62.addWidget(self.text_a4)


        self.verticalLayout_29.addLayout(self.horizontalLayout_62)

        self.line_51 = QFrame(self.layoutWidget_18)
        self.line_51.setObjectName(u"line_51")
        self.line_51.setFrameShape(QFrame.HLine)
        self.line_51.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_29.addWidget(self.line_51)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_64 = QLabel(self.layoutWidget_18)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(50, 20))
        self.label_64.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_63.addWidget(self.label_64)

        self.price_a4 = QLabel(self.layoutWidget_18)
        self.price_a4.setObjectName(u"price_a4")
        self.price_a4.setMinimumSize(QSize(40, 20))
        self.price_a4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.price_a4)


        self.verticalLayout_29.addLayout(self.horizontalLayout_63)

        self.line_52 = QFrame(self.layoutWidget_18)
        self.line_52.setObjectName(u"line_52")
        self.line_52.setFrameShape(QFrame.HLine)
        self.line_52.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_29.addWidget(self.line_52)


        self.gridLayout_4.addWidget(self.groupBox_25, 0, 3, 1, 1)

        self.groupBox_26 = QGroupBox(self.tab_7)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setMinimumSize(QSize(200, 210))
        self.groupBox_26.setMaximumSize(QSize(200, 210))
        self.layoutWidget_19 = QWidget(self.groupBox_26)
        self.layoutWidget_19.setObjectName(u"layoutWidget_19")
        self.layoutWidget_19.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_30 = QVBoxLayout(self.layoutWidget_19)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_65 = QLabel(self.layoutWidget_19)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(50, 20))
        self.label_65.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_64.addWidget(self.label_65)

        self.number_a5 = QLabel(self.layoutWidget_19)
        self.number_a5.setObjectName(u"number_a5")
        self.number_a5.setMinimumSize(QSize(40, 20))
        self.number_a5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.number_a5)


        self.verticalLayout_30.addLayout(self.horizontalLayout_64)

        self.line_53 = QFrame(self.layoutWidget_19)
        self.line_53.setObjectName(u"line_53")
        self.line_53.setFrameShape(QFrame.HLine)
        self.line_53.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_53)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_66 = QLabel(self.layoutWidget_19)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_65.addWidget(self.label_66)

        self.text_a5 = QPushButton(self.layoutWidget_19)
        self.text_a5.setObjectName(u"text_a5")
        self.text_a5.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_65.addWidget(self.text_a5)


        self.verticalLayout_30.addLayout(self.horizontalLayout_65)

        self.line_54 = QFrame(self.layoutWidget_19)
        self.line_54.setObjectName(u"line_54")
        self.line_54.setFrameShape(QFrame.HLine)
        self.line_54.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_54)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_67 = QLabel(self.layoutWidget_19)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setMinimumSize(QSize(50, 20))
        self.label_67.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_66.addWidget(self.label_67)

        self.price_a5 = QLabel(self.layoutWidget_19)
        self.price_a5.setObjectName(u"price_a5")
        self.price_a5.setMinimumSize(QSize(40, 20))
        self.price_a5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.price_a5)


        self.verticalLayout_30.addLayout(self.horizontalLayout_66)

        self.line_55 = QFrame(self.layoutWidget_19)
        self.line_55.setObjectName(u"line_55")
        self.line_55.setFrameShape(QFrame.HLine)
        self.line_55.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_30.addWidget(self.line_55)


        self.gridLayout_4.addWidget(self.groupBox_26, 0, 4, 1, 1)

        self.groupBox_27 = QGroupBox(self.tab_7)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setMinimumSize(QSize(200, 210))
        self.groupBox_27.setMaximumSize(QSize(200, 210))
        self.layoutWidget_20 = QWidget(self.groupBox_27)
        self.layoutWidget_20.setObjectName(u"layoutWidget_20")
        self.layoutWidget_20.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_31 = QVBoxLayout(self.layoutWidget_20)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_68 = QLabel(self.layoutWidget_20)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setMinimumSize(QSize(50, 20))
        self.label_68.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_67.addWidget(self.label_68)

        self.number_a6 = QLabel(self.layoutWidget_20)
        self.number_a6.setObjectName(u"number_a6")
        self.number_a6.setMinimumSize(QSize(40, 20))
        self.number_a6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.number_a6)


        self.verticalLayout_31.addLayout(self.horizontalLayout_67)

        self.line_56 = QFrame(self.layoutWidget_20)
        self.line_56.setObjectName(u"line_56")
        self.line_56.setFrameShape(QFrame.HLine)
        self.line_56.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_56)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_69 = QLabel(self.layoutWidget_20)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_68.addWidget(self.label_69)

        self.text_a6 = QPushButton(self.layoutWidget_20)
        self.text_a6.setObjectName(u"text_a6")
        self.text_a6.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_68.addWidget(self.text_a6)


        self.verticalLayout_31.addLayout(self.horizontalLayout_68)

        self.line_57 = QFrame(self.layoutWidget_20)
        self.line_57.setObjectName(u"line_57")
        self.line_57.setFrameShape(QFrame.HLine)
        self.line_57.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_57)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.label_70 = QLabel(self.layoutWidget_20)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setMinimumSize(QSize(50, 20))
        self.label_70.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_69.addWidget(self.label_70)

        self.price_a6 = QLabel(self.layoutWidget_20)
        self.price_a6.setObjectName(u"price_a6")
        self.price_a6.setMinimumSize(QSize(40, 20))
        self.price_a6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_69.addWidget(self.price_a6)


        self.verticalLayout_31.addLayout(self.horizontalLayout_69)

        self.line_58 = QFrame(self.layoutWidget_20)
        self.line_58.setObjectName(u"line_58")
        self.line_58.setFrameShape(QFrame.HLine)
        self.line_58.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_31.addWidget(self.line_58)


        self.gridLayout_4.addWidget(self.groupBox_27, 0, 5, 1, 1)

        self.groupBox_28 = QGroupBox(self.tab_7)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setMinimumSize(QSize(200, 210))
        self.groupBox_28.setMaximumSize(QSize(200, 210))
        self.layoutWidget_21 = QWidget(self.groupBox_28)
        self.layoutWidget_21.setObjectName(u"layoutWidget_21")
        self.layoutWidget_21.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_32 = QVBoxLayout(self.layoutWidget_21)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_71 = QLabel(self.layoutWidget_21)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setMinimumSize(QSize(50, 20))
        self.label_71.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_70.addWidget(self.label_71)

        self.number_a7 = QLabel(self.layoutWidget_21)
        self.number_a7.setObjectName(u"number_a7")
        self.number_a7.setMinimumSize(QSize(40, 20))
        self.number_a7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_70.addWidget(self.number_a7)


        self.verticalLayout_32.addLayout(self.horizontalLayout_70)

        self.line_59 = QFrame(self.layoutWidget_21)
        self.line_59.setObjectName(u"line_59")
        self.line_59.setFrameShape(QFrame.HLine)
        self.line_59.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_32.addWidget(self.line_59)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.label_72 = QLabel(self.layoutWidget_21)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_71.addWidget(self.label_72)

        self.text_a7 = QPushButton(self.layoutWidget_21)
        self.text_a7.setObjectName(u"text_a7")
        self.text_a7.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_71.addWidget(self.text_a7)


        self.verticalLayout_32.addLayout(self.horizontalLayout_71)

        self.line_60 = QFrame(self.layoutWidget_21)
        self.line_60.setObjectName(u"line_60")
        self.line_60.setFrameShape(QFrame.HLine)
        self.line_60.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_32.addWidget(self.line_60)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_73 = QLabel(self.layoutWidget_21)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setMinimumSize(QSize(50, 20))
        self.label_73.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_72.addWidget(self.label_73)

        self.price_a7 = QLabel(self.layoutWidget_21)
        self.price_a7.setObjectName(u"price_a7")
        self.price_a7.setMinimumSize(QSize(40, 20))
        self.price_a7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_72.addWidget(self.price_a7)


        self.verticalLayout_32.addLayout(self.horizontalLayout_72)

        self.line_61 = QFrame(self.layoutWidget_21)
        self.line_61.setObjectName(u"line_61")
        self.line_61.setFrameShape(QFrame.HLine)
        self.line_61.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_32.addWidget(self.line_61)


        self.gridLayout_4.addWidget(self.groupBox_28, 1, 0, 1, 1)


        self.verticalLayout_36.addLayout(self.gridLayout_4)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_16 = QSpacerItem(550, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_16)

        self.groupBox_4 = QGroupBox(self.tab_7)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_35 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_35.setSpacing(7)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, -1, -1, 30)
        self.text_sum_a = QLabel(self.groupBox_4)
        self.text_sum_a.setObjectName(u"text_sum_a")
        font3 = QFont()
        font3.setPointSize(18)
        self.text_sum_a.setFont(font3)
        self.text_sum_a.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.text_sum_a)


        self.horizontalLayout_31.addWidget(self.groupBox_4)

        self.horizontalSpacer_17 = QSpacerItem(550, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_17)


        self.verticalLayout_36.addLayout(self.horizontalLayout_31)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_25 = QVBoxLayout(self.tab_8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox_16 = QGroupBox(self.tab_8)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setMinimumSize(QSize(200, 210))
        self.groupBox_16.setMaximumSize(QSize(200, 210))
        self.layoutWidget_8 = QWidget(self.groupBox_16)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_43 = QLabel(self.layoutWidget_8)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(50, 20))
        self.label_43.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_33.addWidget(self.label_43)

        self.number_b7 = QLabel(self.layoutWidget_8)
        self.number_b7.setObjectName(u"number_b7")
        self.number_b7.setMinimumSize(QSize(40, 20))
        self.number_b7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.number_b7)


        self.verticalLayout_19.addLayout(self.horizontalLayout_33)

        self.line_23 = QFrame(self.layoutWidget_8)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShape(QFrame.HLine)
        self.line_23.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_23)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_23 = QLabel(self.layoutWidget_8)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_34.addWidget(self.label_23)

        self.text_b7 = QPushButton(self.layoutWidget_8)
        self.text_b7.setObjectName(u"text_b7")
        self.text_b7.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_34.addWidget(self.text_b7)


        self.verticalLayout_19.addLayout(self.horizontalLayout_34)

        self.line_24 = QFrame(self.layoutWidget_8)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShape(QFrame.HLine)
        self.line_24.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_24)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_44 = QLabel(self.layoutWidget_8)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(50, 20))
        self.label_44.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_35.addWidget(self.label_44)

        self.price_b7 = QLabel(self.layoutWidget_8)
        self.price_b7.setObjectName(u"price_b7")
        self.price_b7.setMinimumSize(QSize(40, 20))
        self.price_b7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.price_b7)


        self.verticalLayout_19.addLayout(self.horizontalLayout_35)

        self.line_25 = QFrame(self.layoutWidget_8)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShape(QFrame.HLine)
        self.line_25.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_19.addWidget(self.line_25)


        self.gridLayout_3.addWidget(self.groupBox_16, 1, 0, 1, 1)

        self.groupBox_20 = QGroupBox(self.tab_8)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setMinimumSize(QSize(200, 210))
        self.groupBox_20.setMaximumSize(QSize(200, 210))
        self.layoutWidget_12 = QWidget(self.groupBox_20)
        self.layoutWidget_12.setObjectName(u"layoutWidget_12")
        self.layoutWidget_12.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_23 = QVBoxLayout(self.layoutWidget_12)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_51 = QLabel(self.layoutWidget_12)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(50, 20))
        self.label_51.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_45.addWidget(self.label_51)

        self.number_b11 = QLabel(self.layoutWidget_12)
        self.number_b11.setObjectName(u"number_b11")
        self.number_b11.setMinimumSize(QSize(40, 20))
        self.number_b11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.number_b11)


        self.verticalLayout_23.addLayout(self.horizontalLayout_45)

        self.line_35 = QFrame(self.layoutWidget_12)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShape(QFrame.HLine)
        self.line_35.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_35)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_27 = QLabel(self.layoutWidget_12)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_46.addWidget(self.label_27)

        self.text_b11 = QPushButton(self.layoutWidget_12)
        self.text_b11.setObjectName(u"text_b11")
        self.text_b11.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_46.addWidget(self.text_b11)


        self.verticalLayout_23.addLayout(self.horizontalLayout_46)

        self.line_36 = QFrame(self.layoutWidget_12)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setFrameShape(QFrame.HLine)
        self.line_36.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_36)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_52 = QLabel(self.layoutWidget_12)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(50, 20))
        self.label_52.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_47.addWidget(self.label_52)

        self.price_b11 = QLabel(self.layoutWidget_12)
        self.price_b11.setObjectName(u"price_b11")
        self.price_b11.setMinimumSize(QSize(40, 20))
        self.price_b11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.price_b11)


        self.verticalLayout_23.addLayout(self.horizontalLayout_47)

        self.line_37 = QFrame(self.layoutWidget_12)
        self.line_37.setObjectName(u"line_37")
        self.line_37.setFrameShape(QFrame.HLine)
        self.line_37.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_23.addWidget(self.line_37)


        self.gridLayout_3.addWidget(self.groupBox_20, 1, 4, 1, 1)

        self.groupBox_17 = QGroupBox(self.tab_8)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(200, 210))
        self.groupBox_17.setMaximumSize(QSize(200, 210))
        self.layoutWidget_9 = QWidget(self.groupBox_17)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.layoutWidget_9.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_20 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_45 = QLabel(self.layoutWidget_9)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMinimumSize(QSize(50, 20))
        self.label_45.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_36.addWidget(self.label_45)

        self.number_b8 = QLabel(self.layoutWidget_9)
        self.number_b8.setObjectName(u"number_b8")
        self.number_b8.setMinimumSize(QSize(40, 20))
        self.number_b8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.number_b8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_36)

        self.line_26 = QFrame(self.layoutWidget_9)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShape(QFrame.HLine)
        self.line_26.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_26)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_24 = QLabel(self.layoutWidget_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_37.addWidget(self.label_24)

        self.text_b8 = QPushButton(self.layoutWidget_9)
        self.text_b8.setObjectName(u"text_b8")
        self.text_b8.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_37.addWidget(self.text_b8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_37)

        self.line_27 = QFrame(self.layoutWidget_9)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShape(QFrame.HLine)
        self.line_27.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_27)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_46 = QLabel(self.layoutWidget_9)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMinimumSize(QSize(50, 20))
        self.label_46.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_38.addWidget(self.label_46)

        self.price_b8 = QLabel(self.layoutWidget_9)
        self.price_b8.setObjectName(u"price_b8")
        self.price_b8.setMinimumSize(QSize(40, 20))
        self.price_b8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.price_b8)


        self.verticalLayout_20.addLayout(self.horizontalLayout_38)

        self.line_28 = QFrame(self.layoutWidget_9)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShape(QFrame.HLine)
        self.line_28.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_20.addWidget(self.line_28)


        self.gridLayout_3.addWidget(self.groupBox_17, 1, 1, 1, 1)

        self.groupBox_12 = QGroupBox(self.tab_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setMinimumSize(QSize(200, 210))
        self.groupBox_12.setMaximumSize(QSize(200, 210))
        self.layoutWidget_3 = QWidget(self.groupBox_12)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_35 = QLabel(self.layoutWidget_3)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(50, 20))
        self.label_35.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_19.addWidget(self.label_35)

        self.number_b4 = QLabel(self.layoutWidget_3)
        self.number_b4.setObjectName(u"number_b4")
        self.number_b4.setMinimumSize(QSize(40, 20))
        self.number_b4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.number_b4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)

        self.line_11 = QFrame(self.layoutWidget_3)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_11)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_19 = QLabel(self.layoutWidget_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_20.addWidget(self.label_19)

        self.text_b4 = QPushButton(self.layoutWidget_3)
        self.text_b4.setObjectName(u"text_b4")
        self.text_b4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_20.addWidget(self.text_b4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.line_12 = QFrame(self.layoutWidget_3)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShape(QFrame.HLine)
        self.line_12.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_12)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_36 = QLabel(self.layoutWidget_3)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(50, 20))
        self.label_36.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_21.addWidget(self.label_36)

        self.price_b4 = QLabel(self.layoutWidget_3)
        self.price_b4.setObjectName(u"price_b4")
        self.price_b4.setMinimumSize(QSize(40, 20))
        self.price_b4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.price_b4)


        self.verticalLayout_15.addLayout(self.horizontalLayout_21)

        self.line_13 = QFrame(self.layoutWidget_3)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShape(QFrame.HLine)
        self.line_13.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_15.addWidget(self.line_13)


        self.gridLayout_3.addWidget(self.groupBox_12, 0, 3, 1, 1)

        self.groupBox_18 = QGroupBox(self.tab_8)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setMinimumSize(QSize(200, 210))
        self.groupBox_18.setMaximumSize(QSize(200, 210))
        self.layoutWidget_10 = QWidget(self.groupBox_18)
        self.layoutWidget_10.setObjectName(u"layoutWidget_10")
        self.layoutWidget_10.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_21 = QVBoxLayout(self.layoutWidget_10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_47 = QLabel(self.layoutWidget_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMinimumSize(QSize(50, 20))
        self.label_47.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_39.addWidget(self.label_47)

        self.number_b9 = QLabel(self.layoutWidget_10)
        self.number_b9.setObjectName(u"number_b9")
        self.number_b9.setMinimumSize(QSize(40, 20))
        self.number_b9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.number_b9)


        self.verticalLayout_21.addLayout(self.horizontalLayout_39)

        self.line_29 = QFrame(self.layoutWidget_10)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShape(QFrame.HLine)
        self.line_29.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_29)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_25 = QLabel(self.layoutWidget_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_40.addWidget(self.label_25)

        self.text_b9 = QPushButton(self.layoutWidget_10)
        self.text_b9.setObjectName(u"text_b9")
        self.text_b9.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_40.addWidget(self.text_b9)


        self.verticalLayout_21.addLayout(self.horizontalLayout_40)

        self.line_30 = QFrame(self.layoutWidget_10)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShape(QFrame.HLine)
        self.line_30.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_30)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_48 = QLabel(self.layoutWidget_10)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMinimumSize(QSize(50, 20))
        self.label_48.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_41.addWidget(self.label_48)

        self.price_b9 = QLabel(self.layoutWidget_10)
        self.price_b9.setObjectName(u"price_b9")
        self.price_b9.setMinimumSize(QSize(40, 20))
        self.price_b9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.price_b9)


        self.verticalLayout_21.addLayout(self.horizontalLayout_41)

        self.line_31 = QFrame(self.layoutWidget_10)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShape(QFrame.HLine)
        self.line_31.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_21.addWidget(self.line_31)


        self.gridLayout_3.addWidget(self.groupBox_18, 1, 2, 1, 1)

        self.groupBox_14 = QGroupBox(self.tab_8)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setMinimumSize(QSize(200, 210))
        self.groupBox_14.setMaximumSize(QSize(200, 210))
        self.layoutWidget_5 = QWidget(self.groupBox_14)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_17 = QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_39 = QLabel(self.layoutWidget_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(50, 20))
        self.label_39.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.label_39)

        self.number_b6 = QLabel(self.layoutWidget_5)
        self.number_b6.setObjectName(u"number_b6")
        self.number_b6.setMinimumSize(QSize(40, 20))
        self.number_b6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.number_b6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_25)

        self.line_17 = QFrame(self.layoutWidget_5)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShape(QFrame.HLine)
        self.line_17.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_17)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_21 = QLabel(self.layoutWidget_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_26.addWidget(self.label_21)

        self.text_b6 = QPushButton(self.layoutWidget_5)
        self.text_b6.setObjectName(u"text_b6")
        self.text_b6.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_26.addWidget(self.text_b6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_26)

        self.line_18 = QFrame(self.layoutWidget_5)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShape(QFrame.HLine)
        self.line_18.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_18)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_40 = QLabel(self.layoutWidget_5)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 20))
        self.label_40.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_27.addWidget(self.label_40)

        self.price_b6 = QLabel(self.layoutWidget_5)
        self.price_b6.setObjectName(u"price_b6")
        self.price_b6.setMinimumSize(QSize(40, 20))
        self.price_b6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.price_b6)


        self.verticalLayout_17.addLayout(self.horizontalLayout_27)

        self.line_19 = QFrame(self.layoutWidget_5)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_19.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_17.addWidget(self.line_19)


        self.gridLayout_3.addWidget(self.groupBox_14, 0, 5, 1, 1)

        self.groupBox_13 = QGroupBox(self.tab_8)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(200, 210))
        self.groupBox_13.setMaximumSize(QSize(200, 210))
        self.layoutWidget_4 = QWidget(self.groupBox_13)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_37 = QLabel(self.layoutWidget_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 20))
        self.label_37.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_22.addWidget(self.label_37)

        self.number_b3 = QLabel(self.layoutWidget_4)
        self.number_b3.setObjectName(u"number_b3")
        self.number_b3.setMinimumSize(QSize(40, 20))
        self.number_b3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.number_b3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)

        self.line_14 = QFrame(self.layoutWidget_4)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_14)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_20 = QLabel(self.layoutWidget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_23.addWidget(self.label_20)

        self.text_b3 = QPushButton(self.layoutWidget_4)
        self.text_b3.setObjectName(u"text_b3")
        self.text_b3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_23.addWidget(self.text_b3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_23)

        self.line_15 = QFrame(self.layoutWidget_4)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShape(QFrame.HLine)
        self.line_15.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_15)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_38 = QLabel(self.layoutWidget_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(50, 20))
        self.label_38.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_24.addWidget(self.label_38)

        self.price_b3 = QLabel(self.layoutWidget_4)
        self.price_b3.setObjectName(u"price_b3")
        self.price_b3.setMinimumSize(QSize(40, 20))
        self.price_b3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.price_b3)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.line_16 = QFrame(self.layoutWidget_4)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShape(QFrame.HLine)
        self.line_16.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_16.addWidget(self.line_16)


        self.gridLayout_3.addWidget(self.groupBox_13, 0, 2, 1, 1)

        self.groupBox_15 = QGroupBox(self.tab_8)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setMinimumSize(QSize(200, 210))
        self.groupBox_15.setMaximumSize(QSize(200, 210))
        self.layoutWidget_6 = QWidget(self.groupBox_15)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_41 = QLabel(self.layoutWidget_6)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(50, 20))
        self.label_41.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_28.addWidget(self.label_41)

        self.number_b5 = QLabel(self.layoutWidget_6)
        self.number_b5.setObjectName(u"number_b5")
        self.number_b5.setMinimumSize(QSize(40, 20))
        self.number_b5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.number_b5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_28)

        self.line_20 = QFrame(self.layoutWidget_6)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_20.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_20)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_22 = QLabel(self.layoutWidget_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_29.addWidget(self.label_22)

        self.text_b5 = QPushButton(self.layoutWidget_6)
        self.text_b5.setObjectName(u"text_b5")
        self.text_b5.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_29.addWidget(self.text_b5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_29)

        self.line_21 = QFrame(self.layoutWidget_6)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShape(QFrame.HLine)
        self.line_21.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_21)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_42 = QLabel(self.layoutWidget_6)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(50, 20))
        self.label_42.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_30.addWidget(self.label_42)

        self.price_b5 = QLabel(self.layoutWidget_6)
        self.price_b5.setObjectName(u"price_b5")
        self.price_b5.setMinimumSize(QSize(40, 20))
        self.price_b5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.price_b5)


        self.verticalLayout_18.addLayout(self.horizontalLayout_30)

        self.line_22 = QFrame(self.layoutWidget_6)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_22.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_18.addWidget(self.line_22)


        self.gridLayout_3.addWidget(self.groupBox_15, 0, 4, 1, 1)

        self.groupBox_11 = QGroupBox(self.tab_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(200, 210))
        self.groupBox_11.setMaximumSize(QSize(200, 210))
        self.layoutWidget_2 = QWidget(self.groupBox_11)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_32 = QLabel(self.layoutWidget_2)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(50, 20))
        self.label_32.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_16.addWidget(self.label_32)

        self.number_b2 = QLabel(self.layoutWidget_2)
        self.number_b2.setObjectName(u"number_b2")
        self.number_b2.setMinimumSize(QSize(40, 20))
        self.number_b2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.number_b2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_16)

        self.line_8 = QFrame(self.layoutWidget_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_8)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_17.addWidget(self.label_18)

        self.text_b2 = QPushButton(self.layoutWidget_2)
        self.text_b2.setObjectName(u"text_b2")
        self.text_b2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_17.addWidget(self.text_b2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.line_9 = QFrame(self.layoutWidget_2)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.HLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_9)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_34 = QLabel(self.layoutWidget_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(50, 20))
        self.label_34.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_18.addWidget(self.label_34)

        self.price_b2 = QLabel(self.layoutWidget_2)
        self.price_b2.setObjectName(u"price_b2")
        self.price_b2.setMinimumSize(QSize(40, 20))
        self.price_b2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.price_b2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.line_10 = QFrame(self.layoutWidget_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_14.addWidget(self.line_10)


        self.gridLayout_3.addWidget(self.groupBox_11, 0, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.tab_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMinimumSize(QSize(200, 210))
        self.groupBox_10.setMaximumSize(QSize(200, 210))
        self.layoutWidget = QWidget(self.groupBox_10)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 40, 171, 123))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_31 = QLabel(self.layoutWidget)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(50, 20))
        self.label_31.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_13.addWidget(self.label_31)

        self.number_b1 = QLabel(self.layoutWidget)
        self.number_b1.setObjectName(u"number_b1")
        self.number_b1.setMinimumSize(QSize(40, 20))
        self.number_b1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.number_b1)


        self.verticalLayout_13.addLayout(self.horizontalLayout_13)

        self.line_5 = QFrame(self.layoutWidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(50, 20))

        self.horizontalLayout_14.addWidget(self.label_10)

        self.text_b1 = QPushButton(self.layoutWidget)
        self.text_b1.setObjectName(u"text_b1")
        self.text_b1.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.text_b1)


        self.verticalLayout_13.addLayout(self.horizontalLayout_14)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_33 = QLabel(self.layoutWidget)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(50, 20))
        self.label_33.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_15.addWidget(self.label_33)

        self.price_b1 = QLabel(self.layoutWidget)
        self.price_b1.setObjectName(u"price_b1")
        self.price_b1.setMinimumSize(QSize(40, 20))
        self.price_b1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.price_b1)


        self.verticalLayout_13.addLayout(self.horizontalLayout_15)

        self.line_7 = QFrame(self.layoutWidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.line_7)


        self.gridLayout_3.addWidget(self.groupBox_10, 0, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.tab_8)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setMinimumSize(QSize(200, 210))
        self.groupBox_21.setMaximumSize(QSize(200, 210))
        self.layoutWidget_13 = QWidget(self.groupBox_21)
        self.layoutWidget_13.setObjectName(u"layoutWidget_13")
        self.layoutWidget_13.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_24 = QVBoxLayout(self.layoutWidget_13)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_53 = QLabel(self.layoutWidget_13)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMinimumSize(QSize(50, 20))
        self.label_53.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_48.addWidget(self.label_53)

        self.number_b12 = QLabel(self.layoutWidget_13)
        self.number_b12.setObjectName(u"number_b12")
        self.number_b12.setMinimumSize(QSize(40, 20))
        self.number_b12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.number_b12)


        self.verticalLayout_24.addLayout(self.horizontalLayout_48)

        self.line_38 = QFrame(self.layoutWidget_13)
        self.line_38.setObjectName(u"line_38")
        self.line_38.setFrameShape(QFrame.HLine)
        self.line_38.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_38)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_28 = QLabel(self.layoutWidget_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_49.addWidget(self.label_28)

        self.text_b12 = QPushButton(self.layoutWidget_13)
        self.text_b12.setObjectName(u"text_b12")
        self.text_b12.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_49.addWidget(self.text_b12)


        self.verticalLayout_24.addLayout(self.horizontalLayout_49)

        self.line_39 = QFrame(self.layoutWidget_13)
        self.line_39.setObjectName(u"line_39")
        self.line_39.setFrameShape(QFrame.HLine)
        self.line_39.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_39)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_54 = QLabel(self.layoutWidget_13)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(50, 20))
        self.label_54.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_50.addWidget(self.label_54)

        self.price_b12 = QLabel(self.layoutWidget_13)
        self.price_b12.setObjectName(u"price_b12")
        self.price_b12.setMinimumSize(QSize(40, 20))
        self.price_b12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.price_b12)


        self.verticalLayout_24.addLayout(self.horizontalLayout_50)

        self.line_40 = QFrame(self.layoutWidget_13)
        self.line_40.setObjectName(u"line_40")
        self.line_40.setFrameShape(QFrame.HLine)
        self.line_40.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_24.addWidget(self.line_40)


        self.gridLayout_3.addWidget(self.groupBox_21, 1, 5, 1, 1)

        self.groupBox_19 = QGroupBox(self.tab_8)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setMinimumSize(QSize(200, 210))
        self.groupBox_19.setMaximumSize(QSize(200, 210))
        self.layoutWidget_11 = QWidget(self.groupBox_19)
        self.layoutWidget_11.setObjectName(u"layoutWidget_11")
        self.layoutWidget_11.setGeometry(QRect(20, 40, 161, 123))
        self.verticalLayout_22 = QVBoxLayout(self.layoutWidget_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_49 = QLabel(self.layoutWidget_11)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(50, 20))
        self.label_49.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_42.addWidget(self.label_49)

        self.number_b10 = QLabel(self.layoutWidget_11)
        self.number_b10.setObjectName(u"number_b10")
        self.number_b10.setMinimumSize(QSize(40, 20))
        self.number_b10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.number_b10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_42)

        self.line_32 = QFrame(self.layoutWidget_11)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShape(QFrame.HLine)
        self.line_32.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_32)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_26 = QLabel(self.layoutWidget_11)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 20))

        self.horizontalLayout_43.addWidget(self.label_26)

        self.text_b10 = QPushButton(self.layoutWidget_11)
        self.text_b10.setObjectName(u"text_b10")
        self.text_b10.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_43.addWidget(self.text_b10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_43)

        self.line_33 = QFrame(self.layoutWidget_11)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShape(QFrame.HLine)
        self.line_33.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_33)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_50 = QLabel(self.layoutWidget_11)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(50, 20))
        self.label_50.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_44.addWidget(self.label_50)

        self.price_b10 = QLabel(self.layoutWidget_11)
        self.price_b10.setObjectName(u"price_b10")
        self.price_b10.setMinimumSize(QSize(40, 20))
        self.price_b10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.price_b10)


        self.verticalLayout_22.addLayout(self.horizontalLayout_44)

        self.line_34 = QFrame(self.layoutWidget_11)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShape(QFrame.HLine)
        self.line_34.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_22.addWidget(self.line_34)


        self.gridLayout_3.addWidget(self.groupBox_19, 1, 3, 1, 1)


        self.verticalLayout_25.addLayout(self.gridLayout_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_14 = QSpacerItem(550, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)

        self.groupBox_3 = QGroupBox(self.tab_8)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_34 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_34.setSpacing(7)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(-1, -1, -1, 30)
        self.text_sum_b = QLabel(self.groupBox_3)
        self.text_sum_b.setObjectName(u"text_sum_b")
        self.text_sum_b.setFont(font3)
        self.text_sum_b.setAlignment(Qt.AlignCenter)

        self.verticalLayout_34.addWidget(self.text_sum_b)


        self.horizontalLayout_12.addWidget(self.groupBox_3)

        self.horizontalSpacer_15 = QSpacerItem(550, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_15)


        self.verticalLayout_25.addLayout(self.horizontalLayout_12)

        self.tabWidget_2.addTab(self.tab_8, "")

        self.verticalLayout_33.addWidget(self.tabWidget_2)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.groupBox_2 = QGroupBox(self.tab_6)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(500, 20, 371, 271))
        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 180, 151, 41))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 90, 121, 51))
        self.groupBox_5 = QGroupBox(self.tab_6)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(10, 10, 420, 280))
        self.btn_settings_1 = QPushButton(self.groupBox_5)
        self.btn_settings_1.setObjectName(u"btn_settings_1")
        self.btn_settings_1.setGeometry(QRect(240, 210, 150, 41))
        self.btn_settings_1.setMinimumSize(QSize(150, 40))
        self.layoutWidget1 = QWidget(self.groupBox_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 50, 301, 141))
        self.gridLayout = QGridLayout(self.layoutWidget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.text_settings_1 = QLineEdit(self.layoutWidget1)
        self.text_settings_1.setObjectName(u"text_settings_1")
        self.text_settings_1.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.text_settings_1, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.text_settings_2 = QLineEdit(self.layoutWidget1)
        self.text_settings_2.setObjectName(u"text_settings_2")
        self.text_settings_2.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.text_settings_2, 1, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.text_settings_3 = QLineEdit(self.layoutWidget1)
        self.text_settings_3.setObjectName(u"text_settings_3")
        self.text_settings_3.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.text_settings_3, 2, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab_6)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 320, 420, 280))
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(270, 220, 131, 41))
        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 40, 381, 161))
        self.verticalLayout_37 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget2)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_37.addWidget(self.label_12)

        self.label_11 = QLabel(self.layoutWidget2)
        self.label_11.setObjectName(u"label_11")
        font4 = QFont()
        font4.setPointSize(9)
        self.label_11.setFont(font4)

        self.verticalLayout_37.addWidget(self.label_11)

        self.line_62 = QFrame(self.layoutWidget2)
        self.line_62.setObjectName(u"line_62")
        self.line_62.setFrameShape(QFrame.HLine)
        self.line_62.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_37.addWidget(self.line_62)

        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_37.addWidget(self.label_13)

        self.comboBox = QComboBox(self.layoutWidget2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)

        self.verticalLayout_37.addWidget(self.comboBox)

        self.tabWidget.addTab(self.tab_6, "")

        self.verticalLayout_4.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1400, 32))
        self.menubar.setFont(font)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setFont(font)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_2.setFont(font)
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_3.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_Excel)
        self.menu_3.addAction(self.action_Excel_2)
        self.menu_3.addAction(self.action_Excel_3)
        self.menu_3.addAction(self.action_Excel_4)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u7ba1\u7406", None))
        self.action_Excel.setText(QCoreApplication.translate("MainWindow", u"\u4eceExcel\u6587\u4ef6\u5bfc\u5165\u5546\u54c1\u4fe1\u606f", None))
        self.action_Excel_2.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5546\u54c1\u4fe1\u606f\u5230Excel", None))
        self.action_Excel_3.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u65f6\u95f4\u5bfc\u51fa\u9500\u552e\u8bb0\u5f55\u5230Excel", None))
        self.action_Excel_4.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5168\u90e8\u9500\u552e\u8bb0\u5f55\u5230Excel", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5bfc\u5165\u6a21\u677f", None))
        ___qtablewidgetitem = self.table_sell_out.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1id", None));
        ___qtablewidgetitem1 = self.table_sell_out.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.table_sell_out.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        ___qtablewidgetitem3 = self.table_sell_out.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem4 = self.table_sell_out.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None));
        ___qtablewidgetitem5 = self.table_sell_out.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        ___qtablewidgetitem6 = self.table_sell_out.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u603b\u4ef7", None));
        self.btn_sell_3.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6210\u51fa\u8d27", None))
        self.checkBox_1.setText(QCoreApplication.translate("MainWindow", u"\u4e0d\u6253\u5370", None))
        self.btn_sell_2.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_sell_4.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0\u67e5\u8be2", None))
        self.btn_sell_5.setText(QCoreApplication.translate("MainWindow", u"id\u67e5\u8be2", None))
        ___qtablewidgetitem7 = self.table_prepare_goods.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1id", None));
        ___qtablewidgetitem8 = self.table_prepare_goods.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem9 = self.table_prepare_goods.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u4f59\u8d27\u91cf", None));
        ___qtablewidgetitem10 = self.table_prepare_goods.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        ___qtablewidgetitem11 = self.table_prepare_goods.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem12 = self.table_prepare_goods.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        self.btn_sell_6.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u67e5\u8be2\u8bb0\u5f55", None))
        self.btn_sell_1.setText(QCoreApplication.translate("MainWindow", u"\u552e\u51fa\u9009\u4e2d\u5546\u54c1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u51fa\u8d27", None))
        ___qtablewidgetitem13 = self.table_goods.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1id", None));
        ___qtablewidgetitem14 = self.table_goods.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem15 = self.table_goods.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u4f59\u8d27\u91cf", None));
        ___qtablewidgetitem16 = self.table_goods.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        ___qtablewidgetitem17 = self.table_goods.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem18 = self.table_goods.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u6210\u672c\u4ef7", None));
        ___qtablewidgetitem19 = self.table_goods.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        self.btn_goods_5.setText(QCoreApplication.translate("MainWindow", u"\u66f4\u65b0\u5e93\u5b58", None))
        self.btn_goods_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u5546\u54c1\u4fe1\u606f", None))
        self.btn_goods_1.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0\u67e5\u8be2", None))
        self.btn_goods_2.setText(QCoreApplication.translate("MainWindow", u"id\u67e5\u8be2", None))
        self.btn_goods_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u67e5\u8be2\u8bb0\u5f55", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5546\u54c1\u4fe1\u606f\u8868", None))
        ___qtablewidgetitem20 = self.table_new_goods.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1id", None));
        ___qtablewidgetitem21 = self.table_new_goods.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem22 = self.table_new_goods.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u4f59\u8d27\u91cf", None));
        ___qtablewidgetitem23 = self.table_new_goods.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        ___qtablewidgetitem24 = self.table_new_goods.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem25 = self.table_new_goods.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"\u6210\u672c\u4ef7", None));
        ___qtablewidgetitem26 = self.table_new_goods.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        self.btn_new_goods_1.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0\u4e00\u884c", None))
        self.btn_new_goods_2.setText(QCoreApplication.translate("MainWindow", u"\u51cf\u5c0f\u4e00\u884c", None))
        self.btn_new_goods_3.setText(QCoreApplication.translate("MainWindow", u"\u5408\u5e76", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u7ba1\u7406", None))
        ___qtablewidgetitem27 = self.table_sale.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem28 = self.table_sale.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1id", None));
        ___qtablewidgetitem29 = self.table_sale.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem30 = self.table_sale.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        ___qtablewidgetitem31 = self.table_sale.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem32 = self.table_sale.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"\u6210\u672c\u4ef7", None));
        ___qtablewidgetitem33 = self.table_sale.horizontalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        ___qtablewidgetitem34 = self.table_sale.horizontalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None));
        ___qtablewidgetitem35 = self.table_sale.horizontalHeaderItem(8)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"\u603b\u6210\u672c\u4ef7", None));
        ___qtablewidgetitem36 = self.table_sale.horizontalHeaderItem(9)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"\u603b\u9500\u552e\u989d", None));
        ___qtablewidgetitem37 = self.table_sale.horizontalHeaderItem(10)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"\u5229\u6da6", None));
        self.btn_sale_1.setText(QCoreApplication.translate("MainWindow", u"\u6309\u540d\u79f0\u67e5\u8be2", None))
#if QT_CONFIG(tooltip)
        self.btn_sale_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4f8b\u5982\uff1a</p><p>\u7cbe\u786e\u5230\u5e74\uff1a2022</p><p>\u7cbe\u786e\u5230\u6708\uff1a2022.4</p><p>\u7cbe\u786e\u5230\u5929\uff1a2022.4.3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_sale_2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u65f6\u95f4\u67e5\u8be2", None))
        self.btn_sale_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u67e5\u8be2\u7ed3\u679c", None))
        self.btn_sale_4.setText(QCoreApplication.translate("MainWindow", u"\u9009\u4e2d\u5546\u54c1\u9000\u8d27", None))
        self.btn_sale_5.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d\u9500\u552e\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u8d26\u5355", None))
        ___qtablewidgetitem38 = self.table_stock.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None));
        ___qtablewidgetitem39 = self.table_stock.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1id", None));
        ___qtablewidgetitem40 = self.table_stock.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        ___qtablewidgetitem41 = self.table_stock.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"\u578b\u53f7", None));
        ___qtablewidgetitem42 = self.table_stock.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4f4d", None));
        ___qtablewidgetitem43 = self.table_stock.horizontalHeaderItem(5)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None));
        ___qtablewidgetitem44 = self.table_stock.horizontalHeaderItem(6)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None));
        ___qtablewidgetitem45 = self.table_stock.horizontalHeaderItem(7)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"\u603b\u4ef7", None));
        self.btn_stock_1.setText(QCoreApplication.translate("MainWindow", u"\u6309\u540d\u79f0\u67e5\u8be2", None))
#if QT_CONFIG(tooltip)
        self.btn_stock_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u4f8b\u5982\uff1a</p><p>\u7cbe\u786e\u5230\u5e74\uff1a2022</p><p>\u7cbe\u786e\u5230\u6708\uff1a2022.4</p><p>\u7cbe\u786e\u5230\u5929\uff1a2022.4.3</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_stock_2.setText(QCoreApplication.translate("MainWindow", u"\u6309\u65f6\u95f4\u67e5\u8be2", None))
        self.btn_stock_3.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u67e5\u8be2\u7ed3\u679c", None))
        self.btn_stock_4.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u9009\u4e2d\u8fdb\u8d27\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u8fdb\u8d27", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u9762\u79ef", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u957f", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5bbd", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5468\u957f", None))
        self.text_cal_2.setText("")
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u66f2", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_a1.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a1.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a1.setText("")
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"\u5934\u5934", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_a2.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a2.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a2.setText("")
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"\u82b1\u677f", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_a3.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a3.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a3.setText("")
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"\u516b\u5b9d", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_a4.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a4.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a4.setText("")
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"\u7ebf\u6761", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_a5.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a5.setText("")
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a5.setText("")
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"\u89d2\u82b1", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.number_a6.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a6.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a6.setText("")
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"\u706f\u76d8", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.number_a7.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_a7.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_a7.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u8ba1", None))
        self.text_sum_a.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u65b0\u6b3e", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"8\u516c\u5206\u7ebf\u6761", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b7.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b7.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b7.setText("")
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"\u8349\u89d2\u82b1", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.number_b11.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b11.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b11.setText("")
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u5e03", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b8.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b8.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b8.setText("")
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"\u516b\u5b9d", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b4.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b4.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b4.setText("")
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"\u76f4\u89d2", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.number_b9.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b9.setText("")
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b9.setText("")
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u591a\u5409", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b6.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b6.setText("")
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b6.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"2\u516c\u5206\u957f\u57ce\u7ebf", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b3.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b3.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b3.setText("")
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u56db\u5927\u738b", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b5.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b5.setText("")
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b5.setText("")
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u8fb9\u739b\u66f2\u624e", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b2.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b2.setText("")
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u8fde\u4f53\u5934\u5934", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u957f\u5ea6", None))
        self.number_b1.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b1.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b1.setText("")
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"\u706f\u76d8", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.number_b12.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b12.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b12.setText("")
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"\u8fde\u4f53\u659c\u89d2", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf", None))
        self.number_b10.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4ef7", None))
        self.text_b10.setText("")
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c", None))
        self.price_b10.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u8ba1", None))
        self.text_sum_b.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u8001\u6b3e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u8ba1\u7b97", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7248\u672c\uff1a", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Excel\u4fe1\u606f\u8bbe\u7f6e", None))
        self.btn_settings_1.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5730\u70b9\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8bdd\uff1a", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6253\u5370\u673a\u8bbe\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u6253\u5370\u673a\uff1a", None))
        self.label_11.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u4e0b\u65b9\u83dc\u5355\u9009\u62e9\u9ed8\u8ba4\u6253\u5370\u673a\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
    # retranslateUi

