import re
def arithmetic_arranger(problems, statprint = False):
  first = ''
  second = ''
  sumx = ''
  lines = ''
  string = ''

  if (len(problems) > 5):
    return "Error: Too many problems."

  #split to get numbers and - or +
  for problem in problems:
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return ("Error: Operator must be '+' or '-'.")
      return ("Error: Numbers must only contain digits.")
    
  #split it into numbers and operator
  
    firstnum = problem.split(" ")[0]
    secondnum = problem.split(" ")[2]
    operator = problem.split(" ")[1]
    
    if (len(firstnum) >=5 or len(secondnum) >=5) :
      return ("Error: Numbers cannot be more than four digits.")

    sum = ""
    if (operator == "+"):
      sum = str(int(firstnum) + int(secondnum))
    elif (operator == "-"):
      sum = str(int(firstnum) - int(secondnum))


  #Set length of sum and top and bottom and line values
    length = max(len(firstnum), len(secondnum)) +2
    top = str(firstnum).rjust(length)
    bottom = operator + str(secondnum).rjust(length - 1)
    line = ''
    res = str(sum).rjust(length)
    for s in range(length):
      line += '-'

    if problem != problems[-1]:
      first += top + '    '
      second += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      second += bottom
      lines += line
      sumx += res
  
  if statprint:
    string = first + '\n' + second + '\n' + lines + '\n' + sumx
  else:
    string = first + '\n' + second + '\n' + lines
  return string
