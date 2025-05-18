# f = open("/home/noman/MyFiles/Machine Learning/Python//funny.txt", "a")
# f.write("\nI Love c++")
# f.close()

f = open("/home/noman/MyFiles/Machine Learning/Python/File//funny.txt", "r")
f_out = open("/home/noman/MyFiles/Machine Learning/Python/File//funny_wc.txt", "w")

for line in f:
    tokens = line.split(' ')
    f_out.write("word count: "+str(len(tokens)) + line)



f.close()
f_out.close()