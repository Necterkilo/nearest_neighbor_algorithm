"""
The nearest neighbor algorithm (NNA) is used to solve the traveling
salesman problem. In the problem, a salesman starts at a random city and
repeatedly visits the nearest city until every one has been visited. The
result would be quick, but cost ineffective. The NNA attempts to find
the cheapest and fastest route for the traveling salesman.
"""


def nearest_neighbor_algorithm(matrix: list, start_index: int) -> tuple:
    """Calculates the nearest neighbor algorithm (NNA).

    :parameter matrix: A symmetrical matrix.
    :parameter start_index: The first index the NNA should compute.
    :returns: The sum of the elements selected and their indexes.
    """
    row_index = start_index
    used_indexes = []
    total = int()
    count = int()
    while count < len(matrix):
        lowest_ele = max(matrix[row_index])
        for ele in matrix[row_index]:
            if count == len(matrix) - 1:
                if matrix[row_index].index(ele) == start_index:
                    lowest_ele = ele
                    break
            if ele < lowest_ele and ele != 0:
                if matrix[row_index].index(ele) not in used_indexes:
                    lowest_ele = ele
        used_indexes.append(row_index)
        row_index = matrix[row_index].index(lowest_ele)
        total += lowest_ele
        count += 1
    used_indexes.append(start_index)

    return total, used_indexes


def main():
    # Ask the user to input a graph.
    vertex_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Defines vertexes.
    num_of_rows = int(input("How many rows are in the graph? "))
    print("Please type each digit one at a time by row, and replace every"
          "hyphen with a zero:")
    graph = [[int(input(f"Row {vertex_str[i]}, column {vertex_str[j]}: "))
              for j in range(num_of_rows)] for i in range(num_of_rows)]

    # Ask the user to specify the starting index of the matrix.
    start_vertex_prompt = \
        input("Please specify the starting vertex: ").upper()
    start_vertex = vertex_str.index(start_vertex_prompt)

    # The NNA is called with the matrix and starting index.
    total_cost, used_vertices = \
        nearest_neighbor_algorithm(graph, start_vertex)

    # Converts the indexes used to string vertices.
    vertices_traversed = "".join(vertex_str[i] for i in used_vertices)

    # Print the results of the algorithm to stdout.
    print(f"The total cost of the trip is: ${total_cost}.\nThe vertices "
          f"traversed are: {vertices_traversed}.")
    input("Press [Enter] to finish...")


if __name__ == "__main__":
    main()
