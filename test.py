# coding: utf8
from LayerClass import Layer, learning_cycle
from NeuronClass import Neuron, linear, sigmoid
from SynapseClass import Synapse
from GraphClass import Graph

LEARNING_SPEED = 0.7
MOMENT = 0.5
RMSE_MINIMUM = 0.000000001
MSE_MINIMUM = 0.0000000001
MAX_ITERATION_NUMBER = 1000


def test_all(input_ideal, output_ideal, all_layers):
    for i in range(0, len(input_ideal)):
        learning_cycle(
            all_layers, input_ideal[i], output_ideal[i],
            LEARNING_SPEED, MOMENT, RMSE_MINIMUM, MSE_MINIMUM,
            MAX_ITERATION_NUMBER
        )

    # new_graph = Graph(all_layers)
    # new_graph.paint_graph()


def generate_layers_xor():
    input_neuron_1 = Neuron('input_neuron_1', linear)
    input_neuron_2 = Neuron('input_neuron_2', linear)
    neuron_1_1 = Neuron('neuron_1_1', sigmoid)
    neuron_1_2 = Neuron('neuron_1_2', sigmoid)
    output_neuron = Neuron('output_neuron', sigmoid)

    input_neurons = [input_neuron_1, input_neuron_2]
    input_synapses = [
        Synapse(input_neuron_1, neuron_1_1, 0.45),
        Synapse(input_neuron_1, neuron_1_2, 0.78),
        Synapse(input_neuron_2, neuron_1_1, -0.12),
        Synapse(input_neuron_2, neuron_1_2, 0.13),
    ]
    input_layer = Layer('input_layer', input_neurons, input_synapses)
    input_layer.set_linked_synapses()

    layer_1_neurons = [neuron_1_1, neuron_1_2,]
    layer_1_synapses = [
        Synapse(neuron_1_1, output_neuron, 1.5),
        Synapse(neuron_1_2, output_neuron, -2.3),
    ]
    layer_1 = Layer('layer_1', layer_1_neurons, layer_1_synapses)
    layer_1.set_linked_synapses()

    output_neurons = [output_neuron]
    output_synapses = [
        Synapse(output_neuron, output_neuron, 1.0),
    ]
    output_layer = Layer('output_layer', output_neurons, output_synapses)
    output_layer.set_linked_synapses()

    all_layers = [input_layer, layer_1, output_layer]

    return all_layers


def generate_layers_linear_regression():
    input_neuron = Neuron('input_neuron', sigmoid)
    output_neuron = Neuron('output_neuron', sigmoid)
    independ_neuron = Neuron('independ_neuron', sigmoid, initial=1)

    input_neurons = [input_neuron]
    input_synapses = [
        Synapse(input_neuron, output_neuron, 1.0),
    ]
    input_layer = Layer('input_layer', input_neurons, input_synapses)
    input_layer.set_linked_synapses()

    layer_1_neurons = [independ_neuron]
    layer_1_synapses = [
        Synapse(independ_neuron, output_neuron, 1.0),
    ]
    layer_1 = Layer('layer_1', layer_1_neurons, layer_1_synapses)
    layer_1.set_linked_synapses()

    output_neurons = [output_neuron]
    output_synapses = [
        Synapse(output_neuron, output_neuron, 1.0),
    ]
    output_layer = Layer('output_layer', output_neurons, output_synapses)
    output_layer.set_linked_synapses()

    all_layers = [input_layer, layer_1, output_layer]

    return all_layers


if __name__ == '__main__':
    # all_layers = generate_layers_1()

    # input_ideal = [[0, 0], [0, 1], [1, 0], [1, 1]]
    # output_ideal = [[0], [1], [1], [0]]
    # all_layers = generate_layers_xor() work!

    input_ideal = []
    output_ideal = []
    for i in range(0, 900):
        input_ideal.append([i/1000])
        output_ideal.append([i/2000])
    all_layers = generate_layers_linear_regression()# work!

    test_all(input_ideal, output_ideal, all_layers)