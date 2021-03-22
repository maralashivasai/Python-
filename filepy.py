file=open("D:\python\sample.txt",'w')

file.write("Hello world");
file.close()


with open("D:\python\sample.txt",'w+')as f:
    for line in f:
        print(line)

    f.writelines(["hello\n","hiii\n","heyy\n"])
