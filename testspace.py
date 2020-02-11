import _sqlite3
import json
import os
import shutil

filePath = "C:\\Users\\Roger\\source\\repos\\JsonMockDataCreator\\Jsons\\"
archPath = "C:\\Users\\Roger\\source\\repos\\JsonMockDataCreator\\Archive"
spamPath = "C:\\Users\\Roger\\source\\repos\\JsonMockDataCreator\\Spam"
conn = _sqlite3.connect('servers.db')
c = conn.cursor()
sampleList = os.listdir(filePath)

for item in sampleList:
    dingle = item
    with open(filePath+dingle) as data:
        input = json.load(data)

    tempServerId = input['ServerId']
    isOnMasterList = False
    masterList = c.execute("select Name,num from masterList")
    MLResult = c.fetchall()
    i = 0
    for item in MLResult:
        dingles = MLResult[i]
        testNum = dingles[0]
        testName = dingles[1]
        testPhrase = testName+'-'+testNum
        if testPhrase == tempServerId:
            # print(tempServerId + ' is on the Master List')
            isOnMasterList = True
        i = i+1
    if not isOnMasterList:
        print(" ")
        print(tempServerId + ' is not on the Master List')

    tempMemory = input['Memory']
    tempOs = input['Os']
    tempGpu = input['Gpu']
    tempCpuCores = input['CpuCores']
    tempCpu = input['Cpu']
    tempModel = input['Model']
    tempRackId= input['Rack']['RackId']

    if isOnMasterList:
        c.execute("""update Server set Gpu= ?, Memory= ?, Os=?, CpuCores=?, Cpu= ?, Model= ?, RackId= ? where serverId =
         '%s'""" % tempServerId, (tempGpu, tempMemory, tempOs, tempCpuCores, tempCpu, tempModel, tempRackId))

        c.execute("""insert into Metric(MetricId, Time, Cpu, Gpu, PartA, PartB, PartC, PartD, Disk, Ram, PingLatency,
            ServerId) values(?,?,?,?,?,?,?,?,?,?,?,?)""",
                  [input['Metric']['MetricId'], input['Metric']['Time'], input['Metric']['Cpu'], input['Metric']['Gpu'],
                   input['Metric']['PartA'], input['Metric']['PartB'], input['Metric']['PartC'], input['Metric']['PartD'],
                   input['Metric']['Disk'],input['Metric']['Ram'], input['Metric']['PingLatency'], tempServerId])

        c.execute("""delete from Database where serverId='%s'""" % tempServerId)
        for Database in input['Databases']:
            tempDbId = Database['DatabaseId']
            tempInput = Database['DatabaseName']
            tempStatus = Database['Status']
            c.execute("""insert into Database(DatabaseId, DatabaseName, Status, ServerId) values (?,?,?,?)""",
                      (tempDbId, tempInput, tempStatus, tempServerId))

        c.execute("""delete from Service where serverId='%s'""" % tempServerId)
        for Service in input['Services']:
            tempServiceId = Service['ServiceId']
            tempServiceName = Service['ServiceName']
            tempServiceStatus = Service['Status']
            c.execute("""insert into Service(ServiceId, ServiceName, Status, ServerId) values (?,?,?,?)""",
                      (tempServiceId, tempServiceName, tempServiceStatus, tempServerId))

        c.execute("""delete from RunningJob where serverId='%s'"""% tempServerId)
        for RunningJob in input['RunningJobs']:
            c.execute("""insert into RunningJob(User, JobName, StartTime, CoresAllocated,ReservedTime, serverID) 
            values(?,?,?,?,?,?)""", (RunningJob['User'], RunningJob['JobName'], RunningJob['StartTime'],
                                     RunningJob['CoresAllocated'], RunningJob['ReservedTime'], tempServerId))

        # print(tempServerId+' was moved to the archive folder!')
        shutil.move(filePath+dingle, archPath)
    else:
        print(tempServerId+' was moved to the spam folder!')
        shutil.move(filePath+dingle, spamPath)


conn.commit()
conn.close()