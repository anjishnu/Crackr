import textprocess, cPickle as pickle
from collections import defaultdict
import postagger as pt


#Loading important files
skills = pickle.load(open("skillset.dat"))
paths_loc = "clusters.txt"
#Loaded clusters trained using Brown Clustering
 

def performTask(rawtext):
    text=textprocess.preprocess(rawtext)
    POS_text = pt.tag(text)
    print POS_text
    #Didn't do toLower earlier because the stanford tagger might make
    # use of the capitalizations
    text = text.lower()
    skilldict = buildskilldict(skills)
    naive_skills= generate_naive(text,skilldict)
    expanded_skills = new_guesses(POS_text,naive_skills,words,clusters)
    return naive_skills, expanded_skills

#joblisting = open("onejob.txt",'r').read()
#jl = textprocess.preprocess(joblisting)

def parse_paths_file(paths_loc):
    f = open(paths_loc,'r')
    words = defaultdict(list)
    clusters = defaultdict(list)
    for line in f:
        cluster, word, nums = line.split()
        words[word] = [nums,cluster]
        clusters[cluster] += [(word,nums)]
    return words, clusters

words, clusters = parse_paths_file(paths_loc)
print "Clusters successfully loaded"

def buildskilldict(skills):
    sd = defaultdict()
    for tup in skills:
        skills, count = tup
        sd[skills]=count
    return sd

def generate_naive(jl,skilldict):
    lst = []
    jl=jl.split()
    for word in jl:
        if word in skilldict:
            lst +=[word]
            #print lst
    #bigrams
    for index in range(len(jl)-1):
        bigram = jl[index]+' '+jl[index+1]
        if bigram in skilldict:
            lst+=[bigram]
    #trigrams
    for index in range(len(jl)-2):
        trigram = jl[index]+' '+jl[index+1]+' '+jl[index+2]
        if trigram in skilldict:
            lst+=[trigram]
    return set(lst)

def new_guesses(jlpos,skillist,words,clusters):
    #Note: skillist here is the output of generate_naive
    viableclusters = []
    for skill in skillist:
        try:
            viableclusters += [words[skill] [1]]
        except:
            print skill
    viablewords = []
    for cluster in set(viableclusters):
        for tup in clusters[cluster]:
            word, count = tup
            viablewords+=[word]
    viablewords = set(viablewords)
    finallst = []
    index = 0
    indices = []
    thirdlst = []
    for tup in jlpos:
        word, tag = tup
        if tag=='CC':
            print word
            print jlpos[index-1] [1] [0], jlpos[index-1] [1] [0] 
        if tag[0]=='N' or tag[0]=='J' or (tag=='CC' and jlpos[index-1] [1] [0]=='N'):
            if word.lower() in viablewords:
                finallst += [(word)]
                indices +=[index]
                thirdlst += [(word,index)]
        index+=1
    #print finallst
    #print indices
    finallst2 = stich(finallst,indices)
    """
    for word in jl.split():
        if word in viablewords:
            finallst+=[word]
    """
    return finallst,finallst2,thirdlst

def stich (words,indices):
    #Stiches proximate words together to form longer keywords
    output = []
    prev = -1
    buff = []
    for i in range(len(indices)):
        index = indices[i]
        if index == prev+1:
            buff +=[words[i]]
            #print "buffer is ",buff
        else:
            #dump
            tstr = ""
            for word in buff:
                tstr += word+' '
            if tstr.strip()!= '':
                output += [tstr.strip()]
            buff = []
            buff +=[words[i]]
            #print "buffer is ",buff
 
        prev = index

    return output
