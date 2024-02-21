def arithmetic_arranger(problems, display_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  line1, line2, line3, line4 = "", "", "", ""
  for i, problem in enumerate(problems):
      parts = problem.split()
      num1, operator, num2 = parts[0], parts[1], parts[2]

      if operator not in ['+', '-']:
          return "Error: Operator must be '+' or '-'."
      if not num1.isdigit() or not num2.isdigit():
          return "Error: Numbers must only contain digits."
      if len(num1) > 4 or len(num2) > 4:
          return "Error: Numbers cannot be more than four digits."

      sum_width = max(len(num1), len(num2)) + 2
      top = num1.rjust(sum_width)
      bottom = operator + num2.rjust(sum_width - 1)
      dashes = '-' * sum_width
      if operator == '+':
        result = str(int(num1) + int(num2))
      else:
        result = str(int(num1) - int(num2))
      answer = result.rjust(sum_width)

      if i < len(problems) - 1:
        line1 += top + '    '
        line2 += bottom + '    '
        line3 += dashes + '    '
        line4 += answer + '    '
      else:
        line1 += top
        line2 += bottom
        line3 += dashes
        line4 += answer

  if display_answers:
    arranged_problems = '\n'.join([line1, line2, line3, line4])
  else:
    arranged_problems = '\n'.join([line1, line2, line3])

  return arranged_problems
