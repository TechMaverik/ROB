# ROB - Robotics On Board
<image src="static/studio.png" height=300px width=300px></image>

The project ROB is a robotic arm developed with in-house software, hardware assembly, and custom PCB design. ROB-Studio is the software used to interact with the robot.  
Version 1.0 features a 5-degree-of-freedom robotic arm powered by 6 servo motors, capable of lifting up to 50 g of payload. ROB-Studio is made using the software framework 
called HL-Engine 3, which acts as a middleware to communicate with Hardware and Software.

## ROB version 1.0
## Components Used
1. Servo Motor MG995
2. Servo Motor SG90
3. PCA9685 Servomotor Driver
4. OLED Display 128 x 64
5. ESP32

## Firmware
The baremetal interfacing and control system code is written in Micropython for ESP32

## Procedure of connection of motors and arm pieces
1. Upload the files under Firmware Folder
2. Make sure to provide a valid SSID and Password in the code as per your network connection.
3. Connect the servo motors from channel 0 to channel 5 in order base,shoulder,elbow,wrist-pitch,wrist-yaw,pick.
4. Make sure the servo is set to 90 degress.
5. Adjust the home position according to your requirements.

## Procedure to run the ROB-Studio
1. Install python 3.10 or later version
2. Create a virtual environment called .robot using the command <code>python3 -m venv .robot</code> ( One time )
3. Now run <code> pip3 install -r requirements.txt </code> ( One time )
4. Now run <code> chmod +x ./launcher </code> ( One time )
5. <b>To run the app run ./launcher.py </b>

## Alternative steps to run ROB-Studio
1. Follow the steps till line number 3
2. Now run <code>source .rob/bin/activate </code>
3. Now run <code>python run.py</code>

## ROB Studio
<image src="static/StudioHome.png"></image>
You can control the robor arm by adjusting the slider of each joints and by pressing the Move button. Inorder to record the particular orienttation, one has to adjust the arm and press the Record Button.
<image src="static/StudioRecord.png"></image>
Your recorded operations can be seen under Record and Play tab. You can start running the application by pressing the Play button.
<image src="static/StudioDevice.png"></image>
You can connect the ROB studion to the ROB by entering the IP Address displayed on ROB OLED Display. A sample is shown above.
