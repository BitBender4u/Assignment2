def fun():
  for i in range(1,50):
    if i%3==0 :
      print("Fizz")
    elif i%5==0:
      print("Buzz")
    if i%3==0 and i%5==0:
      print("FizzBuzz")
    else:
      print(i)

fun()
