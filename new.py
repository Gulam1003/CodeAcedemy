#Write a Python program to find the list of words that are longer than n from a given list of words.
size = int(input("Enter size of text : "))
lst = ["gualm","ansari","taksis","sarfaraz"]
nw_lst = []
for ele in lst:
    if  len(ele) >size:
        nw_lst.append(ele)

print(nw_lst)

