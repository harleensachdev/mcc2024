def candestroyalltargets(x, N, M, K, a):
    remaininghp = a[:] #list of remaining hp for each target
    arrowsused = 0 
    i = 0 #index first target

    while i<N: #check not last target 
        if remaininghp[i] > 0: #check target is not already destroyed, repeat code till destroyed
            arrowsused+=1 #use 1 arrow
            if arrowsused > K: # ensure arrows are left
                return False 
            power = M*x #calculate arrow power in stages
            for j in range(i,N):
                effect = max(0, power-(j-i)**2) #no negatives
                if effect == 0:
                    break
                remaininghp[j] -= effect # subtract damage from target hp 

        while i<N and remaininghp[i] <= 0:
            i += 1 # go to next target if it isnt last target and target damage is 0 

    return True
def minimumpowerneeded(N,M,K,a):
    left, right = 1, max(a)*2 
    answer = right
    
    while left<=right:
        mid = (left+right)//2
        if candestroyalltargets(mid, N, M, K, a):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

inputdata = """5000 1999506 4"""
data = inputdata.splitlines()
N,M,K = map(int, data[0].split())
a = list(map(int,data[1].split()))
print(minimumpowerneeded(N,M,K,a))
