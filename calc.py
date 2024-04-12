def main():

  print("This is a calculator")
  print("choose your operator as a number (1 = add, 2 = minus, 3 = multiply, 4 = divide)")
  opttype = int(input(">"))
  print("You choose")
  if (opttype == 1):
    print("+")
    add()

  if (opttype == 2):
    print("-")
    minus()
  if (opttype == 3):
    print("x")
    multiply()
  if (opttype == 4):
    print("/")
    divide()
def minus():
  x = int(input())
  y = int(input())
  print(x-y)
  
def divide():
  x = int(input())
  y = int(input())
  if y == 0: print("cannot divide by zero")
  else:
    print(x/y)
  
  print("This is calculator")
  
  
def add():
  x = int(input())
  y = int(input())
  print( x+y)

def multiply():
  x = int(input())
  y = int(input())
  print( x*y)
  

if __name__ == "__main__":
  main()

