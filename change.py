#Title: Project3-c
print("Please enter an amount in cents less than a dollar.")
cents = int(input( ))
q = cents//25
cents -= (q*25)
d = cents // 10
cents -= (d * 10)
n = cents // 5
cents -= (n * 5)
p = cents // 1
print("Your change will be:")
print("Q:",str(q))
print("D:",str(d))
print("N:",str(n))
print("P:",str(p))





