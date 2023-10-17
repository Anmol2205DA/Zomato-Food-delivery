import pandas as pd
import jsonlines

df=pd.read_csv('data/required.csv')
dic_cuisine={}
dic_address={}
for i in range(df.shape[0]):
    # print(df.c[i],df.cuisine[i])
    dic_cuisine.update({df.c[i]:df.cuisine[i]})
    dic_address.update({df.address[i]:df.restaurant_address[i]})


print(dic_cuisine,dic_address)