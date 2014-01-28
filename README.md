<b>README:</b>

Keyword extraction is an extremely interesting topic in Information Retrieval- keywords are widely acknowledged to be extremely important in the field of text retrieval, and particularly while developing large scale modern search engines that limit the size of the inverted index used by the system.

In this project we propose to build a system using modern NLP techniques such as Part of Speech Tagging, Brown Clustering and Rapid Automatic Keywords Extraction (RAKE) to use a small initial seed of keywords to generate more candidate keywords in a semi-supervised manner and expose the system as a JSON based web service. 

The service can be launched by going to the webserver module and running the python script serve.py 

$ python serve.py 

Serves the module on a webserver on port 8080 of localhost.

<b><> Technologies and Frameworks Used</b>

Front-end: HTML/CSS/Javascript, Jquery, Bootstrap 

Backend: Python 2.7, web.py 

Part-of-Speech Tagger: Stanford POSTagger with NLTK bindings 

The system also utilizes a C++ implementation of Brown's Clustering Algorithm and Rapid Automatic Keyword Extraction

<b>RAKE: </b>

This system uses a customized implementation of RAKE built on the design by github user Aneesha. (https://github.com/aneesha/RAKE)

<b>Brown Clustering: </b>

This system uses Percy Liang’s Brown Clustering Implementation in C++.
Data:
Datasets for skills and job listings were provided by www.Collegefeed.com and are confidential. 
Terminology Used:
NAIVE: Naive selection of keywords that were already present in the seed corpus. 
RAKE: Keywords extracted via the Rapid Automatic Keyword Extraction Algorithm 
CRAKR: New approach to Keyword Extraction using Part-of-Speech tagging on a candidate document and Brown Clustering on a large corpus of contextual documents.

<b>
Key Software Modules:

serve.py – Main server file
textprocess.py – contains code for textprocessing
postagger.py – interface with the Stanford POS Tagger
rake.py – A customized python implementation of the RAKE algorithm
candygen.py – Contains the implementations of the  Naïve keyword extraction and CRAKR algorithms.
index.html/index_helpers.js – Contains code for the Front end and GUI 

</b>
