import streamlit as st
import pandas as pd
import json

data = pd.read_csv("test.csv")
json_data = data.to_json(orient='records')



with open("testj.json",'w') as file:
    file.write(json_data)
    file.close()

with open("testj.json", 'r') as f:
    jsonread = json.load(f)
    # f.close()


prefify_json = json.dumps(jsonread,indent=4)

with open("testj1.json",'w') as ff:
    ff.write(prefify_json)
    ff.close()


with open('testj.json', 'r') as fileloop:
    dataloop = json.load(fileloop)
    fileloop.close()

for item in dataloop:
    date = item['date']
    temp_max = item['temp_max']
    print(f"{date}, {temp_max}")


