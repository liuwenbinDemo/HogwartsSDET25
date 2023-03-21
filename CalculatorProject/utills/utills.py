import os

import openpyxl
import re


def get_add_data(data_path, test_title):
    book = openpyxl.open(data_path)
    sheet = book.active
    add_data = []
    for row in sheet["A2":"H22"]:
        line = []
        i = 0
        title_text = ""
        for ceil in row:
            i = i + 1
            if i == 3:
                title_text = ceil.value
                if title_text == test_title:
                    line.append(title_text)
            if title_text == test_title:
                if i == 6:
                    col = re.split(r'[：\n]', ceil.value)
                    try:
                        line.append(int(col[1]))
                    except:
                        try:
                            line.append(float(col[1]))
                        except:
                            line.append(col[1])

                    try:
                        line.append(int(col[3]))
                    except:
                        try:
                            line.append(float(col[3]))
                        except:
                            line.append(col[3])
                elif i == 7:
                    line.append(ceil.value)
        if title_text == test_title:
            add_data.append(line)
    return add_data

# print(get_add_data("../data/add.xlsx", "【边界】有效边界值相加，结果计算正确"))