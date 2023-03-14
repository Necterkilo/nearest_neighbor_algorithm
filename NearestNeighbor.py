def graph_maker():
    final_matrix = []
    num_rows = int(input("How many rows are in the graph? "))
    num_columns = int(input("How many columns are in the graph? "))
    print("Please type each digit one at a time by row, and replace every hyphen with a zero:")
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            row.append(int(input()))
        final_matrix.append(row)

    return final_matrix


def starting_index_selector():
    starting_index = int()
    starting_index_prompt = input("Please specify the starting vertex: ")
    vertex_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                         'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                         'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    for i in vertex_dictionary:
        if i in starting_index_prompt.upper():
            starting_index = vertex_dictionary[i]

    return starting_index


def nearest_neighbor_algorithm(matrix: list, starting_index: int):
    total = 0
    row_index = starting_index
    used_indexes = []
    count = 0
    while count < len(matrix):
        lowest_ele = max(matrix[row_index])
        for ele in matrix[row_index]:
            if count == len(matrix) - 1:
                if matrix[row_index].index(ele) == starting_index:
                    lowest_ele = ele
                    break
            if ele < lowest_ele and ele != 0:
                if matrix[row_index].index(ele) not in used_indexes:
                    lowest_ele = ele
        used_indexes.append(row_index)
        row_index = matrix[row_index].index(lowest_ele)
        total += lowest_ele
        count += 1
    used_indexes.append(starting_index)

    return used_indexes, total


def vertices_traveled(used_vertices: list):
    vertex_dictionary = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
                         'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20,
                         'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
    vertex_values = list(vertex_dictionary.values())
    vertex_keys = list(vertex_dictionary.keys())
    return_vertices = str()
    for i in used_vertices:
        return_vertices += vertex_keys[vertex_values[i]]

    return return_vertices


indexes, total_cost = nearest_neighbor_algorithm(graph_maker(), starting_index_selector())
vertices = vertices_traveled(indexes)

print("The vertices traversed are: " + vertices + "\n" + "The total cost of the trip is: " + str(total_cost))
