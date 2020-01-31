
import _sqlite3
import json
import os
samplelist = os.listdir('C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons')
conn = _sqlite3.connect('servers.db')
c = conn.cursor()
samplelist = os.listdir('C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons')
for item in samplelist:
    dingle=item
    with open("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\"+dingle) as data:
        input = json.load(data)

    tempServerId = input['ServerId']
   # print(tempServerId)
    tempServerName = input['ServerName']
    tempGpu = input['Gpu']
    testgpu = c.execute("""Select Gpu from Server where ServerId = '%s'"""% tempServerId)
    result =c.fetchone()
    tryingsomething=(tempGpu,)
    test= str(result[0])
    print(test)
    print(tempGpu)
    if (result[0]==tempGpu):
        print('match')
    else:
         print ('mismatch')
  #  testgpu= c.execute("""Select gpu from server where serverId = tempServerId""")

    tempMemory = input['Memory']
    tempOs = input['Os']
    tempCpuCores = input['CpuCores']
    tempCpu = input['Cpu']
    tempModel = input['Model']
