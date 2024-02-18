# Homework
## Question 1: What is the sum of the outputs of the generator for limit = 5?
Answer is: 
- C: 8.382332347441762

```
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)

numbers = []
for sqrt_value in generator:
    print(sqrt_value)
    numbers.append(sqrt_value)

sum(numbers)
```

## Question 2: What is the 13th number yielded by the generator?
Answer is: 
- B: 3.605551275463989

```
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 13
generator = square_root_generator(limit)

i = 0
for sqrt_value in generator:
  i += 1
  print(i, ":", sqrt_value)
```

## Question 3: Append the 2 generators. After correctly appending the data, calculate the sum of all ages of people.
Answer is:
- C: 353
```
def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

ages = []
for person in people_1():
  for key, age in person.items():
    if key == "Age":
      ages.append(age) 

def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


for person in people_2():
  for key, age in person.items():
    if key == "Age":
      ages.append(age) 

print(f"Sum of ages: {sum(ages)}")
```

## Question 4: Merge the 2 generators using the ID column. Calculate the sum of ages of all the people loaded as described above.
Answer is:
- B: 266
``` 
import pandas as pd 

def people_1():
    for i in range(1, 6):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 25 + i, "City": "City_A"}

people_1_data = [person for person in people_1()]
df_people_1_data = pd.DataFrame(people_1_data)


def people_2():
    for i in range(3, 9):
        yield {"ID": i, "Name": f"Person_{i}", "Age": 30 + i, "City": "City_B", "Occupation": f"Job_{i}"}


people_2_data = [person for person in people_2()]
df_people_2_data = pd.DataFrame(people_2_data)

merged_df = df_people_2_data.set_index('ID').combine_first(df_people_1_data.set_index('ID')).reset_index()
print(merged_df)
print(sum(merged_df["Age"]))
```