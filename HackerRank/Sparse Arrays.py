def matchingStrings(strings, queries):
    l = []
    for i in queries:
        l.append(strings.count(i))
    return l

strings_count = int(input())
strings = []

for _ in range(strings_count):
    strings_item = input()
    strings.append(strings_item)

queries_count = int(input())
queries = []

for _ in range(queries_count):
    queries_item = input()
    queries.append(queries_item)

res = matchingStrings(strings, queries)

print('\n'.join(map(str, res)))

Link: https://www.hackerrank.com/challenges/sparse-arrays/problem
