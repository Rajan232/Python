# Program to find out cost of entry tickets for the Zoo


child_ticket_cost = 5

adult_ticket_cost = 10

family_ticket_cost = 26

x = int(input("Number of Adults:"))

y = int(input("Number of children: "))

if x % 2 >= 0 and y % 2 >= 0:
    x1 = x//2
    y1 = y//2
    x = x % 2
    y = y % 2

else:
    x1 = 0
    y1 = 0

if x1 == y1:
    z = (x1 + y1)//2
    print("Number of family tickets:", z)
    total = child_ticket_cost * y + adult_ticket_cost * x + family_ticket_cost * z

elif x1 != y1:
    if x1 > y1:
        n = x1 - y1
        x1 = y1
        z = (x1 + y1) // 2
        print("Number of family tickets:", z)
        total = child_ticket_cost * y + adult_ticket_cost * (x + n) + family_ticket_cost * z
        print("Total cost:", total)
    else:
        n = y1 - x1
        y1 = x1
        z = (x1 + y1) // 2
        print("Number of family tickets:", z)
        total = child_ticket_cost * (y + n) + adult_ticket_cost * x + family_ticket_cost * z
        print("Total cost:", total)
