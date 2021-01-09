##Author: Luke Gitchel
##Purpose: Open URL with multiple browsers and monitor the resources each of them consume
##Date: 11/22/2019
import os
import re
import webbrowser
# import thread
import psutil
from datetime import datetime
import time
import pandas
import keyboard
import threading
import tkinter as tk
import sys
import traceback
# from goto import with_goto

from tkinter import *

## Browser Path Locations
class GlobalVariables:
    def __init__(self):
        pass
    ## Windows Browsers
    msEdgeChromiumPath = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
    # msEdgeChromiumBetaPath = 'C:\\Program Files (x86)\\Microsoft\\Edge Beta\\Application\\msedge.exe'
    msEdgePath = 'C:\\Windows\\SystemApps\\Micros~1\\MicrosoftEdge.exe'
    internetExplorerPath = 'C:\\Program Files\\Internet Explorer\\iexplore.exe'

    windowsGoogleChromePath = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    windowsFirefoxPath = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'

    ## Linux Browsers
    linux2GoogleChromePath = '/bin/google-chrome'
    linux2FirefoxPath = '/usr/bin/firefox'

    # browserPaths = [msEdgeChromiumStablePath, msEdgeChromiumBetaPath, googleChromePath, firefoxPath]
    # browserPaths = [firefoxPath, msEdgeChromiumPath, googleChromePath]
    browserOptions = ['firefox', 'msedge', 'googlechrome']
    browserSelection = ''
    # browserchoice = ''
    # processes = []
    INSTALLEDMEMORY = 32000000000.0
    Open_Gui = False
    browsers = ['firefox.exe', 'msedge.exe', 'chrome.exe']
    stop = False
    userInput = ''
    startTime = time.time()
    runTime = 0
    userInputSplit = ''
    inputURL = ''

    osTypes = ['win32', 'linux2']
    currentOS = str(sys.platform)
    # if currentOS == osTypes[0]:
    #     osVar = Win32Variables.
    #
    # elif currentOS == osTypes[1]:
    #     osVar = "linux2Variables"



class Process:
    def __init__(self):
        pass

    processes = []
    pID = 0
    nice = 0
    pName = ''
    createTime = time.time()
    cores = 0
    cpuUsage = 0
    memoryUsage = 0
    readBytes = 0
    writeBytes = 0

    # processes.append({
    #     'pid': pID, 'priority/nice': nice, 'name': pName, 'create_time': createTime,
    #     'cores': cores, 'cpuUsage': cpuUsage, 'memoryUsage': memoryUsage,
    #     'readBytes': readBytes, 'writeBytes': writeBytes,
    # })

class Averages:
    def __init__(self):
        pass
    FireFoxCPUUsage = 0.0
    FireFoxMemoryUsage = 0.0

    GoogleChromeCPUUsage = 0.0
    GoogleChromeMemoryUsage = 0.0

    MsEdgeCPUUsage = 0.0
    MsEdgeMemoryUsage = 0.0

class FireFoxUsage:
    def __init__(self):
        pass

    firefoxCPUUsage = 0.0
    firefoxTotalCPUUsage = 0.0
    firefoxMemoryUsage = 0.0
    firefoxTotalMemoryUsage = 0.0

    firefoxAverageCPUUsage = 0.0
    firefoxAverageMemoryUsage = 0.0
    firefoxCounter = 0
    fCount = 0

# class MsEdgeBetaUsage:
#     def __init__(self):
#         pass
#
#     msEdgeBetaCPUUsage = 0.0
#     msEdgeBetaMemoryUsage = 0.0
#
#     msEdgeBetaAverageCPUUsage = 0.0
#     msEdgeBetaAverageMemoryUsage = 0.0
#     msEdgeBetaCounter = 0
#     msBetaCount = 0

class MsEdgeUsage:
    def __init__(self):
        pass

    msEdgeCPUUsage = 0.0
    msEdgeTotalCPUUsage = 0.0
    msEdgeMemoryUsage = 0.0
    msEdgeTotalMemoryUsage = 0.0

    msEdgeAverageCPUUsage = 0.0
    msEdgeAverageMemoryUsage = 0.0
    msEdgeCounter = 0
    msCount = 0

