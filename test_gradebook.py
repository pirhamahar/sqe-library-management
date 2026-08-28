from src.gradebook.gradebook import Gradebook

gradebook = Gradebook()

assert gradebook.add_student("Ali", 101) is True
assert gradebook.add_student("Ahmed", 101) is False

print("Duplicate roll number test passed.")
