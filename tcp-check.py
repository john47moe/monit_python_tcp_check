import subprocess
threashold=4
host_dict={'10.10.10.4':'jmaster.ops.raindrop.best','10.10.10.5':'jworker.ops.raindrop.best'}
netstat_cmd = "netstat -anlp | grep ESTABLISHED | grep ':8080' | awk -F ':'  '{ print $2 }' | awk '{ print $2 }'"
result = subprocess.check_output(netstat_cmd, shell=True)
list_result = result.split('\n')
for ipadd in list_result:
        if ipadd in host_dict.keys():
                if ipadd in host_dict.keys():
                        print ipadd,host_dict[ipadd].upper()
