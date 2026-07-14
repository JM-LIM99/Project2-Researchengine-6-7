# Moteur de recherche des lettres 6, 7 (Stagiaire de CERES)

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
