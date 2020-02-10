import _sqlite3
import json
import os
import shutil
# def filter(string):
samplelist = os.listdir('C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons')
conn = _sqlite3.connect('servers.db')
c = conn.cursor()
samplelist = os.listdir('C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons')
for item in samplelist:
    dingle=item
    with open("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\"+dingle) as data:
        input = json.load(data)

    tempServerId = input['ServerId']
    isOnMasterList = False
    masterList=c.execute("select Name,num from masterList")
    MLResult=c.fetchall()
    i=0
    for item in MLResult:
        dingles=MLResult[i]
        testNum=dingles[0]
        testName=dingles[1]
        testPhrase=testName+'-'+testNum
        if (testPhrase==tempServerId):
            print(tempServerId +' is on the masterlist')
            isOnMasterList=True
        #print(testPhrase)
        i=i+1
        #print(dingles)
    if isOnMasterList==False:
        print(tempServerId +' is not on the masterlist')
    print(" ")


   # print(tempServerId)
    tempServerName = input['ServerName']
    tempGpu = input['Gpu']
    # testy = c.execute("""Select RackId from Rack where RackId = '%s'"""% input['Rack']['RackId'])
    # result =c.fetchone()
    # test= str(result[0])
    # print (test)
    # c.execute("""delete from  Rack where RackId= '%s'"""%test)
    #testgpu= c.execute("""Select serverId from (?) where serverId = ?""" ,tempServerId)

    tempMemory = input['Memory']
    tempOs = input['Os']
    tempCpuCores = input['CpuCores']
    tempCpu = input['Cpu']
    tempModel = input['Model']
    tempRackId= input['Rack']['RackId']
    c.execute("""update Server
    set
    Gpu= ?,
    Memory= ?,
    Os=?,
    CpuCores=?,
    Cpu= ?,
    Model= ?,
    RackId= ?
    where serverId = '%s'""" %tempServerId,(tempGpu,tempMemory,tempOs,tempCpuCores,tempCpu,tempModel,tempRackId)
    )
    # c.execute("""update Server
    # set
    # Gpu='test'
    # where Gpu='Nvidia 1'""")
    if isOnMasterList==True:
        print(tempServerId+' was moved to the archive folder!')
        shutil.move("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\"+dingle,"C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Archive")
    else:
        print(tempServerId+' was moved to the spam folder!')
        shutil.move("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\"+dingle,"C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Spam")


conn.commit()
conn.close()