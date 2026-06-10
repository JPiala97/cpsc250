import sys


class Dog:
    def __init__(self, name, cousin=None):
        self.name = name
        self.cousin = cousin


class Cat:
    def __init__(self, name, cousin=None):
        self.name = name
        self.cousin = cousin


bailey = Dog("Bailey")  # create bailey, with no cousins
misty = Cat("Misty", bailey)  # create misty, assign bailey as her cousin
bailey.cousin = misty  # assign misty as bailey's cousin

print("\nREFERENCE COUNT after creation of bailey and misty")
print(f"bailey's reference count: {sys.getrefcount(bailey)-1}")
print(f"misty's reference count: {sys.getrefcount(misty)-1}")

del bailey

print("\nREFERENCE COUNT after deletion of bailey")
print(f"misty's reference count: {sys.getrefcount(misty)-1}")

print("Eeek!  Memory Leak!!! Bailey has been deleted, but Misty still references it!!!")

misty.cousin = None

print("\nREFERENCE COUNT after deletion of bailey by hand")
print(f"misty's reference count: {sys.getrefcount(misty)-1}")

del misty
