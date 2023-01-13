from collections import defaultdict

kolumny = ['BA', 'CA', 'BC']
data = [["A","B","C"],
           ["C","D"],
           ["A","B","C"]]
supp = 2

itemset = {x:0 for x in kolumny}
fset = []
for x in itemset:
    for y in data:
        if all(z in y for z in x):
            itemset[x] += 1

arr = list(itemset.keys())
for x in arr:

    if itemset[x] < supp:
        del itemset[x]

arr = list(itemset.keys())
fset.extend(arr)

newitemset = []

for i,x in enumerate(arr):
    for y in arr[i+1:]:
        newitemset.append("".join(sorted(set(list(x) + list(y)))))
        #print(list(x) + list(y))
itemset = set(newitemset)
print(sorted("bca"))
print(arr)
print(newitemset)
print(itemset)