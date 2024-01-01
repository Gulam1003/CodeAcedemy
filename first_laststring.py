str =input("Enter String : ").strip()

if len(str)>=2:
    stri = [str[0:2],str[-2:]]
    final_str = "".join(stri)
    print(final_str)

else:
    print("Empty string")