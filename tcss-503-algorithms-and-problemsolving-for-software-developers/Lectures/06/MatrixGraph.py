class MatrixGraph:
    
    def __init__(selv, v_count):
        self.v_count = v_count
        self.adj_matrix = [[0 for _ in range(v_count)] for _ in range(v_count)]
    
    def _can_color(self, color, node):
        for i in range(self.v_count):
            if self.adj_matrix[node][i] == 1 and color[i] == color[node]:
                return False
        return True