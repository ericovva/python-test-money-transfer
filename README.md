**Setup**
----
clone this repository

install docker and docker-compose on your machine

use commands:
```
docker-compose up postgres
docker-compose up --build
```
go to default IP http://192.168.99.100 in your browser

**Run tests**
----
```
docker exec -it <container_hash> /bin/bash
python mange.py test
```

**Get available accounts**
----
  Returns json data about accounts.

* **URL**

  /account

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[{
        "id": "26271333-ad32-495d-9be6-511148572aaf",
        "balance": "0.00",
        "currency": "USD"
    },]`
  
  
  
**Get payments**
----
  Returns json data about payments.

* **URL**

  /payment

* **Method:**

  `GET`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[{
        "id": 1,
        "amount": "123.12",
        "direction": 1,
        "tr_hash": "2df0fe0c-a7e9-41bf-918a-58bfe61d8abf",
        "account": "a22d244e-bc86-4f4e-8ce8-b087f6281011",
        "to_account": "a22d244e-bc86-4f4e-8ce8-b087f6281011"
    },]`
  
**Post payments**
----
  Post json data for transfer.

* **URL**

  /payment

* **Method:**

  `POST`
  
* **Data Params**

  `{
        "amount": "123.12",
        "account": "a22d244e-bc86-4f4e-8ce8-b087f6281011",
        "to_account": "a22d244e-bc86-4f4e-8ce8-b087f6281011"
    },`

* **Success Response:**

  * **Code:** 201 <br />
    **Content:** `{
      "amount": "23.12",
      "account": "a22d244e-bc86-4f4e-8ce8-b087f6281011",
      "to_account": "26271333-ad32-495d-9be6-511148572aaf"
    },`
* **Error Response:**
  * **Code:** 400 <br />
  `{
    "detail": "Invalid accounts"
   }`
   * **Code:** 400 <br />
  `{
    "detail": "Not enough money"
   }`
   * **Code:** 400 <br />
  `{
    "non_field_errors": [
        "Amount less than zero"
    ]
   }`
   * **Code:** 400 <br />
  `{
    "non_field_errors": [
        "A valid number is required."
    ]
   }`
   * **Code:** 400 <br />
  `{
     "account": [
        "This field may not be null."
    ],
    "to_account": [
        "This field may not be null."
    ],
      "amount": [
        "This field may not be null."
    ]
   }`
