# 少女前线后勤计算器

# from GF_cal import *
from GF_reader import *
import time

print("    ***************************************************")
print("    *                                                 *")
print("    *          少 女 前 线 后 勤 计 算 器             *")
print("    *                                                 *")
print("    *                                                 *")
print("    *                                                 *")
print("    * 请输入后勤数据表名称(默认为GF.csv)              *")
print("    * 并将其放置在本程序所在目录下                    *")
print("    *                                                 *")
print("    ***************************************************")
print("    确认无误后请按任意键继续...")
path_name=input()
if path_name == "":
    path_name = "GF.csv"

clear()

while (True):

    cate_dict = {}
    # [[每关人力],[每关弹药],[每关口粮],[每关零件]]
    rlist = [[] for i in range(4)]  
    tlist = []

    durations = read_csv(cate_dict, tlist, rlist,path_name)

    # 转换rlist为 numpy array 方便后续操作
    resources = np.array(rlist)


    print("    ***************************************************")
    print("    *                                                 *")
    print("    *          少 女 前 线 后 勤 计 算 器             *")
    print("    *                                                 *")
    print("    *                                                 *")
    print("    *                                                 *")
    print("    *  请选择一项功能，输入对应编号:                  *")
    print("    *                                                 *")
    print("    *   1 - 计算后勤收益         2 - 后勤收益一览     *")
    print("    *                                                 *")
    print("    ***************************************************")
    print("\n\n\n")
    type_cal = input("    ")

    if type_cal == "1":

        clear()
        print("\n    请输入后勤时长，例如:  0:30（英文冒号） 代表0小时30分钟，回车键确认")
        input_time = input("    ")
        print("\n    您输入的时长为：",input_time,"\n") 
        print("    即 ",Duration(input_time).d," 分钟\n")

        print("    ***************************************************")
        print("    *          少 女 前 线 后 勤 计 算 器             *")
        print("    *                                                 *")
        print("    *                                                 *")
        print("    *                                                 *")
        print("    *  请选择哪一项资源优先，输入对应编号:            *")
        print("    *                                                 *")
        print("    *       1 - 人力                2 - 弹药          *")
        print("    *       3 - 口粮                4 - 零件          *")
        print("    *                                                 *")
        print("    ***************************************************")
        input_type = input("    ")
        print("\n    后勤时长：", Duration(input_time).d," 分钟\n")

        # 初始化资源
        manpower = 0.0
        ammo = 0.0
        mre = 0.0
        part = 0.0


        if input_type == "1":
            print("    当前为：人力优先获取")

            r, time_idx= time_limitation (durations, tlist, resources, Duration(input_time).d)
            idx = np.argsort(r[0])[-4:]

            for j in range(4):
                manpower  += r[0][idx[j]]
                ammo += r[1][idx[j]]
                mre += r[2][idx[j]]
                part += r[3][idx[j]]
            #print("idx: ",idx)
            #print("time_idx: ", time_idx)
            print("    后勤任务列表：")
            print("    ",cate_dict[idx[0]]," ",cate_dict[idx[1]]," ",cate_dict[idx[2]]," ",cate_dict[idx[3]])
            print("    %5d 分钟内可获取最大人力资源:"%(Duration(input_time).d))
            print_list(idx,cate_dict,tlist,rlist,manpower,ammo,mre,part)
            print("")

        elif input_type == "2":
            print("    当前为：弹药优先获取")
            
            r, time_idx = time_limitation (durations, tlist, resources, Duration(input_time).d)
            idx = np.argsort(r[1])[-4:]
            #print("idx: ",idx)
            #print("time_idx: ", time_idx)
            for j in range(4):
                manpower  += r[0][idx[j]]
                ammo += r[1][idx[j]]
                mre += r[2][idx[j]]
                part += r[3][idx[j]]
            
            print("    后勤任务列表：")
            print("    ",cate_dict[idx[0]]," ",cate_dict[idx[1]]," ",cate_dict[idx[2]]," ",cate_dict[idx[3]])
            print("    %5d 分钟内可获取最大弹药资源:"%(Duration(input_time).d))
            print_list(idx,cate_dict,tlist,rlist,manpower,ammo,mre,part)
            print("")


        elif input_type == "3":
            print("    当前为：口粮优先获取")
            
            r, time_idx = time_limitation (durations, tlist, resources, Duration(input_time).d)
            idx = np.argsort(r[2])[-4:]
            #print("idx: ",idx)
            #print("time_idx: ", time_idx)
            for j in range(4):
                manpower  += r[0][idx[j]]
                ammo += r[1][idx[j]]
                mre += r[2][idx[j]]
                part += r[3][idx[j]]
            
            print("    后勤任务列表：")
            print("    ",cate_dict[idx[0]]," ",cate_dict[idx[1]]," ",cate_dict[idx[2]]," ",cate_dict[idx[3]])
            print("    %5d 分钟内可获取最大口粮资源:"%(Duration(input_time).d))
            print_list(idx,cate_dict,tlist,rlist,manpower,ammo,mre,part)
            print("")


        elif input_type == "4":
            print("    当前为：零件优先获取")
            
            r, time_idx = time_limitation (durations, tlist, resources, Duration(input_time).d)
            idx = np.argsort(r[3])[-4:]
            #print("idx: ",idx)
            #print("time_idx: ", time_idx)
            for j in range(4):
                manpower  += r[0][idx[j]]
                ammo += r[1][idx[j]]
                mre += r[2][idx[j]]
                part += r[3][idx[j]]
            
            print("    后勤任务列表：")
            print("    ",cate_dict[idx[0]]," ",cate_dict[idx[1]]," ",cate_dict[idx[2]]," ",cate_dict[idx[3]])
            print("    %5d 分钟内可获取最大零件资源:"%(Duration(input_time).d))
            print_list(idx,cate_dict,tlist,rlist,manpower,ammo,mre,part)
            print("")

        else:
            print("请输入正确编号! \n")
            time.sleep(5)
            raise ValueError
    
    elif type_cal == "2":
        print("")
        sheet(cate_dict,tlist,rlist)
        print("")
    
    else:
        print("请输入正确编号! \n")
        time.sleep(5)
        raise ValueError

    input("    按任意键返初始界面...")
    clear()




