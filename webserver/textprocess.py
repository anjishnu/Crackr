import string

print "textprocessing module loaded"

text = "jobtabs.txt"

def parser(text):
    f = open(text,'r+')
    lsts = []
    for line in f:
        tmp = line.split('\t')[8]
        #Comment this out to remove the preprocessing step
        tmp = preprocess(tmp)
        lsts += [tmp]
    return lsts

def bigstringify(lst):
    bigstr = ''
    for item in lst:
        bigstr += item
    return bigstr

def preprocess(text):
    #text can be a big or small string
    st = ''
    for letter in text:
        if letter in string.whitespace[:-1]:
            st += ' '
        elif letter in '.,?!/\\()[]{}':
            st += ' '+letter+' '
        elif letter in '~`-*()[]{}<>)""\':; ':
            st += ' '
        else:
            st += letter
    return st + ' \n'

def run():
    outparse = parser(text)
    bigstr = bigstringify(outparse)
    f = open("big.txt",'w')
    f.write(bigstr)
    f.close()
    print "Execution complete"
    
#f = open("onejob.txt",'r+')

#text = f.read()

