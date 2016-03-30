#calculate money saved when purchasing things at discount.

#get amount of purchase in form of float write to variable
total = input("How much did you pay? (i.e.37.25):$ ")
sale = input("What percent was the sale? (i.e 40): ")

#I'm not positve a this is the best way to do this but 
#100% sale == 5 finger discount
if total == 0.0 or sale == 100: 
    raw_input("STOP RIGHT THERE, CRIMINAL SCUM!!!")
    exit()
else:
    paid_percent = 100.0 - sale
    fullprice = round(total * 100 / paid_percent, 2)
    savings = round(fullprice - total, 2)

#let user know what (she|he) saved
print "If you paid $%r at %r percent off, you saved $%r.  You would have paid $%r at fullprice" % (total, sale, savings, fullprice)

#say nice things based on the sale
if sale >= 50.0: 
    print "Wow! that was a pretty good sale!"
elif sale <= 20.0:
    print "Every little bit helps."
else:
    print "Cool beans. Cool beans." 
