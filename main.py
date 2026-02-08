#this name is i lazy lang
#or il
#Copyright by Liweizhimesly
#AI write:
import os

# 获取当前脚本的绝对路径，然后构建目标文件的绝对路径
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "pg.il")  # 这里用你的实际文件名

print(f"正在尝试读取: {file_path}")
i = 0
fp=""
for j1 in file_path:
    if j1 == "\\":
        fp = j1+"/"
    else:
        fp = j1
def rfl(fp):
    """
    读取文件所有行，去除每行末尾的换行符（\n和\r），返回包含所有行的列表
    
    参数:
        file_path: 文件路径（字符串）
        
    返回:
        list: 包含文件所有行内容的列表，若文件不存在或出错则返回空列表
    """
    lines = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # 读取所有行，自动处理不同系统的换行符（\n、\r\n等）
            for line in f:
                # 去除行尾的换行符（rstrip会移除末尾所有指定字符，默认包含空格，这里明确指定只删\n和\r）
                cleaned_line = line.rstrip('\n\r')
                
                lines.append(cleaned_line.lstrip())
                        
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在")
    except Exception as e:
        print(f"读取文件时出错：{e}")
    
    return lines
# 预处理阶段：收集标签
raw_codes = rfl(fp)
i = 1
bqline = []  # 存储标签名
bqlline = []  # 存储标签对应的行号
codes = []    # 存储处理后的代码

# 第一遍：收集所有标签
while i-1 < len(raw_codes):
    code0 = raw_codes[i-1]
    if code0 != "" :
        if code0[-1] == ":":
            bqline.append(code0[:-1])  # 去掉冒号存储标签名
            bqlline.append(len(codes) + 1)  # 标签指向下一行
        else:
            codes.append(code0)
    i += 1

# 第二遍：替换跳转指令中的标签为行号
i = 1
final_codes = []
while i-1 < len(codes):
    code0 = codes[i-1].lstrip()
    if code0[:3] in {"ngt", "gto"} and not code0[4:].isdigit():
        # 处理标签跳转
        label_found = False
        for j in range(len(bqline)):
            if code0[4:] == bqline[j]:
                final_codes.append((code0[:4] + str(bqlline[j])))
                label_found = True
                break
        if not label_found:
            print(f"your \"'{code0[4:]}'\" label been eaten!")
            final_codes.append(code0)
    else:
        final_codes.append(code0)
    i += 1
codes = final_codes  # 使用处理后的代码
#i write:
if os.name=="nt":
    clrcmd="cls"
else:
    clrcmd="clear"
