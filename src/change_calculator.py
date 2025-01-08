
def change_calculator(change):
    change_dic = {}
    count_10 = 0
    count_5 = 0
    count_2 = 0
    count_1 = 0
    change_list = [1,2,5,10]
    while change >0:
        for item in reversed(change_list):
            if change >= item:
                change = change - item
                if item == 10:
                    count_10 += 1
                elif item == 5:
                    count_5 +=1
                elif item == 2:
                    count_2 += 1
                if item == 1:
                    count_1 +=1
    if count_10 != 0: change_dic['10'] = count_10
    if count_5 !=0 : change_dic['5'] = count_5
    if count_2 !=0 : change_dic['2'] = count_2
    if count_1 !=0 : change_dic['1'] = count_1
    return change_dic
result = change_calculator(13)
print(result)
        
                    
                    
                    
            
    


    
    