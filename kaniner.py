import random as rnd
 
class Kaniner:
  def __init__(self, sex, age):
    self.sex = sex
    self.age = age

kaniner_list = []
kön = ["Kvinna", "Man"]

for i in range(5):
    sex = rnd.choice(kön)
    age = rnd.randint(1,10)
    k = Kaniner(sex, age)
    kaniner_list.append(k)

i = 0
for year in range(10):
    for kanin in kaniner_list:
        print(f"Year:{year}: Sex: {kanin.sex}, Age: {kanin.age}")
        
        while i < len(kaniner_list):
            kanin = kaniner_list[i]
            kanin.age += 1

            if kanin.age > 10:
                kaniner_list.pop(i)
            else:
                i += 1

    if any(kanin.sex == "Man" for kanin in kaniner_list):
        for kanin in kaniner_list:
            if kanin.sex == "Kvinna" and kanin.age > 2:
                sex = rnd.choice(kön)
                age = rnd.randint(1, 10)
                k = Kaniner(sex, age)
                kaniner_list.append(k)

