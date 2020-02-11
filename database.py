import _sqlite3
import json
import os
# samplelist = os.listdir('C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons')
# for item in samplelist:
#     print(item)
conn = _sqlite3.connect('servers.db')
c = conn.cursor()
# if c ('servers.db') is not null
# c.execute("""CREATE TABLE Server(
#     ServerId text primary key,
#     ServerName text,
#     RackID text,
#     ServerTypeID text,
#     Os text,
#     Memory text,
#     Cpu text,
#     CpuCores text,
#     Gpu text,
#     Model text,
#     foreign key (RackId) references Rack(RackId),
#     foreign key (ServerTypeId) references ServerType(TypeId)
#     )""")
# c.execute("""CREATE TABLE Rack(
#     RackId text primary key,
#     Name text,
#     LocationId text,
#     foreign key(LocationId) references Location(LocationId)
#     )""")
# c.execute("""CREATE TABLE Location(
#     LocationId text primary key,
#     BuildingNumber text,
#     Room text
#     )""")
# c.execute("""CREATE TABLE ServerType(
#     TypeId text primary key,
#     TypeName text
#     )""")
# c.execute("""CREATE TABLE Metric(
#     MetricId text primary key,
#     Time text,
#     Cpu real,
#     Ram real,
#     PartA real,
#     PartB real,
#     PartC real,
#     PartD real,
#     Disk real,
#     Gpu real,
#     PingLatency real,
#     ServerId text,
#     foreign key (ServerId) references Server(ServerId)
#     )""")
# c.execute("""CREATE TABLE Service(
#     ServiceId text primary key,
#     ServiceName text,
#     Status text,
#     ServerId text,
#     foreign key (ServerId) references Server(ServerId)
#     )""")
# c.execute("""CREATE TABLE Database(
#     DatabaseId text primary key,
#     DatabaseName text,
#     Status text,
#     ServerId text,
#     foreign key (ServerId) references Server(ServerId)
#     )""")
# c.execute("""CREATE TABLE RunningJob(
#     CoresAllocated text,
#     ReservedTime text,
#     ServerId text,
#     User text,
#     JobName text,
#     StartTime text,
#     foreign key (ServerId) references Server(ServerId)
#     constraint RunningJob_pk primary key(ServerId, User, JobName, StartTime)
#     )""")
# c.execute("""CREATE TABLE MasterList(
#      Type text,
#      Name text,
#      num text,
#      constraint MasterList_pk primary key(Type, Name)
#      )""")

