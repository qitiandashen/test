import random
import csv
import json
def Creat_num():
  list1=['139','188','185','155','151','152','153']
  str='0123456789'
  for i in range(100):
    str_res=random.choice(list1)+"".join(random.choice(str)for i in range(8))
    list_res = list(str_res)
    f=json.dumps(str_res)
    print(str_res)
    #print(list_res)
    print(json.loads(str_res))
    #print(type(json.dumps(str_res)))