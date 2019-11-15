#https://pt.stackoverflow.com/questions/296286/encontrar-determinado-texto-em-uma-string
!pip install excel
!pip install pandasql
!pip install sqlite3

import pandas as pd
import pandasql as pdsql
import sqlite3
import re

df1 = pd.read_excel('AVALIA_PRODUTO.xlsx', 'AVALIA')
df2 = pd.read_excel('AVALIA_PRODUTO.xlsx', 'PM')

df1['SEARCHED'] = '-'

df2 = df2[['PRODUTOS','RESULT']]

for a in range(len(df1['REV_TEXTO'])):
  text_COS = df1['REV_TEXTO'].loc[a]
  for a in range(len(df2['PRODUTOS'])):
    PM = df2['PRODUTOS'].loc[a]
    if re.search(f"""\\b{PM}\\b""", text_COS, re.IGNORECASE):
      #print("A string tem o nome Enzo")
      df2['RESULT'].loc[a] = 'OK'
    #else:
      #print("A string não tem o nome Enzo")


df2[df2['RESULT'] == 'OK']
df2

#============================

create_table1 = []
cont = 0
for a in range(len(df1['REV_TEXTO'])):
    split_a = df1['REV_TEXTO'].loc[a].split()
    
    new = []
    for b in split_a:
        #print(a)
        if len(b) < 11:
            #print('nnnn')
            if b[:2] != 'PR':
                if b[:1] == 'P':
                    #print(b)
                    new.append(b)
        
    df1['SEARCHED'].loc[a] = f"""{new}"""
    print(len(df1['SEARCHED'].loc[a]), df1['SEARCHED'].loc[a])
    add_cos(df1['SEARCHED'].loc[a],  'ok')          
    cont += 1 
    

#========================

import re

nome = 'dded MT01 inspection (CTE01042635).\n'

if re.search(f"""\\bMT01\\b""", nome, re.IGNORECASE):
    print("A string tem o nome Enzo")
else:
    print("A string não tem o nome Enzo")
