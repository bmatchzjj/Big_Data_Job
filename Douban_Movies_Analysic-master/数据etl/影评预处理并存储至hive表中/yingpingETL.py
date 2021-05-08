#-*-coding:utf-8-*-

# fp_w = open("new_5045678.txt", "a", encoding="utf-8")
# with open("5045678 .txt", "r", encoding="utf-8") as fp:
#     for line in fp.readlines():
#         line_list = line.split("\t")
#         if len(line_list)==6:
#             fp_w.write(line)
#         else:
#             print(line)
#
# fp_w.close()
# print("OK !")
fp_w = open("new_1291858.txt", "a", encoding="utf-8")
with open("1291858 .txt", "r", encoding="utf-8") as fp:
    for line in fp.readlines():
        line_list = line.split("\t")
        if len(line_list)==6:
            fp_w.write(line)
        else:
            print(line)

fp_w.close()
print("OK !")
