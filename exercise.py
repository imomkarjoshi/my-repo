# def fizzBuzz(input):
#     if(input % 15 == 0):
#         return "FizzBuzz"

#     if(input % 5 == 0):
#         return "Buzz"

#     if(input % 3 == 0):
#         return "Fizz"

#     return input

sentence = "This is a common interview question"

occurance = {}
for x in sentence:
    if x in occurance:
        occurance[x] += 1
    else:
        occurance[x] = 1
max_val = 0
for x in occurance:
    max_val = max(max_val, occurance[x])


print(max_val)
