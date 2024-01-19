 #  Computer Vision Bootcamp

## Variable Types and Functional Programming: 
### Task 1: 
 **📑 Code Explanation**
```python
sales_amounts = [1500, 2200, 1800, 2000, 2500, 2100, 1900]
```
 Example list

 ```python
total_sales = sum(sales_amounts)
```
Calculate total  sales

 ```python
average_sales = total_sales / len(sales_amounts)

```
Calculate average sales


 ```python
print("total sales:", total_sales)
print("average sales:", average_sales)
```
Print

**📊 Out Put**

![image](https://github.com/batooldshilleh/ComputerVisionBootcamp/assets/93814390/39544911-aa3f-476a-96c2-ed4485fe479f)

### Task 2: 
 **📑 Code Explanation**
```python
def calculate_discounted_total(basket, discount_percentage=10):
    total_cost = sum(basket.get(product, 0) for product in basket)

    discount_amount = (discount_percentage / 100) * total_cost

    discounted_total = total_cost - discount_amount

    return discounted_total
```

function for Calculate  discounted total , with two argumant 

 ```python
oducts_prices = {
    'apple': 2.50,
    'banana': 1.50,
    'orange': 3.00,
    'grapes': 4.50,
}

basket = {
    'apple': 3,
    'banana': 2,
    'grapes': 1,
}

```
 Example list

 ```python
discounted_total = calculate_discounted_total(basket)

```
Calculate total discounted 


 ```python
print("discounted total:", discounted_total)
```
Print

**📊 Out Put**

![image](https://github.com/batooldshilleh/ComputerVisionBootcamp/assets/93814390/c9afb545-5eca-4fd4-8291-89f5975f7f92)

## Object-Oriented Programming (OOP): 
### Task 3: 
 **📑 Code Explanation**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity
```
 Create class with three Argumants name , price ,quantity
 and function (method) for calculate price

 ```python
apple = Product(name='Apple', price=2.50, quantity=5)
```
Create instance

 ```python
print("Product Name:", apple.name)
print("Price per unit:", apple.price)
print("Quantity:", apple.quantity)
print("Total Price:", apple.calculate_total_price())
```
Print and use instance

**📊 Out Put**

![image](https://github.com/batooldshilleh/ComputerVisionBootcamp/assets/93814390/b163a4b0-c292-4954-bfcd-f2615bee757d)

### Task 4: 
 **📑 Code Explanation**
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def calculate_total_cost(self, quantity):
        return self.price * quantity
```
 Create class with three Argumants name , price ,quantity
 and two functions (methods) 
 * first one for calculate price
 * second one for calculate cost

 ```python
apple = Product(name='Apple', price=2.50, quantity=5)
```
Create instance

 ```python
print("Product Name:", apple.name)
print("Price per unit:", apple.price)
print("Quantity:", apple.quantity)
print("Total Price:", apple.calculate_total_price())
```
Print and use instance

 ```python
desired_quantity = 10
total_cost = apple.calculate_total_cost(desired_quantity)
print(f"Total Cost for {desired_quantity} units:", total_cost)
```
Calculate the total cost for a specific quantit

**📊 Out Put**

![image](https://github.com/batooldshilleh/ComputerVisionBootcamp/assets/93814390/ee7cc141-ecaf-4445-b57f-62221347d2b1)


## Linear Algebra: 
### Task 5: 
 **📑 Code Explanation**
```python
def multiply_matrices(mat1, mat2):
    result = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]
    
    return result
```
function to multiply two matrices

 ```python
def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
```
function to find the determinant of a 2x2 matrix

 ```python
def determinant_3x3(matrix):
    det = 0
    for i in range(3):
        det += matrix[0][i] * determinant_2x2([[matrix[1][(i+1)%3], matrix[1][(i+2)%3]],
                                                 [matrix[2][(i+1)%3], matrix[2][(i+2)%3]]])
    return det
```
 function to calculate the determinant of a 3x3 matrix

  ```python
def inverse_3x3(matrix):
    det = determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is singular, cannot find inverse.")
    
    adjugate = [[0] * 3 for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            cofactor = determinant_2x2([[matrix[(i+1)%3][(j+1)%3], matrix[(i+1)%3][(j+2)%3]],
                                         [matrix[(i+2)%3][(j+1)%3], matrix[(i+2)%3][(j+2)%3]]])
            adjugate[j][i] = ((-1) ** (i + j)) * cofactor
    
    inverse = [[element / det for element in row] for row in adjugate]
    
    return inverse
```
function to calculate the inverse of a 3x3 matrix
 ```python
mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result_product = multiply_matrices(mat1, mat2)
print("Matrix Product:")
for row in result_product:
    print(row)

result_det_2x2 = determinant_2x2([[4, 3], [2, 1]])
print("\nDeterminant of 2x2 Matrix:", result_det_2x2)

result_det_3x3 = determinant_3x3([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print("\nDeterminant of 3x3 Matrix:", result_det_3x3)

result_inverse_3x3 = inverse_3x3([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
print("\nInverse of 3x3 Matrix:")
for row in result_inverse_3x3:
    print(row)

```
Example usage

**📊 Out Put**

![image](https://github.com/batooldshilleh/ComputerVisionBootcamp/assets/93814390/215f6662-0f0f-447f-a2c5-548ce6b1e112)


