import numpy as np

# Sigmoid activation and derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    
def sigmoid_derivative(x):
    return x * (1 - x)

# Input for logic gates
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# Uncomment one of these for different gates:

# For AND gate
y = np.array([[0], [0], [0], [1]])

# For OR gate
# y = np.array([[0], [1], [1], [1]])

# Seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_layer_neurons = 2
hidden_layer_neurons = 2
output_neurons = 1

# Random weights
hidden_weights = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
hidden_bias = np.random.uniform(size=(1, hidden_layer_neurons))
output_weights = np.random.uniform(size=(hidden_layer_neurons, output_neurons))
output_bias = np.random.uniform(size=(1, output_neurons))

# Training
epochs = 10000
learning_rate = 0.1

for epoch in range(epochs):
    # Forward Propagation
    hidden_input = np.dot(X, hidden_weights) + hidden_bias
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, output_weights) + output_bias
    final_output = sigmoid(final_input)

    # Error
    error = y - final_output

    # Backpropagation
    d_output = error * sigmoid_derivative(final_output)

    error_hidden = d_output.dot(output_weights.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights and biases
    output_weights += hidden_output.T.dot(d_output) * learning_rate
    output_bias += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    hidden_weights += X.T.dot(d_hidden) * learning_rate
    hidden_bias += np.sum(d_hidden, axis=0, keepdims=True) * learning_rate

# Final output after training
print("\nFinal Output After Training:")
for i in range(len(X)):
    print(f"{X[i]} => {final_output[i][0]:.4f}")
