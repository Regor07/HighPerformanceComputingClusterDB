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
c.execute("""insert into server(serverId,servername, gpu,memory,os,cpucores,cpu,model) values(?,?,?,?,?,?,?,?)""",(tempserverId,tempserverName,tempGpu,tempMemory,tempOs,tempCpuCores,tempCpu,tempModel))
# c.execute("""insert into server (serverId) values (?)""",(tempserverId,),)
# c.execute("""insert into server (servername) values (?) where serverId = tempserverId""",(tempserverName,),)
# c.execute("""insert into server (gpu) values (?)""",(tempGpu,),)
# c.execute("""insert into server (memory) values (?)""",(tempMemory,),)
# c.execute("""insert into server (os) values (?)""",(tempOs,),)
# c.execute("""insert into server (cpucores) values (?)""",(tempCpuCores,),)
# c.execute("""insert into server (cpu) values (?)""",(tempCpu,),)
# c.execute("""insert into server (model) values (?)""",(tempModel,),)
conn.commit()
conn.close()