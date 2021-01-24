text = input("Input a string of integers: ")
text2 = list(text) 					#turn input into list
cipher = int(input("Add with: "))
text3 = []
sum = 0

for i in range(len(text2)):				#iterate through text2
	text2 = list(map(int, text2))			#turn text2 into integer
	text2[i] = text2[i] + cipher			#add every piece with cipher
	sum = sum + text2[i]				#calculate sum
	print(text2[i])
print("Your sum is: ", summe)




