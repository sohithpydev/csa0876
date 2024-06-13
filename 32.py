common = []
uncommon = []
def common_uncommon(list_1, list_2):
    for i in list_1:
        if i in list_2:
            common.append(i)
        else:
            uncommon.append(i)
    for i in list_2:
        if i not in list_1:
            uncommon.append(i)
    return common, uncommon
list_1 = [1,2,3]
list_2 = [3,4,5]
print(common_uncommon(list_1,list_2))




