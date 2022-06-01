#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Timer

import pymysql
import threading
from datetime import datetime

conn = pymysql.connect(host='localhost', user='root', password='qwpo1209', db='ccan', charset='utf8')
file = open(r'C:\Users\jacke\OneDrive\Desktop\strangeid.trc')
lines = file.readlines()

init = [[0 for _ in range(14)] for _ in range(1000)] #전체 데이터
first = [[0 for _ in range(14)] for _ in range(1000)] #초기 5초 데이터
package = [[0 for _ in range(14)] for _ in range(20)] #묶어서 전송할 데이터

 #파일 전체 읽어오기

j = k = Len = Dump = cnt = times = index = 0

curs = conn.cursor()

start_time = datetime.now()

sql = '''TRUNCATE table can''' #테이블 데이터 제거
sql += ";"
curs.execute(sql)

def mysql():
    sql2 = '''REPLACE INTO can(Sec, ID, Count, Flag, Amount) VALUES'''
    for i in range(20):
        sql2 += '''("''' + str((float(package[i][1]))/1000) + '''", "''' + str(package[i][0]) + '''", ''' + str(package[i][11]) + ''', "''' + str(package[i][12]) +  '''", ''' + str(package[i][13]) + ''')'''
        if(i != 19):
            sql2 += ','
    sql2 += ';'

    curs.execute(sql2)
    conn.commit()


def Check_time(line):
    while (True):
        date_diff = datetime.now() - start_time
        sec_diff = float(date_diff.seconds) + (float(date_diff.microseconds) / 1000000)
        trc_sec = float(line[1]) / 1000
        if trc_sec < sec_diff :
            break


def if_time():
    init[Dump][12] = 0 if init[Dump][11] - first[Dump][11] <= 0 else 1


for line in lines: #파일 한줄씩 읽어서 line에 저장
    if line[0] == ';': continue
    line = line.split() #공백으로 구분
    del line[0:3:2]
    temp = line[0]
    line[0] = line[1]
    line[1] = temp
    Check_time(line)
    for i in line:
        if k == 2:
            Len = int(i)
        if k == Len + 3:
            k = 0
            j+=1
        for ji in range(j+1):
            if k == 0: #CAN ID 리스트에 넣기
                if init[ji][k] == i:
                    init[ji][k] = i
                    init[ji][13] += 1
                    if float(first[ji][1]) <= 4500:
                        first[ji][k] = i
                        first[ji][13] += 1
                    k+=1
                    Dump = ji
                    j -= 1
                    break
                elif (j == ji): #빈 리스트에 처음 CAN ID 넣기
                    init[ji][k] = i
                    init[ji][13] = 1
                    if float(first[ji][1]) <= 4500:
                        first[ji][k] = i
                        first[ji][13] = 1
                    k += 1
                    Dump = ji
                    break
                else:
                    continue
            else: #리스트에 CAN 데이터 채우기
                if k == 1: #시간
                    init[Dump][k] = i
                    if float(first[Dump][1]) <= 4500:
                        first[Dump][k] = i
                    k+=1
                    break
                if k == 2: #길이
                    init[Dump][k] = i
                    if float(first[Dump][1]) <= 4500:
                        first[Dump][k] = i
                    k+=1
                    break
                elif (2 < k < Len + 3): #데이터
                    if k == 3:
                        cnt = 0
                    if init[Dump][k] != i:
                        init[Dump][k] = i
                        if float(first[Dump][1]) <= 4500:
                            if first[Dump][k] != i:
                                first[Dump][k] = i
                        cnt += 1
                        k+=1
                        if k == Len+3:
                            if j==Dump:
                                init[Dump][11] = 0
                                if float(first[Dump][1]) <= 4500:
                                    first[Dump][11] = 0
                            else:
                                init[Dump][11] = cnt
                                if float(first[Dump][1]) <= 4000:
                                    if first[Dump][11] <= cnt:
                                        first[Dump][11] = cnt
                        break
                    else:
                        init[Dump][k] = i
                        k+=1
                        if k == Len+3:
                            if j==Dump:
                                init[Dump][11] = 0
                                if float(first[Dump][1]) <= 4500:
                                    first[Dump][11] = 0
                            else:
                                init[Dump][11] = cnt
                                if float(first[Dump][1]) <= 4500:
                                    if first[Dump][11] <= cnt:
                                        first[Dump][11] = cnt
                        break

    #특정 행위 구간 카운트 비교
    time = float(init[Dump][1])
    if 10000.4 <= time <= 13000.2: if_time()
    elif 30001.2 <= time <= 33001.2: if_time()
    elif 50002.0 <= time <= 53000.2: if_time()
    elif 300120.0 <= time <= 320008.0: if_time()
    elif 480192.0 <= time <= 495196.0: if_time()
    elif 495198.0 <= time <= 520202.0: if_time()
    else:
        init[Dump][12] = 0

    '''if float(init[Dump][1]) >= 5000.2:
        print(first)'''

    if(index >= 20) :
        mysql()
        index = 0
    else :
        package[index] = init[Dump]
        index += 1


file.close()
conn.close()