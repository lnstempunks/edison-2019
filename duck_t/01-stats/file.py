def main():
    f = open("out.txt", "r+")
    fl = f.readlines()
    for i in range(5):
        print(fl[i])
    f.write("My name is Tyler, and I can't wait to teach you guys Python.")
    f.close()

main()
