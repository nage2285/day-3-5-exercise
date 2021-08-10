# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Love calculator

#name1 = str(["a-z"]*26)

#name2 = str(["a-z"]*26)

combined_string = name1 + name2 

#print(type(combined_string))

combined_string_lower = combined_string.lower() 
#combined_string_count = combined_string_lower.count()

#true = "TRUE".lower()
#love = "LOVE".lower()


#love_score = combined_string_lower
#print(type(love_score))

lv = combined_string_lower.count('t')
lv1 = combined_string_lower.count('r')
lv2 = combined_string_lower.count('u')
lv3 = combined_string_lower.count('e')
lv4 = combined_string_lower.count('l')
lv5 = combined_string_lower.count('o')
lv6 = combined_string_lower.count('v')
lv7 = combined_string_lower.count('e')

#print(type(lv))
count = lv + lv1 + lv2 + lv3
count2 = lv4 + lv5 + lv6 + lv7

#print(type(count))


count_final = (10*count + count2)

#count_int = int(count_final)

#ruelove') and 'true'.count('truelove') and 'love'.count('truelove')
#lv = lvc + lvc1 + lvc2 

if (count_final <= 10) or (count_final >= 90) :
  print(f"Your score is {count_final}, you go together like coke and mentos.")
elif (count_final >= 40) and (count_final <= 50) :
  print (f"Your score is {count_final}, you are alright together.")
else :
  print (f"Your score is {count_final}")   



