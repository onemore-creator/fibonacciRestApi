
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

## 1. Fibonacci Value Endpoint

- **Endpoint:** `/fibonacci/count/{number}`
- **Description:** Calculates the Fibonacci value for the specified number.
- **HTTP Method:** GET
- **Status Code:** 200 OK
- **Response Model:** `FibonacciResponse`
- **Parameters:**
  - `number` (path parameter): Integer for which Fibonacci value is calculated.
- **Response:**
  - JSON format: `{"number": "<Fibonacci value as string>"}`

## 2. Fibonacci Sequence Endpoint

- **Endpoint:** `/fibonacci/count/from1toN/{number}`
- **Description:** Retrieves the Fibonacci sequence from 1 to the specified number, excluding blacklisted numbers.
- **HTTP Method:** GET
- **Status Code:** 200 OK
- **Response Model:** Paginated list of `FibonacciResponse`
- **Parameters:**
  - `number` (path parameter): Integer specifying the upper limit of the sequence.
- **Response:**
  - JSON format: Paginated list of Fibonacci sequence without blacklisted numbers.

## 3. Blacklist Management Endpoints

### 3.1 Add Number to Blacklist

- **Endpoint:** `/fibonacci/blacklist/add/{number}`
- **Description:** Adds a number to the blacklist.
- **HTTP Method:** POST
- **Status Code:** 201 Created
- **Parameters:**
  - `number` (path parameter): Integer to be added to the blacklist.
- **Response:**
  - Response body: Result of `sadd` operation.

### 3.2 Delete Number from Blacklist

- **Endpoint:** `/fibonacci/blacklist/delete/{number}`
- **Description:** Deletes a number from the blacklist.
- **HTTP Method:** DELETE
- **Status Code:** 204 No Content
- **Parameters:**
  - `number` (path parameter): Integer to be removed from the blacklist.
- **Response:**
  - Response body: Result of `srem` operation.

### 3.3 Flush Blacklist

- **Endpoint:** `/fibonacci/blacklist/delete`
- **Description:** Deletes all numbers from the blacklist.
- **HTTP Method:** DELETE
- **Status Code:** 204 No Content
- **Response:**
  - Response body: Result of `del` operation.

### 3.4 Get Blacklist

- **Endpoint:** `/fibonacci/blacklist/get`
- **Description:** Retrieves the current blacklist.
- **HTTP Method:** GET
- **Status Code:** 200 OK
- **Response Model:** `BlacklistResponse`
- **Response:**
  - JSON format: `{"numbers": [<blacklisted numbers>]}` (empty list if no blacklisted numbers)



# Possible TODO

Theoretically, we can move the blacklist operation completely to redis. It wasn`t done since we can get pretty the same reslt with celery. What I mean is that we can keep both fibonacci operation result and blacklist in redis and then just request SDIFF

