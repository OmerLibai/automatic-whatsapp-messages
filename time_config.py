import time
import datetime

# Constants
SECONDS_IN_MINUTE = MINUTES_IN_HOUR = 60


def get_time(str_time):
    """
    Gets a string containing a time and returns a list containing all the different parts.
    The string is split with by the ':' delimiter.
    :param str_time: The string which represents the time.
    :return: A list containing the different parts of the string (hours, minutes, seconds etc.).
    """
    return str_time.split(':')


def wait_time(time_to_sleep):
    """
    Waits the entered time.
    :param time_to_sleep: The time to wait. Can be either a string (where : is the delimiter) or a list.
    Must enter both hours and minutes even if they're 0. optional: enter seconds too. 
    """
    if type(time_to_sleep) != type([]):
        time_to_sleep = time_to_sleep.split(':')  # convert to list
    time.sleep(int(time_to_sleep[0]) * SECONDS_IN_MINUTE * MINUTES_IN_HOUR + int(time_to_sleep[1]) * SECONDS_IN_MINUTE)
    if len(time_to_sleep) >= 3:  # has the user entered seconds?
        time.sleep(int(time_to_sleep[2]))


def wait_until(target_time):
    """
    Waits until a given hour/minute.
    :param target_time: A list containing both the hour and minute or a string containing both.
    """
    if not is_time_passed(target_time):
        print "started waiting, target time is: ", target_time
        if type(target_time) != type([]):
            target_time = target_time.split(':')
        seconds = datetime.datetime.now().second
        if seconds != 0:
            time.sleep(60-seconds)
        minute = datetime.datetime.now().minute
        if minute != int(target_time[1]):
            if int(target_time[1]) > minute:
                time.sleep(((int(target_time[1]))-minute) * SECONDS_IN_MINUTE)
            else:
                time.sleep((60-minute + int(target_time[1])) * SECONDS_IN_MINUTE)
        hours = (int(target_time[0]) - datetime.datetime.now().hour) * SECONDS_IN_MINUTE * MINUTES_IN_HOUR
        time.sleep(hours)
        print "finished waiting at this time: ", datetime.datetime.now()
    else:
        print 'time has already passed today!'


def is_time_passed(target_time):
    """
    Checks if the target time has passed today.
    :param target_time: A list which contains the hour and minute or a string with the hour and minute.
    If it's a string, the different parts are seperated by the ':' delimiter.
    :return: Has the target time passed today. 
    """
    if type(target_time) != type([]):
        target_time = target_time.split(':')
    return ((int(target_time[0]) == datetime.datetime.now().hour
             and int(target_time[1]) < datetime.datetime.now().minute)
            or (int(target_time[0]) < datetime.datetime.now().hour))
