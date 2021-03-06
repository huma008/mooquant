# -*- coding: utf-8 -*-
# MooQuant
#
# Copyright 2017 bopo.wang<ibopo@126.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: bopo.wang <ibopo@126.com>
"""

import datetime

import pytz


# 时间转原生格式
def datetime_is_naive(dateTime):
    """ Returns True if dateTime is naive."""
    return dateTime.tzinfo is None or dateTime.tzinfo.utcoffset(dateTime) is None


# 移除时区信息
def unlocalize(dateTime):
    return dateTime.replace(tzinfo=None)


# 本地化时间转换
def localize(dateTime, timeZone):
    """Returns a datetime adjusted to a timezone:
       返回将一个日期时间调整到一个时区

     * If dateTime is a naive datetime (datetime with no timezone information), timezone information is added but date
       and time remains the same.
     * If dateTime is not a naive datetime, a datetime object with new tzinfo attribute is returned, adjusting the date
       and time data so the result is the same UTC time.
    """

    if datetime_is_naive(dateTime):
        ret = timeZone.localize(dateTime)
    else:
        ret = dateTime.astimezone(timeZone)

    return ret


def as_utc(dateTime):
    return localize(dateTime, pytz.utc)


# 时间转时间戳
def datetime_to_timestamp(dateTime):
    """ Converts a datetime.datetime to a UTC timestamp."""
    diff = as_utc(dateTime) - epoch_utc
    return diff.total_seconds()


# 时间戳转时间
def timestamp_to_datetime(timeStamp, localized=True):
    """ Converts a UTC timestamp to a datetime.datetime."""
    ret = datetime.datetime.utcfromtimestamp(timeStamp)

    if localized:
        ret = localize(ret, pytz.utc)

    return ret


# 获取第一个星期一
def get_first_monday(year):
    ret = datetime.date(year, 1, 1)

    if ret.weekday() != 0:
        diff = 7 - ret.weekday()
        ret = ret + datetime.timedelta(days=diff)

    return ret


def get_last_monday(year):
    ret = datetime.date(year, 12, 31)

    if ret.weekday() != 0:
        diff = ret.weekday() * -1
        ret = ret + datetime.timedelta(days=diff)

    return ret


epoch_utc = as_utc(datetime.datetime(1970, 1, 1))
