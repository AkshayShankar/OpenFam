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
            for x in range(m+1):
                if(f2==1 and flag1==1 and (f1==1 or f==1)):
                    break
                co=0 #LIBFABRIC_PORT
                c1=0
                
                cou = 0
                coun=0
                
                
                for y in range(m+1):
                    if(f2!=1):
                        f2=0 #FAM_PATH
                    #Code to check if fam_path is being shared, we do this by checking if fam_path and IP are the repeated"""
                        str1 = memser[x]['rpc_interface']
                        str2 = memser[y]['rpc_interface']
                        s1 = str1.rpartition(':')[0]
                        s2 = str2.rpartition(':')[0]
                        if(memser[x]['fam_path'] == memser[y]['fam_path']):
                            if(s1==s2):
                                c1=c1+1
                        if(c1==2):
                            f2=1
                
                #Code to check if the rpc_interface is the repeated or not by checking if the IP address and port number is the same
                    if(f==0 and f1==0):
                        f = 0 #RPC_INTERFACE
                        f1=0 #RPC_INTERFACE
                        ss1 = str1.split(":",1)[1]
                        ss2 = str2.split(":",1)[1]
                        if(s1==s2):
                            cou=cou+1
                            if(ss1==ss2):
                                coun = coun+1
                        elif(s1!=s2):
                            if(ss1==ss2):
                                coun=coun+1
                        if(cou==2 and coun==2):
                            print("IP:Port is being shared at ", x)
                            f = 1
                            f1=1
                        if(cou==2 and coun!=2):
                            f=1
                        if(coun==2 and cou!=2):
                            f1=1
                    
                #Code for rpc_interface ends here

                #Code here to check if Libfabric_port is the repeated or not, depends on the IP Address and the libfabric_port
                    if(flag1!=1):
                        flag1=0 #LIBFABRIC_PORT
                        if(s1==s2):
                            if(memser[x]['libfabric_port'] == memser[y]['libfabric_port']):
                                co = co+1
                        if(co==2):
                            flag1 = 1

                #Code for Libfabric_port ends here
                
            if(f2==1):
               print("The fam_path is being shared")
            if(flag1==1):
                    print("The Libfabric_port is repeated")
            if(f==1 and f1!=1):
                    print("The IP adress is the repeated but Port is different") 
            if(f2!=1):
                print("The fam_path is not being shared") 
            if(f!=1):
                if(f1==1):
                    print("IP is not being shared but Port is being shared ")
                elif(f1!=1):
                    print("IP:Host is not being shared, RPC is unique") 
            if(flag1!=1):
                print("The Libfabric_port is not repeated")
    except Exception as exc:
        print('The error is\n%s' % str(exc))
validation()
compare()