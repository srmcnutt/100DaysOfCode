from prettytable import PrettyTable
# from rich import print

table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmanader", "Fire"])
table.align = "l"
print(table)