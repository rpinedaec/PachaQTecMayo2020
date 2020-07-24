from peewee import *
from datetime import date

#db = SqliteDatabase('people.db')
db = MySQLDatabase('peewee_test', user='root', password='pachaqtec',
                         host='localhost', port=3306)

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" databa


db.connect()
#db.create_tables([Person, Pet])
# uncle_bob = Person(name='Bob', birthday=date(1983, 8, 28), is_relative=True)
# uncle_bob.save()
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# grandma.save()
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
# herb.save()

# grandma = Person.select().where(Person.name == 'Grandma').get()

# print(grandma.name)

# grandma.name = "Anita"
# grandma.save()
# grandma = Person.select().where(Person.name == 'Anita').get()
# print(grandma.name)

# bob_kitty = Pet.create(owner=grandma, name='Kitty', animal_type='cat')

tio_herb = Person.select().where(Person.name == 'Herb').get()

print(tio_herb.name)

# fido_pet = Pet.create(owner = tio_herb, name = "rufo", animal_type = "perro")

fido = Pet.select().where(Pet.name=='rufo').get()

fido.delete_instance()


