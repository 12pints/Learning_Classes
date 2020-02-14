seatingChart={"David":3, "Fredje":2, "Aad":1, "Melia":2, "DieSlet":3, "Perle":1,"Svi":2}

#for each name, table pair in tjhe seating chart:

for (name,table) in seatingChart.items():
    #print the name and what table that person is on
    print(name," is at table: ", table)

print()

for i in range (1,4):
    print ("the guests at table", i, " are: ", sep="", end=" ")
    for (name, table) in seatingChart.items():
        #if table number is this number (i, iterated)
        if i == table:
            print(name, end=" ")
    print()
