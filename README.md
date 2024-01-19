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


