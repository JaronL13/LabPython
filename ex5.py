# Bytter ut alt med mine egne maal
my_name = 'Jaron Larsen'
my_age = 27
my_height = 176 # cm
my_weight = 90 # kg 
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d centimeters tall." % my_height
print "He's %d kilos heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, tro to get it exactly right
print " If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
