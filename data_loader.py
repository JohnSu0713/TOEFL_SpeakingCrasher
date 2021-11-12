import time
path = 'Question.txt'


def load_data():
    data = []
    topic = ""
    f = open(path, 'r')
    for line in f.readlines():
        if not line[0].isdigit():
            topic += ("" + line.strip())
        else:
            if topic:
                data.append(topic)
            topic = line.strip()
    data.append(topic)
    return data
    f.close()


# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    # print('Fire in the hole!!')
