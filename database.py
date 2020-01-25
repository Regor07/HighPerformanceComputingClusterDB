import _sqlite3
import json
conn = _sqlite3.connect('servers.db')
c = conn.cursor()
# c.execute("""CREATE TABLE server(
#     serverId text primary key,
#     servername text,
#     rackID text,
#     serverTypeID text,
#     os text,
#     memory text,
#     cpu text,
#     cpucores text,
#     gpu text,
#     model text,
#     foreign key (rackID) references rack(rackID),
#     foreign key (serverTypeID) references servertype(typeID)
#     )""")
# c.execute("""CREATE TABLE rack(
#     rackID text primary key,
#     name text,
#     locationID text,
#     foreign key(locationID) references location(locationID)
# )""")
# c.execute("""CREATE TABLE location(
#     locationID text primary key,
#     buildingNumber text,
#     room text
# )""")
# c.execute("""CREATE TABLE servertype(
#     typeID text primary key,
#     typeName text
#     )""")
# c.execute("""CREATE TABLE metric(
#     metricID text primary key,
#     Time text,
#     cpu real,
#     ram real,
#     disk real,
#     gpu real,
#     pingLatency real,
#     serverId text,
#     foreign key (serverId) references server(serverId)
#     )""")
# c.execute("""CREATE TABLE service(
#     serviceID text primary key,
#     serviceName text,
#     status text,
#     running text,
#     serverId text,
#     foreign key (serverId) references server(serverId)
#     )""")
# c.execute("""CREATE TABLE database(
#     databaseID text primary key,
#     databaseName text,
#     status text,
#     serverId text,
#     foreign key (serverId) references server(serverId)
#     )""")
# c.execute("""CREATE TABLE runningjob(
#     coresAllocated text,
#     reservedTime text,
#     serverID text,
#     user text,
#     jobName text,
#     startTime text,
#     foreign key (serverID) references server(serverID)
#     constraint runningjob_pk primary key(serverID, user, jobName, startTime)
#     )""")
with open("C:\\Users\\hicks\\source\\repos\\JsonMockDataCreator\\Jsons\\Db-01.json") as data:
    input=json.load(data)

tempserverId= input['ServerId']
tempserverName= input['ServerName']
tempGpu= input['Gpu']
tempMemory= input['Memory']
tempOs= input['Os']
tempCpuCores= input['CpuCores']
tempCpu= input['Cpu']
tempModel= input['Model']
c.execute("""insert into server(serverId,servername, gpu,memory,os,cpucores,cpu,model,serverTypeID,rackID) values(?,?,?,?,?,?,?,?,?,?)""",(tempserverId,tempserverName,tempGpu,tempMemory,tempOs,tempCpuCores,tempCpu,tempModel,input['ServerType']['TypeID'],input['Rack']['RackID']))
c.execute("""insert into rack(rackID,name,locationID) values(?,?,?)""",(input['Rack']['RackID'],input['Rack']['Name'],input['Rack']['Location']['LocationID']))
c.execute("""insert into location(locationID,buildingNumber,room) values (?,?,?)""", (input['Rack']['Location']['LocationID'],input['Rack']['Location']['BuildingNumber'],input['Rack']['Location']['Room']))
c.execute("""insert into metric(metricID,Time,cpu,gpu,disk,ram,pingLatency,serverId) values(?,?,?,?,?,?,?,?)""",(input['Metric']['MetricId'],input['Metric']['Time'],input['Metric']['Cpu'],input['Metric']['Gpu'],input['Metric']['Disk'],input['Metric']['Ram'],input['Metric']['PingLatency'],tempserverId))
c.execute("""insert into servertype(typeName,typeID) values(?,?)""",(input['ServerType']['TypeName'],input['ServerType']['TypeID']))

for runningjob in input['RunningJobs']:
    c.execute("""insert into runningjob(user,jobName,startTime,coresAllocatedreservedTime,serverID) values(?,?,?,?,?,?)""",(runningjob['RunningJobs']['User']),runningjob['RunningJobs']['JobName'],runningjob['RunningJobs']['StartTime'],runningjob['RunningJobs']['CoresAllocated'],runningjob['RunningJobs']['ReservedTime'],tempserverId)
for database in input['Databases']:
    tempddbId= database['DatabaseId']
    tempInput=database['DatabaseName']
    tempStatus=database['Status']
    c.execute("""insert into database(databaseID, databaseName,status,serverId) values (?,?,?,?)""",(tempddbId,tempInput,tempStatus,tempserverId))
for service in input['Services']:
    tempserviceID= service['ServiceID']
    tempServiceName= service['ServiceName']
    tempserviceStatus= service['Status']
    c.execute("""insert into service(serviceID, serviceName,status,serverId) values (?,?,?,?)""", (tempserviceID,tempServiceName,tempserviceStatus,tempserverId))

conn.commit()
conn.close()