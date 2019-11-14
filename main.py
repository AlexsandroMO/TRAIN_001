'''!pip install pandas
!pip install excel
!pip install pandasql
!pip install sqlite3
'''

import pandas as pd
import pandasql as pdsql
import sqlite3


df1 = pd.read_excel('AVALIA_PRODUTO.xlsx', 'AVALIA')
df2 = pd.read_excel('AVALIA_PRODUTO.xlsx', 'PM')

df1['SEARCHED'] = '-'

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
        
    df1['SEARCHED'].loc[a] = new
                    
    cont += 1 
    
    #print('--->>>', cont)
    
    
    
  def add_cos(cos, rev):

    conn = sqlite3.connect('DB_PROJECT.db')
    c = conn.cursor()

    qsl_datas = f"""
                INSERT INTO TABLE_COS(COS,REV)
                VALUES ('{cos}', '{rev}');
    """

    c.execute(qsl_datas)

    conn.commit()
    conn.close()
    
 for i in range(len(df1['SEARCHED'])):
    print(df1['SEARCHED'].loc[i])
    add_cos(df1['SEARCHED'].loc[i],df1['REV'].loc[i])
    
    
    
    
def criar_tabela1():
    #===========================================
    #Criar Tabela USER
    conn = sqlite3.connect('DB_PROJECT.db')
    c = conn.cursor()
    table_createdb = f"""
    
    CREATE TABLE IF NOT EXISTS TABLE_COS (
    ID INTEGER PRIMARY KEY,
    COS VARCHAR(300) NOT NULL,
    REV VARCHAR(2) NOT NULL
    )"""

    status = True
    
    return status
    
    
def criar_tabela2():
    #===========================================
    #Criar Tabela USER
    conn = sqlite3.connect('DB_PROJECT.db')
    c = conn.cursor()
    table_createdb = f"""
    
    CREATE TABLE IF NOT EXISTS TABLE_PM (
    ID INTEGER PRIMARY KEY,
    PM VARCHAR(15) NOT NULL,
    STATUS_PM VARCHAR(3) NOT NULL
    )"""

    status = True
    
    return status 
    
    
