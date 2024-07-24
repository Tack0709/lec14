import argparse
from recursive import fibonacci
from recursive import factorial

def main():
    parser = argparse.ArgumentParser(description = 'factorial or fibonacci one number')
    parser.add_argument('arg1', type=int,
                        help='first argment')
    parser.add_argument('arg3', choices=['factorial', 'fibonacci'],
                        help='factorial or fibonacci (default: fibonacci)')
    
    args = parser.parse_args()
    a = args.arg1
    b = args.arg2

    print(a,b)

    print(factorial(5))


if __name__ == '__main__':
    main()