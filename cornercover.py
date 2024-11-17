def coverscorners(testcase):
    results = []
    for n,m,A,B in testcase:
        fitsfigure = (A<=m and B<=n) or (A<=n and B<=m) #checks if subgrid is smaller than actual grid by comparing dimensions
        covercorner = False 
        if A<=m and B<=n: #checks that one of the subgrid dimensions are equal to the grid dimension and the other one is less than its comparable dimension
            covercorner |= (A==m or B==n)
        if A<=n and B<=m:
            covercorner |= (A==n or B==m)
        if fitsfigure and covercorner: #if both conditions are satisfied
            results.append("YES")
        else:
            results.append("NO")
    return results

T = int(input())
testcases = [tuple(map(int, input().split())) for _ in range(T)] #divides input into groups of integers depending on number of test cases
results = coverscorners(testcases)
print("\n".join(results))

