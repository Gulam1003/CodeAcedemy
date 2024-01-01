#sent = input("Enter your text: ")
str = input().strip()
list_str = list(str)
fre = [list_str.count(ele) for ele in list_str]
print(fre)
s_count = dict(zip(list_str,fre))
print(s_count)