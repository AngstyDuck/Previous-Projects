"""
-Edit value of variable address (at line 74) to address of txt file
-Run prog to print out numpy array

"""


import numpy as np


def text_to_nested_list(file_address_input):
    #
    # Reads the text file readlines and returns a nested list.
    #
    # Input:
    # The location of the txt file
    #
    # Output:
    # Nested list. In the outermost element of list
    # are lists that represent the dataset of 1 experiment (where actual temp of water is __).
    # In the next layer contains 3 elements, first element is actual temperature of water, then
    # list containing instances of time where temp is taken, last list contains the values of
    # these respective temperatures.
    #
    txt_file_open = open(file_address_input, 'r')
    file_readlines = txt_file_open.readlines()

    data_frame_collective = []
    for i in file_readlines:
        #print(i)
        i_list = i.split()
        frame_name = int(i_list[0])
        i_list = i_list[1:]
        time_list = []
        temp_list = []
        for j in range(1,int(len(i_list)/2)):
            time_list.append(round(float(i_list[j*2-2]),0))
            temp_list.append(float(i_list[j*2-1]))
        #print("time_list: {0}, temp_list: {1} ".format(time_list, temp_list))
        data_frame_collective.append([frame_name,time_list,temp_list])
    return data_frame_collective


def function_for_jerry(address_input):
    #
    # Reads text file created for raspi, and outputs a numpy array
    # Requires: function text_to_nested_list
    #
    # Input:
    # Address of txt file
    #
    # Output:
    # A numpy array (which represents a matrix), first column represents actual temperature
    # of water, subsequent columns represent first 15 temperatures recorded for water
    #

    address = address_input
    data_frame_collective = text_to_nested_list(address)

    output_matrix = np.empty([0,16])

    for i in data_frame_collective:
        data_row = i[2][:15]
        data_row.insert(0,i[0])
        data_row = np.array([data_row])
        data_row.reshape(-1,1)
        output_matrix = np.vstack((output_matrix, data_row[:1]))

    return output_matrix




address = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\data_real_2.txt'
print(function_for_jerry(address))