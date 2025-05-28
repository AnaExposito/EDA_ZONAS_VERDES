
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


carpeta_graficos = 'graficos_zonas_verdes'


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


print("DataFrame final de zonas verdes por provincias:")
print(zonas_verdes_provincias)

print ("_____")

zonas_verdes_persona = pd.read_csv('data_zonas_verdes/Superficie ocupada por parques, jardines y zonas verdes urbanas (m_persona).csv', sep=';',encoding='latin1')
zonas_verdes_persona_provincias = zonas_verdes_persona.iloc[3:10]
zonas_verdes_persona_provincias.columns = ['provincia', 'col2', '2009', '2008', '2007', '2006', '2005'] #nombres de columnas
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

print("DataFrame final de zonas verdes por persona y por provincias:")
print(zonas_verdes_persona_provincias)


print ("_____")

supeficie_agricola = pd.read_csv('data_zonas_verdes/Superficie agricola (% s_ superficie total).csv', sep=';',encoding='latin1')
supeficie_agricola_provincias = supeficie_agricola.iloc[3:10]
supeficie_agricola_provincias.columns =['provincia', 'col2','2023', '2022', '2021', '2020', '2019', '2018', '2016', '2005']
supeficie_agricola_provincias = supeficie_agricola_provincias.reset_index(drop=True)
supeficie_agricola_provincias = supeficie_agricola_provincias.drop([4,5]) #datos no interesantes
supeficie_agricola_provincias = supeficie_agricola_provincias.drop([6])
supeficie_agricola_provincias = supeficie_agricola_provincias.drop(columns = 'col2')
supeficie_agricola_provincias  = supeficie_agricola_provincias [sorted(supeficie_agricola_provincias.columns)]
for col in supeficie_agricola_provincias:
    if col != 'provincia':
        supeficie_agricola_provincias[col] = (
            supeficie_agricola_provincias[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )

print("DataFrame final de superficie agricola por provincia:")
print(supeficie_agricola_provincias)

print ("_____")


superficie_forestal= pd.read_csv('data_zonas_verdes/Superficie forestal (% s  superficie total).csv', sep=';',encoding='latin1')
superficie_forestal_provinincia = superficie_forestal.iloc[:9]
superficie_forestal_provinincia.columns =['provincia', 'col2', '2023', '2022', '2021', '2020', '2019', '2018', '2016', '2010', '2005']
superficie_forestal_provinincia  = superficie_forestal_provinincia.drop(columns='col2')
superficie_forestal_provinincia  = superficie_forestal_provinincia [sorted(superficie_forestal_provinincia.columns)] #ordenar
superficie_forestal_provinincia = superficie_forestal_provinincia.drop([1,2]) #datos no interesantes
superficie_forestal_provinincia = superficie_forestal_provinincia.drop([0]) 
superficie_forestal_provinincia = superficie_forestal_provinincia.dropna(how= 'all') #valores nan
superficie_forestal_provinincia = superficie_forestal_provinincia.drop([8]) 
superficie_forestal_provinincia= superficie_forestal_provinincia.reset_index(drop=True)  #indice a partir de 0

for col in superficie_forestal_provinincia:
    if col != 'provincia':
        superficie_forestal_provinincia[col] = (
            superficie_forestal_provinincia[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )

print("DataFrame final de superficie forestal por provincia:")
print(superficie_forestal_provinincia)


print ("_____")


superficie_forestal_publica= pd.read_csv(
    'data_zonas_verdes/Superficie forestal publica (% s_ superficie forestal total).csv',
    sep=';',
    encoding='latin1')

superficie_forestal_publica_provincias = superficie_forestal_publica.iloc[:9]
superficie_forestal_publica_provincias.columns =['provincia', 'col2','2023', '2022', '2021', '2020', '2019', '2018', '2016', '2005']
superficie_forestal_publica_provincias = superficie_forestal_publica_provincias.dropna(how ='all')
superficie_forestal_publica_provincias = superficie_forestal_publica_provincias.drop([8])
superficie_forestal_publica_provincias = superficie_forestal_publica_provincias.drop(columns="col2")
superficie_forestal_publica_provincias = superficie_forestal_publica_provincias.drop([1])
superficie_forestal_publica_provincias = superficie_forestal_publica_provincias.drop([2])
superficie_forestal_publica_provincias = superficie_forestal_publica_provincias[sorted(superficie_forestal_publica_provincias.columns)]
superficie_forestal_publica_provincias= superficie_forestal_publica_provincias.reset_index(drop=True) 

for col in superficie_forestal_publica_provincias:
    if col != 'provincia':
        superficie_forestal_publica_provincias[col] = (
            superficie_forestal_publica_provincias[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )


print("DataFrame final de superficie forestal publica por provincia:")
print(superficie_forestal_publica_provincias)


print ("_____")



especial_proteccion= pd.read_csv(
    'data_zonas_verdes/Superficie municipal de especial proteccion (% superficie total).csv',
    sep=';',
    encoding='latin1')

especial_proteccion_provincia = especial_proteccion.iloc[:10]
especial_proteccion_provincia = especial_proteccion_provincia.dropna(how= 'all')
especial_proteccion_provincia.columns = ['provincia', 'col2', '2023', '2022', '2021', '2020', '2019','2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011','2010', '2009', '2008', '2006']
especial_proteccion_provincia= especial_proteccion_provincia.drop(columns="col2")
especial_proteccion_provincia= especial_proteccion_provincia[sorted(especial_proteccion_provincia)]
especial_proteccion_provincia = especial_proteccion_provincia.dropna(how='all')
especial_proteccion_provincia = especial_proteccion_provincia.drop(1)
especial_proteccion_provincia = especial_proteccion_provincia.drop(2)
especial_proteccion_provincia = especial_proteccion_provincia.reset_index(drop=True)
especial_proteccion_provincia = especial_proteccion_provincia.drop([4,5])

for col in especial_proteccion_provincia:
    if col != 'provincia':
        especial_proteccion_provincia[col] = (
            especial_proteccion_provincia[col]
            .astype(str)
            .str.replace(',', '.', regex=False)
            .astype(float)
        )

print("DataFrame final de superficie especial proteccion por provincia:")
print(especial_proteccion_provincia)

print ("_____")
print ("_____")
