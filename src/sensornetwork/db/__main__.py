import mysql.connector
from sys import argv
from sensornetwork import HOST_INFO
from getpass import getpass
from sensornetwork.db import INIT_SCRIPT, DROP_SCRIPT


def main(script):
    username = input("Root Username:")
    password = getpass("Root Password:")
    conn = mysql.connector.connect(
        host=HOST_INFO[0],
        user=username,
        password=password,
        autocommit=True
    )
    cursor = conn.cursor()
    results = None
    with open(script, 'r') as f:
        results = cursor.execute(f.read(), multi=True)
    for result in results:
        print(result)
    cursor.close()


if __name__ == "__main__":
    if len(argv) > 1:
        mode = argv[1].casefold()[0]
        if mode == 'i':
            print("Initializing db...")
            main(INIT_SCRIPT)
        elif mode == 'd':
            print("Dropping db...")
            main(DROP_SCRIPT)
        else:
            raise RuntimeError(f"Invalid argument {argv[1]}")
    else:
        raise RuntimeError("Did you mean to add 'init' or 'drop'?")
