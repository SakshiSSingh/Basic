def equalStacks(h1, h2, h3):
    
    h1.reverse()
    h2.reverse()
    h3.reverse()
    stacks = [h1, h2, h3]
    sums = [sum(h1), sum(h2), sum(h3)]

    while (sums[0] != sums[1]) or (sums[0] != sums[2]):
        n = stacks[sums.index(max(sums))].pop()
        sums[sums.index(max(sums))] -= n
    return sums[0]

Link: https://www.hackerrank.com/challenges/equal-stacks/problem
