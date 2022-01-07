import assembler

tweeted = False
while not tweeted:
    printFact = assembler.returnFact()
    if len(printFact) <= 140:
        print(printFact) # tweeting functionality will happen here
        tweeted = True
    else:
        continue