from datetime import datetime


def main():
    timestamp = 18976442004
    dt_object = datetime.fromtimestamp(timestamp)
    print("dt_object =", dt_object)
    print("type(dt_object) =", type(dt_object))


if __name__ == '__main__':
    main()
