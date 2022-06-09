import yaml
import string

""" This is the code to make a Yaml file into a dictionary in python"""


def yaml_loader(filepath):
    with open(filepath,"r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath,data):
     with open(filepath,"w") as file_descriptor:
         yaml.dump(data, file_descriptor)

if __name__ == "__main__":
    file_path = "test.yaml"
    data = yaml_loader(file_path)


"""Here we check if the Memservers are unique or not"""


c = 0
d=0
memser = data['Memservers']
for m in memser:
    d=d+1
    c=0
    for i in memser:
        if(m==i):
            c = c+1


"""Limitation is that code is meant for only m Memservers because if it is the same Memserver it overwrites the previous one"""


if(d!=8):
    print("The Memory Servers are not unique")
    exit()
else:
    print("The Memory Servers are unique")
"""print(data['Memservers'][0]['rpc_interface'])"""

"""Code here to check if RPC Interface is the same or not, depends on libfabric_port, if_device and rpc_interface"""


co=0
flag = 0
for x in range(m):
    co=0
    for y in range(m):
        if(memser[x]['rpc_interface'] == memser[y]['rpc_interface']):
            if(memser[x]['libfabric_port'] == memser[y]['libfabric_port']):
                if(memser[x]['if_device'] != memser[y]['if_device']):
                    co = co+1
    if(co==1):
        print("RPC Interface is the same because same rpc_interface, libfabric_port and different device", x)
        flag = 1
        break
        
if(flag!=1):
    print("RPC Unqiue")
str = memser[1]['rpc_interface']

"""s = str.rpartition(':')[0]
print(s)
print(str.split(":",1)[1])"""


"""Code for checking if Fam path is being shared or not"""

cou = 0
f = 0
for a in range(m):
    cou=0
    for b in range(m):
        if(memser[a]['fam_path'] == memser[b]['fam_path']):
            str1 = memser[a]['rpc_interface']
            str2 = memser[b]['rpc_interface']
            s1 = str1.rpartition(':')[0]
            s2 = str2.rpartition(':')[0]
            ss1 = str1.split(":",1)[1]
            ss2 = str2.split(":",1)[1]
            if(s1==s2):
                if(ss1!=ss2):


                    """Showing the fam and the port number just for verification"""


                    print(s1, " and ", s2)
                    print(ss1, " and ", ss2)
                    cou = cou+1
    if(cou==1):
        print("Fam path is being shared at ", a)
        f = 1        
if(f!=1):
    print("Fam Path is not being shared")
    