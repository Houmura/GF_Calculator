#   少女前线后勤计算器

import csv
import numpy as np
import time
from os import system

class Duration():
    d = 0.0
    def __init__(self,tlist):
        self.tlist = tlist
        if (tlist.split(":")[0][0] == "0") and (len(tlist.split(":")[0]) != 1):   
            self.h = self.tlist.split(":")[0][1:]
            self.m = self.tlist.split(":")[1]
        else:
            self.h = self.tlist.split(":")[0]
            self.m = self.tlist.split(":")[1]

        if len(tlist.split(":")) == 3:
            self.s = self.tlist.split(":")[2]
            self.d = (float(self.h) * 60 + float(self.m) + float(self.s)/60.0)
        elif len(tlist.split(":")) == 2:
            self.d = (float(self.h) * 60 + float(self.m))
        else:
            print("请输入有效时长! \n")
            time.sleep(5)
            raise ValueError
        
    def show(self):
        print("%d minutes"%(self.d))


def read_csv(cate_dict, tlist, rlist, path_name):
    with open(path_name,'r',encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile)
        for i,row in enumerate(reader):
            if i != 0:
                row = row
                cate_dict[i-1] = row[0]+""+row[1]
                tlist.append(row[2])

                for ii in range(3,7):
                    if row[ii] == "":
                        row[ii] = "0.0"
                    rlist[ii-3].append(float(row[ii]))

    durations = []
    for i in range(len(tlist)):
        durations.append(Duration(tlist[i]).d)
    
    return durations



def time_limitation (durations, tlist, resources, max_duration):
    # 将超出时限的资源置零，不干扰后续的排序
    # 返回满足条件处理好的资源列表
    time_idx = []
    r = np.copy (resources)
    for i in range(len(tlist)):
        if durations[i] > max_duration:
            time_idx.append(i)
            for ii in range(4):
                r[ii][i] = 0.0
    return r, time_idx



def sheet(cate_dict,tlist,rlist):
    print("    |    后勤编号    |    时长    | 人力 | 弹药 | 口粮 | 零件 ")
    for i in range(len(tlist)):
        print("    | %10s | %10s | %4d | %4d | %4d | %4d "%(cate_dict[i],tlist[i],rlist[0][i],rlist[1][i],rlist[2][i],rlist[3][i]))


def print_list(idx,cate_dict,tlist,rlist,manpower,ammo,mre,part):
    print("    |    后勤编号    |    时长    | 人力 | 弹药 | 口粮 | 零件 ")
    for i in range(4):
        print("    | %10s | %10s | %4d | %4d | %4d | %4d "%(cate_dict[idx[i]],tlist[idx[i]],rlist[0][idx[i]],\
            rlist[1][idx[i]],rlist[2][idx[i]],rlist[3][idx[i]]))
    print("    |      合计      |            | %4d | %4d | %4d | %4d "%(manpower,ammo,mre,part))


def cal_total_max_idx(durations, tlist, rlist, max_duration):
    total = []
    for i in range(len(tlist)):
        total.append(3*rlist[0][i]+3*rlist[1][i]+3*rlist[2][i]+rlist[3][i])  
    for i in range(len(tlist)):
        if durations[i] > max_duration:
            total[i] = 0.0
    total = np.array(total)
    idx = np.argsort(total)[-4:]
    return idx


def clear():
    system('cls')

