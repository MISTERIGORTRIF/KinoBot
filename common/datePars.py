from datetime import timedelta, datetime
import pytz


def timer():
    s = str()
    st = str(datetime.now(pytz.timezone('Europe/Moscow')))[:16].split()[0].split("-")
    for l in st: s += l
    return s


def add_day():
    data = []
    rez = ""

    original = str(datetime.now(pytz.timezone('Europe/Moscow')))[:16].split()

    r1 = original[0].split("-")
    r2 = original[1].split(":")

    for l in r1: data.append(l)
    for l in r2: data.append(l)

    data = list(map(int, data))

    addedday = datetime(data[0], data[1], data[2])
    addedday += timedelta(days=1)

    addedday = str(addedday).split()[0].split("-")

    for l in addedday: rez += l

    return rez

