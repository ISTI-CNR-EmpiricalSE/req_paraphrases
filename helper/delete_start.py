import os

# delete start from plain-PROMISE

f1 = open("plain-PROMISE_dirty.txt", "r")
f2 = open("plain-PROMISE_clean.txt", "w")
dirty_line = f1.readline()
while dirty_line:
    # eliminare dai due punti in poi
    index = dirty_line.find(":")
    # controlla che i due punti ci siano davvero
    if index != -1:
        # se dopo i due punti c'è uno spazio superfluo elimina anche quello
        if dirty_line[index+1].isspace():
            index = index +1
        clean_line = dirty_line[index+1:]
    else:
        clean_line = dirty_line
    f2.write(clean_line)
    dirty_line = f1.readline()
f1.close()
f2.close()



