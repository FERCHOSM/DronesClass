import time
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
import Tkinter as tk

def set_velocity_body(vehicle, vx, vy, vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,
            0, 0,
            mavutil.mavlink.MAV_FRAME_BODY_NED,
            0b0000111111000111, #-- BITMASK -> Consider only the velocities
            0, 0, 0,        #-- POSITION
            vx, vy, vz,     #-- VELOCITY
            0, 0, 0,        #-- ACCELERATIONS
            0, 0)
    vehicle.send_mavlink(msg)
    vehicle.flush()

def arm_and_takeoff(TargetAltitude):
    #Says its checking for any error
    print ('Pre-arm Checks...')
    #Says the drone is ready to arm
    print ("Ready to arm: ", drone.is_armable)
    #While the drone is not armable 
    while not drone.is_armable:
        #Prints that it is not armable
        print("Vehicle is not armable, waiting....")
        #If the drone still no armable it will print it every second
        time.sleep(1)
    #It says that the motors will be armed  
    print("WARNING: Arming Motors")
    #It sets the drone in GUIDED Mode
    drone.mode = VehicleMode("GUIDED")
    #It arms the drone
    drone.armed = True
    #Says the drone is armed
    print ("Vehicle Armed")
    #If the drone is not armed ot will wait every second the chance to arm
    while not drone.armed:
        print("Waiting for arming...")
        time.sleep(1)
    #Alerts of taking off
    print("Taking off")
    #Drone takes off to the number of meters defined
    drone.simple_takeoff(TargetAltitude)

    while True:
        #Defines the variable Altitude to encapsule drone's altitude
        Altitude = drone.location.global_relative_frame.alt
        #It prints the altitude
        print("Altitude: ",Altitude)
        #If altitude is at 95% of the defined value it will cout as if it has reached the altitued
        if Altitude >= TargetAltitude * 0.95: 
            print ("Altitude Reached")
            break
        #It waits 1 second
        time.sleep(1)
#It defines the function key
def key(event):
    #it says that we are using the standard keys
    if event.char == event.keysym: #-- standard keys
        #If "r" key is pressed the mode would be changed to RTL
        if event.keysym == 'r':
            drone.mode = VehicleMode("RTL")
            
    else: #-- non standard keys
        #If "Up" is pressed the velocity will change by 5m/S in x axis
        if event.keysym == 'Up':
            set_velocity_body(drone,5,0,0)
        #If "Down" is pressed the velocity will change by -5m/S in x axis    
        elif event.keysym == 'Down':
            set_velocity_body(drone,-5,0,0)
        #If "Left" is pressed the velocity will change by -5m/S in y axis    
        elif event.keysym == 'Left':
            set_velocity_body(drone,0,-5,0)
        #If "Right" is pressed the velocity will change by 5m/S in y axis  
        elif event.keysym == 'Right':
            set_velocity_body(drone,5,5,0)

#Vehicle Connection
drone = connect('127.0.0.1:14551', wait_ready=True)

# Take off to 10 m altitude
arm_and_takeoff(10)
 
# Read the keyboard with tkinter
root = tk.Tk()
print(">> Control the drone with the arrow keys. Press r for RTL mode")
root.bind_all('<Key>', key)
root.mainloop()