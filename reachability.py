#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    print('input:',input)
    data = list(map(int, input.split()))
    print('data:',data)
    n, m = data[0:2]
    print('n:',n)
    print('m:',m)
    data = data[2:]
    print('data:',data)
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print('edges:',edges)
    x, y = data[2 * m:]
    print('x:',x)
    print('y:',y)
    adj = [[] for _ in range(n)]
    print('adj:',adj)
    x, y = x - 1, y - 1
    print('x:',x)
    print('y:',y)
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print('edges:',edges)
    print(reach(adj, x, y))