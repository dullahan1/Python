def arithmetic_arranger(problems, result = False):
  firstAnswer = ""
  operators = ""
  dashlines = ""
  secondAnswer = ""
  sumup = ""
  answer = ""
  sum = ""


  if(len(problems) > 5):
    return "Error: Too many problems."

  for problem in problems:
    
    firstNumber = problem.split(" ")[0]
    operators = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

      
    if not firstNumber.isnumeric() or not secondNumber.isnumeric():
      return "Error: Numbers must only contain digits."

    if (len(firstNumber) > 4 or len(secondNumber) > 4):
      return "Error: Numbers cannot be more than four digits."

    if (operators == '+' or operators == '-'):
      if operators == "+": 
        sum = str(int(firstNumber) + int(secondNumber))
      if operators == "-":
        sum = str(int(firstNumber) - int(secondNumber))
    else: 
      return "Error: Operator must be '+' or '-'."

    length = max(len(firstNumber) , len(secondNumber)) + 2
    fisrtline = str(firstNumber).rjust(length)
    secondline = operators + str(secondNumber.rjust(length - 1))
    sltn = str(sum.rjust(length))
    
   
    dash_line= ""
    for dash in range(length):
      dash_line += "-"

    if problem != problems[-1]: 
      firstAnswer += fisrtline + '    '
      secondAnswer += secondline + '    '
      dashlines += dash_line + '    '
      sumup += sltn + '    '
    else: 
      firstAnswer += fisrtline
      secondAnswer += secondline 
      dashlines += dash_line 
      sumup += sltn  

  if result: 
    arranged_problems = firstAnswer + "\n" + secondAnswer + "\n" + dashlines + "\n" + sumup
  else:
    arranged_problems = firstAnswer + "\n" + secondAnswer + "\n" + dashlines    
  return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))