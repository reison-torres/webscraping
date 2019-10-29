#!/usr/bin/env python
# coding: utf-8

# __Cargamos las librerias Phython__

# In[34]:


import urllib3 # Libreria para descargar URL
import re # Libreria para exprecion regular
import numpy as np # Libreria para crear manipulacion de array
import pandas as pd # Libreria para crear manipulacion de DataFrame


# __Definicion de funciones__
# ********
# 
# 
# **_Funcion:download_**
# 
# Funcion para descargar el sitio web

# In[3]:


# download: funcion para descargar el sitio web
# parametros in:
# url: direccion del sitio web
# num_retries: numeros de reintentos de la solicitud en caso de error
# user_agent: informacion de la peticion por defecto el valor 'wswp' (Estandar web scraping con Python)
def download(url,user_agent='wswp',num_retries=2):
    print ('Downloading:', url)
    
    headers = {'User-agent': user_agent}
    
    http = urllib3.PoolManager()
    response = http.request('GET', url, retries=False,headers=headers)
    
    if response.status == 200:
        html = response.data
    else:
        print('Download error: cod_status => ', response.status)
        html = None
        if num_retries > 0:            
            if 500 <= response.status < 600:                
                # retry 5XX HTTP errors                
                return download(url, user_agent, num_retries-1)
    
    return html.decode('utf-8')


# **_Funcion: extractData_**
# 
# Esta funcion extrae los datos del HTML, por medio de patrones utilizando expreciones regulares

# In[30]:


# extractData: extrae los datos del HTML
# parametros in:
# html: HTML de la pagina web descargada
def extractData(html):
    colum_names = ['grupo','nombre','presentacion','cantidad','unidad','cal_extra','cal_primera','valor','fecha_publicacion']
    array_html = re.findall('<img src="../img/logosolo.gif" align="bottom" />(.*?)<br />.*?<div class="table-responsive">(.*?)</div><b>', html,flags=re.DOTALL)
    df_data = pd.DataFrame(columns=colum_names)
    for html_grupo in array_html:
        grupo = re.findall('(.*?) Actualizado el: (.{10})', html_grupo[0],flags=re.DOTALL)
        tbody_tr = re.findall('<tbody>(.*?)</tbody>', html_grupo[1],flags=re.DOTALL)
        array_data = re.findall('<tr.*?>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?<td.*?>(.*?)</td>.*?</tr>', tbody_tr[0],flags=re.DOTALL)
        
        #creamos array con los datos
        col_grupo = np.full((len(array_data),1), grupo[0][0]) # crear columna grupo
        col_fpublicacion = np.full((len(array_data),1), grupo[0][1]) # crear columna fecha publicacion
        all_data = np.hstack((col_grupo,array_data,col_fpublicacion)) # crear dataset

        df_data = df_data.append(pd.DataFrame(all_data,columns=colum_names),ignore_index=True)
        #print(array_data)
        #print(all_data)
    return df_data


# __Descargamos HTML del sitio web__

# In[5]:


url = 'https://www.corabastos.com.co/sitio/historicoApp2/reportes/prueba.php'
html = download(url)
# print("html => ", html)


# __Extraer los datos del HTML y Creamos el DataSet__

# In[36]:


df_data = extractData(html)
df_data.head(10) # mostramos las primeras 10 filas del dataset


# **Exportamos el DataSet a un archivo con formato CSV**

# In[45]:


#print(df_data.loc[0,'fecha_publicacion'])
df_data.to_csv('../data/datos_' + df_data.loc[0,'fecha_publicacion'] + '.csv',index=False)


# In[ ]:




