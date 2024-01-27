digits="234"
phone_map={'2':'abc','3':'def','4':'ghi','5':"jkl",'6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
if digits=="":
    print("[]")
charOfNumber=list(phone_map[digits[0]])
for i in digits[1:]:
    charOfNumber=[old+new for old in charOfNumber for new in list(phone_map[i])]
  
print(charOfNumber)