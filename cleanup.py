import pandas as pd
import csv
import sys


def main():
  if len(sys.argv) > 1:
    csv_fn = sys.argv[1]
  else:
    csv_fn = 'temp_db.csv'

  df = pd.read_csv(csv_fn)
  df = df.drop_duplicates(['fullname'], keep='first')
  df = df.sort_values(by='shortform')
  df.to_csv(csv_fn, index=False, quoting=csv.QUOTE_ALL)

if __name__ == '__main__':
	main()