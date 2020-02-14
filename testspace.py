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

    tempMemory = input['Memory']
    tempOs = input['Os']
    tempGpu = input['Gpu']
    tempCpuCores = input['CpuCores']
    tempCpu = input['Cpu']
    tempModel = input['Model']
    tempRackId = input['Rack']['RackId']
    tempServerId = input['ServerId']
    tempServerName = input['ServerName']
    tempServerTypeId = input['ServerType']['TypeId']
    tempLocationId = input['Rack']['Location']['LocationId']
    isOnMasterList = False
    srvDoesExist = False
    typDoesExist = False
    rackDoesExist = False
    locDoesExist = False
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0

    masterList = c.execute("select Name,num from masterList")
    MLResult = c.fetchall()
    servList = c.execute("select ServerId from Server")
    SLResult = c.fetchall()
    srvTypeList = c.execute("select TypeId from ServerType")
    STResult = c.fetchall()
    rackList = c.execute("select RackId from Rack")
    RResult = c.fetchall()
    locList = c.execute("select LocationId from Location")
    LResult = c.fetchall()
    for item1 in MLResult:
        dingles = MLResult[i]
        testNum = dingles[0]
        testName = dingles[1]
        testPhrase = testName+'-'+testNum
        if testPhrase == tempServerId:
            # print(tempServerId + ' is on the Master List')
            isOnMasterList = True
        i = i+1
    for item2 in SLResult:
        if tempServerId == SLResult[j]:
            srvDoesExist = True
        j = j+1
    for item3 in STResult:
        if tempServerTypeId == STResult[k]:
            typDoesExist = True
        k = k+1
    for item4 in RResult:
        if tempRackId == RResult[l]:
            rackDoesExist = True
        l = l+1
    for item5 in LResult:
        if tempLocationId == LResult[m]:
            locDoesExist = True
        m = m+1
    if not isOnMasterList:
        print(" ")
        print(tempServerId + ' is not on the Master List')

    if not typDoesExist:
        c.execute("""insert into ServerType(TypeId, TypeName) values(?,?)""",
            (input['ServerType']['TypeId'], input['ServerType']['TypeName']))

    if not rackDoesExist:
        c.execute("""insert into Rack(RackId, Name, LocationId) values(?,?,?)""", (input['Rack']['RackId'],
            input['Rack']['Name'], input['Rack']['Location']['LocationId']))

    if not locDoesExist:
        c.execute("""insert into Location(LocationId, BuildingNumber, Room) values (?,?,?)""", (
            input['Rack']['Location']['LocationId'], input['Rack']['Location']['BuildingNumber'],
            input['Rack']['Location']['Room']))

    if isOnMasterList and not srvDoesExist:
        c.execute("""insert into Server(ServerId, ServerName, Gpu, Memory, Os, CpuCores, Cpu, Model, ServerTypeId,
            RackId) values(?,?,?,?,?,?,?,?,?,?)""", (tempServerId, tempServerName, tempGpu, tempMemory, tempOs,
                                                     tempCpuCores, tempCpu, tempModel, input['ServerType']['TypeId'],
                                                     input['Rack']['RackId']))
        srvDoesExist = True

    if isOnMasterList and srvDoesExist:
        c.execute("""update Server set Gpu= ?, Memory= ?, Os=?, CpuCores=?, Cpu= ?, Model= ?, RackId= ? where serverId =
         '%s'""" % tempServerId, (tempGpu, tempMemory, tempOs, tempCpuCores, tempCpu, tempModel, tempRackId))

        c.execute("""insert into Metric(MetricId, Time, Cpu, Gpu, PartA, PartB, PartC, PartD, Disk, Ram, PingLatency,
            ServerId) values(?,?,?,?,?,?,?,?,?,?,?,?)""",
                  [input['Metric']['MetricId'], input['Metric']['Time'], input['Metric']['Cpu'], input['Metric']['Gpu'],
                   input['Metric']['PartA'], input['Metric']['PartB'], input['Metric']['PartC'], input['Metric']['PartD'],
                   input['Metric']['Disk'], input['Metric']['Ram'], input['Metric']['PingLatency'], tempServerId])

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

        c.execute("""delete from RunningJob where serverId='%s'""" % tempServerId)
        for RunningJob in input['RunningJobs']:
            c.execute("""insert into RunningJob(User, JobName, StartTime, CoresAllocated,ReservedTime, serverID)
            values(?,?,?,?,?,?)""", (RunningJob['User'], RunningJob['JobName'], RunningJob['StartTime'],
                                     RunningJob['CoresAllocated'], RunningJob['ReservedTime'], tempServerId))
        shutil.move(filePath + dingle, archPath)

    else:
        print(tempServerId+' was moved to the spam folder!')
        shutil.move(filePath+dingle, spamPath)

conn.commit()
conn.close()
