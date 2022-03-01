n, m = list(map(int,input().split()))

s = []


def dfs(n, m):

    if len(s) == m:
        print(' '.join(list(map(str, s))))

    for i in range(1, n+1):
        if len(s) == m:
            return
        s.append(i)
        dfs(n, m)
        s.pop()


dfs(n, m)
