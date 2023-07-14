class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Function to get the parent index of a node
    def parent(self, index):
        return (index - 1) // 2

    # Function to get the left child index of a node
    def left_child(self, index):
        return 2 * index + 1

    # Function to get the right child index of a node
    def right_child(self, index):
        return 2 * index + 2

    # Function to swap two nodes in the heap
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    # Function to percolate up a node in the heap
    def percolate_up(self, index):
        while index > 0 and self.heap[index].priority < self.heap[self.parent(index)].priority:
            parent_index = self.parent(index)
            self.swap(index, parent_index)
            index = parent_index

    # Function to percolate down a node in the heap
    def percolate_down(self, index):
        while True:
            smallest = index
            left = self.left_child(index)
            right = self.right_child(index)

            # Compare with left child
            if left < len(self.heap) and self.heap[left].priority < self.heap[smallest].priority:
                smallest = left

            # Compare with right child
            if right < len(self.heap) and self.heap[right].priority < self.heap[smallest].priority:
                smallest = right

            # If the smallest is not the current node, swap and continue percolating down
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break

    # Function to enqueue a node into the heap
    def enqueue(self, node):
        self.heap.append(node)
        self.percolate_up(len(self.heap) - 1)

    # Function to dequeue the node with the minimum priority from the heap
    def dequeue(self):
        if not self.heap:
            return None

        # Remove the root node
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Percolate down to maintain heap property
        self.percolate_down(0)

        return root

    # Function to check if the heap is empty
    def is_empty(self):
        return len(self.heap) == 0










