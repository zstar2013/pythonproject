import os
def printer(filename):
    printername = "\\LENOVO-PC\\HP LaserJet M1005 "
    cmd = "print " + printername + " " + filename
    print("print :"+ cmd)
    if not os.system(cmd):
        print("printing...")
    else:
        print("some error occurs.")
if __name__ == "__main__":
    filename = "G:\\油耗相关\\油耗\\2016年油耗\\油表封面\\集团油耗油表封面.doc"
    printer(filename)