import sys
try:
    #print(var)
    file=open("notafile")
except FileNotFoundError:
    print("such no file")

except NameError:
    print("var not defined")
except:
    print("unkonwn error")

