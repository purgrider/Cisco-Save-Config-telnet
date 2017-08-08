import getpass
import sys
import telnetlib
import os
import platform

if sys.version_info[0] < 3: #Python Version Check
    input = raw_input

user = input("Enter your username: ") #Request Network Credentials
password = getpass.getpass()

try:
 f = open ('mydevices.txt') #Enter filename with IPs to pull configs against
except IOError:
 print('An error occurred trying to read the file or this file doesnt exist.')
 sys.exit()




for line in f:
    print "Telnet to " + (line)
    HOST = line.strip()
    tn = telnetlib.Telnet(HOST)

    tn.read_until("Username: ")
    tn.write(user + "\n")
    print "Inputting username"
    if password:
        tn.read_until("Password: ")
        tn.write(password + "\n")
    print "Inputting password"

    tn.read_until("#")
    print "Enable prompt detected"
    tn.write("write\n")
    print "Writing config"
    tn.read_until("#")
    print "Config written"
    print "Exiting " + (line)
    tn.write("exit\n")
