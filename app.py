import datetime;
import socket;
 
# current_Time stores current time
current_Time = datetime.datetime.now()
print("current time:-", current_Time)
 
# time_Stamp store timestamp of current time
time_Stamp = current_Time.timestamp()
print("timestamp:-", time_Stamp)

host_Name=socket.gethostname()
print("current host name is:-", host_Name )