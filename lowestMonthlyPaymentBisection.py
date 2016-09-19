def lowestPayment(balance, annualInterestRate):
    monthInterest = annualInterestRate / 12
    lowerBound = balance / 12
    upperBound = balance * (1 + monthInterest) ** 12 / 12
    guess = (lowerBound + upperBound) / 2
    while(True):
        previousBalance = balance
        for x in range(0, 12):
            unpaidBalance = previousBalance - guess
            previousBalance = unpaidBalance + monthInterest * unpaidBalance
        last_guess = guess
        if(previousBalance < 1 and previousBalance > -1):
            print("Lowest payment:", round(guess, 2))
            break
        elif(previousBalance > 0):
            guess = (guess + upperBound) / 2
            lowerBound = last_guess
        else:
            guess = (guess + lowerBound) / 2
            upperBound = last_guess
lowestPayment(320000, 0.2)