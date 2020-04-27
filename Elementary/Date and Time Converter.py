months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July',
          8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def date_time(time: str) -> str:
    dan = int(time[0:2])
    mesec = int(time[3:5])
    mesec = months[mesec]
    godina = int(time[6:10])

    if time[11:13] == 00:
        sat = 0
    else:
        sat = int(time[11:13])

    if time[14:16] == 00:
        minut = 0
    else:
        minut = int(time[14:16])

    if minut == 1:
        return ('{} {} {} year {} hour {} minute'.format(
            dan, mesec, godina, sat, minut))

    else:
        return ('{} {} {} year {} hours {} minutes'.format(
            dan, mesec, godina, sat, minut))


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))
