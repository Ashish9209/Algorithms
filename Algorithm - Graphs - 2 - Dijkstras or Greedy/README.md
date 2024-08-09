# Greedy Algorithms

A **greedy algorithm** builds up a solution for an optimization problem by making the best decision at each step. 

## Characteristics

- **Simple and Efficient:** Greedy algorithms are easy to implement and often perform well in practice.
- **Not Always Correct:** Greedy algorithms do not always produce the optimal solution. They are correct only if the problem satisfies certain properties.

## Requirements for Greedy Algorithms

For a greedy algorithm to work correctly, the problem must satisfy:

- **Optimal Substructure Property:** The optimal solution to the problem can be constructed from optimal solutions of its subproblems.
- **Greedy Property:** A global optimum can be arrived at by selecting a local optimum.

# Dijkstra’s Algorithm

**Dijkstra’s Algorithm** is used to find the shortest distances between a start vertex and all other vertices in a graph.

## How It Works

- **Distance Tracking:** The algorithm keeps track of all the distances from the start vertex to each vertex.
- **Breadth-First Search:** It updates distances as it performs a breadth-first search through the graph.

## Time Complexity

Dijkstra’s Algorithm runs in \( O((E + V) \log V) \), where \( E \) is the number of edges and \( V \) is the number of vertices in the graph.
