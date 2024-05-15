from time import sleep
from datetime import datetime


def log(information='Everything Ok…', time=datetime.now()):
    print(information, time)


log('Some problem...', '16:59:49')
log()
sleep(2)
log('Another Problem…')
sleep(3)
log()