class ChromeUsage:
    def __init__(self):
        pass

    chromeCPUUsage = 0.0
    chromeTotalCPUUsage = 0.0
    chromeMemoryUsage = 0.0
    chromeTotalMemoryUsage = 0.0

    chromeAverageCPUUsage = 0.0
    chromeAverageMemoryUsage = 0.0
    chromeCounter = 0
    gCount = 0

def GetProcessInfo():
    Process.processes = []
    # Clear Processes info
    # processes = []
    # Get all process info
    for infoProcess in psutil.process_iter():
        with infoProcess.oneshot():
            # Get process id
            Process.pID = infoProcess.pid
            # Get name
            Process.pName = infoProcess.name()
            # Get time created
            Process.createTime = datetime.fromtimestamp(infoProcess.create_time())
            try:
                # Get number of CPU cores
                Process.cores = len(infoProcess.cpu_affinity())
                Process.cpuUsage = infoProcess.cpu_percent()
                status = infoProcess.status()
            except psutil.AccessDenied:
                Process.cores = 0
                # Get CPU usage percentage
                Process.cpuUsage = infoProcess.cpu_percent()
                # Get status of process (running, idle, etc.)
                status = infoProcess.status()
                # print('cpu access denied')
            try:
                # Get the process priority (lower equals higher priority)
                Process.nice = int(infoProcess.nice())
            except psutil.AccessDenied:
                Process.nice = 0
                # print('nice access denied')
            try:
                # Get memory usage
                Process.memoryUsage = infoProcess.memory_percent()
            except psutil.AccessDenied:
                Process.memoryUsage = 0
                # print('memory access denied')
            ioCounters = infoProcess.io_counters()
            Process.readBytes = ioCounters.read_bytes
            Process.writeBytes = ioCounters.write_bytes

            firstTimeSplit = str(Process.createTime).split(' ')
            secondTimeSplit = firstTimeSplit[1].split(':')
            num = 0
            # timeElapsed = 0
            currentTime = time.ctime()
            currentTimeSplit = currentTime.split(' ')
            for timeSection in currentTimeSplit:
                # print ("timeSection" + str(timeSection))
                if timeSection.__contains__(":"):
                    timeSplit = timeSection
                # if timeValue:
                #     timeSplit = timeSection
                # if timeSection == timeREGEX:

            # print ("timeValue" + str(timeValue))
            # print ("timeSplit" + str(timeSplit))

            currentTimeSplitShort = timeSplit.split(':')
            ## FOR TROUBLESHOOTING PURPOSES
            # if pName == browsers[0]:
            # while num < 1:
            #     print('current time:                ' + str(currentTime))
            #     print('current time split           ' + str(currentTimeSplit))
            #     print('current time split[4]        ' + str(currentTimeSplit[3]))
            #     print('first time split             ' + str(firstTimeSplit))
            #     print('second time split            ' + str(secondTimeSplit))
            #     print('first time split [1]         ' + str(firstTimeSplit[1]))
            #     print('second time split [1]        ' + str(secondTimeSplit[1]))
            #     print('current time split short     ' + str(currentTimeSplitShort))
            #     print()
            #     num += 1
            timeDiffHour = int(currentTimeSplitShort[0]) - int(secondTimeSplit[0])
            timeDiffMin = int(currentTimeSplitShort[1]) - int(secondTimeSplit[1])
            timeDiffSec = int(currentTimeSplitShort[2]) - int(secondTimeSplit[2])
            # print(str(timeDiffHour))
            # print(str(timeDiffMin))
            # print(str(timeDiffSec))
            try:
                if 1 >= timeDiffHour >= 0:
                    if 2 >= timeDiffMin >= 0:
                        # if timeDiffSec <= 30:
                        ## Firefox
                        if Process.pName == GlobalVariables.browsers[0] and FireFoxUsage.firefoxCounter != 0:
                            FireFoxUsage.firefoxCPUUsage = FireFoxUsage.firefoxCPUUsage + Process.cpuUsage
                            FireFoxUsage.firefoxMemoryUsage = FireFoxUsage.firefoxMemoryUsage + Process.memoryUsage

                            FireFoxUsage.firefoxTotalCPUUsage = FireFoxUsage.firefoxTotalCPUUsage + Process.cpuUsage
                            FireFoxUsage.firefoxAverageCPUUsage = FireFoxUsage.firefoxTotalCPUUsage / FireFoxUsage.firefoxCounter

                            FireFoxUsage.firefoxTotalMemoryUsage = FireFoxUsage.firefoxTotalMemoryUsage + Process.memoryUsage
                            FireFoxUsage.firefoxAverageMemoryUsage = FireFoxUsage.firefoxTotalMemoryUsage / FireFoxUsage.firefoxCounter
                        ## MS Edge
                        if Process.pName == GlobalVariables.browsers[1]:
                            MsEdgeUsage.msEdgeCPUUsage = MsEdgeUsage.msEdgeCPUUsage + Process.cpuUsage
                            MsEdgeUsage.msEdgeMemoryUsage = MsEdgeUsage.msEdgeMemoryUsage + Process.memoryUsage

                            MsEdgeUsage.msEdgeTotalCPUUsage = MsEdgeUsage.msEdgeTotalCPUUsage + Process.cpuUsage
                            MsEdgeUsage.msEdgeAverageCPUUsage = MsEdgeUsage.msEdgeTotalCPUUsage / MsEdgeUsage.msCount

                            MsEdgeUsage.msEdgeTotalMemoryUsage = MsEdgeUsage.msEdgeTotalMemoryUsage + Process.memoryUsage
                            MsEdgeUsage.msEdgeAverageMemoryUsage = MsEdgeUsage.msEdgeTotalMemoryUsage / MsEdgeUsage.msCount
                        ## Chrome
                        if Process.pName == GlobalVariables.browsers[2] and ChromeUsage.chromeCounter != 0:
                            ChromeUsage.chromeCPUUsage = ChromeUsage.chromeCPUUsage + Process.cpuUsage
                            ChromeUsage.chromeMemoryUsage = ChromeUsage.chromeMemoryUsage + Process.memoryUsage

                            ChromeUsage.chromeTotalCPUUsage = ChromeUsage.chromeTotalCPUUsage + Process.cpuUsage
                            ChromeUsage.chromeAverageCPUUsage = ChromeUsage.chromeTotalCPUUsage / ChromeUsage.chromeCounter

                            ChromeUsage.chromeTotalMemoryUsage = ChromeUsage.chromeTotalMemoryUsage + Process.memoryUsage
                            ChromeUsage.chromeAverageMemoryUsage = ChromeUsage.chromeTotalMemoryUsage / ChromeUsage.chromeCounter


                        for browser in GlobalVariables.browsers:
                            if Process.pName == browser:
                                counters = [FireFoxUsage.firefoxCounter, MsEdgeUsage.msEdgeCounter, ChromeUsage.gCount]

                                for counter in counters:
                                    if counter <= 2:

                                        Process.processes.append({
                                            'pid': Process.pID, 'priority/nice': Process.nice, 'name': Process.pName, 'create_time': Process.createTime,
                                            'cores': Process.cores, 'cpuUsage': Process.cpuUsage, 'memoryUsage': Process.memoryUsage,
                                            'readBytes': Process.readBytes, 'writeBytes': Process.writeBytes,
                                        })
            except:
                print("Error: There was an error!")
            # try:
            #
            # except:
            #     print('error')

                # processes.append({
                #     'pid': pID, 'name': pName, 'create_time': createTime,
                #     'cores': cores, 'cpuUsage': cpuUsage, 'status': status, 'priority/nice': nice,
                #     'memoryUsage': memoryUsage, 'readBytes': readBytes, 'writeBytes': writeBytes,
                #     'numberThreads': numberThreads, 'username': username,
                # })
