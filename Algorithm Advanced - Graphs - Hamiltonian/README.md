
This code defines a class for finding Hamiltonian paths and cycles in a graph using a backtracking approach. Here's a breakdown of how it works:

### Overview

A **Hamiltonian path** is a path in a graph that visits each vertex exactly once. A **Hamiltonian cycle** is a cycle that visits each vertex exactly once and returns to the starting vertex.

### Code Explanation

#### `Hamiltonian` Class

**Purpose:** To find all Hamiltonian paths and cycles in a graph.

1. **Initialization (`__init__` method):**
   - **`vertices`:** List of vertex names (or identifiers).
   - **`adj_matrix`:** Adjacency matrix representing the graph. If `adj_matrix[i][j]` is `1`, there is an edge between vertex `i` and vertex `j`.
   - **`start`:** Starting vertex for the search.
   - **`path`:** List to keep track of the current path being explored.
   - **`visited_vertices`:** List to keep track of which vertices have been visited (0 = not visited, 1 = visited).
   - **`hpaths`:** List to store all Hamiltonian paths found.
   - **`cycles`:** List to store all Hamiltonian cycles found.
   - **`num_vertices`:** Number of vertices in the graph.

2. **Traverse Method (`traverse`):**
   - **Purpose:** Initializes the path with the starting vertex and starts the recursive search for paths and cycles.
   - **Actions:**
     - Adds the starting vertex to the `path`.
     - Calls the `search` method to start the recursive exploration.

3. **Search Method (`search`):**
   - **Purpose:** Recursively explores the graph to find Hamiltonian paths and cycles.
   - **Steps:**
     1. **Check for Hamiltonian Path:**
        - Verifies if all vertices have been visited and if there are no duplicate vertices in the path.
        - If valid, adds the path to `hpaths`.
     2. **Check for Hamiltonian Cycle:**
        - Checks if the current vertex is the starting vertex and if the path length equals the number of vertices plus one (since the start vertex should appear twice).
        - If valid, adds the path to `cycles`.
     3. **Explore Neighbors:**
        - Iterates over all possible neighbors of the current vertex.
        - If a neighbor is connected (i.e., there is an edge) and has not been visited, it:
          - Marks the neighbor as visited.
          - Adds the neighbor to the `path`.
          - Recursively calls `search` for the neighbor.
        - **Backtracking:**
          - After exploring, it marks the neighbor as not visited (backtracking) and removes the neighbor from the `path`.

#### Example Usage

1. **Vertices and Adjacency Matrix:**
   - `vertices` represent the graph nodes.
   - `adjacency_matrix` defines connections between nodes (edges).

2. **Instantiate and Traverse:**
   - Creates an instance of the `Hamiltonian` class with the given vertices and adjacency matrix.
   - Calls the `traverse` method to find all Hamiltonian paths and cycles.

3. **Print Results:**
   - Outputs the Hamiltonian paths and cycles found in the graph.

### Summary

- **Hamiltonian Class:** Finds all Hamiltonian paths and cycles using a backtracking algorithm.
- **`traverse` Method:** Initializes the search process.
- **`search` Method:** Recursively explores paths and backtracks if necessary.
- **Example Usage:** Sets up a graph, runs the algorithm, and prints the results.

This code helps in solving the Hamiltonian path and cycle problems, which are fundamental in graph theory and have applications in various fields such as scheduling and route planning.

