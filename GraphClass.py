# coding: utf8
from tkinter import *


class Graph:

    def __init__(self, layers_list):
        self.layers_list = layers_list
        self.main_window = make_main_window()
        self.field_network = make_field_network(self.main_window)
        self.fx = 120
        self.fy = 120
        self.size = 15
        self.additional_coordinates = 50
        self.neuron_color = 'black'
        self.neuron_label_color = 'black'
        self.neuron_input_color = 'blue2'
        self.neuron_output_color = 'blue2'
        self.synapse_color = 'black'
        self.synapse_weight_color = 'green'
        self.synapse_gradient_color = 'red'

    def paint_graph(self):
        neurons = {}
        for layer_number in range(0, len(self.layers_list)):
            layer = self.layers_list[layer_number]
            list_of_neurons = layer.neurons_list
            neurons.update(self.paint_neurons(list_of_neurons, layer_number))

        for layer_number in range(0, len(self.layers_list)):
            layer = self.layers_list[layer_number]
            list_of_synapses = layer.synapses_list
            self.paint_synapses(list_of_synapses, neurons)

        self.main_window.mainloop()

    def paint_neurons(self, list_of_neurons, layer_number):
        neurons = {}
        i = 0
        for neuron in list_of_neurons:
            x_center = self.fx*layer_number + self.additional_coordinates
            y_center = self.fy*i + self.additional_coordinates + i*30*layer_number
            x_1 = x_center - self.size
            y_1 = y_center - self.size
            x_2 = x_center + self.size
            y_2 = y_center + self.size

            self.field_network.create_oval(
                x_1, y_1, x_2, y_2, fill=self.neuron_color
            )
            # show neuron name
            self.field_network.create_text(
                x_1 - 30, y_1 - 20, anchor='nw',
                text=neuron.name, fill=self.neuron_label_color
            )
            # show neuron input
            self.field_network.create_text(
                x_center - 40, y_center - 15, anchor='nw',
                text='{:.2f}'.format(neuron.input),
                fill=self.neuron_input_color
            )
            # show neuron output
            self.field_network.create_text(
                x_center + 20, y_center - 15, anchor='nw',
                text='{:.2f}'.format(neuron.output),
                fill=self.neuron_output_color
            )
            i += 1
            neurons.update({neuron.name: [x_center, y_center]})

        return neurons

    def paint_synapses(self, list_of_synapses, neurons_coordinates):
        for synapse in list_of_synapses:
            x_1, y_1 = find_coordinates(synapse.neuron_transmitter.name, neurons_coordinates)
            x_2, y_2 = find_coordinates(synapse.neuron_receiver.name, neurons_coordinates)

            if x_1 == x_2:
                x_2 = x_1 + 100

            self.field_network.create_line(
                x_1, y_1, x_2, y_2, fill=self.synapse_color
            )
            # show synapse weight
            self.field_network.create_text(
                (x_1 + x_2) / 2, (y_1 + y_2) / 2, anchor='nw',
                text='{:.3f}'.format(synapse.weight),
                fill=self.synapse_weight_color
            )
            # show synapse gradient
            # self.field_network.create_text(
            #     (x_1 + x_2) / 2, (y_1 + y_2) / 2 - 12, anchor='nw',
            #     text='{:.3f}'.format(synapse.gradient),
            #     fill=self.synapse_gradient_color
            # )


def find_coordinates(neuron_name, neurons_coordinates):
    return neurons_coordinates[neuron_name]


def make_main_window():
    main_window = Tk()
    main_window.resizable(False, False)
    main_window.geometry("820x620+0+20")

    return main_window


def make_field_network(main_window):
    field_network = Canvas(main_window, bg='white')
    field_network.place(x=10, y=10, width=800, height=600)

    return field_network


if __name__ == '__main__':
    from test import generate_layers_1

    all_layers = generate_layers_1()
    new_graph = Graph(all_layers)
    new_graph.paint_graph()