from collections import defaultdict

kolumny = ["A","B","C","D","E"]
data = [["A","C","D"],
           ["B","C","E"],
           ["A","B","C","E"],
           ["B","E"]]


def Asocjacja(items: list, minSupp: float, minConf: float):
	
    supp = int(minSupp * len(items))

    itemset = {x:0 for x in kolumny}
    fsets = []
    w = 0
    while True:

        for x in itemset:
            for y in items:
                if all(z in y for z in x):
                    itemset[x] += 1

        arr = list(itemset.keys())
        for x in arr:
            if itemset[x] < supp:
                del itemset[x] 

        arr = list(itemset.keys())
        fsets.extend(arr)

        newitemset = []

        for i,x in enumerate(arr):
            for y in arr[i+1:]:
                newitemset.append("".join(sorted(set(list(x) + list(y)))))

        #print(arr)
        
        if len(arr) <=1:
            arules = []
    

            a = arr[0]
            for i,x in enumerate(list(a)):
                tab1 = a[:i]
                tab2 = a[i+1:]
                tab = tab1+tab2
                one = 0
                rest = 0

                for y in items:
                    if all(z in y for z in tab):
                        rest += 1
                    if x in y:
                        one += 1

                #print(rest,one)
                if one>0 and rest/one >= minConf:
                    arules.append(f"{x} -> {tab} with confidence {rest/one:.2f}") 

            return [fsets,arules]

        itemset = {x:0 for x in newitemset}

    

print(Asocjacja(data,0.5,0.66))
        