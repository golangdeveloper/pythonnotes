import json

def reloads(f = 'm.json'):
  return [json.loads(line) for line in open(f)]

def countstrmap(ss):
  counts = {}
  for x in ss:
    if x in counts:
      counts[x]+=1
    else:
      counts[x]=1
  return counts

# print(reloads())
print("1 过滤字典")
print([rec["name"] for rec in reloads()])
print("2 计数")
print(countstrmap([rec["name"] for rec in reloads()]))
