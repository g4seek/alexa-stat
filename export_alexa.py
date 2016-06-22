# encoding: utf-8
import os
from xlwt import *
from datetime import datetime


def export_data(input_dir, export_path):
    """
    将每天抓取的数据按月份汇总到Excel
    :param input_dir: 输入数据目录
    :param export_path: 输出路径
    """

    # 1. 列出输入目录的文件
    file_names = []
    try:
        file_names = os.listdir(input_dir)
        print ("Files in the directory:" + str(file_names))
    except OSError:
        print "Source directory does not exist."

    # 2. 创建Excel工作簿
    book = Workbook()
    sheet = book.add_sheet("alexa")
    col = 0
    for file_name in file_names:
        # 3. 在每一列中写入一天的数据
        day = file_name[:-4]
        input_path = input_dir + "/" + file_name
        input_file = open(input_path, "r")
        sheet.write(0, col, day)
        row = 1
        for line in input_file.readlines():
            sheet.write(row, col, line)
            row += 1
        col += 1
    # 4. 保存文件
    book.save(export_path)
    print ("Result saved in file:" + export_path)


if __name__ == "__main__":
    month_now = datetime.now().strftime("%Y-%m")
    input_month = raw_input("Input the year and month of data. Eg(" + month_now + "). Enter for current month:")
    if not input_month:
        input_month = month_now

    # 导出当月的全球alexa排名
    print ("-" * 10 + "global" + "-" * 10)
    global_input_dir = "E:/doc/alexa/global/" + input_month
    global_export_path = "E:/doc/alexa/global/" + input_month + ".xls"
    export_data(global_input_dir, global_export_path)

    # 导出当月的中国alexa排名
    print ("-" * 10 + "china" + "-" * 10)
    china_input_dir = "E:/doc/alexa/china/" + input_month
    china_export_path = "E:/doc/alexa/china/" + input_month + ".xls"
    export_data(china_input_dir, china_export_path)
