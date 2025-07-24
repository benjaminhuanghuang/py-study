# Depth-First Search

## Pseudocode

Stack: [start_pos]
Predecessors: {start_pos: None}  Used to build the path and record the visited cells

Algorithm
• Pop the stack
• Is this the goal?
• If so, we are done
• Otherwise, push **undiscovered neighbors** onto the stack and add them to predecessors/discovered
• Repeat until stack is empty

## Sample

GUI Code/grid_tracer

helpers.py

dfs.py
