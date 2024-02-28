import pandas as pd
# Dataframe
std={'id':[1,2,3,4,5],
    'name':['rohit','rakesh','sachin','shubham','varun'],
    'marks':[90,22,4,2,32]
    }
# df=pd.DataFrame(std)
# index=['a','b','c','d']
df=pd.DataFrame(std,index=['a','b','c','d','e'])
print(df)

# Set

s1=set([1,23,4,5])
print(s1)   # ordered


s2={4,3,6,1,7,4}
s3={1,2,9,4,3,6} 
s4=s2|s3
s5=s2&s3
s6=s2-s3
s7=s2^s3

print(s4,s5,s6,s7)