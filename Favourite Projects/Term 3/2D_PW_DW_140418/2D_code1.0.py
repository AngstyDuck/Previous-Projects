#Installed dependencies: pandas, xlrd
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import math
import os, os.path
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#For pandas to open and print an excel file
# file_read = pd.ExcelFile(r"C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\temp_51.xlsx")
# sheet_1 = pd.read_excel(r"C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\temp_51.xlsx",sheet_name=0)


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
    # Modules:
    # numpy
    #
    #retrieve dataframe from text file
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
    # Modules:
    # nil
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
            time_list.append(round(float(i_list[j*2-2]),2))
            temp_list.append(float(i_list[j*2-1]))
        #print("time_list: {0}, temp_list: {1} ".format(time_list, temp_list))
        data_frame_collective.append([frame_name,time_list,temp_list])
    return data_frame_collective


def nested_list_to_pickle(input_list):
    #
    # Receives the nested list from function text_to_nested_list and converts data into pickle and
    # sorts accordingly.
    #
    # Input:
    # Output of text_to_nested_list; Nested list. In the outermost element of list
    # are lists that represent the dataset of 1 experiment (where actual temp of water is __).
    # In the next layer contains 3 elements, first element is actual temperature of water, then
    # list containing instances of time where temp is taken, last list contains the values of
    # these respective temperatures.
    #
    # Output:
    # None. Will print('done') once per pickle file written.
    #
    # Note:
    # This function is supposed to be used just once. It will overwrite existing pickle files if
    # they exist in the folders.
    #
    # Modules:
    # pickle, pandas
    #

    count_dict = {'10':0, '15':0, '20':0, '25':0, '30':0, '35':0, '40':0, '45':0, '50':0, '55':0, '60':0}
    for i in input_list:
        the_value = i[0]
        count_dict['{0}'.format(the_value)] += 1
        sub_dataframe = pd.DataFrame({'time (s)': i[1], 'reading': i[2]})
        pickle_out = open(r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\pickle_file_real\{1}\{1}_{0}.pickle'.format(
            count_dict['{0}'.format(the_value)], the_value), 'wb')
        pickle.dump(sub_dataframe, pickle_out)
        pickle_out.close()
        print('done')


def read_pickle_in_pandas(input_file):
    #
    # Takes in open() variable and output pandas dataframe
    #
    # Input:
    # Directory to the file, like
    # r'\Users\User\Desktop\Work\2D\2D_PW_DW\Data\pickle_file_real\10\10_1.pickle'
    #
    # Output:
    # The Dataframe in Pandas format
    #
    # Modules:
    # pickle, pandas
    #

    file = input_file
    pickle_in = open(file, 'rb')
    output = pickle.load(pickle_in)
    return output


def pandas_to_nparray(input_dataframe):
    #
    # Converts Pandas dataframe of our database into a numpy array
    #
    # Input:
    # Dataframe in pandas format. (output of function read_pickle_in_pandas)
    #
    # Output:
    # numpy array of 2 rows. First row is all timings, second row is  all
    # readings at respective timings
    #
    # Modules:
    # pandas
    #

    reading_array = input_dataframe['reading'].as_matrix()
    time_array = input_dataframe['time (s)'].as_matrix()
    output_array = np.vstack((time_array, reading_array))
    return output_array


def single_graph_plotter(input_array):
    #
    # Plot graph cos I'll prob forget those functions in the next 3 mins lol
    #
    # Input:
    # Array of 2 rows. (The array of one temperature of water) First row consist of timings of one temp of water,
    # other row is temp recorded for respective timings for one temp of water.
    #
    # Output:
    # None. A graph appears
    #
    # Modules:
    # matplotlib.pyplot, numpy
    #

    array = input_array
    nested_list = array.tolist()
    x = nested_list[0]
    y = nested_list[1]

    plt.plot(x, y, 'ro')
    plt.show()


