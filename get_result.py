import os
path = "D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310/save"
dirs = os.listdir(path)
print(len(dirs))
result = open('D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310/result.txt', 'w')
for i in range(1052):
    print("i = ", i)
    txt_pth = "D:/environments/AI_city_reID_py36/AICity-track2-Re-id-csmvl310/save/" + str(dirs[i])
    f = open(txt_pth,'r')
    list_num = []
    for line in f:
        text = line[:-1] + ' '
        list_num.append(text)
#         print(type(line))
    print(len(list_num))
    print(list_num)
    for j in range(len(list_num)):
        result.write(list_num[j])
    result.write("\n")
#     if i == 2:
#         break