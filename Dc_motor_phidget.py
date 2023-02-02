
from Phidget22.Phidget import *
from Phidget22.Net import *
from Phidget22.Devices.BLDCMotor import *
from Phidget22.Devices.TemperatureSensor import *
import time
import random
import warnings

warnings.filterwarnings("ignore")

#Declare any event handlers here. These will be called every time the associated event occurs.

def onTemperatureChange(self, temperature):
	print("Temperature: " + str(temperature))


#Enable server discovery to allow your program to find other Phidgets on the local network.
Net.enableServerDiscovery(PhidgetServerType.PHIDGETSERVER_DEVICEREMOTE)


#Create your Phidget channels
bldcMotor0 = BLDCMotor()
temperatureSensor0 = TemperatureSensor()
   
#Set addressing parameters to specify which channel to open (if any)
bldcMotor0.setIsRemote(True)
temperatureSensor0.setIsRemote(True)
   
#Assign any event handlers you need before calling open so that no events are missed.
temperatureSensor0.setOnTemperatureChangeHandler(onTemperatureChange)
   
#Open your Phidgets and wait for attachment
bldcMotor0.openWaitForAttachment(20000)
temperatureSensor0.openWaitForAttachment(20000)


param=round(random.uniform(-1,1),2)
paramnew=2

while True:
    if paramnew==2:
        bldcMotor0.setTargetVelocity(param)
        paramnew=0
    else:
        if  random.randint(1,10) >=1:
            print("happend")
            paramnew=round(random.uniform(-1,1),2)
            if param <0 and paramnew >0 or paramnew <0 and param >0:
                if abs(param-paramnew)>0.5:
                    if paramnew >0:
                        paramnew=paramnew - 0.5
                    if paramnew<0:
                        paramnew=paramnew + 0.5
    
    
                    bldcMotor0.setTargetVelocity(paramnew)
    
    
    # Setting Stall Velocity
    # 0 to 2000
    bldcMotor0.setStallVelocity(random.randint(1000,1500))
    
    # Setting Acceleration
    # 0.10 to 100
    bldcMotor0.setAcceleration(round(random.uniform(30,75),2))
    

    
    time.sleep(1)

"""   
#Do stuff with your Phidgets here or in your event handlers.
# -1.00 to 1.00
bldcMotor0.setTargetVelocity(1)


# Setting Stall Velocity
# 0 to 2000
bldcMotor0.setStallVelocity(10)

# Setting Acceleration
# 0.10 to 100
bldcMotor0.setAcceleration(0.1)

# Setting Breaking Strength
# 0.00 to 1.00
bldcMotor0.setBrakingStrength(2)

try:
    input("Press Enter to Stop\n")
except (Exception, KeyboardInterrupt):
    pass

#Close your Phidgets once the program is done.
bldcMotor0.close()
temperatureSensor0.close()

"""
