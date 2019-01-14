'''
@file generate masterList json obj from csv file
@author chin hui han
'''
import pandas as pd
import json
import sys
import csv

def main():
  if len(sys.argv) > 1:
    csv_fn = sys.argv[1]
  else:
    csv_fn = 'temp_db.csv'

  #@TODO check if this way of reading csv is robust to escape chars
  df = pd.read_csv(csv_fn, quoting=csv.QUOTE_NONE, delimiter=r",\s?", engine="python")
  df.sort_values(by="fullname", inplace=True)
  df.reset_index(drop=True, inplace=True)

  def form_name(row):
    return "{} ({})".format(row['fullname'], row['shortform'])

  df['name'] = df.apply(form_name, axis=1)
  df['url'].fillna('', inplace=True)
  with open('./js/masterArr.js','w') as fd:
    fd.write('const masterList = \n')
    fd.write('[\n')
    for ind, row in df.iterrows():
      fd.write('  {\n')
      fd.write('    name: \"{}\",\n'.format(row['name']))
      fd.write('    url: \"{}\"\n'.format(row['url']))
      fd.write('  }')
      if ind < len(df)-1:
        fd.write(',')
      fd.write('\n')
    fd.write(']\n')
  

if __name__ == '__main__':
  main()
