def parse_connection_string(connection_string):
    dialect_list = {
        "dialect": "",
        "driver": "",
        "username": "",
        "password": "",
        "host": "",
        "port": "",
        "database": ""
    }
    print(connection_string)
    if connection_string.split(':')[0].find("sqlite") != -1:
        dialect_list['dialect'] = connection_string.split(':')[0]
        dialect_list['database'] = connection_string.split('///')[1]
    elif connection_string.split(':')[0].find('postgresql') != -1:
        dialect_list['dialect'] = 'postgresql' # always!!!
        if connection_string.split(':')[0].split('+') != -1:
            dialect_list['driver'] = connection_string.split(':')[0].split('+')[1]
        # login and password
        dialect_list['username'] = connection_string.split('://')[1].split('@')[0].split(':')[0]
        dialect_list['password'] = connection_string.split('://')[1].split('@')[0].split(':')[1]
        # check if port is True
        if connection_string.split('://')[1].split('@')[1].split('/')[0].find(':') != -1:
            dialect_list["host"] = connection_string.split('://')[1].split('@')[1].split('/')[0].split(':')[0]
            dialect_list['port'] = connection_string.split('://')[1].split('@')[1].split('/')[0].split(':')[1]
            print('check HERE if ', connection_string.split('://')[1].split('@')[1].split('/')[0])
        else:
            # here only for host, without port, so
            dialect_list["host"] = connection_string.split('://')[1].split('@')[1].split('/')[0]
        # and in the end we write our database
        dialect_list['database'] = connection_string.split('://')[1].split('@')[1].split('/')[1]
    else:
        dialect_list["dialect"] = connection_string.split("://")[0]
        dialect_list["username"] = connection_string.split("://")[1].split('/')[0].split(':')[0]
        dialect_list["password"] = connection_string.split("://")[1].split('/')[0].split(':')[1]
        dialect_list["database"] = connection_string.split("://")[1].split('/')[1]
    return dialect_list


print(parse_connection_string("sqlite3:///b4_7.sqlite3"))
print(parse_connection_string("postgresql+psycopg2://admin:1234@localhost/b4_7"))
print(parse_connection_string("m2sql://admin:1234/b4_7"))
