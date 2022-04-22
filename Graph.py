from DisjointSet import DisjointSet


class Graph:
    def __init__(self, vertex_count=0):
        self.vertex_count = vertex_count
        self.adjacency_matrix = [[0] * self.vertex_count for _ in range(self.vertex_count)] if vertex_count > 0 else None
        self.edge_list = {}
        self.vertex_list = []

    def load_graph_from_file(self, path):
        file_data = open(path)
        self.vertex_count = int(file_data.readline())
        self.adjacency_matrix = [[0] * self.vertex_count for _ in range(self.vertex_count)]
        for line in file_data.readlines()[1:]:
            line = line.split(" ")
            self.add_edge(int(line[0]), int(line[1]), float(line[2]))
            if int(line[0]) not in self.vertex_list:
                self.vertex_list.append(int(line[0]))
            if int(line[1]) not in self.vertex_list:
                self.vertex_list.append(int(line[1]))

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_matrix[vertex1][vertex2] = weight
        self.adjacency_matrix[vertex2][vertex1] = weight
        self.edge_list[(vertex1, vertex2)] = weight

    def print_adjacency_matrix(self):
        print('', end='\t')
        for i in range(self.vertex_count):
            print(f'{i}'.rjust(10), end=' ')
        print('')
        for i in range(self.vertex_count):
            print(i, end='\t')
            for j in range(self.vertex_count):
                print(str(self.adjacency_matrix[i][j]).rjust(10), end=' ')
            print('')

    def print_edge_list(self):
        print(str(self.edge_list))

    def get_minimum_spanning_tree(self, custom_vertices=None):
        edge_count = 0
        minimum_spanning_tree = {}

        ds = DisjointSet(custom_vertices) if custom_vertices else DisjointSet(self.vertex_list)

        # Sorting the weights in non-increasing order
        sorted_edges = dict(sorted(self.edge_list.items(), key=lambda x: x[1]))

        if custom_vertices:
            for key, value in self.edge_list.items():
                if key[0] not in custom_vertices or key[1] not in custom_vertices:
                    sorted_edges.pop(key)

        for key, value in sorted_edges.items():
            vertex_u = key[0]
            vertex_v = key[1]
            weight = value

            main_parent_u = ds.find(vertex_u)
            main_parent_v = ds.find(vertex_v)

            if main_parent_u != main_parent_v:
                edge_count += 1
                minimum_spanning_tree[(vertex_u, vertex_v)] = weight
                ds.union(main_parent_u, main_parent_v)

        return minimum_spanning_tree

    def get_DFS(self, start=0, dfs_path=None, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = []
        if dfs_path is None:
            dfs_path = {}

        visited_vertices.append(start)

        for i in range(self.vertex_count):
            if self.adjacency_matrix[start][i] != 0 and i not in visited_vertices:
                dfs_path[(start, i)] = self.adjacency_matrix[start][i]
                self.get_DFS(i, dfs_path, visited_vertices)
