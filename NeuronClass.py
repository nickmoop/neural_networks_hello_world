# coding: utf8
from my_math_functions import (
    linear, derivative_linear, sigmoid, derivative_sigmoid
)


class Neuron:

    def __init__(self, name, activation_function, input=0, output=0, initial=0):
        self.name = name
        self.input = input
        self.output = output
        self.activation_function = activation_function
        if activation_function == linear:
            self.derivative_function = derivative_linear
        elif activation_function == sigmoid:
            self.derivative_function = derivative_sigmoid
        self.initial = initial
        self.linked_synapses = []
        self.delta = 0

    def calculate_output(self):
        self.output = self.activation_function(self.input)

    def send_output_to_next_layer(self):
        for synapse in self.linked_synapses:
            synapse.send_signal()

    def calculate_delta(self, output_ideal):
        self.delta = (output_ideal - self.output) * self.derivative_function(self.output)

    def set_default(self):
        self.output = 0
        self.input = self.initial


def calculate_all_neurons_delta(reversed_list_of_layers):
    for layer in reversed_list_of_layers[1:]:
        for neuron in layer.neurons_list:
            delta_sum = 0
            for synapse in layer.synapses_list:
                if synapse.neuron_transmitter == neuron:
                    delta_sum += synapse.weight * synapse.neuron_receiver.delta

            neuron.delta = neuron.derivative_function(neuron.output) * delta_sum


def calculate_output_neurons_delta(list_of_layers, output_ideal):
    output_layer_neurons = list_of_layers[-1].neurons_list
    i = 0
    for neuron in output_layer_neurons:
        neuron.calculate_delta(output_ideal[i])
        i += 1


def set_input_neurons(input_layer, input_ideal):
    i = 0
    for neuron in input_layer.neurons_list:
        neuron.input = input_ideal[i]
        i += 1


def clear_all_signals(all_layers):
    for layer in all_layers:
        for neuron in layer.neurons_list:
            neuron.set_default()


if __name__ == '__main__':
    print(sigmoid(0.45))