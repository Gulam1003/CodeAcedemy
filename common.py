
def comparingg_fun(lst1, lst2):
    found_common_word = False
    for i in lst1:
        for j in lst2:
            if i==j:

                print("True")
                found_common_word=True
                break

    if not found_common_word:
                print("Found no common word")





list1 = ["gulam", "ansari"]
list2 = ["taksis", "ansari"]

comparingg_fun(list2, list1)
