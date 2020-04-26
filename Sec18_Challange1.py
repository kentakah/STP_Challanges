import logging.config
from sqlite_rx import get_default_logger_settings
from sqlite_rx.server import SQLiteServer


def main():

    # database is a path-like object giving the pathname 
    # of the database file to be opened. 

    # You can use ":memory:" to open a database connection to a database 
    # that resides in RAM instead of on disk

    logging.config.dictConfig(get_default_logger_settings(logging.DEBUG))
    server = SQLiteServer(database=":memory:",
                          bind_address="tcp://127.0.0.1:5000")
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


if __name__ == '__main__':
    main()
