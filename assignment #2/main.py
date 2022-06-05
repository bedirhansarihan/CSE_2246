import typing

class Graph():

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

        self.size = self.graph_size()
        self.vertices = self.create_vertices()
        self.edge_connections()
        self.result = self.color_algorithm()


        self.write_output_file()

    def color_algorithm(self) -> typing.Dict[int, int]:
        """

        :return:
        """
        result = {}

        for v in self.vertices:
            adj_vertex_colors = set()
            print(f"neighbors of the vertex {v.vertice_id}: {v.edgeList}")
            for e in v.edgeList:
                if e in result:
                    adj_vertex_colors.add(result[e])

            color = 0           # first-color
            for c in adj_vertex_colors:
                if color != c:
                    break
                else:
                    color = color + 1


            result[v.vertice_id] = color
            print(f"current colored vertices: {result}")
            v.color = color         # update vertice_color
            v.isColored = True      # vertice is colored

        return result
    def graph_size(self) -> int:
        """
        it returns number of vertices
        :return:
        """
        with open(self.input_file) as f:
            size = int(f.readline().split()[1])

        return size

    def create_vertices(self) -> typing.List:
        """
        it creates vertice objects
        :return:
        """
        vertices = []
        for i in range(self.size):
            if i == 0:
                v = Vertice()

            v = Vertice()
            vertices.append(v)

        return vertices

    def edge_connections(self):
        """
        for each vertices, it stores their adjacency vertex in vertice.edgeList: list
        :return:
        """
        with open(self.input_file) as f:
            for line in f.readlines():
                split_line = line.split()

                if split_line[0] == 'e':
                    v_id1 = int(split_line[1])
                    v_id2 = int(split_line[2])

                    self.vertices[v_id1 - 1].vertice_id = v_id1
                    self.vertices[v_id1 - 1].edgeList.append(v_id2)

                    self.vertices[v_id2-1].vertice_id = v_id2                   # vertice_id
                    self.vertices[v_id2-1].edgeList.append(v_id1)             # edges


                    self.vertices[v_id1 - 1].degree += 1

    def write_output_file(self):
        max = 0
        for i in self.result:

            if self.result[i] > max:
                max = self.result[i]

        max = max +1    # color_number starts from 1

        with open(self.output_file, 'w') as f:
            f.write(str(max))
            f.write('\n')
            for y in self.result:
                f.write(str(self.result[y]))
                f.write(' ')



class Vertice():

    def __init__(self,):

        self.vertice_id = 0
        self.degree = 0
        self.color = None
        self.isColored = False


        self.edgeList: typing.List = []

if __name__ == '__main__':

    x = Graph("test1.txt", "output1.txt")
    x = Graph("test2.txt", "output2.txt")
    x = Graph("test3.txt", "output3.txt")
    x = Graph("test4.txt", "output4.txt")
