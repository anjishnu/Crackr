import cPickle as pickle
from collections import defaultdict

filepath = "skills.csv"
def parser(filepath):
    f = open(filepath,'r')
    count=0
    index = defaultdict(int)
    for line in f:
        line = line.lower()
        line=line.replace('"',' ')
        splitline= line.replace('&',',').replace('and',',').split(',')
        for word in splitline:
            word = word.strip()
            index[word]+=1
        count+=1
        #print ne.lower()
    print "Number of skills parsed", count
    return index

def smoother(index):
    #the smoother function takes the parsed output of
    #skillparser and removes all elements that have only
    #one occurrance (could be typos etc)
    d = defaultdict()
    for key in index:
        if index[key]>1:
            d[key]=index[key]
    return d

def pickledata(index,filename):
    f = open(filename,'w')
    pickle.dump(index,f)
    f.close()
    print "Successfully pickled in ", filename

def skillsort(index):
    #Converts the output of parser/smoother into a sorted list
    #So we can find the top skills available.
    lst = []
    for key in index:
        lst += [(key,index[key])]
    return sorted(lst, key=lambda x: x[1], reverse=True)
    