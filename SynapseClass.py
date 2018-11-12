# coding: utf8


class Synapse:

    def __init__(self, neuron_transmitter, neuron_receiver, weight, name=None):
        self.neuron_transmitter = neuron_transmitter
        self.neuron_receiver = neuron_receiver
        self.weight = weight
        self.gradient = 0
        self.previous_delta_weight = 0
        if name:
            self.name = name
        else:
            self.name = '{} -> {}'.format(
                neuron_transmitter.name, neuron_receiver.name
            )

    def send_signal(self):
        signal = self.neuron_transmitter.output * self.weight
        self.neuron_receiver.input += signal

    def calculate_gradient(self):
        self.gradient = self.neuron_transmitter.output * self.neuron_receiver.delta

    def correct_weight(self, learning_speed, moment):
        delta_weight = learning_speed * self.gradient + moment * self.previous_delta_weight
        self.previous_delta_weight = delta_weight
        self.weight += delta_weight


def correct_synapses_weights(reversed_list_of_layers, learning_speed, moment):
    for layer in reversed_list_of_layers[1:]:
        for synapse in layer.synapses_list:
            synapse.calculate_gradient()
            synapse.correct_weight(learning_speed, moment)
