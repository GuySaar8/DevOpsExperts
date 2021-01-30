# Q 1&2
try:
    a=1/0
    print(a)
except ZeroDivisionError:
    print ("WTF are you doing?")

# Q 3
# yes, The finally block, if specified,
# will be executed regardless if the try block raises an error or not.
try:
    x=1
finally:
    print("finally")

# Q 4
#
"""
 When an error occurs, or exception as we call it, 
 Python will normally stop and generate an error message.
 in order to make the script running we can handle the error stream.
 except can 'catch' any exception, except syntax error. 
 python do a check of syntax before running the code. 
 that is why the except can catch the syntax error.
"""

# Q 5
"""
 we have less control over the script and may 
 enconter an error that we need to invastage.
 we should be more spesific when we use the except
 block to catch an "error"
 
"""

# Q 6

"""
except IOError:
    IOError Exception. It is an error raised when an input/output operation fails, 
    such as the print statement or the open() function when trying to open a file 
    that does not exist. It is also raised for operating system-related errors
    
    Changed in version 3.3: EnvironmentError, IOError, 
    WindowsError, socket.error, select.error and mmap.error have been 
    merged into OSError, and the constructor may return a subclass.
    
except ZeroDivisionError:
    Raised when the second argument of a division or modulo operation is 
    zero. The associated value is a string indicating the type of the 
    operands and the operation.

"""

# Q 7 & 8 & 9
# write to file
w=open("words.txt",'a')
w.writelines("Guy Saar")
w.close()

# read from file
w=open("words.txt",'r')
In [15]: w.readlines()
Out[15]: ['Guy Saar']


"""
    read file in linux
    guy@Mint-PC:~$ cat words.txt
    Guy Saar
"""

# Q 10
w=open("words.txt",'a')
w.write("משהו בעברית")
w.close()

w=open("words.txt",'r')
In [17]: w.readlines()
Out[17]: ['Guy Saarמשהו בעברית']


# Q 11
"""
 Documentation:
    1.https://pillow.readthedocs.io/en/3.0.x/installation.html
    2. https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html#more-on-reading-images
"""
pip3 install pillow

from PIL import Image
image1 = Image.open('DSC00004.jpg')
image1.save('test.png')

size300 = (300,300)
image1 = Image.open('DSC00004.jpg')
image1.thumbnail(size300)
image1.save('test2.jpg')

image1 = Image.open('test2.jpg')
image1.rotate(90).save('test2_90.jpg')
image1.convert(mode='L').save('test2_b&w.jpg')
