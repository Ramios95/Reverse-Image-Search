# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 03:22:36 2018

@author: Rami Yousfi & Aymen Hamrouni
"""

#import helper library
from sklearn.cluster import KMeans
import numpy as np
from pymongo import MongoClient
import matplotlib.pyplot as plt

#connect to database
client=MongoClient('mongodb://localhost:27017/Tp_Photos')
db=client.DB_Photos
collection=db.collection_edge

directory='D:/aim/tp search/static'
dir_edge = 'eh_descriptors'

table_edge=[]
with open(directory+'/'+dir_edge+ '/'+'eh'+str(1)+'.txt','r') as f:
    lines = f.readlines()
for i in lines:
    table_edge.append(i.split())



array_edge=np.array(table_edge)
Kmeans=KMeans(n_clusters=20).fit(array_edge)
#assign every image the cluster that it belongs to 
Clusters=Kmeans.predict(array_edge)
centroids = Kmeans.cluster_centers_
for k in range(0,10000):
    cluster=str(Clusters[k])
    line_DB={"index":k,"edge_value":table_edge[k],"cluster":cluster}
    collection.insert_one(line_DB)
    