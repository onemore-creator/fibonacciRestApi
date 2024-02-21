
# Fibonacci simple Rest API 

## How to deploy

In order to deploy the application you should run this simple command:

```bash
docker-compose up
```

To test

```bash
docker-compose --profile test up 
```

Then you should ba able to access the application on http://localhost:8080

And you can also see swagger docs on http://0.0.0.0:8080/docs
## Features

# FastAPI Router Features

## 1. Fibonacci Endpoint

- **Endpoint:** `/fibonacci/count/{number}`
- **Description:** Calculates the Fibonacci value for the specified number.
- **HTTP Method:** GET
- **Parameters:**
  - `number` (path parameter): Integer for which Fibonacci value is calculated.
- **Response:**
  - Successful Response: 200 OK
    - JSON format: `{"result": <Fibonacci value>}`
  - Error Response: 400 Bad Request
    - Detail: "Invalid input. Please provide a valid integer" or "Unexpected error"

## 2. Fibonacci Sequence Endpoint

- **Endpoint:** `/fibonacci/count/from1toN/{number}`
- **Description:** Retrieves the Fibonacci sequence from 1 to the specified number, excluding blacklisted numbers.
- **HTTP Method:** GET
- **Parameters:**
  - `number` (path parameter): Integer specifying the upper limit of the sequence.
- **Response:**
  - Successful Response: 200 OK
    - JSON format: Paginated list of Fibonacci sequence without blacklisted numbers.
  - Error Response: 400 Bad Request
    - Detail: "Invalid input. Please provide a valid integer" or "Unexpected error"

## 3. Blacklist Management Endpoints

### 3.1 Add Number to Blacklist

- **Endpoint:** `/fibonacci/blacklist/add/{number}`
- **Description:** Adds a number to the blacklist.
- **HTTP Method:** POST
- **Parameters:**
  - `number` (path parameter): Integer to be added to the blacklist.
- **Response:**
  - Successful Response: 200 OK
    - JSON format: `1` (assuming the result of `sadd` operation)
  - Error Response: 500 Internal Server Error

### 3.2 Delete Number from Blacklist

- **Endpoint:** `/fibonacci/blacklist/delete/{number}`
- **Description:** Deletes a number from the blacklist.
- **HTTP Method:** DELETE
- **Parameters:**
  - `number` (path parameter): Integer to be removed from the blacklist.
- **Response:**
  - Successful Response: 204 No Content
  - Error Response: 500 Internal Server Error

### 3.3 Get Numbers from Blacklist

- **Endpoint:** `/fibonacci/blacklist/get`
- **Description:** Retrieves the current blacklist.
- **HTTP Method:** GET
- **Response:**
  - Successful Response: 200 OK
    - JSON format: `{"numbers": [<blacklisted numbers>]}` (empty list if no blacklisted numbers)
  - Error Response: 500 Internal Server Error (if unable to retrieve blacklist)


# Possible TODO

Theoretically, we can move the blacklist operation completely to redis. It wasn`t done since we can get pretty the same reslt with celery. What I mean is that we can keep both fibonacci operation result and blacklist in redis and then just request SDIFF

