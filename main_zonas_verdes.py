
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


carpeta_graficos = 'graficos_zonas_verdes'
os.makedirs(carpeta_graficos, exist_ok=True)

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
            .astype(float))


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


#index


dataframes = [zonas_verdes_provincias,zonas_verdes_persona_provincias,supeficie_agricola_provincias , superficie_forestal_provinincia, superficie_forestal_publica_provincias
 , especial_proteccion_provincia]
for df in dataframes:
    df.set_index('provincia', inplace= True)
    print (df)
    print ("_____")


print (zonas_verdes_provincias)
zonas_verdes_provincias.to_csv('zonas_verdes_provincias')

print (zonas_verdes_persona_provincias)
zonas_verdes_persona_provincias.to_csv('zonas_verdes_persona_provincias')

print (supeficie_agricola_provincias)
supeficie_agricola_provincias.to_csv('supeficie_agricola_provincias')

print (superficie_forestal_provinincia)
superficie_forestal_provinincia.to_csv('superficie_forestal_provinincia')

print (superficie_forestal_publica_provincias)
superficie_forestal_publica_provincias.to_csv('superficie_forestal_publica_provincias')

print (especial_proteccion_provincia)
especial_proteccion_provincia.to_csv('especial_proteccion_provincia')


print ("_____")
print ("_____")

df1 = zonas_verdes_provincias.T 
provincias_grafico = ['Araba/Álava', 'Bizkaia', 'Gipuzkoa']
df1 = df1[provincias_grafico]

plt.figure(figsize=(10, 6))
for provincia in df1.columns:
    plt.plot(df1.index, df1[provincia], marker='o', label=provincia)
plt.title("Evolución de zonas Verdes por provincia (2005–2009)")
plt.xlabel("Año")
plt.ylabel("Porcentaje %")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
nombre_archivo_grafico_zonas_verdes = 'grafico zonas verdes.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()




#tendencias zonas verdes
provincias = ['Araba/Álava', 'Bizkaia', 'Gipuzkoa']

dfs = {"Zonas verdes (%)": zonas_verdes_provincias.T[provincias],
       "Zonas verdes por persona (m²)": zonas_verdes_persona_provincias.T[provincias],}

plt.figure(figsize=(18, 12))
for i, (titulo, df) in enumerate(dfs.items(), 1):
    plt.subplot(2, 3, i)
    for provincia in df.columns:
        plt.plot(df.index, df[provincia], marker='o', label=provincia)
    plt.title(titulo)
    plt.xlabel("Año")
    plt.ylabel("%" if "por persona" not in titulo else "m²/persona")
plt.tight_layout()
plt.show()
nombre_archivo_grafico_zonas_verdes = 'grafico zonas verdes persona.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()

#tendencia superficie forestal
provincias = ['Araba/Álava', 'Bizkaia', 'Gipuzkoa']

dfs = {
    "Superficie forestal (%)": superficie_forestal_provinincia.T[provincias],
    "Superficie forestal pública (%)": superficie_forestal_publica_provincias.T[provincias],

}

plt.figure(figsize=(18, 12))
for i, (titulo, df) in enumerate(dfs.items(), 1):
    plt.subplot(2, 3, i)
    for provincia in df.columns:
        plt.plot(df.index, df[provincia], marker='o', label=provincia)
    plt.title(titulo)
    plt.xlabel("Año")
    plt.ylabel("%" if "por persona" not in titulo else "m²/persona")
plt.tight_layout()
plt.show()
nombre_archivo_grafico_zonas_verdes = 'grafico zonas verdes persona 2.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()

#tendencia superficie especial proteccion
provincias = ['Araba/Álava', 'Bizkaia', 'Gipuzkoa']

# Transponer y filtrar los DataFrames
dfs = {
    "Zonas de especial protección (%)": especial_proteccion_provincia.T[provincias],
}

plt.figure(figsize=(10,6))
for i, (titulo, df) in enumerate(dfs.items(), 1):
    for provincia in df.columns:
        plt.plot(df.index, df[provincia], marker='o', label=provincia)
    plt.title(titulo)
    plt.xlabel("Año")
plt.tight_layout()
plt.show()
nombre_archivo_grafico_zonas_verdes = 'grafico zonas especial proteccion.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()



años = ['2018', '2019', '2020', '2021', '2022', '2023']

superficie_agricola = pd.read_csv('supeficie_agricola_provincias', index_col='provincia')
superficie_forestal = pd.read_csv('superficie_forestal_provinincia', index_col='provincia')
superficie_forestal_publica = pd.read_csv('superficie_forestal_publica_provincias', index_col='provincia')
especial_proteccion = pd.read_csv('especial_proteccion_provincia', index_col='provincia')

