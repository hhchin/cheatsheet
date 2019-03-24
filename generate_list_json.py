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
    csv_fn = 'master.csv'

  rm_quote = lambda x: x.replace('"', '')
  #@TODO check if this way of reading csv is robust to escape chars
  #df = pd.read_csv(csv_fn,  quotechar='\"', quoting=csv.QUOTE_ALL, sep=r",", engine="python", skipinitialspace=True)
  df = pd.read_csv(csv_fn)
  df = df.rename(columns=rm_quote)
  df.sort_values(by="fullname", inplace=True)
  df.reset_index(drop=True, inplace=True)

  def form_name(row):
    return '{} ({})'.format(rm_quote(row['fullname']), rm_quote(row['shortform']))

  #df['name'] = df.apply(form_name, axis=1)
  df['url'].fillna('', inplace=True)
  with open('./js/masterArr.js','w') as fd:
    fd.write('const masterList = \n')
    fd.write('[\n')
    for ind, row in df.iterrows():
      fd.write('{\n')
      if pd.isnull(row['shortform']):
        shortform_str = ''.join([w[0] for w in row['fullname'].split()])
        name_str = row['fullname']
      else:
        shortform_str = row['shortform']
        name_str = '{} ({})'.format(rm_quote(row['fullname']), rm_quote(row['shortform']))
      fd.write('shortform: \"{}\",\n'.format(shortform_str))
      fd.write('name: \"{}\",\n'.format(name_str))
      if row['url'] != "":
        fd.write('url: \"{}\"\n'.format(row['url']))
      fd.write('}')
      if ind < len(df)-1:
        fd.write(',')
      fd.write('\n')
    fd.write(']\n')
  

if __name__ == '__main__':
  main()
