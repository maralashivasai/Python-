import argparse
ap=argparse.ArgumentParser();
ap.add_argument("-a","--Firstop",required=True,help="firstop")
ap.add_argument("-b","--Secondop",required=True,help="Secondop")

arg=vars(ap.parse_args())
a=int(arg['Firstop'])
b=int(arg['Secondop'])
print("add is ",a+b);

