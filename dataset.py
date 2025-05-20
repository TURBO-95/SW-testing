import random
import string
import csv

first_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivan', 'Julia']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Martinez', 'Lee']
genders = ['Male', 'Female']

def random_email(first, last):
    domains = ['example.com', 'mail.com', 'test.org']
    return f"{last.lower()}.{first.lower()}{random.randint(1,1000000000000000000)}@{random.choice(domains)}"

def random_password(length=10):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def generate_user():
    first = random.choice(first_names)
    last = random.choice(last_names)
    email = random_email(first, last)
    password = random_password()
    gender = random.choice(genders)
    return {
        'firstName': first,
        'lastName': last,
        'email': email,
        'password': password,
        'gender': gender
    }

def generate_users(n=10000):
    return [generate_user() for _ in range(n)]

if __name__ == "__main__":
    users = generate_users(10000)
    with open('users.csv', 'w', newline='') as csvfile:
        fieldnames = ['firstName', 'lastName', 'email', 'password', 'gender']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for user in users:
            writer.writerow(user)