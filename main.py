import requests
import xml.etree.ElementTree as ET
import pandas as pd
import gspread as gspread
import datetime as datetime
from gspread_dataframe import set_with_dataframe
from clases import Info

# Aquí ingresar id del spreadsheet que se desea ocupar para almacenar los datos, y json de permisos de service account
###############################################################
sheet_id = ''
service_account_json_file=''
###############################################################

# Instanciamos objeto para guardar la info
info = Info()

# Obtenemos la info con la url para cada país y la guardamos en info.dict
for pais in info.paises:

  print(pais)

  url = 'http://tarea-4.2021-1.tallerdeintegracion.cl/gho_' + pais + '.xml'
  response = requests.get(url)
  tree = ET.fromstring(response.content)

  # Recorremos los nodos de datos del árbol
  for node in tree:
    # Dentro de cada nombre buscamos el indicador GHO y verificamos que se encuentre entre los indicadores deseados (info.indicadores_gho)
    GHO = node.find("GHO")
    indicador = GHO.text if GHO is not None else None
    if indicador in info.indicadores_gho:
      # Guardamos el valor que hay en el tree de cada key de info.dict. los key corresponden a los nombres de los nodos que nos interesa obtener de cada indicador GHO
      for key in info.dict:
        KEY = node.find(key)
        info.dict[key].append(KEY.text) if KEY is not None else info.dict[key].append(None)

# Guardamos info.dict en un DataFrame de Pandas, para pasarlo al Spreadsheet
df = pd.DataFrame(data=info.dict)
df["YEAR"]= df["YEAR"].apply(lambda x: str(datetime.date(int(x), 1, 1)))
df["Numeric"] = pd.to_numeric(df["Numeric"])
df["Low"] = pd.to_numeric(df["Low"])
df["High"] = pd.to_numeric(df["High"])

# Credenciales de Google Cloud
# ACCES GOOGLE SHEET
gc = gspread.service_account(filename=service_account_json_file)
print("CONEXION CON SERVICE ACCOUNT")
sh = gc.open_by_key(sheet_id)
print("OPEN SPREADSHEET")
worksheet = sh.get_worksheet(0) #-> 0 - first sheet, 1 - second sheet etc. 
print("OPEN SHEET")

# APPEND DATA TO SHEET
set_with_dataframe(worksheet, df) #-> THIS EXPORTS YOUR DATAFRAME TO THE GOOGLE SHEET
print("SET DATAFRAME IN SHEET")
