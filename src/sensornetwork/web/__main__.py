import sensornetwork.web as web
from bottle import run
from sensornetwork import HOST_INFO

def main():
    run(host=HOST_INFO[0], port=web.PORT)

if __name__ == "__main__":
    main()