# @with_goto
def ShowProcesses():
    # if Open_Gui:
    #     ShowGui()
    import argparse
    parser = argparse.ArgumentParser(description="Process Viewer & Monitor")
    parser.add_argument("-c", "--columns", help="""Columns to show,
                                                available are name,create_time,cores,cpu_usage,status,nice,memory_usage,read_bytes,write_bytes,n_threads,username.
                                                Default is name,cpu_usage,memory_usage,read_bytes,write_bytes,status,create_time,nice,n_threads,cores.""",
                        default="name,cpuUsage,memoryUsage,readBytes,writeBytes,status,createTime,nice,numberThreads,cores")
    parser.add_argument("-s", "--sort-by", dest="sort_by", help="Column to sort by, default is memory_usage .", default='create_time')
    parser.add_argument("--descending", action="store_true", help="Whether to sort in descending order.")
    parser.add_argument("-n", help="Number of processes to show, will show all if 0 is specified, default is 25 .", default=500)

    # parse arguments
    args = parser.parse_args()
    columns = args.columns
    sort_by = args.sort_by
    descending = args.descending
    n = int(args.n)

    GlobalVariables.runTime = time.time() - float(GlobalVariables.startTime)
    print(GlobalVariables.runTime)
    # Convert to pandas dataframe
    dataframe = pandas.DataFrame(Process.processes)
    newResultsDataframe = pandas.DataFrame(Process.processes)
    # Set the process id as index of process
    dataframe.set_index('pid', inplace=True)
    dataframe.sort_values('create_time', inplace=True)

    # Sort rows by column passed as argument
    dataframe.sort_values('create_time', inplace=True, ascending=descending)
    # Convert to proper date format
    dataframe['create_time'] = dataframe['create_time'].apply(datetime.strftime, args=("%Y-%m-%d %H:%M:%S",))
    newResultsDataframe['create_time'] = newResultsDataframe['create_time'].apply(datetime.strftime, args=("%Y-%m-%d %H:%M:%S",))
    dataframe['writeBytes'] = dataframe['writeBytes'].apply(get_size)
    dataframe['readBytes'] = dataframe['readBytes'].apply(get_size)

    newResultsDataframe.sort_values('create_time', inplace=True, ascending=descending)

    # newResultsDataframe['writeBytes'] = newResultsDataframe['writeBytes'].apply(get_size)
    # newResultsDataframe['readBytes'] = newResultsDataframe['readBytes'].apply(get_size)
    #
    # newResultsDataframe['memoryUsage'] = newResultsDataframe['memoryUsage'].apply(GetMemorySize)
    # newResultsDataframe['memoryUsage'] = newResultsDataframe['memoryUsage'].apply(get_size)
    #
    # newResultsDataframe['cpuUsage'] = newResultsDataframe['cpuUsage'].apply(GetMemorySize)
    # newResultsDataframe['cpuUsage'] = newResultsDataframe['cpuUsage'].apply(get_size)

    if n == 0:
        print(dataframe.to_string())
        print("n == 0 (line 258)")

    elif n > 0:
        if GlobalVariables.runTime < 60:
            newResultsDataframe.sort_values('create_time', inplace=True, ascending=descending)
            print('New Values:')
            print(newResultsDataframe.head(len(newResultsDataframe)).to_string())
            print()
            # FireFoxUsage.firefoxMemoryUsage = GetMemorySize(FireFoxUsage.firefoxMemoryUsage)
            # FireFoxUsage.firefoxMemoryUsage = get_size(FireFoxUsage.firefoxMemoryUsage)
            #
            # MsEdgeUsage.msEdgeMemoryUsage = GetMemorySize(MsEdgeUsage.msEdgeMemoryUsage)
            # MsEdgeUsage.msEdgeMemoryUsage = get_size(MsEdgeUsage.msEdgeMemoryUsage)
            #
            # ChromeUsage.chromeMemoryUsage = GetMemorySize(ChromeUsage.chromeMemoryUsage)
            # ChromeUsage.chromeMemoryUsage = get_size(ChromeUsage.chromeMemoryUsage)
            if GlobalVariables.userInputSplit[1] == GlobalVariables.browserOptions[0]:
                print()
                print('FirefoxMemUsage ' + str(FireFoxUsage.firefoxMemoryUsage) + '% ; ' + 'FirefoxCounter ' + str(FireFoxUsage.firefoxCounter) + ' ; ' + 'fCount ' + str(FireFoxUsage.fCount))
                print()
                print("Firefox: ")
                print("Firefox CPU Usage: " + str(FireFoxUsage.firefoxCPUUsage) + "%")
                print("Firefox Average CPU Usage: " + str(FireFoxUsage.firefoxAverageCPUUsage) + "%")
                print("Firefox Memory Usage: " + str(FireFoxUsage.firefoxMemoryUsage) + "%")
                print("Firefox Average Memory Usage: " + str(FireFoxUsage.firefoxAverageMemoryUsage) + "%")
                print()
            if GlobalVariables.userInputSplit[1] == GlobalVariables.browserOptions[1]:
                print()
                print("MSEdgeUsage " + str(MsEdgeUsage.msEdgeMemoryUsage) + '% ; ' + 'MSCounter ' + str(MsEdgeUsage.msEdgeCounter) + ' ; ' + 'MSCount ' + str(MsEdgeUsage.msCount))
                print()
                print("MS Edge Chromium")
                print("MS Edge CPU Usage: " + str(MsEdgeUsage.msEdgeCPUUsage) + "%")
                print("MS Edge Average CPU Usage: " + str(MsEdgeUsage.msEdgeAverageCPUUsage) + "%")
                print("MS Edge Memory Usage: " + str(MsEdgeUsage.msEdgeMemoryUsage) + "%")
                print("MS Edge Average Memory Usage: " + str(MsEdgeUsage.msEdgeAverageMemoryUsage) + "%")
                # print("msedgecounter: " + str(MsEdgeUsage.msEdgeCounter))
                # print("mscount: " + str(MsEdgeUsage.msCount))
                print()
            if GlobalVariables.userInputSplit[1] == GlobalVariables.browserOptions[2]:
                print()
                print('ChromeMemUsage ' + str(ChromeUsage.chromeMemoryUsage) + '% ; ' + 'ChromeCounter ' + str(ChromeUsage.chromeCounter) + ' ; ' 'gCount ' + str(ChromeUsage.gCount))
                print()
                print("Google Chrome: ")
                print("Chrome CPU Usage: " + str(ChromeUsage.chromeCPUUsage) + "%")
                print("Chrome Average CPU Usage: " + str(ChromeUsage.chromeAverageCPUUsage) + "%")
                print("Chrome Memory Usage: " + str(ChromeUsage.chromeMemoryUsage) + "%")
                print("Chrome Average Memory Usage: " + str(ChromeUsage.chromeAverageMemoryUsage) + "%")

        else:
            # print()
            ShowAverages()

            print()
            print()
            print()

            ClearData()


            Program()
            # goto1()
            # print("To quit the program type 'quit', otherwise type nothing ; then press enter.")
            # toQuit = input()
            # if toQuit.toLower() == "quit":
            #     print("This program will now be terminated, thank you for being a user.")
            #     quit()
            # else:
            #     RunStats()

