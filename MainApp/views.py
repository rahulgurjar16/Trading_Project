from .models import *
import csv
import pandas as pd
from django.http import HttpResponse

# def get_data(request):
#     with open('file.csv', 'r') as file:
#         my_reader = csv.reader(file, delimiter=',')
#         first_line = file.readline()
#         print(first_line)
    


def get_data(request):
     with open('file.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            _, created = CsvData.objects.get_or_create(
                data = ['banknifty','date','time','open','high','low','close','volume'],
                banknifty=row[0],
                date=row[1],
                time=row[2],
                open=row[3],
                high=row[4],
                low=row[5],
                close=row[6],
                volume=row[7]
                )

    # make a copy
        df = df.copy()

        # convert index to datetime
        df.index = pd.to_datetime(df.index)

        # sort the index (evidently required by resample())
        df = df.sort_index()

        aggregation_dict = {
            'volume': 'mean', 
            'open': 'sum', 
            'high': 'sum',
            'low': 'sum',
            'close': 'sum',
            'Adj_Close': 'sum'
        }

        rename_dict = {
            'open': 'first',
            'high': 'max_price',
            'low': 'min_price',
            'close': 'last_price',
            'volume': 'vol (shares)',
            'Adj_Close': 'last',
        }

        return (df.resample(timedelta).agg(aggregation_dict).rename(columns=rename_dict))


