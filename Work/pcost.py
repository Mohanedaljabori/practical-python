# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    f = open(filename, 'rt')

    rows = csv.reader(f)

    next(rows)

    for row in rows:
        try: 
            total_cost += float(row[1]) * float(row[2])
        except ValueError:
            print('Could not parse', row)
            
    f.close()
    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Work\Data\missing.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)