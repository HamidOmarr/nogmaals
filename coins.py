# name of student: 
# number of student:
# purpose of program: 
# function of program:
# structure of program: 

toPay = int(float(input('Amount to pay: '))* 100) #toPay is een variable dat een input roept dat een getal verwacht
paid = int(float(input('Paid amount: ')) * 100) #Paid is een variable dat een input roept dat een getal verwacht
change = paid - toPay #change is een variable dat de getallen van het variable Paid en toPay naar en som veranderd

if change > 0: #als change groter is dan 0 is de Variable coinValue 500
  coinValue = 500 #Coinvalue = 500 als change groter is dan 0
  
  while change > 0 and coinValue > 0: #terwijl variable change groter is dan 0 en coinValue is groter is dan 0
    nrCoins = change // coinValue #variable nrCoins is change of coinvalue

    if nrCoins > 0: #als nrCoins groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue  , ' Euro!' ) #laat zien hoeveel nrCoins je hebt en je coinValue en dat je moet teruggeven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' Euro did you return? ')) #nrCoinsReturned kun je typen hoeveel je terug hebt gegeven
      change -= nrCoinsReturned * coinValue #het variable change - of is het variable nrCoinsreturned keer coinvalue is het som na de input

# comment on code below: 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #als change groter is dan 0 laat zien deze string dat hieronder is geschreven. Anders laat zien (done)
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')