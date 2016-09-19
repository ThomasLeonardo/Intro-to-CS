def minimumPaymentBalance(balance, annualInterestRate, monthlyPaymentRate):
    """
    Takes credit card balance, annual interest rate, and mimimum monthly payment rate,
    then prints credit card balance each month for one year,
    provided whoever is responsible for it only pays the minimum required
    """    
    
    monthlyInterestRate = annualInterestRate / 12 #interest rate each month
    previousBalance = balance #current balance
    for month in range(1, 13): #one year
        minimumMonthlyPayment = monthlyPaymentRate * previousBalance #minimum payment required
        monthlyUnpaidBalance = previousBalance - minimumMonthlyPayment #debt before interest on unpaid amount
        previousBalance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance #debt after monthly interest
        print("Month", month, "Remaining balance:", round(previousBalance, 2)) #prints remaining balance rounded to two decimal places
        