import _sqlite3
import json
import os

serverPath = "C:\\Users\\Roger\\PycharmProjects\\HighPerformanceComputingClusterDB\\"
filePath = "C:\\Users\\Roger\\source\\repos\\JsonMockDataCreator\\Jsons\\"
archPath = "C:\\Users\\Roger\\source\\repos\\JsonMockDataCreator\\Archive"
spamPath = "C:\\Users\\Roger\\source\\repos\\JsonMockDataCreator\\Spam"

conn = _sqlite3.connect('FinalDatabase1Month.db')
c = conn.cursor()
# if not os.path.isfile(serverPath + 'servers.db'):
c.execute("""CREATE TABLE Server(
    ServerId text primary key,
    ServerName text,
    RackId text,
    ServerTypeId text,
    Os text,
    Memory text,
    Cpu text,
    CpuCores text,
    Gpu text,
    Model text,
    foreign key (RackId) references Rack(RackId),
    foreign key (ServerTypeId) references ServerType(TypeId)
    )""")
c.execute("""CREATE TABLE Rack(
    RackId text primary key,
    Name text,
    LocationId text,
    foreign key(LocationId) references Location(LocationId)
    )""")
c.execute("""CREATE TABLE Location(
    LocationId text primary key,
    BuildingNumber text,
    Room text
    )""")
c.execute("""CREATE TABLE ServerType(
    TypeId text primary key,
    TypeName text
    )""")
c.execute("""CREATE TABLE Metric(
    MetricId text primary key,
    Time text,
    Cpu real,
    Ram real,
    Disk real,
    Gpu real,
    PingLatency real,
    ServerId text,
    foreign key (ServerId) references Server(ServerId)
    )""")
c.execute("""CREATE TABLE Partition(
    PartitionId text,
    Capacity text,
    Usage text,
    ServerId text,
    Time text,
    foreign key (ServerId) references Server(ServerId)
    foreign key (Time) references Metric(Time)
    constraint Partition_pk primary key(ServerId, PartitionId, Time)
    )""")
c.execute("""CREATE TABLE Service(
    ServiceId text,
    ServiceName text,
    Status text,
    ServerId text,
    foreign key (ServerId) references Server(ServerId)
    constraint Service_pk primary key(ServerId, ServiceId)
    )""")
c.execute("""CREATE TABLE Database(
    DatabaseId text,
    DatabaseName text,
    Status text,
    ServerId text,
    foreign key (ServerId) references Server(ServerId)
    constraint Database_pk primary key(ServerId, DatabaseId)
    )""")
c.execute("""CREATE TABLE RunningJob(
    CoresAllocated text,
    ReservedTime text,
    ServerId text,
    User text,
    JobName text,
    StartTime text,
    foreign key (ServerId) references Server(ServerId)
    constraint RunningJob_pk primary key(ServerId, User, JobName, StartTime)
    )""")
c.execute("""CREATE TABLE MasterList(
     Type text,
     Name text,
     Num text,
     constraint MasterList_pk primary key(Type, Name)
     )""")

conn.commit()
conn.close()
