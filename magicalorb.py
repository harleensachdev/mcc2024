import heapq
results = []
def orbformation(t, testcases):
    mod = 10**9 + 7 
    for n,a in testcases:
        maxheap = [-x for x in a] #invert all values (neg to pos or pos to neg)
        heapq.heapify(maxheap) #makes maxheap into a heap structure so when elements are popped, structure is mantained. it also sorts elements
        while len(maxheap)>1:# repeats process until one element left
            y = -heapq.heappop(maxheap) #pops out largest element, negative symbol used to invert values back
            x = -heapq.heappop(maxheap) #pops out second largest element
            newpower = x+2*y #calculates a new power using two large elements
            heapq.heappush(maxheap, -newpower) # pushes new power back into maxheap
        largestpower = -heapq.heappop(maxheap) % mod 
        results.append(largestpower)

    return results

t = int(input())
testcases = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    testcases.append((n,a))
results = orbformation(t, testcases)
print('')
for result in results:
    print(result)
