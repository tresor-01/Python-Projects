import time 
# still have problem in guessing and more vowels than five 
# stilll also no able to detect space 
password = input("Enter the password :")

start= time.time()
chars = 'abcdefghijklmnopqrstuvwxyz'
guess= []
for val in range(len(password)):
  a = [i for i in chars]
  for y in range(val):
    a = [x + i for i in chars for x in a]
  guess = guess +a
  if password in guess:
    break
end = time.time()
clock = str(end-start)

print("Your password is :" +password)
print("time taken :" + clock)