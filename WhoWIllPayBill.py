friends = ["Eliazbeth", "Irvin", "Loki", "Sam", "Maddie", "Michelle", "Brad", "Penny", "Mabel", "tHe vOiD"]
import random

bill_payer = random.randint(0, 9)

for_whom_the_bill_tolls = friends[bill_payer]
print(f"Who will pay the bill? {for_whom_the_bill_tolls}")
# This code randomly selects a person from the list of friends to pay the bill.