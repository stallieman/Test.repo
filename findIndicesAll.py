from elasticsearch import Elasticsearch
from elasticsearch import exceptions
import json

try:

    # declare a client instance of the Python Elasticsearch library
    client = Elasticsearch("http://localhost:9200")

    # pass client object to info() method
    elastic_info = Elasticsearch.info(client)
    print ("Cluster info:", json.dumps(elastic_info, indent=4 ))

except Exception as err:
    print ("Elasticsearch client ERROR:", err)
    client = None

# if client is not 'None'
if client != None:

    # returns a list of all the cluster's indices
    all_indices = client.indices.get_alias("*")

    # print all the attributes for client.indices
    print (dir(client.indices), "\n")

    # iterate over the index names
    for ind in all_indices:
        print (ind)
