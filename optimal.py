from yamale import YamaleError
import yamale
import functools
from functools import reduce
import yaml
"""
Validation function validates the input conditions with schema as the reference taken from Surbhi and Prerna's code
"""
def validation():
    #Create a schema object
    schema = yamale.make_schema('./schema.yml', parser='ruamel')
    # Create a Data object
    try:
        data = yamale.make_data('./fam_memoryserver_config.yaml', parser='ruamel')
    except Exception as s: #This line shows an exception if two memory_server_ids are repeated.
        print('The error is\n%s' % str(s))
    #To validate
    try:
        yamale.validate(schema, data)
        print('Validation success! 👍')
    except ValueError as e:
        print('Validation failed!\n%s' % str(e))    


"""
Compare function is created to check the differences between the two memory_server. 
The difference found between the two is printed.
Taken from Prerna
"""

def compare():
    try:
            co=0
            c1=0
            flag = 0
            flag1=0
            cou = 0
            coun=0
            f = 0
            f1=0
            f2=0

            #creates list
            data= open("./fam_memoryserver_config.yaml", 'r')
            parsed_yaml=yaml.safe_load(data)
            print('The length of list is %d'  %int(len(parsed_yaml)))
            #Calculates the number of lists(memory_server_id) available
            mysets = (set(x.items()) for x in parsed_yaml.values())
            #K=reduce(lambda a,b: a.intersection(b), mysets)
            #print('The conditions that are repeated is\n%s' % str(K))
        
            #print(ls)
            fail = 0
            def yaml_loader(filepath):
                with open('./fam_memoryserver_config.yaml',"r") as file_descriptor:
                    data = yaml.load(file_descriptor)
                    return data

            def yaml_dump(filepath,data):
                with open(filepath,"w") as file_descriptor:
                    yaml.dump(data, file_descriptor)

            if __name__ == "__main__":
                file_path = "./fam_memoryserver_config.yaml"
                data = yaml_loader(file_path)
            c = 0
            memser = data['Memservers']
            m = int(len(parsed_yaml))
            print(m)
            rpc_interface_list_ip = []
            rpc_interface_list = []
            lib_fabric_list = []
            memory_type_list = []
            fam_path_list = []
            for x in range(m+1):
                rpc_interface_list.append(memser[x]['rpc_interface'])
                str1 = memser[x]['rpc_interface']
                ss1 = str1.split(":",1)[1]
                s1 = str1.rpartition(':')[0]
                memory_type_list = memser[x]['memory_type']
                rpc_interface_list_ip.append(s1)
                fam_path_list.append(memser[x]['fam_path'])
                lib_fabric_list.append(memser[x]['libfabric_port'])

            #Surbhi's code for validating memory type

                if not(memser[x]['memory_type']=='volatile' or memser[x]['memory_type']=="persistent"):
                    print("Validation Failed for memory type server no: ", c)
                    exit(0)
                s = str(memser[x]['memory_type'])
                i = s[0:3]
                st = str(memser[x]['fam_path'])
                j = st.rfind('/')
                k = st.rfind('_')
                stt = st[j+1:k]
                if(stt == i):
                    fail = 0
                else:
                    fail=-1
                    break

            if(fail==-1):
                print("Memory type: ", i, "\nFam_path: ", stt)
                print("The memory type and fam_path does not match")
                exit(0)
            else: 
                print("The memory type and fam_path matches")
            rpc_ip = 0
            rpc = 0
            lib_fabric = 0
            fam_path = 0
            chec = " "
                

        #Checking for duplicates and validating rpc_interface by checking rpc_interface IP and Port numbers

            if(len(rpc_interface_list)==len(set(rpc_interface_list))):
                rpc = 0
                
                if(len(rpc_interface_list_ip)==len(set(rpc_interface_list_ip))):    
                    rpc_ip = 0
                else:
                    rpc_ip = -1
                    print("Rpc_interface IP Duplicate")
                    chec = "ip"
            else:
                chec = "rpc"
                print("Rpc_interface Duplicate")
                rpc= -1
            #Checking for duplicates and validating fam_path by checking rpc_interface IP and fam_path values

            if(rpc_ip == 0 and rpc ==0):
                if(len(rpc_interface_list_ip)!=len(set(rpc_interface_list_ip))):
                    rpc_ip = -1
                    chec = "ip"
                    print("Rpc_interface IP duplicate")
                    if(len(fam_path_list)==len(set(fam_path_list))):
                        fam_path = 0
                    else:
                        chec = "fam"
                        fam_path = -1
                        print("Fam_path Duplicate")
                else:
                    rpc_ip = 0

            #Checking for duplicates and validating fam_path by checking rpc_interface IP and Lib_fabric values


                if(len(rpc_interface_list_ip)!=len(set(rpc_interface_list_ip))):
                    chec = "ip"
                    print("Rpc_interface Duplicate")
                    if(len(lib_fabric_list)!=len(set(lib_fabric_list))):
                        chec = "lib"
                        lib_fabric = -1
                        print("Libfabric_port Duplicate")
                    else:
                        lib_fabric = 0
                else:
                    rpc_ip = 0
            else:
                print("\n")
            
            if(chec == "lib"):
                res = [idx for idx,val in enumerate(lib_fabric_list) if val in lib_fabric_list[:idx]]
                print("The positions of duplicates for libfabric_port: " + str(res))
            if(chec == "fam"):
                res = [idx for idx,val in enumerate(fam_path_list) if val in fam_path_list[:idx]]
                print("The positions of duplicates for fam_path: " + str(res))
            if(chec == "ip"):
                res = [idx for idx,val in enumerate(rpc_interface_list_ip) if val in rpc_interface_list_ip[:idx]]
                print("The positions of duplicates for rpc_interface IP: " + str(res))
            if(chec == "rpc"):
                res = [idx for idx,val in enumerate(rpc_interface_list) if val in rpc_interface_list[:idx]]
                print("The positions of duplicates rpc_interface: " + str(res))
            if(rpc_ip==0 and rpc == 0 and fam_path==0 and lib_fabric==0):
                print("There are no Duplicates")
    except Exception as exc:
        print('The error is\n%s' % str(exc))
validation()
compare()