def ClearData():
    GlobalVariables.runTime = 0
    GlobalVariables.startTime = 0

    FireFoxUsage.firefoxCounter = 0
    ChromeUsage.chromeCounter = 0
    MsEdgeUsage.msEdgeCounter = 0

    FireFoxUsage.firefoxMemoryUsage = 0
    FireFoxUsage.firefoxTotalMemoryUsage = 0
    FireFoxUsage.firefoxAverageMemoryUsage = 0
    FireFoxUsage.firefoxCPUUsage = 0
    FireFoxUsage.firefoxTotalCPUUsage = 0
    FireFoxUsage.firefoxAverageCPUUsage = 0

def sendURL(sentURL):
    time.sleep(1.5)
    if GlobalVariables.inputURL != "":
        for letter in sentURL:
            keyboard.write(letter)
        keyboard.send('enter')
    else:
        time.sleep(0)
        print("No URL was entered.")
    time.sleep(0.2)

def OpenBrowsers(browserchoice):


    #time.sleep(4)


    if GlobalVariables.currentOS == GlobalVariables.osTypes[0]:
        # Open URL in a new window of Google Chrome
        if browserchoice == 'googlechrome':
            webbrowser.register('google-chrome', webbrowser.open(GlobalVariables.windowsGoogleChromePath, new=0, autoraise=True))
            sendURL(str(GlobalVariables.inputURL))
            time.sleep(1)
        # Open URL in a new window of Safari Firefox
        if browserchoice == 'firefox':
            webbrowser.register('safari-firefox', webbrowser.open(GlobalVariables.windowsFirefoxPath, new=0, autoraise=True))
            sendURL(str(GlobalVariables.inputURL))
            time.sleep(1)
        # # Open URL in a new window of Microsoft Edge Chromium Beta
        # if browserchoice == 'msedgebeta':
        #     webbrowser.register('ms-edge-chromium', webbrowser.open(msEdgeChromiumBetaPath, new=0, autoraise=True))
        #     sendURL(str(inputURL))
        #     time.sleep(1)
        if browserchoice == 'msedge':
            webbrowser.register('ms-edge-chromium', webbrowser.open(GlobalVariables.msEdgeChromiumPath, new=0, autoraise=True))
            sendURL(str(GlobalVariables.inputURL))
            time.sleep(1)







    # sys.setrecursionlimit(1000)
    #
    # if GlobalVariables.osVar == "win32":
    #     osVar = "Win32Variables"
    #     OpenBrowsers(GlobalVariables.browserSelection)
    # elif GlobalVariables.osVar == "linux2":
    #     osVar = "linux2Variables"
    #
    # else:
    #     print("You did not enter a url or this OS is not supported. Type 'help', if you need assistance. ")
    #     print()
    #     print("currentos: " + str(GlobalVariables.currentOS))
    #     ## print("osvar: " + str(GlobalVariables.osVar))
    #     print()
    #     Program()





    # Open URL in a new window of Microsoft Internet Explorer
    # webbrowser.register('ms=internet-explorer', webbrowser.open(internetExplorerPath, new=0, autoraise=True))
    # time.sleep(3)
    # if inputURL != "":
    #     # num = 1
    #     # while num < 6:
    #     #     keyboard.send('tab' & 'shift')
    #     #     num = num + 1
    #     keyboard.send('tab+shift')
    #     #     keyboard.send('shift') & keyboard.send('tab')
    #     # keyboard.send('shift') & keyboard.send('tab')
    #     # time.sleep(20)
    #     # for letter in inputURL:
    #     #     keyboard.write(letter)
    #     # keyboard.send('enter')
    # else:
    #     time.sleep(0)
    #     print("ERROR!!!")
    # time.sleep(0.2)
    # sendURL()
    # time.sleep(2)

