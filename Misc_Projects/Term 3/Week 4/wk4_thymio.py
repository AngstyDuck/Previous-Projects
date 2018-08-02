from pythymiodw import *
from time import sleep
from firebase import firebase

url = 'https://dweek4-f08e5.firebaseio.com/' # URL to Firebase database
token = 'fxF8PN2nAshrXpWAxfzesxfFjpiXlxZg6CiWXdYX' # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)

robot = ThymioReal() # create an eBot object

no_movements = True

while no_movements:

    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the eBot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here


# Write the code to control the eBot here

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

