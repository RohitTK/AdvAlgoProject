class DisjointSet:
    def __init__(self, vertex_list):
        self.vertex_list = vertex_list
        self.parent = {i: i for i in vertex_list}
        self.group = {i: 0 for i in vertex_list}

    # Find the key
    def find(self, key):
        if self.parent[key] == key:
            return key
        else:
            return self.find(self.parent[key])

    # Merge 2 datasets accordingly
    def union(self, left, right):
        left_set = self.find(left)
        right_set = self.find(right)

        if self.group[left_set] > self.group[right_set]:
            self.parent[right_set] = left_set
        elif self.group[left_set] < self.group[right_set]:
            self.parent[left_set] = right_set
        else:
            self.group[left_set] += 1
            self.parent[right_set] = left_set
