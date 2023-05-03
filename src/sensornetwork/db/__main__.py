import mysql.connector
from sys import argv
from sensornetwork import HOST_INFO
from getpass import getpass
from sensornetwork.db import INIT_SCRIPT, DROP_SCRIPT
import datetime
from random import gauss, uniform

def main(script, conn):
    cursor = conn.cursor()
    results = None
    with open(script, 'r') as f:
        results = cursor.execute(f.read(), multi=True)
    for result in results:
        print(result)
    cursor.close()

def fake(conn):
    minutes_per_sample = 30
    samples_per_hour = round(60 / minutes_per_sample)
    samples_per_day = 24*samples_per_hour
    total_samples = 31*samples_per_day
    today = datetime.datetime.now()
    timestamps = [today - datetime.timedelta(minutes=minutes_per_sample*i) for i in range(total_samples)]
    temp_mean = 0.045
    temp_dev = 0.0089
    humid_mean = 0.41
    humid_dev = 0.05
    temps = [gauss(temp_mean, temp_dev) for _ in range(total_samples)]
    humids = [gauss(humid_mean, temp_dev) for _ in range(total_samples)]
    sunrise = 8*60
    sunset = 20*60
    noon = 12 * 60
    t_diff = abs(sunrise-sunset)
    hot = 22
    cold = 20
    lerp = lambda start_value, end_value, t: start_value + (end_value - start_value) * t

    s = ('temperature_recording', 'humidity_recording', 'light_recording')
    st = ""
    s2 = ""
    # break into chunks

    for i_, (temp, humidity, checkpoint) in enumerate(zip(temps, humids, timestamps)):
        i = i_ + 1
        time = (checkpoint.hour*60) + checkpoint.minute
        celsius = temp
        light = None
        t = 0

        #night
        if time < sunrise or time > sunset:
            if time > sunset:
                t = (time - sunset) / t_diff
            else:
                t = (time - sunset + (24*60)) / t_diff
            celsius += lerp(hot, cold, t)
            light = 0
        else:
            light = 1
            t = (time - sunrise) / t_diff
            celsius += lerp(cold, hot, t)
        
        
        v = (celsius, humidity, light)

        for j, (tb, value) in enumerate(zip(s, v)):
            k = (i*3)+j
            q1 = f"INSERT INTO sensornetwork.data_record(record_id, recording, record_time) VALUES ({k}, {value:0.2f}, \"{checkpoint.strftime('%Y-%m-%d %H:%M:%S')}\");"
            st += q1
            q2 = f"INSERT INTO sensornetwork.{tb}(record_id) VALUES ({k});"
            s2 += q2
            if k < 10:
                print(q1,q2)
    with conn.cursor() as cursor:
        with open("hell.txt", "w") as f:
            f.write(st)
        for result in cursor.execute(st, multi=True):
            print(result.statement,'->', result)
        print(s2)
        for result in cursor.execute(s2, multi=True):
            print(result.statement,'->', result)
    conn.commit()

if __name__ == "__main__":
    username = input("dbcreator Username:")
    password = getpass("dbcreator Password:")
    conn = mysql.connector.connect(
        host=HOST_INFO[0],
        user=username,
        password=password,
        autocommit=True
    )
    if len(argv) > 1:
        mode = argv[1].casefold()[0]
        if mode == 'i':
            print("Initializing db...")
            main(INIT_SCRIPT, conn)
        elif mode == 'd':
            print("Dropping db...")
            main(DROP_SCRIPT, conn)
        elif mode == 'f':
            main(DROP_SCRIPT, conn)
            main(INIT_SCRIPT, conn)
            fake(conn)
        else:
            raise RuntimeError(f"Invalid argument {argv[1]}")
    else:
        raise RuntimeError("Did you mean to add 'init' or 'drop'?")
