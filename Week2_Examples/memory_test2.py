import sys

class Dog:
    def __init__(self, name):
        self.name = name


class Cat:
    def __init__(self, name, cousin=None):
        self.name = name
        self.cousin = cousin

bailey = Dog("Bailey")
misty = Cat("Misty", bailey)

print("\nREFERENCE COUNT")
print(f"bailey's reference count: {sys.getrefcount(bailey)-1}")
print(f"misty's reference count: {sys.getrefcount(misty)}-1")

# Note:  These reference counts are increased by 1 over what you might think, because
#       passing the object into the getrefcount function counts as a reference (temporary reference).

del misty

print("\nAFTER DELETION")
print(f"bailey's reference count: {sys.getrefcount(bailey)-1}")
#print(f"misty's reference count: {sys.getrefcount(misty)-1}")
