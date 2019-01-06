# -*- coding=utf-8 -*-
import warnings
import datetime

warnings.filterwarnings("ignore")


def getNowDay():
    DayNow = datetime.datetime.today().strftime('%Y-%m-%d')
    return DayNow


def getYesterDay():
    YesterDay = (datetime.datetime.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')
    return YesterDay


def dateRange(beginDate, endDate):
    dates = []
    dt = datetime.datetime.strptime(beginDate, "%Y-%m-%d")
    date = beginDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")
    return dates


def monthRange(beginDate, endDate):
    monthSet = set()
    for date in dateRange(beginDate, endDate):
        monthSet.add(date[0:7])
    monthList = []
    for month in monthSet:
        monthList.append(month)
    return sorted(monthList)


def dateHourRange(beginDateHour, endDateHour):
    dhours = []
    dhour = datetime.datetime.strptime(beginDateHour, "%Y-%m-%d %H:00:00")
    date = beginDateHour[:]
    while date <= endDateHour:
        dhours.append(date)
        dhour = dhour + datetime.timedelta(hours=1)
        date = dhour.strftime("%Y-%m-%d %H:00:00")
    return dhours


print(getNowDay())

print(getYesterDay())

print(dateRange(beginDate='2018-12-01', endDate='2018-12-31'))

print(monthRange(beginDate='2018-12-01', endDate='2018-12-31'))

print(dateHourRange(beginDateHour='2018-12-01 00:00:00', endDateHour='2018-12-31 00'))

dist_hour = dateHourRange(beginDateHour='2018-12-01 00:00:00', endDateHour='2018-12-31 00')
for hour in dist_hour:
    print(hour)