# Nested class = A class defined within another class
#                   class Outer:
#                       class Inner:

# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevant outside of the outer class
#           Keeps the namespace clean; reduces the possibility of naming conflicts


from employee import Company

company = Company("Krusty Krab")

company.add_employee("Eugene", "Manager")
company.add_employee("Spongebob", "Cook")

print(company.company_name)
for employee in company.list_employees():
    print(employee)