from dronekit import connect, VehicleMode, LocationGlobalRelative
import time



#Vehicle Connection
drone = connect('127.0.0.1:14551', wait_ready=True)

#Function for arming the drone and takeoff with a variable targetAltitude defined later on 
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

		time.sleep(1)

def LandDrone():
	print("Landing...")
	drone.mode = VehicleMode("LAND")
	while True:
			Altitude = drone.location.global_relative_frame.alt

			print("Altitude: ",Altitude)

			if Altitude <= 0: 
				print ("Aircraft Landed")
				break
			time.sleep(1)
#Calls the function for the drone to arm and takeoff
arm_and_takeoff(20)
#Sets the airspeed to 10m/s
drone.airspeed = 10
#Starts to move to first waypoint
print("Moving to waypoint1...")
#Defines variable with waypoint 1 coordenates
waypoint1 = LocationGlobalRelative(20.736293, -103.457382,20)
drone.simple_goto(waypoint1)
#Waits 30 seconds for the drone to complete waypoint
time.sleep(30)
#Starts to move to second waypoint
print("Moving to waypoint2...")
#Defines variable with waypoint 1 coordenates
waypoint2 = LocationGlobalRelative(20.736282, -103.456859,20)
drone.simple_goto(waypoint2)

time.sleep(30)
#Starts to move to third waypoint
print("Moving to waypoint3...")
#Defines variable with waypoint 3 coordenates
waypoint3 = LocationGlobalRelative(20.735751, -103.456917,20)
drone.simple_goto(waypoint3)

time.sleep(30)
#Starts to move to fourth waypoint
print("Moving to waypoint4...")
#Defines variable with waypoint 4 coordenates
waypoint4 = LocationGlobalRelative(20.735844, -103.457421,20)
drone.simple_goto(waypoint4)

time.sleep(30)
#Starts to move to first waypoint again
print("Moving to waypoint1...")
#Defines variable with waypoint 1 coordenates
waypoint1 = LocationGlobalRelative(20.736293, -103.457382,20)
drone.simple_goto(waypoint1)

time.sleep(30)
#Alerts of returning to home
print("Returning to Home...")
#Changes mode to RTL (Return To Launch)
drone.mode = VehicleMode("RTL")
#Prints battery voltage
print("Battery Voltage: ",drone.battery.voltage)

#LandDrone()