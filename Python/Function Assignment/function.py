def calculate_salary(base_salary,bonus_percent=10,deductions=5):
    bonus_amount=base_salary * (bonus_percent / 100)
    deductions_amount=base_salary * (deductions / 100)
    final_salary = base_salary + bonus_amount - deductions_amount
    return final_salary

salary1 = calculate_salary(50000)
print("Salary with default bonus and deductions:", salary1)

salary2 = calculate_salary(50000, 15, 8)
print("Salary with 15% bonus and 8% deductions:", salary2)

salary3 = calculate_salary(base_salary=50000, bonus_percent=20, deductions=10)
print("Salary with 20% bonus and 10% deductions:", salary3)

calculate_salary(50000, bonus_percent=12)




def apply_discount(price,discount_function):
    return discount_function(price)
flat_discount = lambda price: price-50
percentage_discount = lambda price: price * 0.8
original_price = 200
discount_price1 = apply_discount(original_price, flat_discount)
print("Price after $50 flat discount:", discount_price1)
discount_price2 = apply_discount(original_price, percentage_discount)
print("price after 20% discount", discount_price2)





def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print("Fibonacci(10):", fibonacci(10))
print("Fibonacci(15):", fibonacci(15))
print("Fibonacci(20):", fibonacci(20))





products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]
discounted_products = list(
    map(lambda p: {"name": p["name"], "price": p["price"] * 0.9}, products)
)
print("Products after 10% discount:")
for product in discounted_products:
    print(product)

expensive_products = list(
    filter(lambda p: p["price"] > 500, discounted_products)
)
print("\nProducts with price above $500 after discount:")
for product in expensive_products:
    print(product)





products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone", "price": 800},
    {"name": "Tablet", "price": 600},
    {"name": "Monitor", "price": 300}
]

ascending = sorted(products, key=lambda p: p["price"])
print("products stored by price (ascending):")
print(product)

descending = sorted(products, key=lambda p: p["price"], reverse=True)

print("\nproducts sorted by price (descending):")
for product in descending:
    print(product)





import time
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()         
        result = func(*args, **kwargs)   
        end_time = time.time()           
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result                    
    return wrapper
@execution_time
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of 1000 calculated.")
factorial(1000)





def analyze_numbers(numbers):
    squared_numbers = list(map(lambda x: x**2, numbers))
    filtered_numbers = list(filter(lambda x: x > 50, squared_numbers))
    return filtered_numbers
nums=[2,5,8,10,12]
result = analyze_numbers(nums)
print("final result: ",result)




def custom_aggregate(numbers, func):
    result = numbers[0]

    for num in numbers[1:]:   
        result = func(result, num)

    return result   


nums = [2, 3, 4, 5]

sum_result = custom_aggregate(nums, lambda x, y: x + y)
print("sum:", sum_result)

product_result = custom_aggregate(nums, lambda x, y: x * y)
print("product:", product_result)





data = [
    {"name": "Alice", "age": 30, "score": 85},
    {"name": "Bob", "age": 25, "score": 90},
    {"name": "Charlie", "age": 35, "score": 95}
]
names = list(map(lambda person: person["name"], data))
print("Names:", names)
scores = list(map(lambda person: person["score"], data))
average_score = sum(scores) / len(scores)

print("Average Score:", average_score)





def dynamic_function(numbers, operation):
    operations = {
        "add": lambda x, y: x + y,
        "subtract": lambda x, y: x - y,
        "multiply": lambda x, y: x * y,
        "divide": lambda x, y: x / y
    }
    if operation not in operations:
        return "Invalid operation"
    result = numbers[0]
    for num in numbers[1:]:
        result = operations[operation](result, num)

    return result

nums1 = [10, 5, 2]

print("Addition:", dynamic_function(nums1, "add"))
print("Subtraction:", dynamic_function(nums1, "subtract"))
print("Multiplication:", dynamic_function(nums1, "multiply"))
print("Division:", dynamic_function(nums1, "divide"))

nums2 = [100, 20, 5]
print("\nAnother Test (Multiply):", dynamic_function(nums2, "multiply"))