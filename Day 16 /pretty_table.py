from prettytable import PrettyTable
table = PrettyTable()

# methods
table.add_column("Pokemon Name",["Squirtle","Bulbasaur","Charmander"])
table.add_column("Type",["Water","Grass","Fire"])

# atributes
table.align["Pokemon Name"] = "c"
table.align["Type"] = "l"

print(table)