# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 02:20:37 2018

@author: Rami Yousfi & Aymen Hamrouni
"""

import os
import numpy as np
from PIL import Image

from flask import Flask, request, render_template

from pymongo import MongoClient
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt 
os.environ['CUDA_VISIBLE_DEVICES'] = ''

def index_data():
    return 0;
    
def calcDistance(pic1,pic2):
    result=float(0)
    for i in range(0,len(pic1)):
        result+=(float(pic1[i])-float(pic2[i]))**2
    #dist.euclidean(pic1, pic2)
    return result

app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    client=MongoClient('mongodb://localhost:27017/Tp_Photos')
    db=client.DB_Photos
    collection=db.collection_edge
    if request.method == 'POST':
        file = request.files['query_img']

        img = Image.open(file.stream)  # PIL image
        uploaded_img_path = "static/img/0/" + file.filename
        img.save(uploaded_img_path)
        index = file.filename.split('.')[0]
        index = int (index)
        cluster=collection.find({"index":index})[0]["cluster"]
        cluster_picture_edge=[]
        for col in collection.find({"cluster":cluster}):
            cluster_picture_edge.append(col)
        similar_picture=[{"result":0,"index":cluster_picture_edge[0]["index"]}]
        for k in range(1,len(cluster_picture_edge)):
            result=calcDistance(cluster_picture_edge[0]["edge_value"],cluster_picture_edge[k]["edge_value"])
            similar_picture.append({"result":result,"index":cluster_picture_edge[k]["index"]})
        similar_picture=sorted(similar_picture,key=lambda x:x["result"])
        #path='C:/Users/Rami/Desktop/tp/Image-to-Image-search-master/static/img/'
        path='/static/img/0'
        answers =[] 
        for j in range(1,len(similar_picture)):
            if (j == 6): break
            answers.append([path+'/'+str(similar_picture[j]["index"])+'.jpg',' '])

        print(answers)
        

        return render_template('index.html',
                               query_path=uploaded_img_path,
                               answers=answers)
    else:
        return render_template('index.html')

if __name__=="__main__":
    try:
        index_data()
    except Exception as e:
        pass
    app.run("127.0.0.1", debug=False)
