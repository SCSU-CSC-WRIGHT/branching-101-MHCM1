def main():
    """
    The script below includes a function that asks the user five times 
    for a number, adding each input number to the running total before
    printing the result.
    """

    total = 0 # Intializes the total summation
    
    # Prompts user for input number and adds it to the sum for each iteration 
    for i in range(5):
        number = int(input("Enter a number: "))
        total += number

    print("The running total is: ", total)

#Invoking via method
if __name__ == "__main__":
    main()

