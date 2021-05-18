numbers = [1,3,5]

doubled = [x * 2 for x in numbers]
print(doubled)

# for num in numbers:
#     doubled.append(num * 2)


friends = ["lilly", "leslie", "peter"]
starts_s=[friend for friend in friends if friend.startswith("l")]

# for friend in friends:
#     if friend.startswith("L"):
#         starts_s.append(friend)
print(starts_s)

print ("friends:" , id(friends), "starts_s:", id(starts_s))