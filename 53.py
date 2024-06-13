import pandas as pd

data = {
    '2014': [100.5, 150.8, 200.9, 30000, 40000],
    '2015': [12000, 18000, 22000, 30000, 45000],
    '2016': [20000, 50000, 70000, 100000, 125000],
    '2017': [50000, 60000, 70000, 80000, 90000]
}

sales_persons = ['Madhu', 'Kusum', 'Kinshuk', 'Ankit', 'Shruti']

df = pd.DataFrame(data, index=sales_persons)

print(df)
