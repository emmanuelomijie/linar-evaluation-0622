food = 300
transportation = 200
clothing = 3000
cell_phone = 500
pet_food = 500
miscellaneous=1000
health_care=1000
subscription=1000.54
water=200
sum=(food + transportation + clothing + cell_phone + pet_food + miscellaneous + health_care+subscription+water)
avg=sum/10
#line below calc the total
print("Total amount spent is ", str(sum))

#line below calc the average value
print("The mean value is ", str(avg))
allowance = 10000
leftover = allowance - sum

#line below calc the leftover after expenses
print("Your leftover is ", str(leftover))
print("What is your savings")
saving = int(input())
new_saving = saving + leftover