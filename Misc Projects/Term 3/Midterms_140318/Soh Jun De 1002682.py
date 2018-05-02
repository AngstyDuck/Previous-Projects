#Note: Q4,5,6 inside



# MID-TERM EXAM: QUESTION 5
def nroot(n, t, num):
    x0 = 1
    i = 1
    while i < t:
        func1 = x0 ** n - num
        func2 = n * (x0 ** (n - 1))
        x0 = x0 - (func1 / func2)
        i += 1
    return round(x0, 3)


def nroot_complex(n, t, num):
    if num < 0 and n % 2 == 0:
        # case 2, complex with no real part
        const = nroot(n, t, num * (-1))
        return const * 1J

    elif num < 0 and n % 2 != 0:
        # case 3, negative real number
        const = nroot(n, t, num * (-1))
        return const * (-1)


#Question 6
import pickle


def read_stations(f):
    outputDict = {}
    x = f.read()
    splitx = x.split('\n')
    # splitx.remove('')
    for i in range(len(splitx)):
        if splitx[i][0] == '=':
            outputDict[splitx[i][1:-1]] = splitx[i + 1]
    """
    convert file into one string
    split string into lists with '\n'
    as long as the first character of each element is '=', that would be a name of a line. take the [1:-1] of the line name (as dictionary element name), and the next element (as dictionary element value)
    finally, take the values of all dictionary element and split with ','.

    """


def get_stationline(mrt):
    outputDict = {}
    for lines in mrt:
        for stations in mrt[lines]:
            if (stations in outputDict):
                outputDict[stations].append(lines)
            else:
                outputDict[stations] = [lines]
    return outputDict


def get_interchange(stationline):
    outputDict = {}
    for stations in stationline:
        if len(stationline[stations]) > 1:
            outputDict[stations] = stationline[stations]
    return outputDict


##### Testing get_stationline ###########
with open('stations_short.pickle', 'rb') as f:
    mrt_d = pickle.load(f)
    print(get_stationline(mrt_d))
#########################################

##### Testing get_interchange ###########
with open('lines_short.pickle', 'rb') as f:
    lines = pickle.load(f)
    print(get_interchange(lines))


#########################################

###### Testing find_path ################
# You can use these three variables in your find_path
# to get the output of
# mrt_d = read_station()
# lines = get_stationline()
# interchange = get_interchange()
# even if you haven't finished these three functions
#########################################
def find_path(f, start, end):
    with open('stations_short.pickle', 'rb') as f:
        mrt_d = pickle.load(f)
    with open('lines_short.pickle', 'rb') as f:
        lines = pickle.load(f)
    with open('interchange_short.pickle', 'rb') as f:
        interchange = pickle.load(f)
    """
    Check if start and end belong in the same list within a dictionary element. If so, return this path by taking index(start) and index(end) and append all elements in betweeen into a list for output

    if not, 
    """
    pass


#Question 4
def det2(matrix):
    output = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    return output


def determinant(matrix):
    check = len(matrix)

    for i in matrix:
        if len(i) != check:
            return None

    if check == 1:
        return matrix[0][0]
    elif check == 2:
        return det2(matrix)
    elif check == 3:
        part0a = matrix[0][0]
        part0b = [[matrix[1][1], matrix[1][2]], [matrix[2][1], matrix[2][2]]]

        part1a = matrix[0][1]
        part1b = [[matrix[1][0], matrix[1][2]], [matrix[2][0], matrix[2][2]]]

        part2a = matrix[0][2]
        part2b = [[matrix[1][0], matrix[1][1]], [matrix[2][0], matrix[2][1]]]

        output = part0a * det2(part0b) - part1a * det2(part1b) + part2a * det2(part2b)
    else:
        return None
    return output