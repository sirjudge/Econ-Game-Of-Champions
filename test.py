if __name__ == "__main__":
    f = open('commandList.txt','r')
    for line in f:
        print(line[:-1])
