# Uses python3

# Problem Introduction
# A maze is a rectangular grid of cells with walls between some of adjacent cells.
# You would like to check whether there is a path from a given cell to a given
# exit from a maze where an exit is also a cell that lies on the border of the maze
# (in the example shown to the right there are two exits: one on the left border
# and one on the right border). For this, you represent the maze as an undirected
# graph: vertices of the graph are cells of the maze, two vertices are connected by
# an undirected edge if they are adjacent and there is no wall between them. Then,
# to check whether there is a path between two given cells in the maze, it suffices to
# check that there is a path between the corresponding two vertices in the graph.
# Problem Description
# Task. Given an undirected graph and two distinct vertices 𝑢 and 𝑣, check if there is a path between 𝑢 and 𝑣.
# Input Format. An undirected graph with 𝑛 vertices and 𝑚 edges. The next line contains two vertices 𝑢
# and 𝑣 of the graph.
# Constraints. 2 ≤ 𝑛 ≤ 103; 1 ≤ 𝑚 ≤ 103; 1 ≤ 𝑢, 𝑣 ≤ 𝑛; 𝑢 ̸= 𝑣.
# Output Format. Output 1 if there is a path between 𝑢 and 𝑣 and 0 otherwise.

import sys
import numpy


def reach(adj, x, y):
    # write your code here
    # visited = numpy.zeros((4, 1))
    explore(x)
    return visited[y]


def explore(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(w)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = numpy.zeros((4, 1))
    print(reach(adj, x, y))
