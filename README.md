1. Introduction:
     The Stock Portfolio Tracker is a Python-based project that helps users calculate the total value of their stock investments. It allows users to enter stock names and quantities to find their total investment amount.
   
2. Project Objective:
    1.The main objectives of this project are:
    2. To develop a stock investment calculator using Python.
    3. To allow users to enter stock names and quantities.
    4. To store stock prices using Python dictionaries.
    5. To calculate the total investment value automatically.
    6. To display the investment details clearly.
    7. To optionally save investment results in a TXT or CSV file.
       
3. Working Process:
     1. First, the program stores stock names and their prices in a Python dictionary.
     2. The user enters the stock name.
     3. The user enters the quantity of stocks.
     4. The program checks the stock price from the dictionary.
     5. It multiplies the stock price by the quantity.
     6. Finally, it displays the total investment value.
        
 4. Algorithm:
   Step 1: Start the program.
   Step 2: Create a dictionary containing stock names and prices.
   Step 3: Initialize an empty portfolio and total investment as zero.
   Step 4: Display all available stocks.
   Step 5: Get the stock name from the user.
   Step 6: If the user enters "done", stop accepting inputs.
   Step 7: Otherwise, check whether the stock exists in the dictionary.
   Step 8: If valid, get the quantity and calculate the investment value.
   Step 9: Add the investment value to the total investment.
   Step 10: Display the portfolio and total investment.
   Step 11: Save the portfolio details in "portfolio.txt".
   Step 12: Stop the program.

5. Sample output:
===== STOCK PORTFOLIO TRACKER =====
Available Stocks:
AAPL : $ 180
TSLA : $ 250
GOOGL : $ 140
MSFT : $ 400
AMZN : $ 190
Enter stock name: AAPL
Enter quantity: 2
Stock added successfully!
Investment value: $ 360
Enter stock name: TSLA
Enter quantity: 3
Stock added successfully!
Investment value: $ 750
Enter stock name: done
===== YOUR STOCK PORTFOLIO =====
AAPL | Quantity: 2 | Value: $ 360
TSLA | Quantity: 3 | Value: $ 750
Total Investment: $ 1110
Portfolio saved successfully in portfolio.txt

6. Advantages:
     1. Easy to use.
     2. Calculates investment automatically.
     3. Supports multiple stocks.
     4. Saves investment details optionally.
     5. Helps beginners understand Python programming.
        
7. Limitations:
     1. Stock prices are predefined manually.
     2. It does not fetch live stock market prices.
     3. It does not provide real-time market updates.
     4. The calculated investment value depends on the prices stored in the dictionary.
        
8. Mathematical Formula:
Individual Investment Value
Investment Value = Stock Price × Quantity
Total Investment Value
Total Investment = Sum of All Individual Investment Values

Example Calculation:
AAPL:
180 × 2 = $360

TSLA:
250 × 3 = $750

Total Investment:

$360 + $750 = $1,110
        
9. Future Enhancements:
     1. The project can be improved by adding:
     2. Live stock market price integration.
     3.A graphical user interface (GUI).
     4. Portfolio performance tracking.
     5. Profit and loss calculation.
     6. Database storage for investment records.
        
10. Conclusion:
     The Stock Portfolio Tracker project demonstrates the practical use of Python dictionaries, user input, arithmetic operations, and file handling. This project improves programming and problem-solving skills.
