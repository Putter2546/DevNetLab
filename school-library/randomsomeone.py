from faker import Faker
fake = Faker()
print('My name is {}.'.format(fake.name()))
for i in range(10):
    print(fake.name())