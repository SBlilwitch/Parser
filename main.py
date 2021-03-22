# -*- coding: utf-8 -*-
import pandas as pd
from lib import schedule_parser
c = open('test_schedule.inc')
text = c.re ad()
print(text)

if __name__ == "__main__":
    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters=("")
    input_file = "input_data/test_schedule.inc"
    output_csv = ""

    schedule_df = schedule_parser.transform(keywords,parameters,input_file,output_csv)
Hello world

try again