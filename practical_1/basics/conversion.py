age = 18
age_str = str(age)
message = "i am"  +  age_str  +  "years old."
print(message)
num_str = "50"
num_int = int(num_str)
print (num_int)
non_num_str = "hello"
try:
    non_num_int = int (non_num_str)
    print(non_num_str)

except ValueError as e:
    print(f"error:{e}")
    