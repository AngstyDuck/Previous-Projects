# F01 Group 8 1D Final Project Part II
###### Objective: Using Kivy as a UI, create a program that coordinates the Thymio robot and a rpi camera such that the coordinates of an object on the white background seen on the camera, would be sent to the Thymio, and the Thymio would navigate to the position of the object, return to original position, and await further instructions.

kivy_main_Final.py - To be run on a laptop
sm_cam_Final.py - To be run on a Rpi connected to a PiCamera
sm_thymio_Final.py - To be run on a Rpi connected to a Thymio


To use program:
1. Run each program in each device respectively.
2. The rest of the program would be controlled by the UI provided
by the laptop
3. Press 'Start Program!' button in UI to get camera to scan for
objects in the white background, and move the Thymio towards it
and back.
4. To use the program multiple times simply press this button again
once the robot has returned to its original position.
