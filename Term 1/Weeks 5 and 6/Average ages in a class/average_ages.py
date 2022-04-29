years = [2000, 2001, 2000, 1999, 2002, 1998, 2001, 2000, 1997, 2001, 2001, 2003]
ages = []

for year in years:
    ages.append(2022 - year)

average_age = sum(ages) / len(ages)
print(average_age)
