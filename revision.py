# print("hello world\nhello world")

# name="abhi"
# print(len(name))

#PROJECT TIP CALCULATOR
print("WELCOME TO TIP CALCULATOR")
bill=float(input("What was the bill?"))
tip=float(input("how would you like to tip? 10, 12 or 15??"))
people=float(input("how many people are splitting the bill?"))

exact_bill= round((tip + bill)/people , 2)

print(f"each one of you has to pay {exact_bill}")

