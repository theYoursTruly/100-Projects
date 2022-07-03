""" 
    Alarm clock
    Setup alarm for specific time. Count down to that time and emit beep.
    INPUT (on STDIN):
    1) time - in format HH:MM for when to run alarm [TEXT]
    OUTPUT:
    Text with countdown and beep on STDOUT
"""
from time import sleep
from datetime import datetime


def clrscr():
    print('\033[2J\033[H', end='')

def check_input(time_raw):
    if len(time_raw) != 2:
        return 'Invalid input. Expected time in format: HH:MM'
    try:
        alarm_parts = [int(a) for a in time_raw]
        if alarm_parts[0] < 0 or alarm_parts[0] > 23:
            return 'Hour part should be between 00 and 23'
        if alarm_parts[1] < 0 or alarm_parts[1] > 59:
            return 'Minute part should be between 00 and 59'
    except:
        return 'Invalid input'
    return ''

def run_alarm():
    for i in range(10):
        clrscr()
        print('    Alarm' if i%2 else ">>> Alarm <<<", '\a')
        sleep(0.5)
        clrscr()

def set_alarm(hour, minute, now_seconds):
    sleep_time = (hour * 3600 + minute * 60) - now_seconds
    if sleep_time <= 0:
        print('Cannot set alarm in the past')
        return
    for i in range(sleep_time-1, 0, -1):
        clrscr()
        print('Alarm set for {:02}:{:02}\n'.format(hour, minute), str(i) + 'sec left')
        sleep(1)
    run_alarm()
# ----------------------

if __name__ == "__main__":
    now = datetime.now()
    now_sec = now.hour * 3600 + now.minute * 60 + now.second
    user_input = input('It\'s ' + now.strftime("%H:%M") + '. What time you want to set alarm for? [HH:MM]: ')
    alarm_parts = user_input.split(':')

    error_msg = check_input(alarm_parts)
    if error_msg != '':
        print(error_msg)
    else:
        set_alarm(int(alarm_parts[0]), int(alarm_parts[1]), now_sec)
