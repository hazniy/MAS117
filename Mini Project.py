import random
from collections import Counter

# Define the simulation parameters
num_simulations = 100000  # Number of simulations
num_vertices = 5          # Number of vertices on the pentagon
num_steps = 7             # Number of steps Annie takes

# Function to simulate one journey
def simulate_journey():
    current_vertex = 0  # Start at vertex 0
    for _ in range(num_steps):
        # Move to an adjacent vertex
        step = random.choice([-1, 1])  # -1 for anticlockwise, 1 for clockwise
        current_vertex = (current_vertex + step) % num_vertices  # Wrap around
    return current_vertex

# Run the simulations
end_vertices = [simulate_journey() for _ in range(num_simulations)]

# Count occurrences of each ending vertex
vertex_counts = Counter(end_vertices)

# Calculate and print percentages
for vertex in range(num_vertices):
    percentage = (vertex_counts[vertex] / num_simulations) * 100
    print(f"Vertex {vertex}: {percentage:.2f}%")

import matplotlib.pyplot as plt

def simulate_steps_effect(max_steps):
    results = {}
    for steps in range(1, max_steps + 1):
        end_vertices = [simulate_journey(steps) for _ in range(num_simulations)]
        vertex_counts = Counter(end_vertices)
        results[steps] = [vertex_counts[vertex] / num_simulations * 100 for vertex in range(num_vertices)]
    return results

def simulate_journey(steps):
    current_vertex = 0
    for _ in range(steps):
        step = random.choice([-1, 1])
        current_vertex = (current_vertex + step) % num_vertices
    return current_vertex

# Analyze steps effect
max_steps = 20
results = simulate_steps_effect(max_steps)

# Plot results
for vertex in range(num_vertices):
    percentages = [results[steps][vertex] for steps in range(1, max_steps + 1)]
    plt.plot(range(1, max_steps + 1), percentages, label=f"Vertex {vertex}")

plt.xlabel("Number of Steps")
plt.ylabel("Percentage")
plt.title("Effect of Steps on Vertex Percentages")
plt.legend()
plt.grid()
plt.show()

num_vertices = 8  # Change to a polygon with 8 vertices
results = simulate_steps_effect(max_steps=10)

# Define the cube's edges as a graph
cube_edges = {
    0: [1, 3, 4],
    1: [0, 2, 5],
    2: [1, 3, 6],
    3: [0, 2, 7],
    4: [0, 5, 7],
    5: [1, 4, 6],
    6: [2, 5, 7],
    7: [3, 4, 6]
}

def simulate_cube_journey(steps):
    current_vertex = 0  # Start at vertex 0
    for _ in range(steps):
        current_vertex = random.choice(cube_edges[current_vertex])
    return current_vertex

# Simulate on a cube
end_vertices = [simulate_cube_journey(num_steps) for _ in range(num_simulations)]
vertex_counts = Counter(end_vertices)

# Print results
for vertex in range(len(cube_edges)):
    percentage = (vertex_counts[vertex] / num_simulations) * 100
    print(f"Vertex {vertex}: {percentage:.2f}%")

#2
import random
from collections import Counter
import matplotlib.pyplot as plt

# Simulate a random walk on a polygon
def simulate_polygon_journey(start_vertex, num_vertices, num_steps):
    """
    Simulate Annie's journey on a polygon with a given number of vertices and steps.

    Args:
        start_vertex (int): The starting vertex.
        num_vertices (int): Total number of vertices in the polygon.
        num_steps (int): Total number of steps to simulate.

    Returns:
        int: The vertex where Annie ends her journey.
    """
    current_vertex = start_vertex
    for _ in range(num_steps):
        step = random.choice([-1, 1])  # Move clockwise or anticlockwise
        current_vertex = (current_vertex + step) % num_vertices
    return current_vertex

