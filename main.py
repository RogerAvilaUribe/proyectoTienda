from models.item import Item

item1 = Item("Leche", "Leche entera", 5000)
item2 = Item("Arroz", "Arroz Diana", 10000)
item3 = Item("Azucar", "Azucar refinada", 3500)

items = [item1, item2, item3]

for item in items:
    print("nombre", item.get_name())
    print("descripción", item.description)
    print("precio", item.get_price()) 
    print("----")

from models.user import User

user1 = User("Roger", "Avila Uribe", "roger@correo.com", "12345")

print("++++")
print("Nombre:", user1.name)
print("Apellidos:", user1.lastName)
print("Correo:", user1.email)
print("Password:", user1.password)

