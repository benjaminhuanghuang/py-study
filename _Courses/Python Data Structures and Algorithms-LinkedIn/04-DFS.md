# Depth-First Search

## Pseudocode

Stack: [start_pos]
Predecessors: {start_pos: None}

Algorithm
• Pop the stack
• Is this the goal?
• If so, we are done
• Otherwise, push undiscovered neighbors onto the stack and add them to predecessors/discovered
• Repeat until stack is empty
