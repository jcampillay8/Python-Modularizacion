local_val = "magical unicorns"
def square(x):
    return x * x
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"

if __name__ == "__main__":
    print("El archivo esta siendo ejecutado directamente")
else:
    print(". El archivo se llama: ", __name__)


# in the same file, add the following below the User class
print(square(5))
user = User("Anna")
print(user.name)
print(user.say_hello())

print(__name__)

# if __name__ == "__main__":
#     product = Product([args])
#     print(product)
#     print(product.add_tax(0.18))