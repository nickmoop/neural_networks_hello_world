# coding: utf8

from NeuronClass import (
    set_input_neurons, calculate_all_neurons_delta,
    calculate_output_neurons_delta, clear_all_signals
)
from SynapseClass import correct_synapses_weights
from my_math_functions import calculate_rmse, calculate_mse


class Layer:

    def __init__(self, name, neurons_list, synapses_list):
        self.name = name
        self.neurons_list = neurons_list
        self.synapses_list = synapses_list

    def calculate_neurons_outputs(self):
        for neuron in self.neurons_list:
            neuron.calculate_output()

    def send_parameters_to_next_layer(self):
        for neuron in self.neurons_list:
            neuron.send_output_to_next_layer()

    def set_linked_synapses(self):
        for neuron in self.neurons_list:
            for synapse in self.synapses_list:
                if synapse.neuron_transmitter == neuron:
                    synapse.neuron_transmitter.linked_synapses.append(synapse)


def learning_cycle(
    all_layers, input_ideal, output_ideal,
    learning_speed, moment, rmse_minimum, mse_minimum, max_iterations_number
):
    iteration_number = 1
    while iteration_number < max_iterations_number:
        clear_all_signals(all_layers)
        input_layer = all_layers[0]
        output_layer = all_layers[-1]

        set_input_neurons(input_layer, input_ideal)
        send_signal_through_all_layers(all_layers)

        rmse = calculate_rmse(output_layer, output_ideal)
        mse = calculate_mse(output_layer, output_ideal)

        if rmse <= rmse_minimum:
            print('rmse: {} <= {}'.format(rmse, rmse_minimum))
            break
        if mse <= mse_minimum:
            print('mse: {} <= {}'.format(mse, mse_minimum))
            break

        correct_all_weights(all_layers, output_ideal, learning_speed, moment)

        iteration_number += 1

    print_learning_info(iteration_number, input_ideal, all_layers)


def send_signal_through_all_layers(list_of_layers):
    for layer in list_of_layers[:-1]:
        layer.calculate_neurons_outputs()
        layer.send_parameters_to_next_layer()

    list_of_layers[-1].calculate_neurons_outputs()


def correct_all_weights(list_of_layers, output_ideal, learning_speed, moment):
    reversed_list_of_layers = list(list_of_layers)
    reversed_list_of_layers.reverse()

    calculate_output_neurons_delta(list_of_layers, output_ideal)
    calculate_all_neurons_delta(reversed_list_of_layers)
    correct_synapses_weights(reversed_list_of_layers, learning_speed, moment)


def print_learning_info(iteration_number, input_ideal, all_layers):
    # some info
    print('iteration: {}'.format(iteration_number))
    print('input    : {}'.format(input_ideal))
    print('output   : {}'.format(all_layers[-1].neurons_list[0].output))

    for layer in all_layers:
        for synapse in layer.synapses_list:
            print('{}: {}'.format(synapse.name, synapse.weight))
