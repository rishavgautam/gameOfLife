import argparse
parser = argparse.ArgumentParser(description="Parse bool")
parser.add_argument("--do-something", default=False, action="store_true",
                    help="Flag to do something")
args = parser.parse_args()

if args.do_something:
     print("Do something")
else:
     print("Don't do something")

print(f"Check that args.do_something={args.do_something} is always a bool.")