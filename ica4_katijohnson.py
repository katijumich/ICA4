# -*- coding: utf-8 -*-
"""ICA4_KatiJohnson.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DzhH3eh20yfaQG6AGWM7KxV7q_1umghF

Please read the lego_setsHB.csv by using Pandas. Then,

1. use the .info() and .describe() functions to have an overall description of the dataset. 

2. use boolean operators find the Lego sets which have star_rating greater than or equal to 4.

3. find the number of Lego sets whose star_rating greater than or equal to 4. (Hint: conside using .count( ) on the specified column)

4. find the average list price for the Lego sets whose star_rating greater than or equal to 4. (Hint: consider specifying the list_price column after obtaining data and before taking the average)

It is OK to submit any number of steps above, but it would benefit if you try all. 

You can upload a Python code, give a link to your Colab or github. Please don't forget to give access when providing such links.
"""

#import pandas module
import pandas as pd
import csv

#import the dataset
with open("/content/drive/MyDrive/CSC302/DATA/lego_setsHB.csv") as f:
  reader = csv.DictReader(f)
  lego_data = list(reader)

#use the .info() and .describe() functions to have an overall description of the dataset. 
df = pd.DataFrame(lego_data)
df.info()
df.describe()

#use boolean operators find the Lego sets which have star_rating greater than or equal to 4

df['star_rating'] = pd.to_numeric(df['star_rating'])
df.loc[df['star_rating'] >= 4 ]

#find the number of Lego sets whose star_rating greater than or equal to 4. (Hint: conside using .count( ) on the specified column)

high_rating_count = df.loc[df['star_rating'] >= 4, ['star_rating']].count()[0]
print("There are", high_rating_count, "lego sets with a star rating of 4.0 or higher")

#find the average list price for the Lego sets whose star_rating greater than or equal to 4. (Hint: consider specifying the list_price column after obtaining data and before taking the average)

df['list_price'] = pd.to_numeric(df['list_price'])
average_list = df.loc[df['star_rating'] >= 4, ['list_price']].mean()[0].round(2)
print("The average list price for lego sets with a 4.0+ rating is $", average_list, sep='',end=".")