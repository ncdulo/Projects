import sys


if __name__ == '__main__':
    # Very simple argument parsing. I wanted to do it all my own here rather
    # than require something like `click`. I can definitely improve on this.
    # Quick but functional grab of command line arguments. If one doesn't
    # exist, fail entirely.
    try:
        width, length, unit_price = sys.argv[1:]
    except ValueError as e:
        print(f'\n{sys.argv[0]} WIDTH LENGTH UNIT_PRICE\n')
        print('Something went wrong!')
        print(e)
        # Exit status 2: command line usage error. Arguments invalid.
        exit(2)

    try:
        square_feet = float(width) * float(length)
        total_cost = float(unit_price) * square_feet
        total_cost = round(total_cost, 2)
    except ValueError as e:
        print('Something went wrong!')
        print(e)
        print('Please check your arguments, and try again.')
        # Exit status 1: failure, as defined by the (this!) program.
        exit(1)

    print('Cost Estimate')
    print('-------------')
    print(f'  For room sized {width}ft by {length}ft,')
    print(f'  with a total of {square_feet} sq. ft.')
    print(f'  and a price of ${unit_price} per sq. ft.')
    print(f'  The price of tile should be around ${total_cost},')
    print(f'  not including any taxes or other fees.')
