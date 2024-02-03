with open("file.txt","r") as f:
    lines = f.readlines()
with open("new_file.txt","a") as f:
    for line in lines:
        for i in line:
            if i == "*":
                f.write(i.replace("*","&"))
            elif i == "&":
                f.write(i.replace("&","*"))
            else:
                f.write(i)