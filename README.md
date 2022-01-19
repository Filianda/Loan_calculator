# Loan_calculator
This task is from JetBrains Academy course

Let's think about what a loan calculator should be able to do. In general, it takes several parameters like a loan principal and interest, calculates the values the user wants to know (for example, monthly payment or overpayment), and outputs them to the user.

## Stage 1:
### Objectives
Let's start by imitating this behavior. There are some prepared variables in the source code: these are text messages that our loan calculator can output. In this stage, all you need to do is output them in the right order.
### Example
Output:
Loan principal: 1000
Month 1: repaid 250
Month 2: repaid 250
Month 3: repaid 500
The loan has been repaid!

## Stage 2:
### Description
If you found the previous stage too easy, let's add something interesting. The best loans are probably those with a 0% interest.
Let's make some calculations for 0% loan repayments. The user might know the period of the loan and want to calculate the monthly payment. Or the user might know the amount of the monthly repayments and wonder how many months it will take to repay the loan in full.
In this stage, we need to ask the user to input the loan principal amount. Then, the user should indicate what needs to be calculated (the monthly payment amount or the number of months) and enter the required parameter. After that, the loan calculator should output the value that the user wants to know.
Also, let’s assume we don't care about decimal places. If you get a floating-point expression as a result of the calculation, you’ll have to do additional actions. Take a look at Example 4 where you need to calculate the monthly payment. You know that the loan principal is 1000 and want to pay it back in 9 months. The real value of payment can be calculated as:
payment = \dfrac{principal}{months}=\dfrac{1000}{9} =111.11...
Of course, you can’t pay that amount of money. You have to round up this value and make it 112. Remember that no payment can be more than the fixed monthly payment. If your monthly repayment amount is 111, that would make the last payment 112, which is not acceptable. If you make a monthly payment of 112, the last payment will be 104, which is fine. You can calculate the last payment as follows:
lastpayment =principal -(periods-1)*payment = 1000 - 8*112=104
In this stage, you need to count the number of months or the monthly payment. If the last payment differs from the rest, the program should display the monthly payment and the last payment.

### Objectives
The behavior of your program should look like this:
Prompt a user to enter their loan principal and choose which of the two parameters they want to calculate – the number of monthly payments or the monthly payment amount.
To perform further calculations, you'll also have to ask for the required missing value.
Finally, output the results for the user.

### Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

#### Example 1

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:
> m
Enter the monthly payment:
> 150

It will take 7 months to repay the loan
#### Example 2

Enter the loan principal:
> 1000
What do you want to calculate? 
type "m" for number of monthly payments,
type "p" for the monthly payment:
> m
Enter the monthly payment:
> 1000

It will take 1 month to repay the loan
#### Example 3

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment:
> p
Enter the number of months:
> 10

Your monthly payment = 100
#### Example 4

Enter the loan principal:
> 1000
What do you want to calculate?
type "m" for number of monthly payments,
type "p" for the monthly payment
> p
Enter the number of months:
> 9

Your monthly payment = 112 and the last payment = 104.

## Stage 3

### Description
Let's compute all the parameters of the loan. There are at least two kinds of loan: those with annuity payment and those with differentiated payment. In this stage, you are going to calculate only the annuity payment which is fixed during the whole loan term.

Here is the formula:
A_{ordinary\_annuity} = P * \dfrac{i * (1+i)^n}{(1+i)^n-1}A 
ordinary_annuity
 =P∗ (1+i) n  −1 i∗(1+i) n
Where:
AA = annuity payment;
PP = loan principal;
ii = nominal (monthly) interest rate. Usually, it’s 1/12 of the annual interest rate, and usually, it’s a floating value, not a percentage. For example, if your annual interest rate = 12%, then i = 0.01;
nn = number of payments. This is usually the number of months in which repayments will be made.
You are interested in four values: the number of monthly payments required to repay the loan, the monthly payment amount, the loan principal, and the loan interest. Each of these values can be calculated if others are known:
Loan principal:
P = \dfrac{A}{\left( \dfrac{i * (1+i)^n}{(1+i)^n-1} \right)}P= ( (1+i) n −1i∗(1+i) n )A

The number of payments:
n = \log_{1+i} \left( \dfrac{A}{A - i*P} \right)n=log 1+i( A−i∗PA)

### Objectives
In this stage, you should add new behavior to the calculator:
First, you should ask the user which parameter they want to calculate. The calculator should be able to calculate the number of monthly payments, the monthly payment amount, and the loan principal.
Then, you need to ask them to input the remaining values.
Finally, compute and output the value that they wanted.
Note that the user inputs the interest rate as a percentage, for example, 11.7, so you should divide this value by 100 to use it in the formula above.
Please be careful converting "X months" to "Y years and Z months". Avoid writing "0 years and 11 months" (output "11 months" instead) and "1 years and 0 months" (output "1 year" instead).
Note that in this stage, you have to ask the user to input parameters in a specific order which is provided below. Simply skip the value the user wants to calculate:
The first is the loan principal.
The second is the monthly payment.
The next is the number of monthly payments.
The last is the loan interest.
Examples
The greater-than symbol followed by a space (> ) represents the user input. Note that this is not part of the input.

#### Example 1
What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> n
Enter the loan principal:
> 1000000
Enter the monthly payment:
> 15000
Enter the loan interest:
> 10
It will take 8 years and 2 months to repay this loan!
Let’s take a closer look at Example 1.
You know the loan principal, the loan interest and want to calculate the number of monthly payments. What do you do?
1) You need to know the nominal interest rate. It is calculated like this:
i = \dfrac{10\%}{12 * 100\%} = 0.008333...i= 12∗100% 10% =0.008333...
2) Now you can calculate the number of months:
n = \log_{1 + 0.008333...} \left( \dfrac{15000}{15000-0.008333... * 1000000} \right) = 97.71...n=log 1+0.008333...( 15000−0.008333...∗1000000 15000 )=97.71...
3) You need an integer number, so let’s round it up. Notice that the user will pay the same amount every month for 97 months, and in the 98th month the user will pay 0.71... of the monthly payment. So, there are 98 months to pay.
n = 98n=98
4) Finally, you need to convert “98 months” to “8 years and 2 months” so that it is more readable and understandable for the user.

#### Example 2

What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> a
Enter the loan principal:
> 1000000
Enter the number of periods:
> 60
Enter the loan interest:
> 10
Your monthly payment = 21248!
#### Example 3

What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
> p
Enter the annuity payment:
> 8721.8
Enter the number of periods:
> 120
Enter the loan interest:
> 5.6
Your loan principal = 800000!

