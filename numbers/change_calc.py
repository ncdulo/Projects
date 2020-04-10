from decimal import Decimal, InvalidOperation


if __name__ == '__main__':
    try:
        total = Decimal(input('Enter the purchase total: '))
        given = Decimal(input('How much are you paying with? '))
    except InvalidOperation:
        print('Invalid input!')
        exit(2)

    change = given - total

    denominations = {
            'hundreds': 100.0,
            'fifties': 50.0,
            'twenties': 20.0,
            'tens': 10.0,
            'fives': 5.0,
            'ones': 1.0,
            'quarters': 0.25,
            'dimes': 0.10,
            'nickels': 0.05,
            'pennies': 0.01,
        }
    results = {}
    remaining_change = change

    for denomination, value in denominations.items():
        #print(f'{denomination} = ${value}')
        results[denomination] = int(remaining_change / Decimal(value))
        # Determine how much to remove from our change. Multiply the
        # result by the denomination value.
        counted = int(results[denomination] * value)
        remaining_change = remaining_change - counted
        print(counted)

    print('Change Calculator')
    print('-----------------')
    print(f'  For a purchase totalling ${total} and')
    print(f'  the amount given to pay of ${given}, the')
    print(f'  change would be ${change}. Which can be')
    print(f'  broken down as:\n')

    for denomination, number in results.items():
        print(f'   - {number} {denomination}')

    # Loop over results
