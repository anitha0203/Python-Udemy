#           reading data
open_file = open('temp.txt', 'r')

file_data = open_file.read()

open_file.close()

print(file_data)

#           writing data
open_file = open('temp.txt', 'w')

open_file.write('Anitha')

open_file.close()

open_file = open('temp.txt', 'r')
file_data = open_file.read()
open_file.close()
print(file_data)

