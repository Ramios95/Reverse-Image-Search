
# Reverse-Image-Search
**Reverse Image Search Engine** Using **MongoDB** and **Edge Histogram Distance**


# Search by image: 

Give it an image and it will return the similar images based on the images in the database using **Edge Histogram Distance**.<br/>
Uses MongoDB as it's search engine(can Be configured to use Elasticsearch instead).<br/>


# Packages Required: <br/>
- Anaconda <br/>
- Keras with Tensorflow Backend (Python 3.6) <br/>
- (MongoDB and pymongo or Elastic Search and elasticsearch-py (Elastic Search 6.0) ) <br/>


# Output<br/>


**Home Page**
![
](https://i.imgur.com/N0TF7is.png)
**Uploaded Picture 1**
![
](https://i.imgur.com/7VJkqNi.png) <br/>
<br/>
**Uploaded Picture 2** <br/>
<br/>
![
](https://i.imgur.com/UzmJX9C.png)


# Files:

FilltheDB.py : Parses the eh files in the MongoDB  (or Elasticsearch) with their indexes and clusters. <br/>
StartMe.py : launches the webapp to do the reverse image search (Webapp) [ http://localhost:5000 ]. <br/>

# How To Use :

To Use : <br/>
- In fillwithDB.py change D:/aim/tp search/static/eh_descriptors/ehi.txt (i in x) to your where about files. <br/>
- Start FillwithDB.py at first to fill the MongoDB (You'll find the name of the Database in the file). <br/>
- Now that the MongoDB has the path of the images and it's Edge Histogram , Start StartMe.py. <br/>
- Now go to the browser and enter : http://localhost:50000.
