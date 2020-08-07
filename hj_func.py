import matplotlib.pyplot as plt
# import mysql.connector
# lock=Lock()


def predictPrices(excel_list):
    try:
        print("predictPrices")
        print(excel_list)
    except Exception as e:
        print("---异常---：", e)
    return


def loadExcel(file='/database.xlsx'):
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
        for row in range(1, nrows):
            for col in range(ncols):
                # 获取单元格数据
                cell_value = table.cell(row, col).value
                # 把数据追加到excel_list中
                excel_list.append(cell_value)
        return excel_list
    except Exception as e:
        print
        str(e)