def GetPercent(value):
    if value > 0.0:
        newvalue = (value / float(GlobalVariables.INSTALLEDMEMORY))

def GetMemorySize(memPercent):
    # nums = [1000000000000, 1000000000, 1000000, 1000]
    # abrevs = ['TB', 'GB', 'MB', 'KB']
    # for num in nums:
    #     for abrev in abrevs:
    # try:
    # if float(INSTALLEDMEMORY) > 0.0:
    if memPercent > 0.0:
        memPercent = (memPercent / 100) * float(GlobalVariables.INSTALLEDMEMORY)
        return memPercent
    else:
        print("Error Converting Memory Percent!")
        return memPercent
        # pass
        # else:
        #     print("Memory Capacity Not Specified!")
        #     return memPercent
    # except:
    #     print("Memory Conversion Error!")
    #     return memPercent

def get_size(byteNum):
    nums = [1000000000000, 1000000000, 1000000, 1000]
    abrevs = [' TB', ' GB', ' MB', ' KB']
    # for num in nums:
    #     for abrev in abrevs:
    #         if byteNum > num:
    #             byteNum = byteNum / num
    #             byteNum = str(byteNum) + abrev
    #             return byteNum
    if byteNum < nums[1]:
        byteNum = byteNum / nums[1]
        byteNum = str(byteNum / 100) + abrevs[1]
        return byteNum
    elif byteNum < nums[2]:
        byteNum = byteNum / nums[2]
        byteNum = str(byteNum) + abrevs[2]
        return byteNum
    elif byteNum < nums[3]:
        byteNum = byteNum / nums[3]
        byteNum = str(byteNum) + abrevs[3]
        return byteNum
    else:
        return byteNum
    # """
    # Returns size of bytes in a nice format
    # """
    # for unit in ['', 'K', 'M', 'G', 'T', 'P']:
    #     if byteNum < 1024:
    #         # return f"{bytes:.2f}{unit}B"
    #         return "{bytes:.2f}{unit}B"
    #     # bytes /= 1024

