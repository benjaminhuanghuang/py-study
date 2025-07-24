# The Breadth-First Search Algorithm

## Pseudocode

Queue: [start_pos]
Predecessors: {start_pos: None}  Used to build the path and record the visited cells

Algorithm
• Dequeue
• Is this the goal?
• If so, we are done
• Otherwise, push **undiscovered neighbors** onto the stack and add them to predecessors/discovered
• Repeat until queue is empty

## Code

bfs.py
