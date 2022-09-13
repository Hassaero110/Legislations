import configparser

config = configparser.ConfigParser()
config.read("config/sql_database.ini")


def read_sql_config(kwarg):
    return config["DATABASE"][kwarg]
