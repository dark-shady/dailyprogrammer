#https://www.reddit.com/r/dailyprogrammer/comments/7qn07r/20180115_challenge_347_easy_how_long_has_the/

input = """15 18
13 16
9 12
3 4
17 20
9 11
17 18
4 5
5 6
4 5
5 6
13 16
2 3
15 17
13 14"""




inputs = input.split('\n')
pairs = [pair for pair in inputs]
ranges = map(lambda x: list(range(int(x[0]),int(x[1]))), [pair.split() for pair in pairs])

print(len(set([x for sublist in ranges for x in sublist])))

