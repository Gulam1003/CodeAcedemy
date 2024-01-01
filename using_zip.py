import  time

strt = time.time()

sentence_length = 4
sentences = []
for i in range(4):
    sentence = input("Enter you sentence").lower()
    sentences.append(sentence)

sentence_list = "".join(sentences)
char_list = list(sentence_list)
cnt = [char_list.count(cha) for cha in char_list ]
char_dict = dict(zip(char_list,cnt))
print(char_dict)

"""/*result = {}

for let in sentence_list :
    result[let] = result.get(let,0) + 1

print (result)
"""




end = time.time()

elap = end - strt

print(elap)