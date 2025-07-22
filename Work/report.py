# report.py
#
# Exercise 2.4
import csv
import sys

def read_portfolio(filename):
    portfolio = []
    f = open(filename, 'rt')

    rows = csv.reader(f)

    next(rows)

    for row in rows:
        try: 
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
        except ValueError:
            print('Could not parse', row)
            
    f.close()
    return portfolio

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work\Data\portfolio.csv'

portfolio = read_portfolio(filename)
print('Portfolio', portfolio)
