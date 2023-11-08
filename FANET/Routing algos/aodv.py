import time
start = time.time()

class AODVNode:
    def __init__(self, name):
        self.name = name
        self.routing_table = {}

    def route_discovery(self, destination, network):
        if destination not in self.routing_table:
            route = self.find_route(destination, network)
            if route:
                self.routing_table[destination] = route

    def find_route(self, destination, network):
        visited = set()
        route = self._find_route(self.name, destination, network, visited)
        if route:
            return route[::-1]
        return None

    def _find_route(self, current, destination, network, visited):
        if current == destination:
            return [current]

        visited.add(current)

        for neighbor in network[current]:
            if neighbor not in visited:
                route = self._find_route(neighbor, destination, network, visited)
                if route:
                    return [current] + route

        return None

class AODVNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def find_route(self, source, destination):
        if source not in self.nodes:
            return None

        source_node = self.nodes[source]
        source_node.route_discovery(destination, self.get_network_map())
        
        if destination in source_node.routing_table:
            return source_node.routing_table[destination]

        return None

    def get_network_map(self):
        network_map = {}
        for node in self.nodes.values():
            network_map[node.name] = [neighbor for neighbor in node.routing_table]
        return network_map

# Example usage:

sum_time = 0
iterations = 10
individual_time = []
for i in range(iterations):
    start = time.time()
    node_a = AODVNode('A')
    node_b = AODVNode('B')
    node_c = AODVNode('C')
    node_d = AODVNode('D')

    network = AODVNetwork()
    network.add_node(node_a)
    network.add_node(node_b)
    network.add_node(node_c)
    network.add_node(node_d)

    node_a.routing_table['B'] = ['B']
    node_b.routing_table['C'] = ['B', 'C']
    node_c.routing_table['D'] = ['B', 'C', 'D']

    source_node = 'A'
    destination_node = 'D'
    route = network.find_route(source_node, destination_node)

    if route:
        print(f"Route from {source_node} to {destination_node}: {' -> '.join(route)}")
    else:
        print(f"No route found from {source_node} to {destination_node}")

    end = time.time()
    print("The time of execution of above program is :",
        (end-start) * 10**3, "ms")
    time_taken = end-start
    sum_time += (end-start)
    individual_time.append(time_taken)

with open("outputaodv.txt", "w") as file:
		for current in enumerate(individual_time):
			file.write(f"{current}\n")
print(f"The average time of execution for {iterations} iterations is: {sum_time/iterations}")