#codes=rfl(r"pg.il")
#codes=["set 1,2","otv 1"]
aline = [0]*2048
aslin=[""]*2048
i = 1
tmp=0
zt=False
strict=False
will_return=True
cannopls = True
debug=False
point=0
szt = False
while i-1<len(codes):
    code=codes[i-1]
    if code == "choufeng":
        cannopls = False
    #for code in codes:
    elif code == "add":
        aline[point]+=1
    elif code == "sub":
        aline[point]-=1
    elif code == "lft":
        point += 1
    elif code == "rgt":
        if point == 0:
            pass
        else:
            point -= 1
    elif code == "dbg":
        debug=True
    elif code == "dbs":
        debug=True
        szt=True
    elif code == "clr":
        os.system(clrcmd)
    elif code == "ncl" and cannopls == True:
        will_return = False
    elif code == "cli" and cannopls == True:
        will_return = True
    elif code == "pls,out command donot change lines!":
        will_return = False
    elif code == "pls,out command change lines!":
        will_return = True
    elif code[:4]=="out ":
        if will_return==False:
            print(code[4:],end="")
        else:
            print(code[4:])
    elif code[:3]=="out":
        if code[3:]=="":
            print("[out]:What you thinking aboat?or,you are testing?")
        else:
            print("[out]:Where your blank space?")
    elif code[:4]=="set ":
        a = 0
        for char in code:
            if char == ",":
                break
            a += 1
        #print(a)
        var0=int(code[4:a])
        while var0>=len(aline):
            aline.append(0)
            #print(aline)
        
        if code[(a+1):] == "tmp":
            aline[var0]=tmp
            #print(aline)
            i+=1
            continue
        aline[var0]=int(code[(a+1):])
    elif code[:4]=="sts ":
        a = 0
        for char in code:
            if char == ",":
                break
            a += 1
        var0=int(code[4:a])
        while var0>=len(aslin):
            aslin.append("")
            #print(aline)
        
        str0=code[(a+1):]
        #print(aline)
        aslin[var0]=str0
        #print(aline)
    elif code[:4]=="inp ":
        while int(code[4:])>=len(aline):
            aline.append(0)
        aline[int(code[4:])]=int(input())
    elif code[:4]=="ips ":
        while int(code[4:])>=len(aslin):
            aslin.append("")
        aslin[int(code[4:])]=input()
    elif code[:4]=="otv ":
        if will_return==False:
            print(aline[int(code[4:])],end="")
        else:
            print(aline[int(code[4:])])
    elif code[:4]=="ovs ":
        if will_return==False:
            print(aslin[int(code[4:])],end="")
        else:
            print(aslin[int(code[4:])])
    elif code[:4]=="ngt ":
        if debug == True:
            print(f"[dbg]:Now running code is \"",code,"\" in",i,"line.")
        if szt == True:
            print(f"[zt]:now i\'m {zt}.")
        i=int(code[4:])
        continue
    elif code[:1] in {"0", "1", "2", "3","4","5","6","7","8","9"}:
        b = 0
        for char1 in code:
            if char1 == "+":
                num1_0=int(code[0:b])
                if code[b+1] == "v":
                    while int(code[(b+2):])>=len(aline):
                        aline.append(0)
                    tmp=num1_0+aline[int(code[(b+2):])]
                    break
                
                #print(num1_1)
                #print(code[0:b])

                num1_1=int(code[(b+1):])
                tmp=num1_0+num1_1
                break
            if char1 == "-":
                num1_0=int(code[0:b])
                if code[b+1] == "v":
                    while int(code[(b+2):])>=len(aline):
                        aline.append(0)
                    tmp=num1_0-aline[int(code[(b+2):])]
                    break
                
                #print(num1_1)
                #print(code[0:b])

                num1_1=int(code[(b+1):])
                tmp=num1_0-num1_1
                break
            if char1 == "*":
                num1_0=int(code[0:b])
                if code[b+1] == "v":
                    while int(code[(b+2):])>=len(aline):
                        aline.append(0)
                    tmp=num1_0*aline[int(code[(b+2):])]
                    break
                
                #print(num1_1)
                #print(code[0:b])

                num1_1=int(code[(b+1):])
                tmp=num1_0*num1_1
                break
            if char1 == "/":
                num1_0=int(code[0:b])
                if code[b+1] == "v":
                    while int(code[(b+2):])>=len(aline):
                        aline.append(0)
                    tmp=num1_0//aline[int(code[(b+2):])]
                    break
                
                #print(num1_1)
                #print(code[0:b])

                num1_1=int(code[(b+1):])
                tmp=num1_0//num1_1
                break
            b += 1
    elif code[:1] == "v":

        b = 0
        for char1 in code:
            if char1 == "+":
                if code[b+1] == "v":
                    tmp=aline[int(code[(b+2):])]+aline[int(code[1:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[1:b])>=len(aline):
                    tmp=0+num1_1
                    break
                varL=aline[int(code[1:b])]
                
                #print("var",varL,"str",code[1:b])
                tmp=varL+num1_1
                break
            if char1 == "-":
                if code[b+1] == "v":
                    tmp=aline[int(code[(b+2):])]-aline[int(code[1:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[1:b])>=len(aline):
                    tmp=0-num1_1
                    break
                varL=aline[int(code[1:b])]
                
                #print("var",varL,"str",code[1:b])
                tmp=varL-num1_1
                break
            if char1 == "*":
                if code[b+1] == "v":
                    tmp=aline[int(code[(b+2):])]*aline[int(code[1:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[1:b])>=len(aline):
                    tmp=0*num1_1
                    break
                varL=aline[int(code[1:b])]
                
                #print("var",varL,"str",code[1:b])
                tmp=varL*num1_1
                break
            if char1 == "/":
                if code[b+1] == "v":
                    tmp=aline[int(code[(b+2):])]//aline[int(code[1:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[1:b])>=len(aline):
                    tmp=0//num1_1
                    break
                varL=aline[int(code[1:b])]
                
                #print("var",varL,"str",code[1:b])
                tmp=varL//num1_1
                break
            b += 1
    elif code[:4]=="iff ":
        b = 0
        for char1 in code:
            if char1 == "=":
                if code[b+1] == "v":
                    zt=aline[int(code[(b+2):])]==aline[int(code[5:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[5:b])>=len(aline):
                    zt=0==num1_1
                    break
                varL=aline[int(code[5:b])]
                #print("var",varL,"str",code[1:b])
                zt=varL==num1_1
                break
            if char1 == ">":
                if code[b+1] == "v":
                    zt=aline[int(code[(b+2):])]>aline[int(code[5:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[5:b])>=len(aline):
                    zt=0>num1_1
                    break
                varL=aline[int(code[5:b])]
                
                #print("var",varL,"str",code[1:b])
                zt=varL>num1_1
                break
            if char1 == "<":
                if code[b+1] == "v":
                    zt=aline[int(code[(b+2):])]<aline[int(code[5:b])]
                    break
                num1_1=int(code[(b+1):])
                #print(num1_1)
                #print(code[0:b])
                if int(code[5:b])>=len(aline):
                    zt=0<num1_1
                    break
                varL=aline[int(code[5:b])]
                
                #print("var",varL,"str",code[1:b])
                zt=varL<num1_1
                break
            b +=1
    elif code[:4]=="gto ":
        if debug == True:
            print(f"[dbg]:Now running code is \"",code,"\" in",i,"line.")
        if szt == True:
            print(f"[zt]:now i\'m {zt}.")
        if zt == True:
            i=int(code[4:])
            continue
    elif code[:3]=="cde":
        strict=True
    elif code[:3]=="ant":
        strict=False
    elif code=="i lazy":
        if will_return == False:
            print("Hello world!",end="")
        else:
            print("Hello world!")
    elif code=="":
        i = i+1
        continue
    else:
        if strict==True:
            print(f"we don\'t know \"{code}\"!")
    if debug == True:
        print(f"[dbg]:Now running code is \"",code,"\" in",i,"line.")
    if szt == True:
        print(f"[zt]:now i\'m {zt}.")
    i = i+1 
    #print(aline)

    #print("now",i)
