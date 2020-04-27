from math import sqrt


def is_covered(room, sensors):
    w = room[0]
    h = room[1]
    sw = sensors[0][0]
    hw = sensors[0][1]
    r = sensors[0][2]
    d = int(sqrt((w - (w - sw))**2 + (h - (h - hw))**2))

    if sw >= w/2 and hw >= h/2 and r >= d:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))
