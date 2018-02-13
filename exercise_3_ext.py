import argparse
import json

parser =argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-r','--read',help='name of file to read data from', action='store_true', dest='readFile')
group.add_argument('-w','--write',help='name of output file when generating json', action='store_true', dest='writeFile')
parser.add_argument("filename", help="filename")

args = parser.parse_args()

if args.readFile:
    with open(args.filename) as f:
        numbers = json.load(f)
    user_input = int(input("Please enter number: "))
    print([x for x in numbers if x < user_input])

else:
    print("enter numbers (q to end):")
    numbers = []
    while True:
        user_input = input("")
        if user_input == 'q':
            break
        else:
            try:
                number = int(user_input)
            except ValueError:
                print("Not a number!")
                continue
            else:
                numbers.append(number)
    with open(args.filename, 'w+') as f:
        json.dump(numbers, f)