while True:
    try:
        n = input()
        low_cnt, up_cnt, num_cnt, spl_cnt = 0,0,0,0
        for i in n:
            if i.islower():
                low_cnt += 1
            
            elif i.isupper():
                up_cnt+= 1
        
            elif i.isdigit():
                num_cnt += 1
            
            elif i.isspace():
                spl_cnt += 1
        print(low_cnt, up_cnt, num_cnt, spl_cnt)
    except:
        break