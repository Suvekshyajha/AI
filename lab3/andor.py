def perceptron(x1, x2, weights, bias):
    total = x1 * weights[0] + x2 * weights[1] + bias
    return 1 if total >= 0 else 0

# Define logic gates with their weights and biases
gates = {
    "AND": {"weights": [1, 1], "bias": -1.5},
    "OR":  {"weights": [1, 1], "bias": -0.5}
}

inputs = [(0,0), (0,1), (1,0), (1,1)]

# Loop through gates and test each
for gate_name, params in gates.items():
    print(f"\n{gate_name} Gate Output:")
    for x in inputs:
        result = perceptron(x[0], x[1], params["weights"], params["bias"])
        print(f"{x} => {result}")
