import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--input1", help="display a square of a given number", type=int)
parser.add_argument("-n1", "--input2", help="display a square of a given number", type=int)

args = parser.parse_args()

x = args.n1
print(x)


# print(args.input1+args.input2)