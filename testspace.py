
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
    testy = c.execute("""Select RackId from Rack where RackId = '%s'"""% input['Rack']['RackId'])
    result =c.fetchone()
    test= str(result[0])
    print (test)
    c.execute("""delete from  Rack where RackId= '%s'"""%test)
  #  testgpu= c.execute("""Select gpu from server where serverId = tempServerId""")

    tempMemory = input['Memory']
    tempOs = input['Os']
    tempCpuCores = input['CpuCores']
    tempCpu = input['Cpu']
    tempModel = input['Model']
