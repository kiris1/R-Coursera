# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 15:07:13 2017

@author: e543865
"""
import datetime


def date_weekday():
    today = datetime.now()
    weekday = today.weekday()
    print('Today is %s' % weekday)
    
date_weekday()
    