samplelist = os.listdir('C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons')
for item in samplelist:
    dingle=item
    with open("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\"+dingle) as data:
        input = json.load(data)

    tempServerId = input['ServerId']
    tempServerName = input['ServerName']
    tempGpu = input['Gpu']
    tempMemory = input['Memory']
    tempOs = input['Os']
    tempCpuCores = input['CpuCores']
    tempCpu = input['Cpu']
    tempModel = input['Model']
    c.execute("""insert into Server(ServerId, ServerName, Gpu, Memory, Os, CpuCores, Cpu, Model, ServerTypeId,
    RackId) values(?,?,?,?,?,?,?,?,?,?)""", (tempServerId, tempServerName, tempGpu, tempMemory, tempOs,
                                             tempCpuCores,
                                             tempCpu, tempModel, input['ServerType']['TypeId'],
                                             input['Rack']['RackId']))
    c.execute("""insert into Rack(RackId, Name, LocationId) values(?,?,?)""", (input['Rack']['RackId'],
                                                                               input['Rack']['Name'],
                                                                               input['Rack']['Location']['LocationId']))
    c.execute("""insert into Location(LocationId, BuildingNumber, Room) values (?,?,?)""", (
        input['Rack']['Location']['LocationId'], input['Rack']['Location']['BuildingNumber'],
        input['Rack']['Location']['Room']))
    c.execute("""insert into Metric(MetricId, Time, Cpu, Gpu, PartA, PartB, PartC, PartD, Disk, Ram, PingLatency,
    ServerId) values(?,?,?,?,?,?,?,?,?,?,?,?)""", (input['Metric']['MetricId'], input['Metric']['Time'],
                                                   input['Metric']['Cpu'], input['Metric']['Gpu'],
                                                   input['Metric']['PartA'],
                                                   input['Metric']['PartB'], input['Metric']['PartC'],
                                                   input['Metric']['PartD'], input['Metric']['Disk'],
                                                   input['Metric']['Ram'],
                                                   input['Metric']['PingLatency'], tempServerId))
    c.execute("""insert into ServerType(TypeName, TypeId) values(?,?)""",
              (input['ServerType']['TypeName'], input['ServerType']['TypeId']))
    for RunningJob in input['RunningJobs']:
        c.execute(
            """insert into RunningJob(User, JobName, StartTime, CoresAllocated,ReservedTime, serverID) values(?,?,?,?,?,?)""",
            (RunningJob['User'], RunningJob['JobName'],
            RunningJob['StartTime'], RunningJob['CoresAllocated'],
            RunningJob['ReservedTime'], tempServerId))
    for Database in input['Databases']:
        tempDbId = Database['DatabaseId']
        tempInput = Database['DatabaseName']
        tempStatus = Database['Status']
        c.execute("""insert into Database(DatabaseId, DatabaseName, Status, ServerId) values (?,?,?,?)""",
                  (tempDbId, tempInput, tempStatus, tempServerId))
    for Service in input['Services']:
        tempServiceId = Service['ServiceId']
        tempServiceName = Service['ServiceName']
        tempServiceStatus = Service['Status']
        c.execute("""insert into Service(ServiceId, ServiceName, Status, ServerId) values (?,?,?,?)""",
                  (tempServiceId, tempServiceName, tempServiceStatus, tempServerId))

# with open("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\Db-01.json") as data:
#     input = json.load(data)
#
# tempServerId = input['ServerId']
# tempServerName = input['ServerName']
# tempGpu = input['Gpu']
# tempMemory = input['Memory']
# tempOs = input['Os']
# tempCpuCores = input['CpuCores']
# tempCpu = input['Cpu']
# tempModel = input['Model']
# c.execute("""insert into Server(ServerId, ServerName, Gpu, Memory, Os, CpuCores, Cpu, Model, ServerTypeId,
# RackId) values(?,?,?,?,?,?,?,?,?,?)""", (tempServerId, tempServerName, tempGpu, tempMemory, tempOs,
#                                          tempCpuCores,
#                                          tempCpu, tempModel, input['ServerType']['TypeId'],
#                                          input['Rack']['RackId']))
# c.execute("""insert into Rack(RackId, Name, LocationId) values(?,?,?)""", (input['Rack']['RackId'],
#                                                                            input['Rack']['Name'],
#                                                                            input['Rack']['Location']['LocationId']))
# c.execute("""insert into Location(LocationId, BuildingNumber, Room) values (?,?,?)""", (
#     input['Rack']['Location']['LocationId'], input['Rack']['Location']['BuildingNumber'],
#     input['Rack']['Location']['Room']))
# c.execute("""insert into Metric(MetricId, Time, Cpu, Gpu, PartA, PartB, PartC, PartD, Disk, Ram, PingLatency,
# ServerId) values(?,?,?,?,?,?,?,?,?,?,?,?)""", (input['Metric']['MetricId'], input['Metric']['Time'],
#                                                input['Metric']['Cpu'], input['Metric']['Gpu'], input['Metric']['PartA'],
#                                                input['Metric']['PartB'], input['Metric']['PartC'],
#                                                input['Metric']['PartD'], input['Metric']['Disk'],input['Metric']['Ram'],
#                                                input['Metric']['PingLatency'], tempServerId))
# c.execute("""insert into ServerType(TypeName, TypeId) values(?,?)""",
#           (input['ServerType']['TypeName'], input['ServerType']['TypeId']))
# for RunningJob in input['RunningJobs']:
#     c.execute(
#         """insert into RunningJob(User, JobName, StartTime, CoresAllocatedReservedTime, serverID) values(?,?,?,?,?,?)""",
#         (RunningJob['RunningJobs']['User']), RunningJob['RunningJobs']['JobName'],
#         RunningJob['RunningJobs']['StartTime'], RunningJob['RunningJobs']['CoresAllocated'],
#         RunningJob['RunningJobs']['ReservedTime'], tempServerId)
# for Database in input['Databases']:
#     tempDbId = Database['DatabaseId']
#     tempInput = Database['DatabaseName']
#     tempStatus = Database['Status']
#     c.execute("""insert into Database(DatabaseId, DatabaseName, Status, ServerId) values (?,?,?,?)""",
#               (tempDbId, tempInput, tempStatus, tempServerId))
# for Service in input['Services']:
#     tempServiceId = Service['ServiceId']
#     tempServiceName = Service['ServiceName']
#     tempServiceStatus = Service['Status']
#     c.execute("""insert into Service(ServiceId, ServiceName, Status, ServerId) values (?,?,?,?)""",
#               (tempServiceId, tempServiceName, tempServiceStatus, tempServerId))
#
conn.commit()
conn.close()
