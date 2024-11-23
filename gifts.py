def distributegift(n,m,tier):
    from collections import defaultdict
    tiermap = defaultdict(list)
    print(tiermap)
    
    for idx, tier in enumerate(tiers): #sorts their guest indexes based on their tiers
        tiermap[tier].append(idx)

    sortedtiers = sorted(tiermap.items()) #sorts dict in order of tiers (tier1, tier2...)
    giftsgiven = [0] * n #makes a list of 0s as initially no gifts given [0,0,0,0]*30
    remaininggifts = m #initially no gifts given

    for tier,guests in sortedtiers: #goes in order of priority/tiers
        if remaininggifts == 0: #checks sufficient gifts to move onto next tier
            break
        for guest in guests:
            if remaininggifts>0: #checks sufficient gifts within tier
                giftsgiven[guest] = 1 
                remaininggifts -= 1 
            else:
                break

    return giftsgiven

n, m = input().split()
n = int(n)
m = int(m)
tiers = list(map(int,input().split()))
result = distributegift(n,m,tiers)
print(" ".join(map(str,result)))

