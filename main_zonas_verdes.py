
import pandas as pd
import os

print ("Zonas verdes en el País Vasco")




zonas_verdes = pd.read_csv('data_zonas_verdes/Superficie ocupada por parques, jardines y zonas verdes urbanas (%_suelo urbano).csv',sep=';', encoding='latin1')
zonas_verdes.iloc[9:]
zonas_verdes_provincias = zonas_verdes.iloc[2:9] #datos por provincias
zonas_verdes_provincias.columns =['provincia', 'col2', '2009', '2008', '2007', '2006', '2005'] #nombres de columnas
zonas_verdes_provincias = zonas_verdes_provincias.drop([7,8]) #datos no interesantes
zonas_verdes_provincias = zonas_verdes_provincias.reset_index(drop=True)  #indice a partir de 0
zonas_verdes_provincias = zonas_verdes_provincias[sorted(zonas_verdes_provincias.columns)] #ordenar columnas
zonas_verdes_provincias = zonas_verdes_provincias.drop(columns='col2') #eliminar columnas
zonas_verdes_provincias = zonas_verdes_provincias.drop([0])

for col in zonas_verdes_provincias.columns:
    if col!= 'provincia':
        zonas_verdes_provincias[col] = (
            zonas_verdes_provincias[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .astype(float))


print("\nDataFrame final de zonas verdes por provincias:")
print(zonas_verdes_provincias)



zonas_verdes_persona = pd.read_csv('data_zonas_verdes/Superficie ocupada por parques, jardines y zonas verdes urbanas (m_persona).csv', sep=';',encoding='latin1')
zonas_verdes_persona.iloc[9:]
zonas_verdes_persona_provincias.columns=['provincia', 'col2', '2009', '2008', '2007', '2006', '2005'] #nombres de columnas
zonas_verdes_persona_provincias
zonas_verdes_persona_provincias = zonas_verdes_persona_provincias.drop([7,9]) #datos no interesantes
zonas_verdes_persona_provincias= zonas_verdes_persona_provincias.drop(columns='col2')
zonas_verdes_persona_provincias= zonas_verdes_persona_provincias[sorted(zonas_verdes_persona_provincias.columns)]
zonas_verdes_persona_provincias= zonas_verdes_persona_provincias.reset_index(drop=True)  #indice a partir de 0
zonas_verdes_persona_provincias = zonas_verdes_persona_provincias.drop(4)
zonas_verdes_persona_provincias

for col in zonas_verdes_persona_provincias:
    if col != 'provincia':
        zonas_verdes_persona_provincias[col] = (
            zonas_verdes_persona_provincias[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )

print("\nDataFrame final de zonas verdes por persona y por provincias:")
print(zonas_verdes_provincias)