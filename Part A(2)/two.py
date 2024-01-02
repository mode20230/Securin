faces = [1, 2, 3, 4, 5, 6]
total = len(faces) ** 2
print("\nCombinations Distribution:")
sum_count={}
combinations = []
for i in range(1,7):
    for j in range(1,7):
        combinations.append(["Die A:" + str(i) ,"Die B:"+str(j)])
        if i+j not in sum_count:
            sum_count[i+j]=1
        else:
            sum_count[i+j]+=1 
for i in range(0, total, len(faces)):
    print(combinations[i:i + len(faces)])
