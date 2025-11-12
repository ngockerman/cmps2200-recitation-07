# CMPS 2200 Recitation 10## Answers

**Name:** Natalie Gockerman
**Name:**_________________________


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
- Assume n nodes and m edges:
-   each node (n) added to result and fronteir at most once --> Θ(n)
-   iterate over each nodes adjacency set (m) once --> Θ(m)
-   all else is constant work for pop, add, and in
-   therefore Work = Θ(n + m)

- **4)**
- When the connectivity function is run, it will pick any node s and call reachable(graph, s) one time
- if the graph is connected, reachable will return all n nodes in the graph because they are all reachable from the starting node
- if the graph is not connected, reachable will return fewer than n nodes (just the ones reacable from the starting node)
- therefore, either way reachable will only be called 1 time in the worst case
- reachable will not be called at all when the graph is empty

- **5)**
- first, connected sets up by handling base case of empty graph and choosing a starting node --> O(1)
- then, calls reachable which performs work of Θ(n + m) as shown in number 2
- finally, comparing sizes results in O(1) as well
- therfore, work of connected = Θ(n + m)

- **7)**
- In an adjacency matrix, to find all neighbors of a singular node, you must scan the entire row and test each cell for an edge
- In this scenario, reachable visits n nodes
- For each visited node it scans a full row of n and makes n entries per scan --> n^2
- Therefore work = Θ(n^2)
