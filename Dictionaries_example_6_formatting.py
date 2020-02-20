D = {'foo':{'meow':1.23,'mix':2.34}, 'bar':{'meow':4.56, 'mix':None}, 'baz':{'meow':None,'mix':None}}


def dict2txt(D, writefile, column1='-', delim='\t', width=20, order=['mix','meow']):
  import csv
  with open( writefile, 'w' ) as f:
    writer, w = csv.writer(f, delimiter=delim), []
    head = ['{!s:{}}'.format(column1,width)]
    for i in order: head.append('{!s:{}}'.format(i,width))
    writer.writerow(head)
    for i in D.keys():
      row = ['{!s:{}}'.format(i,width)]
      for k in order: row.append('{!s:{}}'.format(D[i][k],width))
      writer.writerow(row)