def polyfit_and_accuracy_calculation(input_array):
    #
    # Attempts to find out which graph best represents the raw output of temperature sensor for
    # each experiment. Realised that log functions aren't as accurate as we thought. Concludes
    # using polynomial functions instead.
    #
    # Input:
    # numpy array of 2 rows and 16/17 columns. First row is time, second row is temperature of water
    # recorded at respective timings
    #
    # Output:
    # a string with a list of the accuracies of various functions. Basically the lower the value, the
    # better a function could represent a particular experiment
    #
    # Modules:
    # numpy, math
    #

    x_array = input_array[0,:]
    y_array = input_array[1,:]


    #------log function
    coeff1 = np.polyfit(np.log(x_array), y_array, 1)  # used in f1
    def f1(x):
        return coeff1[0]*math.log(x)+coeff1[1]
    #------x**2 function
    coeff2 = np.polyfit(x_array, y_array, 2)  # used in f2
    def f2(x):
        return coeff2[0]*(x**2)+coeff2[1]*x+coeff2[2]
    #------x**3 function
    coeff3 = np.polyfit(x_array, y_array, 3)  # used in f3
    def f3(x):
        return coeff3[0] * (x**3) + coeff3[1] * (x ** 2) + coeff3[2] * x + coeff3[3]
    #------x**4 function
    coeff4 = np.polyfit(x_array, y_array, 4)  # used in f4
    def f4(x):
        return coeff4[0] * (x**4) + coeff4[1] * (x**3) + coeff4[2] * (x ** 2) + coeff4[3] * x + coeff4[4]
    #------x**5 function
    coeff5 = np.polyfit(x_array, y_array, 5)  # used in f5
    def f5(x):
        return coeff5[0] * (x**5) + coeff5[1] * (x**4) + coeff5[2] * (x**3) + coeff5[3] * (x ** 2) + coeff5[4] * x + coeff5[5]


    def average_accuracy_test(function):
        list_accuracies = []
        for i in range(len(x_array)):
            accuracy = abs((y_array[i] - function(x_array[i]))/y_array[i])
            list_accuracies.append(accuracy)
        return (sum(list_accuracies))/len(list_accuracies)

    return 'f1: {0}, f2: {1}, f3: {2}, f4: {3}, f5: {4}'.format(average_accuracy_test(f1), average_accuracy_test(f2), average_accuracy_test(f3), average_accuracy_test(f4), average_accuracy_test(f5))


def average_coeff_per_temp(input_temp, input_power=5):
    #
    # returns average coefficient retrieved from all experiments of a particular temprature of
    # water
    #
    # Input:
    # string or int representing temperature of water which we want to extract experiment data
    # from
    #
    # Output:
    # numpy representing average coeff of an equation
    #
    # functions:
    # read_pickle_in_pandas, pandas_to_nparray,
    #
    # Modules:
    # os, os.path, pandas, pickle, numpy
    #

    temp = str(input_temp)
    directory = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\pickle_file_real\{0}'.format(temp)
    list_of_files = os.listdir(directory)

    def single_coeff_finder(input_x_array, input_y_array):
        x_array = input_x_array
        y_array = input_y_array

        coeff = np.polyfit(x_array, y_array, input_power)  # used in f5
        return coeff

    #-------Create a list with (turples of coefficients of an experiment) as element----------
    list_of_list = []
    for i in list_of_files:
        pickle_address = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\pickle_file_real\{0}\{1}'.format(temp, i)
        array = read_pickle_in_pandas(pickle_address)
        nparray = pandas_to_nparray(array)

        x_array = nparray[0, :]
        y_array = nparray[1, :]

        list_of_list.append(list(single_coeff_finder(x_array, y_array)))

    #averages out coefficients and output as list of int
    list_of_average_coefficients = []
    array_of_coefficients = np.array(list_of_list)
    number_of_coefficients = len(list_of_list[0])
    for i in range(0,number_of_coefficients):
        list_of_average_coefficients.append(np.mean(array_of_coefficients[:,i]))

    return np.array(list_of_average_coefficients)


def average_coeff_per_temp_accuracy_tester(input_array_coefficient, input_temp):
    #
    # Runs coeffs provided
    #
    # Input:
    # input_array_coefficient: numpy array of shape (1,). Represents all coefficients of polynomial function, starting
    # with that of the biggest power of x and ending with coeff of x**0
    # input_temp: int or str of temperature of water
    #
    # Output:
    # float representing the value of accuracy of the coefficients used as a polynomial
    # representation of the raw output of temperature sensor
    #
    temp = str(input_temp)
    array_coefficient = input_array_coefficient

    #-------creates polynomial function with power depending on elements of coeff array. Requires variable 'array_coefficient'----------
    input_array_coefficient_len = len(array_coefficient)
    def f(x):
        output = 0
        input_array_coefficient_flipped = np.flip(array_coefficient,0)  #flips the array along vertical axis
        for i in range(input_array_coefficient_len):
            output += input_array_coefficient_flipped[i] * (x**i)
        return output

    #---------------------test polynomial function with all available experiment data in folder; outputs accuracy-----------------------
    directory = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\pickle_file_real\{0}'.format(temp)
    list_of_files = os.listdir(directory)

    list_of_accuracies_across_all_data = []
    for i in list_of_files:
        pickle_address = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\pickle_file_real\{0}\{1}'.format(temp, i)
        array = read_pickle_in_pandas(pickle_address)
        nparray = pandas_to_nparray(array)

        x_array = nparray[0, :]
        y_array = nparray[1, :]

        for i in range(len(x_array)):
            y_test = f(x_array[i])
            accuracy_of_individual_experiment = (abs(y_array[i]-y_test))/y_array[i]
            list_of_accuracies_across_all_data.append(accuracy_of_individual_experiment)
    mean_of_all_accuracies_in_list = np.mean(np.array(list_of_accuracies_across_all_data))

    #------------------------------------------

    return mean_of_all_accuracies_in_list


