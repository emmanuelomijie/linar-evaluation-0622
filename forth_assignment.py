print("welcome, this program is built by Emma")
print("this program function a as calculator")
print("how much do you spend on transport")
transport = int(input())
print("how much do you spend on feeding")
feeding = int(input())
print("how much do you spend on miscellaneous")
miscellaneous = int(input())
print("how much do you spend on water")
water = int(input())
print("how much do you spent on subcribtion")
subcribtion = int(input())
expenses = (transport + feeding + miscellaneous + water + subcribtion)
print("opps, you have spent a total of" ,str(expenses) )
print("how much is your allowance")
allowance = int(input())
leftover = allowance - expenses
print("you have", str(leftover))
print("Thanks for using this program for")
print("LINAR INSTITUTION")