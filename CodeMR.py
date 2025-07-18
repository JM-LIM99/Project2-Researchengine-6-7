
#reference : https://github.com/Antonomaz/tools/tree/master/Produce_Biblio_html

import pandas
import datetime
from datetime import date
import pandas as pd #utilisation pansdas ; datetime  / Using pandas

date_str = date.today().strftime("%d/%m/%Y")
path_xls = "xlsx" #stock excel(ficher) et path de excel / datetime, Excel file and its path

xls = pandas.ExcelFile(path_xls)
df = pandas.read_excel(xls, sheet_name ='Worksheet')

#-dictionnaire
dic ={}

for line in df.iterrows(): # classifier des donneés pour l'étape suivante / Classify the data for the next step
    
    id_base = line[1].iloc[0]
    ID = str(id_base)
    value = list(line[1].values[1:])
    nom_infos = ["Surname","First name","Orignal_Location","Date_year","Month","Day","Current_location","City","County","My_notes","Index_page","Notes_written_on_the_letter"]
    try:
        value[3] = int(value[3])
    except:
        pass
    try:
        value[4] = int(value[4])
    except:
        pass
    try:
        value[5] = int(value[5])
    except:
        pass
    try:
        value[10] = int(value[10])
    except:
        pass
    value = dict(zip(nom_infos, value))
    dic[ID] = value
as_list = [[cle, val["Surname"]] for cle, val in dic.items()
          
#-Json

import json
import re
for nom, struct in [["liste", as_list],["dico", dic]]:
    path_out = f"/{nom}_titires_ID.json" #stocker en Json / Store in JSON
    print(path_out, "w")
    w= open(path_out, "w")
    w.write(json.dumps(struct, indent = 2, ensure_ascii=False))
    w.close()  
# mettre des index en Html.  /  Add indexes in HTML 
with open("test.html", encoding="utf-8") as f:
    header =f.read()
with open("test.json") as f:
    dic_titres = json.load(f)
out = ""
table_header = []
cpt = 0
test = []
for ID, infos in dic_titres.items():
    if len(table_header) == 0:
        table_header = infos.keys()
        out+=" <tr><th>ID</th><th>%s</th><tr>\n"%"</th><th>".join(table_header) #créer les tableaux  / Create the tables
    elems =[infos[cle] for cle in table_header]
    test.append([len(str(infos["Orignal_Location"])),infos["Orignal_Location"]]) #  Ajoute longueur et valeur de Original_Location à test. /  Add the length and value of Original_Location to test.
    elems = [str(x) if str(x) not in ["null", "None", "nan"] else "" for x in elems] # 
    link = f"id=\"{ID}\""
    this_info = "</td><td>".join(elems)
    l = f" <tr><td>{ID}</td><td>{this_info}</td></tr>\n"
    out +=l

out_html = re.sub("{{content_table}}", out, header)
out_html = re.sub("{{date}}", date_str, out_html)
with open("test.html", "w", encoding="utf-8") as w:
    w.write(out_html)