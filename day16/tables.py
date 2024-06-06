from prettytable import PrettyTable

new_table = PrettyTable()

new_table.add_column('Name', ['Alice', 'Matt', 'Kevin'])
new_table.add_column('Position', ['Project Mnager', 'Software Developer', 'CEO'])
new_table.add_column('Experience', [5,7,25])
new_table.add_row(['Ostin','Designer',12])

new_table.align['Experience'] = 'c'
print(new_table)
print(new_table.get_string(fields=["Name"]))
new_table.sortby = 'Experience'
print(new_table)