def ShowRAM():
    print("The configuration currently has " + str(GlobalVariables.INSTALLEDMEMORY) + " bytes of RAM in your computer. If that is correct visit a url, if not then type 'ram:' to change that value.")
    return

def ModifyRAM():
    print("How much memory does your machine have?")
    INSTALLEDMEMORY = input()
    return

def ShowHelp():
    print()
    # browserPaths = [msEdgeChromiumStablePath, msEdgeChromiumBetaPath, googleChromePath, firefoxPath]
    # browserOptions = ['msedgestable', 'msedgebeta', 'googlechrome', 'firefox']

    print('You can change the amount of ram your machine has with the \'RAM:\' command. \nTo see the current RAM, type \'DIR RAM:\'.  \nYou may visit a URL by typing it. \nYou may also quit the '
          'program by typing \'quit\'. \nYou currently have %s bytes of ram in your computer.' '\nTo open a gui add \' gui\' after typing the url.''\nSyntax: "URL OPTION" The Options include \'RAM:\', \'DIR RAM:\', \'GUI\', and \'BROWSER.\'' 'BROWSERS include \'msedge\', \'googlechrome\', and \'firefox\'.\n' % GlobalVariables.INSTALLEDMEMORY)
    return

def RaiseAboveAll(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

def ShowGui():
    print("GUI")

    # # backFrame = tk.Frame(master=app, width=200, height=200, bg='blue').pack()
    #
    # # RunStats()
    #
    # for process in Process.processes:
    #     if process["name"] == browsers[0]:
    #         # nameLabel = tk.Label(master=app, text='Process %s: ' % num, bg='lightblue', ).grid(row=0, column=0)
    #         nameLabel = tk.Label(master=app, text=process["name"], bg='lightblue', ).grid(row=0, column=0)
    #         fireMemUsageLabel = tk.Label(master=app, text=FireFoxUsage.firefoxMemoryUsage, bg='lightblue', ).grid(row=0, column=1)
    #         fireCpuUsageLabel = tk.Label(master=app, text=FireFoxUsage.firefoxCPUUsage, bg='lightblue', ).grid(row=0, column=2)
    #
    # # x = 0
    # # y = 0
    # # num = 0
    # # while num < 10:
    # #     # nameEntry = tk.Label(master=app, text=processes['name'])
    # #
    # #     y += 5
    # #     # nameLabel.place(relx=x, rely=y)
    # #     y += 5
    # #     num += 1
    #
    # # app.lift()
    # # app.mainloop()

def RunStats():
    OpenBrowsers(GlobalVariables.browserSelection)
    time.sleep(4)

    while not GlobalVariables.stop:

        FireFoxUsage.firefoxMemoryUsage = 0.0
        FireFoxUsage.firefoxCPUUsage = 0.0
        ## Firefox

        if str(GlobalVariables.userInputSplit[1]) == GlobalVariables.browserOptions[0]:
            FireFoxUsage.firefoxCounter += 1
        if FireFoxUsage.firefoxCounter <= 1:
            FireFoxUsage.fCount += 1

        MsEdgeUsage.msEdgeCounter = 0
        MsEdgeUsage.msEdgeMemoryUsage = 0.0
        MsEdgeUsage.msEdgeCPUUsage = 0.0
        ## MSEdge Chromium
        if str(GlobalVariables.userInputSplit[1]) == GlobalVariables.browserOptions[1]:
            MsEdgeUsage.msEdgeCounter += 1
        if MsEdgeUsage.msEdgeCounter <= 1:
            MsEdgeUsage.msCount += 1

        ChromeUsage.chromeMemoryUsage = 0.0
        ChromeUsage.chromeCPUUsage = 0.0
        ## Google Chrome
        if str(GlobalVariables.userInputSplit[1]) == GlobalVariables.browserOptions[2]:
            ChromeUsage.chromeCounter += 1
        if ChromeUsage.chromeCounter <= 1:
            ChromeUsage.gCount += 1

        time.sleep(2)
        # processes == []
        # for browser in browsers:
        #     if Process.pName == browser:
        #         for process in Process.processes:
        # if Process.pName == browsers[0]:
        # Process.processes.remove({
        #     'pid': Process.pID, 'priority/nice': Process.nice, 'name': Process.pName, 'create_time': Process.createTime,
        #     'cores': Process.cores, 'cpuUsage': Process.cpuUsage, 'memoryUsage': Process.memoryUsage,
        #     'readBytes': Process.readBytes, 'writeBytes': Process.writeBytes,
        # })
        #             Process.processes.remove({
        #                 Process.pID, Process.nice, Process.pName, Process.createTime,
        #                 Process.cores, Process.cpuUsage, Process.memoryUsage,
        #                 Process.readBytes, Process.writeBytes,
        #             })
        processResults = []
        GetProcessInfo()

        ShowProcesses()

        # ShowAverages()

        threadCount = threading.activeCount()
        googleWebPath = "https://www.google.com/"
        python = "https://www.python.org/"





def ShowAverages():
    Averages.FireFoxCPUUsage = FireFoxUsage.firefoxAverageCPUUsage
    Averages.FirefoxMemoryUsage = FireFoxUsage.firefoxAverageMemoryUsage

    Averages.GoogleChromeCPUUsage = ChromeUsage.chromeAverageCPUUsage
    Averages.GoogleChromeMemoryUsage = ChromeUsage.chromeAverageMemoryUsage

    Averages.MsEdgeCPUUsage = MsEdgeUsage.msEdgeAverageCPUUsage
    Averages.MsEdgeMemoryUsage = MsEdgeUsage.msEdgeAverageMemoryUsage

    print()
    print("Your Average CPU usage for Firefox was " + str(Averages.FireFoxCPUUsage) + ".")
    print("Your Average Memory usage for Firefox was " + str(Averages.FireFoxMemoryUsage) + ".")

    ##print("Your Average CPU usage for Google Chrome was " + Averages.GoogleChromeCPUUsage.to_string() + ".")
    # print("Your Average Memory usage for Google Chrome was " + Averages.GoogleChromeMemoryUsage.to_string() + ".")

    # print("Your Average CPU usage for MsEdge was " + Averages.MsEdgeCPUUsage.to_string() + ".")
    # print("Your Average CPU usage for MsEdge was " + Averages.MsEdgeMemoryUsage.to_string() + ".")
def Program():
    # try:

    # userInput = ""
    while not GlobalVariables.stop:



        # tkFrame = tk.Frame
        print('Author: Luke Gitchel')
        print('College: FHTC - Emporia, Ks')
        print('Degrees: CPD(grad:May 2019), Network Technology(grad:Dec 2020)')
        print()
        print("To display command info, type 'help'. For best results, close all browsers prior to using this program.")
        print()
        print("Please enter a URL and an OPTION. Type \'help\' for syntax assistance.")
        GlobalVariables.userInput = input()

        GlobalVariables.startTime = time.time()
        GlobalVariables.userInputSplit = str(GlobalVariables.userInput).split(" ")

        # print("userinput: " + str(GlobalVariables.userInput))
        # print("userinputsplit: " + str(GlobalVariables.userInputSplit))
        # print("browseroption[0]: " + str(GlobalVariables.browserOptions[0]))
        # print("userinputsplit[1]: " + GlobalVariables.userInputSplit[1])

        GlobalVariables.inputURL = GlobalVariables.userInputSplit[0]
        GlobalVariables.browserSelection = GlobalVariables.userInputSplit[1]
        app = tk.Tk()
        # root = tk.Toplevel()
        app.geometry('400x400')
        # RaiseAboveAll(app)

        if str(GlobalVariables.inputURL).upper() == 'RAM:':
            ModifyRAM()
        elif str(GlobalVariables.inputURL).upper() == 'QUIT':
            quit()
        elif str(GlobalVariables.inputURL).upper() == 'DIR RAM:':
            ShowRAM()
        elif str(GlobalVariables.inputURL).upper() == 'HELP':
            ShowHelp()
        elif str(GlobalVariables.userInput).__contains__("gui"):
            pass
            ShowGui()
            # RunStats()
            # threadOne = threading.Thread(ShowGui())
            # threadTwo = threading.Thread(RunStats())
            # userInputSplit = str(userInput).split(" ")
            # inputURL = userInputSplit[0]
            #
            # if str(userInputSplit[1]).upper() == 'GUI':
            #     # Open_Gui = True
            #     ShowGui()
            # else:
            #     RunStats()
        elif str(GlobalVariables.userInputSplit[1]) == GlobalVariables.browserOptions[0]:
            browserSelection = GlobalVariables.browserOptions[0]
            RunStats()
            # ShowAverages()
        elif str(GlobalVariables.userInputSplit[1]) == GlobalVariables.browserOptions[1]:
            browserSelection = GlobalVariables.browserOptions[1]
            RunStats()
            # ShowAverages()
        elif str(GlobalVariables.userInputSplit[1]) == GlobalVariables.browserOptions[2]:
            browserSelection = GlobalVariables.browserOptions[2]
            RunStats()
            # ShowAverages()
        # elif str(userInputSplit[1]) == browserOptions[3]:
        #     browserSelection = browserOptions[3]
        #     # processes = []
        #     RunStats()
        else:
            print("Error! There was an error with your input.")
            # userInputSplit = str(userInput).split(" ")
            # inputURL = userInputSplit[0]
            # RunStats()
    # except:
    #         print("Error: There was an error with your input.")
    app.mainloop()
    app.attributes('-topmost', 1)
    app.attributes('-topmost', 0)
    # time.sleep(60)
    toQuit = GlobalVariables.userInput
    if toQuit.tolower == "quit":
        app.quit()
if __name__ == '__main__':





    Program()

