n = int(input())
pairs = [tuple(map(int, input().split()))for _ in range(n)]
pairs.sort(key = lambda x:x[0]+x[1],reverse = True) #sorts pairs by sum of a_i and b_i elements in descending order
x,y = 0,0 #e (X) and r (Y) scores
for i in range(n):
    if i%2== 0: #even turn = E, takes maximum
        x += pairs[i][0]
    if i%2 == 1: # odd turn = R, takes minimal
        y += pairs[i][1]
print(x-y)
