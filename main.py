# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import psutil as psutil
import crontab as CronTab
import subprocess



def main():
    # Use a breakpoint in the code line below to debug your script.
    users = psutil.users()

    userList = []

    for i in (users):
        userList.append(i.name)

    print(userList)

    for i in userList:
        cron = CronTab(user=i)
        job = cron.new(
            command=" env DISPLAY=:0.0 /usr/bin/python3 /home/" + i + "/PycharmProjects/AdJoiner/testonboot.py")
        job.every_reboot()
        cron.write() # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
