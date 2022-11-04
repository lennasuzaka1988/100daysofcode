from prettytable.colortable import ColorTable, Themes
from prettytable import MSWORD_FRIENDLY

table = ColorTable(theme=Themes.OCEAN)
table.field_names = ["Pokemon", "Type"]
table.add_row(["Pikachu", "Lightning"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Squirtle", "Water"])
table.align["Pokemon"] = "l"
table.align["Type"] = "l"
# table.set_style(MSWORD_FRIENDLY)

table.vertical_char = "¥"
table.horizontal_char = "•"
print(table.get_string(sortby="Type"))
