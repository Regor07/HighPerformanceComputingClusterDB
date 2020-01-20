import _sqlite3
conn = _sqlite3.connect('servers.db')
c = conn.cursor()
c.execute("""CREATE TABLE server(
    serverId text primary key,
    servername text,
    rackID text,
    serverTypeID text,
    os text,
    memory text,
    cpu text,
    cpucores text,
    gpu text,
    model text,
    foreign key (rackID) references rack(rackID),
    foreign key (serverTypeID) references servertype(typeID)
    )""")
c.execute("""CREATE TABLE rack(
    rackID text primary key,
    name text,
    locationID text,
    foreign key(locationID) references location(locationID)
)""")
c.execute("""CREATE TABLE location(
    locationID text primary key,
    buildingNumber text, 
    room text
)""")
c.execute("""CREATE TABLE servertype(
    typeID text primary key,
    typeName text
    )""")
c.execute("""CREATE TABLE metric(
    metricID text primary key,
    Time text, 
    cpu real,
    ram real,
    disk real,
    gpu real, 
    pingLatency real,
    serverId text, 
    foreign key (serverId) references server(serverId)
    )""")
c.execute("""CREATE TABLE service(
    serviceID text primary key,
    serviceName text,
    status text,
    running text,
    serverId text,
    foreign key (serverId) references server(serverId)
    )""")
c.execute("""CREATE TABLE database(
    databaseID text primary key,
    databaseName text,
    status text,
    serverId text,
    foreign key (serverId) references server(serverId)
    )""")
c.execute("""CREATE TABLE runningjob(
    coresAllocated text,
    reservedTime text,
    serverID text,
    user text,
    jobName text, 
    startTime text,
    foreign key (serverID) references server(serverID)
    constraint runningjob_pk primary key(serverID, user, jobName, startTime)
    )""")
conn.commit()
conn.close()