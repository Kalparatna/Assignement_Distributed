

## Overview
This program simulates a distributed system where different types of data (Users, Orders, Products) are stored in separate SQLite databases. The program performs concurrent insert operations into these databases using Python's threading module.

## Features
- **Simulated Distribution:** Separate databases for each model to mimic distributed storage.
- **Concurrency:** Multi-threaded insert operations.
- **Application-level Validation:** Handles data validation such as null values, negative prices, and invalid orders.
- **Result Output:** Prints inserted records for verification.

## Technologies Used
- Python 3
- SQLite3
- Threading module

## Installation
### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Kalparatna/Assignement_Distributed.git
   cd Assignement_Distributed
   ```

## Usage
Run the following command to execute the script and insert data concurrently into the databases:

```bash
python distrubuted_data.py
```

## This command will:
1. Create tables in the respective SQLite databases if they do not exist.
2. Validate the input data.
3. Insert records concurrently using threads.
4. Print the inserted data from each database.

## Database Structure
### Users Table (users.db)
| id | name  | email            |
|----|-------|-----------------|
| 1  | Alice | alice@example.com|
| ...| ...   | ...              |

### Products Table (products.db)
| id | name       | price  |
|----|------------|--------|
| 1  | Laptop     | 1000.00|
| ...| ...        | ...    |

### Orders Table (orders.db)
| id | user_id | product_id | quantity |
|----|---------|------------|----------|
| 1  | 1       | 1          | 2        |
| ...| ...     | ...        | ...      |

## Application-Level Validation
- **Users:** Allows `NULL` values for `name` field.
- **Products:** Negative prices are filtered out.
- **Orders:** Ensures valid product IDs and positive quantities.

## Expected Output
The script will print the inserted records from each database after execution, similar to the example below:

```
users data:
(1, 'Alice', 'alice@example.com')
...

products data:
(1, 'Laptop', 1000.00)
...

orders data:
(1, 1, 1, 2)
...
```


