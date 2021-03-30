# -*- coding: utf-8 -*-
import re
import fileinput
import numpy as np
import pandas as pd

#eval - convenient function

def read(file_path):
    """
    Фунция открывающий исходный файл и переобразовывает его в массив
    :param file_path: путь к исходному файлу
    :return: массив исходных данных для парсера
    """
    c = open(file_path)
    line = c.readlines()
    return line

def clean(line):
    """
    Функция,удаляющая лишние коментарии из строки и определяющая дефолтные значения
    :param file_name:
    :return: Очищенная строка
    """
    line = re.sub('[--].*', '', line)
    line = re.sub(r"1\*",'DEFAULT',line)
    line = re.sub(r"3\*",'DEFAULT DEFAULT DEFAULT',line)
    line= re.sub(r"2\*",'DEFAULT DEFAULT',line)

    return line

def date_update(data_frame):
    """
    Функция,добавляющая недостающие даты
    :param data_frame: dataframe,полученный после парсинга по ключевым словам
    :return: dataframe c коректными датами
    """
    for i in range(1, len(data_frame.index)):
        if data_frame["Date"][i] == '':
            data_frame["Date"][i] = data_frame["Date"][i - 1]

        else:
            continue
    return data_frame

def parse(lin,df):
    """
    Функция,которая по входящему готовому массиву исходных данных создает dataframe отформатированный по ключевым словам
    :param lin: очищенный массив исходных данных
    :param df: пустой dataframe с готовой шапкой
    :return: dataframe с отсортированными исходными даннами по ключевым словам
    """
    for i in range(1, len(lin)):
        if re.search(r"COMPDAT\b", lin[i - 1]):
            # if lin[i-1]=="COMPDAT":
            for t in range(i, len(lin)):
                # print(lin[i])
                if re.search(r"W|[0-9]", lin[t]):
                    a = re.findall(r'\w+', lin[t])
                    df = df.append({'Date': '',
                                    'Well name': '',
                                    'Local grid name': a[0],
                                    'I': a[1],
                                    'J': a[2],
                                    'K upper': a[3],
                                    'K lower': a[4],
                                    'Flag on connection': a[5],
                                    'Saturation table': a[6],
                                    'Transmissibility factor': a[7],
                                    'Well bore diameter': a[8],
                                    'Effective Kh': a[9],
                                    'Skin factor': a[10],
                                    'D-factor': a[11],
                                    'Dir_well_penetrates_grid_block': a[12],
                                    'Press_eq_radius': a[13] + '.' + a[14]
                                    }, ignore_index=True)

                if re.search(r"COMPDAT|DATES|WEFAC", lin[t]):
                    break

        elif re.search(r"DATES", lin[i - 1]):
            for t in range(i, len(lin)):
                if re.search(r"[0-9]", lin[t]):
                    a = re.findall(r'\w+', lin[t])

                    df = df.append({'Date': a[0] + " " + a[1] + " " + a[2],
                                    'Well name': '',
                                    'Local grid name': '',
                                    'I': '',
                                    'J': '',
                                    'K upper': '',
                                    'K lower': '',
                                    'Flag on connection': '',
                                    'Saturation table': '',
                                    'Transmissibility factor': '',
                                    'Well bore diameter': '',
                                    'Effective Kh': '',
                                    'Skin factor': '',
                                    'D-factor': '',
                                    'Dir_well_penetrates_grid_block': '',
                                    'Press_eq_radius': ''
                                    }, ignore_index=True)

                if re.search(r"COMPDAT|DATES|WEFAC", lin[t]):
                    break


        else:
            if re.search(r"COMPDATL", lin[i - 1]):
                # if lin[i-1]=="COMPDAT":

                for t in range(i, len(lin)):
                    # print(lin[i])
                    if re.search(r"W|[0-9]", lin[t]):
                        a = re.findall(r'\w+', lin[t])
                        df = df.append({'Date': '',
                                        'Well name': a[1],
                                        'Local grid name': a[0],
                                        'I': a[2],
                                        'J': a[3],
                                        'K upper': a[4],
                                        'K lower': a[5],
                                        'Flag on connection': a[6],
                                        'Saturation table': a[7],
                                        'Transmissibility factor': a[8],
                                        'Well bore diameter': a[9],
                                        'Effective Kh': a[10],
                                        'Skin factor': a[11],
                                        'D-factor': a[12],
                                        'Dir_well_penetrates_grid_block': a[13],
                                        'Press_eq_radius': a[14] + '.' + a[14]
                                        }, ignore_index=True)

                    if re.search(r"COMPDAT|DATES|WEFAC", lin[t]):
                        break

            else:
                continue
    final_result= date_update(df)
    return final_result

def key_search(file_name):
    result = re.findall(r"COMPDAT.*",file_name)
    return result

def keyword_search(file_name):
    list_1=[ ]
    keyword='COMPDAT'
    for line in open(file_name ):
        if keyword in line:
            list_1.append(line)
    return list_1

def parse_keywords_COMPDAT_line(well_comp_line):
    """
    очищает строку по ключевому слову COMPDAT
    :param well_comp_line:
    :return:
    """
    well_comp_line=re.sub(r"'|(\s+/$)","",well_comp_line)
    well_comp_line=re.split(r"\s+",well_comp_line)
    return well_comp_line
def parse_keywords_COMPDATL(well_line):
    well_line = re.sub(r"'|(\s+/$)", "", well_line)
    well_line = re.split(r"\s+", well_line)
    return well_line

def transform(file_path):
    """
    Фунция,которая парсит входящего inc-file
    :param file_path: путь к исходному файлу
    :return: генерируется csv-file c данными после парсинга
    """

    #создание пустого dataframe  с готовой шапкой
    data = pd.DataFrame(
        columns=['Date', 'Well name', 'Local grid name', 'I', 'J', 'K upper', 'K lower', 'Flag on connection',
                 'Saturation table', 'Transmissibility factor', 'Well bore diameter', 'Effective Kh', 'Skin factor',
                 'D-factor', 'Dir_well_penetrates_grid_block', 'Press_eq_radius'])

    line=read(file_path)
    lin = [clean(line[i]) for i in range(len(line))]
    df = parse(lin, data)
    df.to_csv('output file', encoding='utf-8', index=False)
    return df
