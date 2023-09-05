#Author Sebastián López 


# TestBatteryDischarge
Test Battery Discharge for Electronic Sensor
This system consists of two key components:
an Arduino code file named "TEST_DISCHARGE_BATTERY," 
designed to transmit real-time battery voltage data.
In this process, the battery receives two levels of discharge:
0 volts through the digital pin for 60 seconds 
and then 5 volts through the same digital pin for the subsequent 60 seconds.
Additionally, the system includes a file named "SAVE_DATA_SQLITE_BATTERY" responsible for storing real-time data
transmitted by Arduino through the Serial port at a speed of 9600 bauds in an SQLITE database. 
These data are updated automatically every 60 seconds. To visualize data regarding different voltages over time 
for the batteries being measured, the system employs a file called "tes1.py." 
This graph is also updated every 60 seconds to reflect the most recent data.
