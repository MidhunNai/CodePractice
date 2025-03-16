# 1. Given an string print reverse of that string
name = "Midhun Nair"
revString = "".join(reversed(name))
print(revString)
# 2. Reverse the only word order
revString = " ".join(reversed(name.split()))
print(revString)
