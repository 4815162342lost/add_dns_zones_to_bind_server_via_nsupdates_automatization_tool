#!/usr/bin/python3
import re
import subprocess
new_dns_add=open("dns_add_after_checks.txt", "w")


with open("dns_to_add.txt", "r") as dns:
    for curren_string in dns.readlines():
        need_remove = 0
        curren_string=curren_string.rstrip()
        curren_string=curren_string.upper()
        data=re.split(" +", curren_string)
        direct_proc=subprocess.Popen("nslookup "+ data [1], shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        direct_proc.wait()
        reverse_proc=subprocess.Popen("nslookup " + data[0], shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        reverse_proc.wait()
        out_direct_proc=direct_proc.stdout.read()
        out_reverse_proc=reverse_proc.stdout.read()


        #ddirect dns entry exists

        if re.search("find", out_direct_proc) == None:
            if re.search(data[0], out_direct_proc, re.IGNORECASE) != None:
                print("Direct zone. The dns entry "  + data[1] + " exists and entry is correct.")
                need_remove+=1
            else:
                print("Direct zone. The dns entry " + data[1] + " exists and entry is not correct. Please, fix it.")

        #reverse dns entry exists
        if re.search("find", out_reverse_proc) == None:
            if re.search(data[1], out_reverse_proc, re.IGNORECASE) != None:
                print("Reverse zone. The dns entry "  + data[0] + " exists and entry is correct.")
                need_remove+=1
            else:
                print("Reverse zone. The dns entry " + data[0] + " exists and entry is not correct. Please, fix it.")
            if need_remove == 1:
                print("Reverse zone OK, but Direct zone is not exists. Direct zone: " + data[1] + ". Reverse zone: " +  data[0])
        else:
            if need_remove == 1:
                print("Direct zone OK, but Reverse zone is not exists. Direct zone: " + data[1] + ". Reverse zone: " + data[0] )

        if need_remove==2:
            pass
        else:
            new_dns_add.write(data[0]  + " " + data[1] + "\n")
print("Checks are done")

