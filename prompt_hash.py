import hashlib
# list the available algorithms for this program
print ('md5 + sha256')

user_input = input("Enter md5 or sha256:     ")

if user_input =='md5':
    user_input2 = input("Enter md5 you want to hash:     ")
    md5_input = hashlib.md5(user_input.encode())
    print (str(md5_input.hexdigest()))
elif user_input =='sha256':
    user_input3 = input("Enter sha256 you want to hash:     ")
    sha256_input = hashlib.sha256(user_input.encode())
    print(str(sha256_input.hexdigest()))
# else:
  #  print ('Please enter "md5" or "sha256"')