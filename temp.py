
import matplotlib
from PyQt5 import QtCore, QtGui, QtWidgets
import hj_ui
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import xlrd

years = [2011, 2012, 2013, 2014, 2015, 2016]
datay = [2011, 2012, 2013, 2014, 2015, 2016]


def loadExcel(file='database.xlsx'):
    try:
        # 打开Excel文件读取数据
        data = xlrd.open_workbook(file)
        # 获取第一个工作表
        table = data.sheet_by_index(0)
        # 获取行数
        nrows = table.nrows
        # 获取列数
        ncols = table.ncols
        # 定义excel_list
        excel_list = []
        for row in range(2, nrows):
            for col in range(ncols):
                # 获取单元格数据
                cell_value = table.cell(row, col).value
                # 把数据追加到excel_list中
                excel_list.append(cell_value)
        return excel_list
    except Exception as e:
        print(str(e))


class ImgDisp(QMainWindow, hj_ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ImgDisp, self).__init__(parent)
        self.flag2draw = False
        self.setupUi(self)
        # set Btn
        self.pushButton.clicked.connect(self.Calculation)
        self.pushButton_2.clicked.connect(self.Paint)
        self.pushButton_5.clicked.connect(self.BtnEnd)
        # self.pushButton_3.clicked.connect(self.PrintData)
        # set thread

        self.Init_Widgets()

    def Init_Widgets(self):
        loadExcel()
        self.PrepareSurfaceCanvas()

        # 添加画布函数

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
        self.ax3d.set_xlabel("years")
        self.ax3d.set_ylabel("price")
        plt.show()

    # 回归计算方法
    def Calculation(self):
        print("Calculation running")
        try:
            print("predictPrices")
            excel_list = loadExcel()
            print(excel_list)
        except Exception as e:
            print("---异常---：", e)
        return

    def Paint(self):
        print("update_figure start")
        self.ax3d.plot(years, datay, c='r')
        self.SurfFigure.draw()

        print("update_figure end")
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
