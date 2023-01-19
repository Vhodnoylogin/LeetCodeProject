from datetime import date, datetime


def task1(val_date: date):
    return val_date.isoformat()

def tt(num, list):
    return list[num]

def read_from_keyboard():
    while True:
        try:
            val_date = input()
            return datetime.strptime(val_date, '%Y%m%d')
        except ValueError:
            print("Wrong date format. Please, input date as YYYYMMDD")


if __name__ == '__main__':
    d = read_from_keyboard()
    res = task1(d)
    print(res)
