import subprocess
import json
i = 0
while i < 2000:# 199865 items in , set 2000 here
    cmd = "curl -XGET -i -H 'accept-encoding: application/json' http://10.10.10.100:8000/api/search\?vertexType\=software\&pageSize\=100\&page\=" + str(i)
    sub = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    sub.wait()
    str1 = sub.stdout.read()
    str1 = str1.decode()
    str2 = str1.split('{', 1)
    str3 = "{" + str2[1]
    # print str1.split('{')
    with open("./demo-data/software/software_" + str(i) + ".json", "w") as f:
        json.dump(str3, f)
        print("write " + str(i + 1) + " time(s)")
    i += 1