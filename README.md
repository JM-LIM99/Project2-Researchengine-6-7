# Moteur de recherche des lettres 6, 7 (Stagiaire de CERES)
L'object de ce code:
Il s'agit de créer un moteur de recherche afin de faciliter la consultaion des lettres(un index manuscrit réalisé par Maria Hooker : 76 volumes) et de développer une carte permettant de visualiser les lieux d'envoi de cette correspondance.

référence de Code de python : https://github.com/Antonomaz/tools/tree/master/Produce_Biblio_html

1. utilisation module : pandas,  datetime , json , re.

2. import le ficher d'excel. chaque données doit avoir l'identification.

3. créer des dictionnaire

4. créer Json des donées

5. mettre sur HTML en forme de tableaux



référence de HTML : https://datatables.net/forums/discussion/25346 et https://github.com/Antonomaz/tools/tree/master/Produce_Biblio_html

1. utilisation de *datatable

2. mettre login form.   Une fois connecté, la fenêtre de connexion disparaît.

3. secretInfo, hidden-col pour cacher des informations

4. Ajouter une fonctionnalité de recherche pour chaque colonne

5. Créer une boîte pour afficher les pages d’index et les notes

Map. référence : naver blog et Chat GPT pas de Geopy


1. Créer un JSON contenant les longitudes et latitudes : je l’ai réalisé manuellement avec l'expression régulière, car Geopy impose une limite de requêtes.

2. récupère le nom et l'années; utiliser "clearLyers"  

3. recherche des donées pertinentes et stocker dans locationCoubts

4. afficher des données par circle: 

5. la taille de circle varie en fonction du nombre des lettres



lien des résultats

https://ceres.huma-num.fr/lettres/recherche

https://ceres.huma-num.fr/lettres/carte


------------English-----------------
Objective of this code:
The purpose is to create a search engine to facilitate the consultation of the letters (a handwritten index compiled by Maria Hooker: 76 volumes) and to develop a map to visualize the places from which this correspondence was sent.



Python code reference: https://github.com/Antonomaz/tools/tree/master/Produce_Biblio_html

1.use modules: pandas, datetime, json, re.

2. import the Excel file. each data item must have an identifier.

3. create dictionaries

4. create the data as JSON

5. output to HTML in table format

HTML reference: https://datatables.net/forums/discussion/25346 and https://github.com/Antonomaz/tools/tree/master/Produce_Biblio_html

1. use DataTable

2. add a login form. once logged in, the login window disappears.

3. secretInfo, hidden-col to hide information

4. add a search feature for each column

5. create a box to show the index pages and notes

Map reference: Naver Blog and ChatGPT (no Geopy)

1. Create a JSON containing longitudes and latitudes: I did it manually using a regular expression, because Geopy imposes a request limit.

2. Retrieve the surname and year; use clearLayers.

3. Search for relevant data and store it in locationCounts.

4. Display the data as circles.

5. The size of the circles varies according to the number of letters.

Link :

https://ceres.huma-num.fr/lettres/recherche

https://ceres.huma-num.fr/lettres/carte



6월 7월 CERES 인턴 임정민  