
Break down and simplify the provided code which includes implementations for Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms:

### Depth-First Search (DFS)

The `dfs` function explores a graph to find a path from a starting vertex to a target vertex. It uses a depth-first approach, meaning it explores as far as possible along each branch before backtracking.

#### Code Explanation

```python
def dfs(graph, current_vertex, target_value, visited = None):
  if visited is None:
    visited = []
  visited.append(current_vertex)
  if current_vertex is target_value:
    return visited
  
  for neighbor in graph[current_vertex]:
    if neighbor not in visited:
      path = dfs(graph, neighbor, target_value, visited)
      if path:
        return path
```

1. **Initialization:**
   ```python
   if visited is None:
     visited = []
   ```
   If `visited` is not provided, initialize it as an empty list.

2. **Visit Current Vertex:**
   ```python
   visited.append(current_vertex)
   ```
   Add the current vertex to the `visited` list.

3. **Check for Target:**
   ```python
   if current_vertex is target_value:
     return visited
   ```
   If the current vertex matches the target, return the path visited so far.

4. **Recursive Exploration:**
   ```python
   for neighbor in graph[current_vertex]:
     if neighbor not in visited:
       path = dfs(graph, neighbor, target_value, visited)
       if path:
         return path
   ```
   For each unvisited neighbor, recursively perform DFS. If a path is found, return it.

### Breadth-First Search (BFS)

The `bfs` function also searches for a path from a starting vertex to a target vertex, but it uses a breadth-first approach, meaning it explores all neighbors at the present depth level before moving on to nodes at the next depth level.

#### Code Explanation

```python
def bfs(graph, start_vertex, target_value):
  path = [start_vertex]
  vertex_and_path = [start_vertex, path]
  bfs_queue = [vertex_and_path]
  visited = set()
  while bfs_queue:
    current_vertex, path = bfs_queue.pop(0)
    visited.add(current_vertex)
    for neighbor in graph[current_vertex]:
      if neighbor not in visited:
        if neighbor is target_value:
          return path + [neighbor]
        else:
          bfs_queue.append([neighbor, path + [neighbor]])
```

1. **Initialization:**
   ```python
   path = [start_vertex]
   vertex_and_path = [start_vertex, path]
   bfs_queue = [vertex_and_path]
   visited = set()
   ```
   - Start with the initial vertex and an empty path.
   - `bfs_queue` keeps track of vertices to explore along with their paths.
   - `visited` is used to keep track of explored vertices.

2. **Processing Queue:**
   ```python
   while bfs_queue:
     current_vertex, path = bfs_queue.pop(0)
     visited.add(current_vertex)
   ```
   While there are vertices to explore, dequeue a vertex and its path. Mark it as visited.

3. **Exploring Neighbors:**
   ```python
   for neighbor in graph[current_vertex]:
     if neighbor not in visited:
       if neighbor is target_value:
         return path + [neighbor]
       else:
         bfs_queue.append([neighbor, path + [neighbor]])
   ```
   For each unvisited neighbor, check if it’s the target. If so, return the path including this neighbor. Otherwise, add the neighbor to the queue with the updated path.

### Example and Output

```python
some_hazardous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['piranhas', 'bees']),
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
}

print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print(dfs(some_hazardous_graph, 'sharks', 'bees'))
```

- `bfs` finds the shortest path from `'sharks'` to `'bees'`.
- `dfs` finds a path (not necessarily the shortest) from `'sharks'` to `'bees'`.

### Summary

- **DFS** explores as deeply as possible along each branch before backtracking.
- **BFS** explores all possible paths level by level from the starting vertex.
- Both functions help in finding paths in a graph but use different strategies to explore the graph.