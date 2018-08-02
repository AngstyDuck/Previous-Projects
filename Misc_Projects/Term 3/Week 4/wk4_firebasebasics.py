from firebase import firebase

url = "https://dweek4-f08e5.firebaseio.com/" # URL to Firebase database
token = "fxF8PN2nAshrXpWAxfzesxfFjpiXlxZg6CiWXdYX" # unique token used for authentication

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = firebase.FirebaseApplication(url, token)



print("Reading from my database.")



"""
firebase.put('/', 'lazy', True) # put the value True into node lazy
firebase.put('/', 'pie', 3.14) # put the value 3.14 into node pie
"""

