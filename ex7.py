print "Mary had a little lamb."             #printer ut setningen
print "Its fleece was white as %s." % 'snow'#printer ut setningen med % som er definert som "snow"
print "And everwhere that Mary went."       #printer ut setningen
print "." *10 # what'd that do?             #printer ut 10 stk av punktum

end1 = "C"                                  #definerer variabler end1-12 med bokstaver
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r" 
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,        #printer ut end1-6 som er 6 bokstaver som blir "Cheese". kommaet skiller slik at raden fortsetter paa neste print og dermed blir det ikke linjeskift
print end7 + end8 + end9 + end10 + end11 + end12        #printer ut de resterende end7-12 som blir "Burger"
