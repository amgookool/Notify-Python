from data.other import *
import csv
file_path = 'data/other/coronavirus.csv'


def read_csv(file_path):
    csv_file = csv.reader(open(file_path, 'r'))
    data=[]
    for column in csv_file:
        state_id = column[0]
        state = column[1]
        country = column[2]
        fst_cnfmd = column[4]
        col_arr = column[7:]
        data.append([state_id,state,country,fst_cnfmd,col_arr])
    return data

data = read_csv(file_path)

print(len(data))
#print(data[0])


#import pandas as pd

#corona_file = pd.read_csv('C:/Users/amgoo/Desktop/Notify-Python/data/other/coronavirus.csv',delimiter=',')
# print(corona_file)
