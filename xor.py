MOD = 998244353
def getbeauty(n,k,s):
    def modexp(base,exp,mod):
        result = 1
        while exp>0:
            if exp%2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result
    pow2k = modexp(2,k,MOD)
    totalbeauty = 0
    for l in range(n): #iterate across all substrings
        adjacentequal = 0
        

n, k = map(int, input().split())
s = input().strip()
