starting_letter_inviting = open("./Input/Letters/starting_letter.txt", "r")
names = open("./Input/Names/invited_names.txt", "r").read().splitlines()
file_path = r"D:\Python Projects\100daysofcode\day_24_write_and_open_files\invites\ "


with starting_letter_inviting as letter:
    letter_data = letter.read()
    for name in names:
        file = file_path + f"{name}" + ".txt"
        letter_d = letter_data.replace("[name]", name)
        with open(file, "w") as invite:
            invite.write(letter_d)
            invite.close()




