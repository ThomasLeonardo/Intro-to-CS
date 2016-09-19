def lowestPayment(balance, annualInterestRate):
    monthInterest = annualInterestRate / 12
    monthValue = 10
    while(True):
        isValid = calculatePayment(monthValue, balance, monthInterest)
        if(isValid):
            print("Lowest payment:", monthValue)
            break
        else:
            monthValue += 10
def calculatePayment(monthValue, balance, monthInterest):
    previousBalance = balance
    for x in range(0, 12):
        unpaidBalance = previousBalance - monthValue
        previousBalance = unpaidBalance + monthInterest * unpaidBalance
    return previousBalance <= 0

lowestPayment(3329, 0.2)