# Simulate multiple journeys and analyze results
def analyze_polygon(num_vertices, num_steps, num_simulations):
    """
    Simulate multiple journeys and calculate the percentage of time Annie ends at each vertex.

    Args:
        num_vertices (int): Number of vertices in the polygon.
        num_steps (int): Number of steps per journey.
        num_simulations (int): Total number of journeys to simulate.

    Returns:
        list: Percentages of ending at each vertex.
    """
    end_vertices = [simulate_polygon_journey(0, num_vertices, num_steps) for _ in range(num_simulations)]
    vertex_counts = Counter(end_vertices)
    return [(vertex_counts[vertex] / num_simulations) * 100 for vertex in range(num_vertices)]

# Effect of steps on percentages
def investigate_steps_effect(max_steps, num_vertices, num_simulations):
    """
    Investigate how the number of steps affects the percentages for each vertex.

    Args:
        max_steps (int): Maximum number of steps to investigate.
        num_vertices (int): Number of vertices in the polygon.
        num_simulations (int): Number of simulations per step count.
    """
    results = {}
    for steps in range(1, max_steps + 1):
        results[steps] = analyze_polygon(num_vertices, steps, num_simulations)

    # Plot the results
    for vertex in range(num_vertices):
        percentages = [results[steps][vertex] for steps in range(1, max_steps + 1)]
        plt.plot(range(1, max_steps + 1), percentages, label=f"Vertex {vertex}")

    plt.title(f"Effect of Steps on Percentages (Polygon with {num_vertices} vertices)")
    plt.xlabel("Number of Steps")
    plt.ylabel("Percentage")
    plt.legend()
    plt.grid()
    plt.show()

# Investigate different polygon sizes
def investigate_polygon_sizes(max_vertices, num_steps, num_simulations):
    """
    Investigate the effect of changing the number of vertices in the polygon.

    Args:
        max_vertices (int): Maximum number of vertices to investigate.
        num_steps (int): Number of steps per journey.
        num_simulations (int): Number of simulations per polygon size.
    """
    for vertices in range(3, max_vertices + 1):  # Start from a triangle (3 vertices)
        percentages = analyze_polygon(vertices, num_steps, num_simulations)
        print(f"Polygon with {vertices} vertices:")
        for vertex, percentage in enumerate(percentages):
            print(f"  Vertex {vertex}: {percentage:.2f}%")
        print()

# Simulate Annie's journey on a cube
def simulate_cube_journey(start_vertex, num_steps, cube_edges):
    """
    Simulate Annie's journey on a cube, represented as a graph.

    Args:
        start_vertex (int): Starting vertex on the cube.
        num_steps (int): Number of steps to simulate.
        cube_edges (dict): Graph representation of the cube.

    Returns:
        int: The vertex where Annie ends her journey.
    """
    current_vertex = start_vertex
    for _ in range(num_steps):
        current_vertex = random.choice(cube_edges[current_vertex])
    return current_vertex

def analyze_cube(num_steps, num_simulations):
    """
    Simulate multiple journeys on a cube and calculate percentages for each vertex.

    Args:
        num_steps (int): Number of steps per journey.
        num_simulations (int): Number of simulations.

    Returns:
        dict: Percentages of ending at each vertex.
    """
    cube_edges = {
        0: [1, 3, 4],
        1: [0, 2, 5],
        2: [1, 3, 6],
        3: [0, 2, 7],
        4: [0, 5, 7],
        5: [1, 4, 6],
        6: [2, 5, 7],
        7: [3, 4, 6],
    }

    end_vertices = [simulate_cube_journey(0, num_steps, cube_edges) for _ in range(num_simulations)]
    vertex_counts = Counter(end_vertices)
    return {vertex: (vertex_counts[vertex] / num_simulations) * 100 for vertex in range(len(cube_edges))}

# Main script
if __name__ == "__main__":
    num_simulations = 100000  # Total number of simulations

    # Task 1: Investigate the effect of the number of steps
    investigate_steps_effect(max_steps=20, num_vertices=5, num_simulations=num_simulations)

    # Task 2: Investigate different polygon sizes
    investigate_polygon_sizes(max_vertices=8, num_steps=7, num_simulations=num_simulations)

    # Task 3: Investigate Annie's journey on a cube
    cube_results = analyze_cube(num_steps=7, num_simulations=num_simulations)
    print("Cube simulation results:")
    for vertex, percentage in cube_results.items():
        print(f"  Vertex {vertex}: {percentage:.2f}%")
