from os import path


def New_file(number):
    number = int(number)*2
    number = str(number)
    new_file = open(number + ".txt", "w")
    new_file.write(number)
    new_file.close
    new_file = open(number + ".txt", "r")
    with open(number + ".txt", "r") as file:
        open_file = file.read()
    return(open_file)


assert New_file(232) == "464"
assert New_file(70) == "140"
assert New_file(2) == "4"

print(path.exists("464.txt"))
print(path.exists("140.txt"))
print(path.exists("4.txt"))





