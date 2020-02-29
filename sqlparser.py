from nltk.stem import WordNetLemmatizer
import re

from nltk.tokenize import word_tokenize
class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 

def action_PK(tables_pk,table_name,line):
    y=line.split("(")[1].split(")")[0]
    #print(y+" "+table_name)
    y=y.replace("`","")
    l=y.split(",")
    tables_pk.add(table_name,l)

file1=open("smart_bot.sql")
lines=file1.readlines()
s="CREATE TABLE"
a="ALTER TABLE"
pk="ADD PRIMARY KEY"
isKey=False
tables=[]
table_attributes={}
tables_pk=my_dictionary()
table_name=""
for line in lines:
    #print(line)
    if(isKey):

        if(line.find(pk)!=-1):
            action_PK(tables_pk,table_name,line)
            isKey=False
        #else:
            #action_constraint(tables_relation,table_name,line)
    else:
        x = re.findall("\A"+s+"",line)
        if(x):
            #print(x)
            y=word_tokenize(str(line))
            tables.append(y[3])
        # if(x):
        #     size=len(x[0])-1
        #     x=x[0][14:size]
        #     tables.append(x)
        #     table_attributes[x]=[]
        #     for j in range(i+1,len(lines)):
        #         if(not re.findall(r';$',lines[j])):
        #             s=lines[j].split()[0]
        #             s=s[1:len(s)-1]
        #             table_attributes[x].append(s)
        #         else:
        #             break
        else:
            y=re.findall("\A"+a+"",line)
            if(y):
                p=word_tokenize(str(line))
                table_name=p[3]
                isKey=True 
                    

# x1=input("enter your query")
# y1=x1.split(" ")
# for d in y1:
#     if(d in tables):
#         sql="select * from "+str(d)
#         print(sql)

print(tables_pk)   
