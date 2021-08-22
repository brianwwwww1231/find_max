# down below are the answer that i wrote previously
# def find_max(a_list):
#     if a_list == []:
#         return 0
#     else:
#         a_list.sort(reverse = True)
#         return a_list[0]

def find_max(a_list):
    # 首先我要先檢查清單是不是空的
    if not a_list:
    # 利用 if not 來判斷 -> 如果a_list有東西，pyhton就會回傳True
    # if not Ture == False -> python 就會跳過這個if判斷(代表有東西)並且去執行接下來的比大小
        return 0
    # 在寫上面的答案前，我確實有想過要用for loop
    # 但就是卡在，我抓出來的每個值，要怎麼去跟其他的值做比大小？
    max_num = a_list[0]
    # 厲害的就在這邊，這邊不管3721，先把整個list的第一個數字先存起來
    for num in a_list:
        if num > max_num:
    # 接下來每個人再來跟這個先存起來的max_num做比較
            max_num = num
    # 只要有for loop叫出來的數字(num)比max_num還要大的話，就把他存進去
    return max_num
    # 最後回傳整趟for loop看過最大的數字

print(find_max([1, 2, 3]))
print(find_max([1, -1 , -5]))
print(find_max([]))