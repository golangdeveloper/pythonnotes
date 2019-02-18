import json

def reloads(f = '../data/m.json'):
  return [json.loads(line) for line in open(f)]

def countstrmap(ss):
  counts = {}
  for x in ss:
    if x in counts:
      counts[x]+=1
    else:
      counts[x]=1
  return counts
def ordermap(m):
  kv=[(k,v) for k,v in m.items()]
  kv.sort(reverse=True)
  return kv
# print(reloads())
print("1 过滤字典")
filter_rs=[rec["name"] for rec in reloads()]
print(filter_rs)
print("2 计数")
cm=countstrmap(filter_rs)
print(cm)
print("3 排序")
print(ordermap(cm))
