from firebase import firebase
import time


url = r"https://dmini-1ac59.firebaseio.com/" # URL to Firebase database
token = "NKLCd1EWC9buuxN9tJw3Oe6djsZQVTjePSdbiZK1" # unique token used for authentication
firebase=firebase.FirebaseApplication(url,token)

cam_value = firebase.get('/cam')
command_value = firebase.get('/command')
coord_value = firebase.get('/coord')


print('cam:{0}, command: {1}, coord: {2}'.format(cam_value, command_value, coord_value))
