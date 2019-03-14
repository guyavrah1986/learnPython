import ping3
import os
import time
import datetime

def runNightlyPing():
    print("runNightlyPing - start")
    numOfMinutesBetweenInterals = 1
    sleepIntervalSec = 10 * numOfMinutesBetweenInterals
    numOfHours = 7
    numOfIntervals = (numOfHours * 60 * 60) / sleepIntervalSec
    moxaIpAddress = "172.30.82.24"
    filePath = r"C:\Users\test6\Desktop"
    fileName = "nightlyPingResults.txt"

    print("runNightlyPing - about to perform " + str(numOfIntervals) + " ping commands")
    fileFullName = os.path.join(filePath, fileName)
    print("runNightlyPing - about to create file with name:" + fileFullName)
    file = open(fileFullName, "w")
    file.write("This file list ping that were done towards MOXA (" + moxaIpAddress + ") every " + str(sleepIntervalSec) + "seconds \n")
    file.write("This ping will be done for " + str(numOfIntervals) + " times \n")
    file.write("---------------------------------------------------------------------------\n")

    tmpCounter = 20
    counter = 0
    while counter < tmpCounter:
        ret = runPing(moxaIpAddress)
        counter+= 1
        now = datetime.datetime.now()
        currTime = str(now.day) + "/" + str(now.month) + "-" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        row = currTime + "=" + ret + "\n"
        file.write(row)
        time.sleep(sleepIntervalSec)


    # finally close the file
    counter+= 1
    if counter == numOfIntervals:
        file.write("All ping requests were done !!")
    else:
        file.write("NOTE: Not all ping requestseee done \n")

    file.close()

def runPing(ipAddress):
    ret = ping3.ping(ipAddress, timeout=1)
    if ret == "None":
        return("ping fail")
    else:
        return("ping success")

def main():
    print("main - start")
    runNightlyPing()
    print("main - end")


if __name__ == "__main__":
    main()
