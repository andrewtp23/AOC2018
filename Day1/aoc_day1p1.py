fname = 'day1b.txt'

total = 0
total_list = []
duplicates = []

with open(fname) as f:
    content = f.readlines()
    content = [y.strip() for y in content] 
    for i in content:
      if i[0] == '+':
        x = i.split('+')
        total += int(x[1])
      elif i[0] == '-':
        x= i.split('-')
        total -= int(x[1])
      else:
        pass
      total_list.append(total)

sl = total_list

dup = 0

for z in total_list:
  y = 0
  if z in sl and y > 0:
    dup = z
    break
  if z in sl:
    y +=1

print(dup)

print(total)