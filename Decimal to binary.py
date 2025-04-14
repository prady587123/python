
def decimal_to_binary(decimal):
  if decimal > 1:
    decimal_to_binary(decimal // 2)
  print(decimal % 2, end="")
decimal = int(input("Enter a decimal number to convert: "))
decimal_to_binary(decimal)