#and finally...

def ultimate_linear_regression_number_smasher_9000(input_power=1):
    #
    # This function is like the avengers infinity war of this project. I'm hyped hohohoho
    #
    # With the max power of a polynomial equation of our choice, it outputs an equation which will be used for our project
    # Note: the number of linear regressions that will happen depends on the power of the polynomial equation (i.e.
    # the number of coeffs that we'll be involving)
    #
    # Input:
    # input_power: str or int that represents max power of polynomial equation
    #
    # Output:
    # string that displays equation we should use.
    #
    # Modules:
    # sklearn, sklearn.metrics
    #
    # Functions:
    # average_coeff_per_temp, average_coeff_per_temp_accuracy_tester
    #

    power = int(input_power)
    list_of_temperatures = [10,15,20,25,30,35,40,45,50,55,60]


    #create the ultimate array
    """
    Creates a numpy array with (len(list_of_temperatures)) number of rows and (power) number of columns.
    First row would be coeffs at temperature:10, last being 60
    First column would be coeffs for all temperature for their x**(max power) of their equations, last being the coeff
    of their x**0 of their equations
    """
    # ultimate_array = np.empty([0,power+1])
    # #print('shape of empty array: {0}'.format(ultimate_array.shape))
    # for i in list_of_temperatures:
    #     array_coeff = average_coeff_per_temp(i, power)
    #     array_coeff = array_coeff.reshape((1,-1))
    #     #print('for array for power {0}, shape is : {1}'.format(i, array_coeff.shape))
    #     ultimate_array = np.vstack((ultimate_array,array_coeff))
    #
    # shape_of_ultimate_array = ultimate_array.shape
    # print('array: {0}, shape: {1}'.format(ultimate_array, shape_of_ultimate_array))
    """
    Converts columns of an array into a nested list, with the first row being in the first element of
    the list. 
    Hence the first element,
    represents list of all coeffs of x**(max power) with the first element of the list
    representing coeff of x**(max power) at temperature = 10
    The last element,
    represents list of all coeffs of x**0 with the last element of the list
    representing coeff of x**0 at temperature = 60
    """
    #-------------change of plans, t set const at 25s------------------
    list_of_raw_input_of_sensor = []
    # list represents the raw input of temperature sensor at time=25 where temperature
    # increases from 10 to 60. First element is where temperature is 10
    for i in list_of_temperatures:
        array_coeff = average_coeff_per_temp(i, power)
        array_coeff = array_coeff.reshape((1, -1))
        # array_coeff represents array of coeff of polynomial function, fisrt element is coeff
        # of biggest power of x, last element is coeff of smallest power of x

        output = 0
        input_array_coefficient_flipped = np.flip(array_coeff, 0)  # flips the array along vertical axis
        input_array_coefficient_len = len(array_coeff)

        for i in range(input_array_coefficient_len):
            output += input_array_coefficient_flipped[i] * (25 ** i)
        # output represents the raw value of input of temperature sensor when temp of water is
        # i and time is 25 seconds
        print(output)
        list_of_raw_input_of_sensor.append(output)

    #print(list_of_raw_input_of_sensor)


















#----------------------------------------------------------------------------------------
address = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\Data\data_real_2.txt'
pickle_address = r'C:\Users\User\Desktop\Work\2D\2D_PW_DW\linear_regression_coefficient.pickle'

# #To update latest text file into pickle format
# nested_list = text_to_nested_list(address)
# nested_list_to_pickle(nested_list)
#
#To test polynomial equation that represents raw output from tem sensor with time per experiment
# array = read_pickle_in_pandas(pickle_address)
# nparray = pandas_to_nparray(array)
# test_coeff = polyfit_and_accuracy_calculation(nparray)
#
# #To create a numpy array of coeff of polynomial equation representing relationship between time and raw input of temperature sensor
# coeff = average_coeff_per_temp(10,1)
# accuracy = average_coeff_per_temp_accuracy_tester(coeff, 50)
# print(coeff)

# da_results = ultimate_linear_regression_number_smasher_9000()

print(array)


