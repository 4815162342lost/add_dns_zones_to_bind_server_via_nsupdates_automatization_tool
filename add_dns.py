#!/usr/bin/python3
import re

direct_output_file=open("direct.txt", "w")
direct_output_file.write("zone backup.local.\n")

reverse_output_file=open("reverse.txt", "w")
reverse_output_file.write("zone 168.192.in-addr.arpa.\n")


with open("dns_to_add.txt", "r") as dns:
    for curren_string in dns.readlines():
        curren_string=curren_string.rstrip()
        data=re.split(" +", curren_string)
        print(data[0], data[1])
        octets=data[0].split(".")
        direct_output_file.write("update add " + data[1] + " 3600 IN A " + data[0] + "\n")
        reverse_output_file.write("update add " + octets[3] + "." + octets[2] +  ".168.192.in-addr.arpa. 3600 PTR " + data[1] + ".\n")

direct_output_file.close()
reverse_output_file.close()