# 2. Filtrar columnas por año y renombrarlas para distinguirlas luego
superficie_agricola = superficie_agricola[años].rename(columns=lambda x: f'sup_agricola_{x}')
superficie_forestal = superficie_forestal[años].rename(columns=lambda x: f'sup_forestal_{x}')
superficie_forestal_publica = superficie_forestal_publica[años].rename(columns=lambda x: f'sup_forestal_publica_{x}')
especial_proteccion = especial_proteccion[años].rename(columns=lambda x: f'esp_proteccion_{x}')


datos_actualizados = pd.concat([
    superficie_agricola,
    superficie_forestal,
    superficie_forestal_publica,
    especial_proteccion
], axis=1)
datos_actualizados.reset_index(inplace=True)

datos_actualizados.to_csv('datos_2018_2023_provincias.csv')

print("Archivo guardado como 'datos_2018_2023_provincias.csv'")
print(datos_actualizados)

datos_actualizados_provincia = datos_actualizados[datos_actualizados["provincia"] != "CAE"]
print("____")

#suma de forestal por provincia

columnas_forestales = [col for col in datos_actualizados_provincia.columns if 'forestal' in col]
tabla_forestal = datos_actualizados_provincia[['provincia'] + columnas_forestales]

print("--- superficie total forestal ---")
print(tabla_forestal)



#forestal2023

provincias = ['Araba/Álava', 'Bizkaia', 'Gipuzkoa']
valores = tabla_forestal[tabla_forestal['provincia'].isin(provincias)]['sup_forestal_2023']

plt.style.use('bmh')
plt.figure(figsize=(8, 8))
plt.pie(valores, labels=provincias, autopct='%1.1f%%', startangle=90, colors=['green', 'lightgreen', 'darkgreen']) #porcentajes
plt.title("Superficie forestal por provincia (2023)")

plt.tight_layout()
plt.show()
nombre_archivo_grafico_zonas_verdes = 'grafico forestal.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()



##Uso de suelo por provincia


datos_suelo_2023 = datos_actualizados_provincia[[
    "provincia", "sup_agricola_2023", "sup_forestal_2023", "sup_forestal_publica_2023", "esp_proteccion_2023"
]]

datos_melted = datos_suelo_2023.melt(
    id_vars=["provincia"],
    var_name="variable",
    value_name="valor_superficie" # Esta es la columna que usaremos directamente
)

datos_melted["variable"] = datos_melted["variable"].map({
    "sup_agricola_2023": "Agrícola",
    "sup_forestal_2023": "Forestal",
    "sup_forestal_publica_2023": "Pública",
    "esp_proteccion_2023": "Protegida"
})


colores_personalizados = {
    "Agrícola": "#EBF049",    # Amarillo
    "Forestal": "#1CA73C",    # Verde
    "Pública": "#0D8F55",     # Verde más oscuro
    "Protegida": "#A48012"    # Naranja 
}

# Graficar
plt.figure(figsize=(12, 6))
sns.barplot(data=datos_melted, x="provincia", y="valor_superficie", hue="variable", palette=colores_personalizados) #alargada
plt.title("Superficie del uso del suelo por provincia (2023)") 
plt.ylabel("Superficie")
plt.xlabel("Provincia")
plt.legend(title="Tipo de Suelo")

plt.show()
nombre_archivo_grafico_zonas_verdes = 'usos de suelo.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()



datos_suelo_2023 = datos_actualizados_provincia[["provincia", "sup_agricola_2023", "sup_forestal_2023", "sup_forestal_publica_2023", "esp_proteccion_2023"]]
datos_para_correlacion = datos_suelo_2023[['sup_agricola_2023', 'sup_forestal_2023',
                                         'sup_forestal_publica_2023', 'esp_proteccion_2023']]
cor_matrix = datos_para_correlacion.corr() #matriz de correlacion

plt.figure(figsize=(9, 7)) 
sns.heatmap(cor_matrix,annot=True,cmap="BrBG",center=0, vmin=-1,vmax=1) 
plt.title("Matriz de correlación entre usos del suelo (2023)")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0) 
plt.show()
nombre_archivo_grafico_zonas_verdes = 'matriz de correlacion.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()

datos_actualizados = pd.DataFrame(datos_actualizados)
df_sin_cae = datos_actualizados[~datos_actualizados['provincia'].isin(['CAE'])]


plt.figure(figsize=(10, 6))
df_sin_cae.groupby("provincia")["esp_proteccion_2023"].mean().sort_values().plot(kind="barh")
plt.title("Promedio de superficie protegida por provincia")
plt.xlabel("Superficie protegida")
plt.ylabel("Provincia") 
plt.tight_layout()
plt.show()
pnombre_archivo_grafico_zonas_verdes = 'grafico especial proteccion.png'
ruta_guardado_grafico_zonas_verdes = os.path.join(carpeta_graficos, nombre_archivo_grafico_zonas_verdes)
plt.savefig(ruta_guardado_grafico_zonas_verdes)
plt.close()


