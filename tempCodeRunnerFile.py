input = """3
2 3 3 3
2 3 2 3
2 3 2 1"""
input = input.split("\n")
input = input[1:]
formattedinput = []
for string in input:
    formattedlist = string.split()
    intformattedlist = list(map(int, formattedlist))
    formattedinput.append(intformattedlist)

for i in range(len(formattedinput)):
    n = formattedinput[i][0]
    m = formattedinput[i][1]
    A = formattedinput[i][2]
    B = formattedinput[i][3]
    
    # Check if A x B or B x A can cover at least two corners
    can_cover = False
    
    # Check A x B
    if (A <= n and B <= m):
        if (A == n and B == m) or (A == n and B == 1) or (A == 1 and B == m):
            can_cover = True
        elif (A == 1 and B == 1):
            can_cover = False
        else:
            can_cover = True

    # Check B x A
    if (B <= n and A <= m):
        if (B == n and A == m) or (B == n and A == 1) or (B == 1 and A == m):
            can_cover = True
        elif (B == 1 and A == 1):
            can_cover = False
        else:
            can_cover = True

    if can_cover:
        print("YES")
    else:
        print("NO")