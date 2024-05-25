# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd

cols = ["sourceDataset", "fieldMaps", "sr", "record"]
rows = []

# Parsing the XML file
xmlparse = Xet.parse('/TC_DataBase/Datafile_28_6_2023/TCbloombergpubTickers/TRAF.xml')
root = xmlparse.getroot()


for i in root:
    psc = i.findall("name").text
    dataset = i.find("sourceDataset").text
    fields = i.find("fieldMaps").text
    datakey = i.find("sr").text
    ticker = i.find("record").text

    rows.append({"sourceDataset": dataset,
                 "fieldMaps": fields,
                 "sr": datakey,
                 "record": ticker,
                 "name": psc })

df = pd.DataFrame(rows, columns=cols)
df.head()
#Writing dataframe to csv
df.to_csv('output.csv')

