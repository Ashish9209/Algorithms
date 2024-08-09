# Pathfinding

Pathfinding is the algorithmic concept of finding the shortest path between two points in a graph. In this course, we cover two main pathfinding techniques:

- **Dijkstra’s Algorithm**
- **A* Algorithm**

## A* Algorithm

The **A* algorithm** is a greedy graph search algorithm designed to efficiently find the shortest path to a target vertex. It is a modification of Dijkstra’s Algorithm, incorporating a heuristic to estimate the distance from each vertex to the goal vertex.

### Key Modifications from Dijkstra’s Algorithm

1. **Adding a Target:**
   - Introduce a specific goal or target for the search.

2. **Gathering Optimal Paths:**
   - Collect possible optimal paths and identify the single shortest path.

3. **Implementing a Heuristic:**
   - Use a heuristic function to estimate the likely distance remaining to the goal.

### Runtime Complexity

- **Time Complexity:** \( O(bd) \)
  - Where \( b \) is the branching factor of the graph and \( d \) is the depth of the goal vertex from the start vertex.

### A* as an Introductory Glimpse into AI

- A* provides an introductory look into artificial intelligence by using heuristic methods to optimize search strategies.

## Modified Dijkstra’s Algorithm

- **Path and Target:**
  - Modified Dijkstra’s algorithm to include path tracking and target vertex.

- **Heuristic Functions:**
  - **Manhattan Heuristic:** Used for estimating distances on a grid.
  - **Euclidean Heuristic:** Used for estimating distances between cities.

This file provides an overview of pathfinding techniques, focusing on the A* algorithm, its modifications from Dijkstra’s Algorithm, and heuristic functions used in the search process.
