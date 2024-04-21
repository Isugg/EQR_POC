from datetime import datetime
from elasticsearch import Elasticsearch
import pandas as pd
from queries import queries
from user_api_key import my_api_key

#Add your own my_api_key.py with your API key. Create mitigating controls around this file.
es = Elasticsearch("https://10.0.0.200:9200", api_key=my_api_key, verify_certs=False)


with open('report.csv', 'a+') as report:
    report.write("Question Number, Username, Hostname, Event code\n")
    for i,q in enumerate(queries):
        resp = es.search(index="*security-**", query=q)
        for hit in resp["hits"]["hits"]:
            name = hit["_source"]['user']['name']
            host = hit["_source"]['host']['name']
            event_code = hit["_source"]['event']['code']
            report.write(f"Question Number: {i+1},"+name+","+host+","+event_code+"\n")


df = pd.read_csv('report.csv').fillna('')

print(df)
