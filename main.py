# -*- coding: utf-8 -*-
import pandas as pd
import re
import numpy as np
from lib import schedule_parser
c = open('input data/test_schedule.inc')

df = pd.DataFrame(columns=['Date','Well name','Local grid name','I','J','K upper','K lower','Flag on connection',
                                'Saturation table','Transmissibility factor','Well bore diameter','Effective Kh','Skin factor',
                                'D-factor','Dir_well_penetrates_grid_block','Press_eq_radius'])



lin=[]
line = c.readlines()


print(line[2])
lin = [schedule_parser.clean(line[i])  for i in range(len(line))]
print(lin[2])


res=[]
resul=[]
compdat=[]
dates=[]
for i in range(1,len(lin)):
    if re.search(r"COMPDAT\b",lin[i-1]):
    #if lin[i-1]=="COMPDAT":
        for t in range(i,len(lin)):
        # print(lin[i])
            if re.search(r"W|[0-9]",lin[t]):
                a=re.findall(r'\w+',lin[t])
                df = df.append({   'Date': '',
                                    'Well name' : '',
                                    'Local grid name' : a[0],
                                    'I':a[1],
                                    'J':a[2],
                                    'K upper':a[3],
                                    'K lower':a[4],
                                    'Flag on connection':a[5],
                                    'Saturation table':a[6],
                                    'Transmissibility factor':a[7],
                                    'Well bore diameter':a[8],
                                    'Effective Kh':a[9],
                                    'Skin factor':a[10],
                                    'D-factor':a[11],
                                    'Dir_well_penetrates_grid_block':a[12],
                                    'Press_eq_radius':a[13]+'.'+a[14]
                                        }, ignore_index=True)                    
                
            if re.search(r"COMPDAT|DATES|WEFAC", lin[t]):
                    break
                
    elif re.search(r"DATES",lin[i-1]):
        for t in range(i,len(lin)):
            if re.search(r"[0-9]",lin[t]):
                    a=re.findall(r'\w+',lin[t])
                    print(a)
                    df = df.append({   'Date': a[0]+" "+a[1]+" "+ a[2],
                                    'Well name' : '',
                                    'Local grid name' :'',
                                    'I':'',
                                    'J':'',
                                    'K upper':'',
                                    'K lower':'',
                                    'Flag on connection':'',
                                    'Saturation table':'',
                                    'Transmissibility factor':'',
                                    'Well bore diameter':'',
                                    'Effective Kh':'',
                                    'Skin factor':'',
                                    'D-factor':'',
                                    'Dir_well_penetrates_grid_block':'',
                                    'Press_eq_radius':''
                                        }, ignore_index=True)      
                    
            if re.search(r"COMPDAT|DATES|WEFAC", lin[t]):
                    break
                
               
    else:
        if re.search(r"COMPDATL",lin[i-1]):
       #if lin[i-1]=="COMPDAT":
           
            for t in range(i,len(lin)):
            # print(lin[i])
                if re.search(r"W|[0-9]",lin[t]):
                    a=re.findall(r'\w+',lin[t])
                    df = df.append({   'Date': '',
                                        'Well name' : a[1],
                                        'Local grid name' : a[0],
                                        'I':a[2],
                                        'J':a[3],
                                        'K upper':a[4],
                                        'K lower':a[5],
                                        'Flag on connection':a[6],
                                        'Saturation table':a[7],
                                        'Transmissibility factor':a[8],
                                        'Well bore diameter':a[9],
                                        'Effective Kh':a[10],
                                        'Skin factor':a[11],
                                        'D-factor':a[12],
                                        'Dir_well_penetrates_grid_block':a[13],
                                        'Press_eq_radius':a[14]+'.'+a[14]
                                            }, ignore_index=True)                    

                if re.search(r"COMPDAT|DATES|WEFAC", lin[t]):
                        break
        
        else:
            continue
#fact = [schedule_parser.clean_res(res[i])  for i in range(len(res))]
#display(df)

for i in range (1,len(df.index)):
                if df["Date"][i]== '':
                   df["Date"][i]=df["Date"][i-1]
                
                else:
                    continue
                    
                    
                    
display(df)

'''
if __name__ == "__main__":
    keywords = ("DATES", "COMPDAT", "COMPDATL")
    parameters=("")
    input_file = "input_data/test_schedule.inc"
    output_csv = ""

    schedule_df = schedule_parser.transform(keywords,parameters,input_file,output_csv)
'''