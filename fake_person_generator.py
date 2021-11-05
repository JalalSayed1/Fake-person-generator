from faker import Faker

# locale = Localization.
fake = Faker(locale=['it_IT', 'en_US'])


name = fake.name()
address = fake.address()
dob = fake.date_of_birth(minimum_age=16)
#datetime.date(1906, 6, 29)
city = fake.city()
job = fake.job()
color_name = fake.color_name()
text = fake.text()
# we can provide a list of words to customise the output sentence
sentence = fake.sentence(ext_word_list=["IT", "Computing"])

# To generate uniques forenames:
names = [fake.unique.first_name() for _ in range(10)]

print()
print(f"Name: {name}")
print()
print(f"Address: {address}")
print()
print(f"DoB: {dob}")
print()
print(f"City: {city}")
print()
print(f"Job: {job}")
print()
print(f"Fav colour: {color_name}")
print()
print(f"Text: {text}")
print()
print(f"Sentence: {sentence}")
print()
print(f"Unique forenames: {names}")
print()





