cook_book = {}
#value
file=open('text.txt', encoding="utf8")
k=0
key_list = ['ingredient_name', 'quantity','measure']
for line in file:
  k+=1
  if k==1:
    Value_List=[]
    key=line[:-1]
  elif k==2:
    num = int(line)
  elif k>num+2:
    k=0
    cook_book[key]=Value_List
  else:
    line=line[:-1]
    value_list = line.split(" | ")
    value_dict = dict(zip(key_list, value_list))
    Value_List. append(value_dict)
file.close()    
#print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingredient in cook_book[dish]:
      if ingredient['ingredient_name'] in shop_list:
        shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
      else:
        shop_list[ingredient['ingredient_name']] = {'quantity': int(ingredient['quantity']) * person_count, 'measure': ingredient['measure']}
  return shop_list        

it = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for k in it:
  print(k,it[k])
