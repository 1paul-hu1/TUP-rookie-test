def main():#main函数入口
    for i  in range(1, 10):#i取1到9
        for j in range(1, i+1):#j取1到i
            print(f"{i} * {j} = {i * j}", end="\t")#直接f-string格式化书写，\t表示键盘上的tab 
        print()#换行，print结尾默认\n，newline，表示回车开新行
if __name__=="__main__":#main函数入口，方便程序的运行。
    main()