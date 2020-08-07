import sys
import temp as tp
from PyQt5.QtWidgets import QApplication

# 主要分为三个部分
# 1.读取串口，解析，存入数据库
# 2.画实时图像
# 3.窗体（最开始的代码），通过Button调用其他两个类的方法    时间（3天）

# 需要以下类完成项目：
# 串口Com：读取数据，协议解析，
# Mysql 连接，存入，删除，查询取出数据
# MyThread 类，多线程
# MainWindow 窗体
# ImgDisp 窗体引用，装入画布
# plt画三维图像


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = tp.ImgDisp()
    ui.show()
    sys.exit(app.exec_())
