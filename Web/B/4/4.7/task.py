def parse_connection_string(conection_sting):
    """
    Takes an input connection string connection_string and returns a dictionary with its components
    :param conection_sting:
    :return: dialect+driver://username:password@host:port/database
    """
    con_str = {
        "dialect": "",
        "driver": "",
        "username": "",
        "password": "",
        "host": "",
        "port": "",
        "database": ""
    }

    conection_sting = conection_sting.split('://')

    if "sqlite3" in conection_sting[0]:
        """{"dialect": "sqlite3", "driver": "", "username": "", "password": "", "host": "", "port": "", "database": 
        "b4_7.sqlite3"} """
        print("First")
        con_str['dialect'] = conection_sting[0]
        con_str['database'] = conection_sting[1].split('/')[1]
    elif "postgresql" in conection_sting[0]:
        """{"dialect": "postgresql", "driver": "psycopg2", "username": "admin", "password": "1234", 
        "host": "localhost", "port": "", "database": "b4_7"}"""
        print("Second")
        con_str['dialect'] = conection_sting[0].split('+')[0]
        con_str['driver'] = conection_sting[0].split('+')[1]
        con_str['username'] = conection_sting[1].split(':')[0]
        con_str['password'] = conection_sting[1].split(':')[1].split('@')[0]
        con_str['host'] = conection_sting[1].split(':')[1].split('@')[1].split('/')[0]
        con_str['database'] = conection_sting[1].split(':')[1].split('@')[1].split('/')[1]
        print(conection_sting[1].split(':'))
    elif "m2sql" in conection_sting[0]:
        """{"dialect": "m2sql", "driver": "", "username": "admin", "password": "1234", "host": "", "port": "", 
        "database": "b4_7"} """
        con_str["dialect"] = conection_sting[0]
        con_str["username"] = conection_sting[1].split(':')[0]
        con_str["password"] = conection_sting[1].split(':')[1].split('/')[0]
        con_str["database"] = conection_sting[1].split(':')[1].split('/')[1]
    return con_str


print(parse_connection_string("sqlite3:///b4_7.sqlite3"))
print(parse_connection_string("postgresql+psycopg2://admin:1234@localhost/b4_7"))
print(parse_connection_string("m2sql://admin:1234/b4_7"))
print(parse_connection_string("sqlite3:/aspinaspo"))
print(parse_connection_string("postgresql+psycopg2://admin:1234@localhost/b4_7"))
