import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
import ui
from PyQt5.QtWidgets import QMainWindow, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import xlrd
import numpy as np
import statsmodels.api as sm
import math

years = [2011, 2012, 2013, 2014, 2015]


# def Fun(p, x):
#     # 线性回归模型
#     regr = linear_model.LinearRegression()
#     # 训练
#     regr.fit(diabetes_X_train, diabetes_y_train)
#     # 预测
#     diabetes_y_pred = regr.predict(diabetes_X_test)
#     return diabetes_y_pred


def loadExcel(file='database.xlsx'):
    try:
        # 打开Excel文件读取数据
        data = xlrd.open_workbook(file)
        # 获取第一个工作表
        sheet = data.sheet_by_index(1)
        # 获取行数
        priceList = sheet.col_values(7)
        if priceList[0] == '猪肉':
            priceList = priceList[2:]
        return priceList
    except Exception as e:
        print(str(e))


class ImgDisp(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ImgDisp, self).__init__(parent)
        self.flag2draw = False
        self.setupUi(self)
        # set Btn
        self.pushButton.clicked.connect(self.Calculation)
        self.pushButton_2.clicked.connect(self.Paint)
        self.pushButton_5.clicked.connect(self.BtnEnd)
        self.pig_meat_price = loadExcel()

        self.Init_Widgets()

    def Init_Widgets(self):
        self.PrepareSurfaceCanvas()

    def PrepareSurfaceCanvas(self):
        # 创建一个合适的画布，通过Figure_canvas()
        self.SurfFigure = Figure_Canvas()
        # 将groupbox这个容器放入gridlaout 网格布局 ，groupBox在hj_ui中通过qtdesigner添加
        self.SurfFigureLayout = QGridLayout(self.groupBox)
        # 画布放入布局中的容器groupBox中
        self.SurfFigureLayout.addWidget(self.SurfFigure)
        self.SurfFigure.ax.remove()
        self.ax3d = self.SurfFigure.fig.gca()
        self.ax3d.set_title("Predict Pig Meat Prices")
        self.ax3d.set_xlabel("weeks")
        self.ax3d.set_ylabel("price")
        plt.show()

    # 计算方法
    def Calculation(self, n):
        try:
            var = self.pig_meat_price[n] * -0.789 + self.pig_meat_price[n + 1] * 1.774 + 0.374
            print(var)
        except Exception as e:
            print("---异常---：", e)
        return var

    def Paint(self):
        n = len(self.pig_meat_price) - 2
        num = np.arange(len(self.pig_meat_price), len(self.pig_meat_price) + 52, 1)
        for i in num:
            print(i)
            var = self.Calculation(n)
            self.pig_meat_price.append(var)
            n = n + 1

        y_Xis = np.arange(0, len(self.pig_meat_price), 1)
        self.ax3d.plot(y_Xis, self.pig_meat_price, 'b^-', label='sales growth')
        x_major_locator = plt.MultipleLocator(52)
        self.ax3d.xaxis.set_major_locator(x_major_locator)
        self.ax3d.axis([0, len(self.pig_meat_price), min(self.pig_meat_price), max(self.pig_meat_price)])
        self.SurfFigure.draw()
        self.ax3d.legend()
        return

    def BtnEnd(self):
        print("结束！！！")
        plt.close()
        exit()
        pass


class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=22, height=20, dpi=100):
        self.fig = Figure(figsize=(width, height))
        super(Figure_Canvas, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)
