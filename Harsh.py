'''
Analyze a sales dataset to identify trends in product sales over time.
Calculate the total sales, average sales per product, and sales by region. 
Use Pandas to handle data grouping and aggregation.
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics



df=pd.read_csv("C:\\Users\harsh\OneDrive\Documents\stock_prices.csv")
c=0
d={'daily returns':[],'moving average':[],'volatility':[]}
while(c<=90):
    daily_returns=0
    moving_average=0
    l=[]
    for j in range(10):
        daily_returns+=((df.loc[c,'Close']-df.loc[c,'Open'])/(df.loc[c,'Open']))*100
        l.append(daily_returns)
        moving_average+=df.loc[c,'Close']
        c+=1
    d['daily returns'].append(float(daily_returns/10))
    d['moving average'].append(float(moving_average/10))
    d['volatility'].append(statistics.stdev(l))


var=pd.DataFrame(d, index=['Apple','Microsoft','Google','Amazon','Meta','Tesla','Netflix','Nvidia','IBM','Intel Core'])
print(var)


def closep():
    u=0
    while(u<=90):
        x=[]
        y=[]
        label = df.loc[u, 'Symbol']
        for j in range(10):
            x.append(df.loc[u,'Date'])
            y.append(float(df.loc[u,'Close']))
            u+=1

        print(label)
        plt.plot(x,y, label=label)

    plt.title('Closing price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid()
    plt.show()
closep()


def additional_features(input):
    o=0
    y=[]
    x=['Apple','Microsoft','Google','Amazon','Meta','Tesla','Netflix','Nvidia','IBM','Intel Core']
    for i in range(10):
        y.append(var.loc[x[o],input])
        o+=1
    plt.scatter(x,y,c=[10,20,30,40,50,60,70,80,90,100], cmap='viridis')
    plt.xlabel('Companies')
    plt.ylabel(input)
    plt.colorbar()
    plt.grid()
    plt.show()
a=input("enter daily returns or moving average or volatility")
additional_features(a)













