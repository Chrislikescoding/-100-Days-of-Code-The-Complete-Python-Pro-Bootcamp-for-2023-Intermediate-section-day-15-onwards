# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from prettytable import PrettyTable

table=PrettyTable()
table.field_names= ["Pokemon name", "Type"]
table.add_rows(
    [
    ["Pikachu  ","Electric"],
    ["Squirtle ","Water  "],
    ["Charmander","Fire   "],
  ]
)
table.align='l'
print(table)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
