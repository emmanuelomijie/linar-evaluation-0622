# using the if , else, and elif statement.... write a code that will group users into group A B and C 
# if user is single let user knows he or she falls under group A 
# if user is rlationship let user knows he or she falls under group B
# if user is married let user knows he or she falls under group C
print("what is your marital status? ( input single, relationship, married)")
status = str(input())
if status == "single" :
    print(" you are in group A")
elif status == "relationship" :
    print("you are in group B")
else :
     status == "married" 
print("you are in group C")
print("thanks for using my platfrom dating site")