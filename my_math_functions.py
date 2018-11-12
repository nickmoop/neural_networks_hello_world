# coding: utf8
import math


def calculate_rmse(output_layer, output_ideal):
    output_error = 0
    i = 0
    for neuron in output_layer.neurons_list:
        output_error += (neuron.output - output_ideal[i]) ** 2
        i += 1

    return output_error**0.5 / len(output_layer.neurons_list)


def calculate_mse(output_layer, output_ideal):
    output_error = 0
    i = 0
    for neuron in output_layer.neurons_list:
        output_error += (neuron.output - output_ideal[i]) ** 2
        i += 1

    return output_error / len(output_layer.neurons_list)


def linear(argument):
    return argument


def derivative_linear(argument):
    return 1


def sigmoid(argument):
    return 1 / (1 + math.exp(-argument))


def derivative_sigmoid(argument):
    return (1 - argument) * argument
