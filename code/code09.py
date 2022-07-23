for i in range(1,33):
    if i!=6 and i!=12 and i!=13 and i!=32:
        print("第",i,"回　",(i*4+1892),"年")
    elif i==32:
        print("第",i,"回　",(i*4+1892)+1,"年")