# -*- coding: utf-8 -*-
import re
import fileinput
import numpy as np
import pandas as pd
def transform(keywords,parameters,input_file,output_csv):
    """
    Читает входной inc-file и трансформирует в csv-file
    :param keywords:
    :param parameters:
    :param input_file:
    :param output_file:
    :return:
    """
    return
#eval - convenient function

def read():
    return
def inspect():
    return
def clean(file_name):
    file_name = re.sub('[--].*', '', file_name)
    file_name = re.sub(r"1\*",'DEFAULT',file_name)
    file_name = re.sub(r"3\*",'DEFAULT DEFAULT DEFAULT',file_name)
    file_name = re.sub(r"2\*",'DEFAULT DEFAULT',file_name)
    #file_name = re.sub(r"[0-9]\*",'DEFAULT',file_name)
 
    #file_name = re.sub('\\n|\\t','',file_name)
    #file_name=
    return file_name



def parse():
    return
def extract_keyword_blocks(file_name):
    list=[]

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

def extract_lines_from_keyword_block():
    return
def parse_keywords_from_blocks():
    return
def parse_keywords_DATA_line():
    return

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


