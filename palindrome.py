i=int(raw_input())
temp=i
z=0
while(temp!=0):
	z=z*10+int(temp%10)
	temp=int(temp/10)
if(x==i):
	print("palindrome")
else:
	print("not a palindrome")
