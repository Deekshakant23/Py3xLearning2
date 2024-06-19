# lambda function
# Lambda Expression
# to do the task the in one line.

def double_salary(salary):
    return salary * 2


new_salary = double_salary(100000)
print(new_salary)


# another way to write the same code for (print double salary)
def double_salary(s1):
    return s1 * 2


result = double_salary(s1=100000)
print(result)

# by lambda expression

double_salary_function = lambda salary: salary * 2
print(double_salary_function(2000))
