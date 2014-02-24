<> Technologies and Frameworks Used

Front-end: HTML/CSS/Javascript, Jquery, Bootstrap 

Backend: Python 2.7, web.py 

Part-of-Speech Tagger: Stanford POSTagger with NLTK bindings 

The system also utilizes a C++ implementation of Brown's Clustering Algorithm and Rapid Automatic Keyword Extraction
RAKE: This system uses a customized implementation of RAKE built on the design by github user Aneesha. (https://github.com/aneesha/RAKE)
Brown Clustering: This system uses Percy Liang’s Brown Clustering Implementation
Data:
Datasets for skills and job listings were provided by www.Collegefeed.com and are confidential. 
Terminology Used:
NAIVE: Naive selection of keywords that were already present in the seed corpus. 
RAKE: Keywords extracted via the Rapid Automatic Keyword Extraction Algorithm 
CRAKR: New approach to Keyword Extraction using Part-of-Speech tagging on a candidate document and Brown Clustering on a large corpus of contextual documents.
Key Software Modules:

serve.py – Main server file
textprocess.py – contains code for textprocessing
postagger.py – interface with the Stanford POS Tagger
rake.py – A customized python implementation of the RAKE algorithm
candygen.py – Contains the implementations of the  Naïve keyword extraction and CRAKR algorithms.
index.html/index_helpers.js – Contains code for the Front end and GUI 
