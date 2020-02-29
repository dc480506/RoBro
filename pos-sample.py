import nltk
import pickle
import json
from nltk.stem import WordNetLemmatizer 
with open('table_attributes.json') as f:
    table_attributes = json.load(f)
print(table_attributes) 
with open('tables_pk.json') as f:
    tables_pk = json.load(f)
print(table_attributes)
tables= pickle.load( open( "tables.p", "rb" ) )
print(tables)
tables_attributes= pickle.load( open( "tables_relation.p", "rb" ) )
print(table_attributes)
def isWhere(pos):
    for i in range(len(pos)):
        if(pos[i][1]=='WP$' or pos[i][1]=='WRB'):
            return i
    return -1

def getAttributes(second_part):
    gr=r"Chunk1: {<CC>?(<NN.?><VB.?>(<JJ.?>*|<IN>)*(<NN.?>|<CD>))*}"

    chunkParser=nltk.RegexpParser(gr)
    chunked=chunkParser.parse(second_part)
    chunked=str(chunked)

    chunked=chunked[3:len(chunked)-1]
    chunked=chunked.split("\n")
    l=[]
    ll=[]
    dic={}

    for line in chunked:
        temp=line[3:len(line)-1].split(" ")
        for j in range(len(temp)):
            l.append(temp[j].split(",")[0])

        ll.append(l[1:])
        l=[]

    #print(chunked)
    print(ll)
    
def findTable(match):
    best_match_list=[]
    for i in tables:
        if i.find(match)!=-1:
            q=[]
            diff=len(i)-len(match)   
            q.append(i)
            q.append(diff)
            best_match_list.append(q)
    best_match_list.sort(key = lambda x: x[1])
    print(best_match_list)
lemmatizer = WordNetLemmatizer()
sample_text=input("Enter your question: ")
tokenized=nltk.word_tokenize(sample_text)
l=[]
for i in tokenized:
    l.append(lemmatizer.lemmatize(i))
pos=nltk.pos_tag(l)
print(pos)
tname=""
p=isWhere(pos)
if(p!=-1):
    first_part=pos[0:p]
    second_part=pos[p+1:]
    getAttributes(second_part)
    tname=findTable(first_part[-1][0])
    #print(first_part)
    # print("ahdkjd")
    #print(second_part)

nouns_list=[i[0] for i in pos if i[1].startswith("N")]
adverbs_list=[i[0] for i in pos if i[1].startswith("R")]
preposition_list=[i[0] for i in pos if i[1].startswith("IN")]
print(nouns_list)
print(adverbs_list)
print(preposition_list)
