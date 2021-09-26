joinedfile = open("users.txt", "r")
joinedUsers = set()
for line in joinedfile:
    joinedUsers.add(line.strip())
joinedfile.close()

