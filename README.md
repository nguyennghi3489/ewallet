# Ewallet

## This is python implementation for ewallet workflow. 
Create/Confirm/Verify flow
![transaction](https://user-images.githubusercontent.com/5178516/236105821-ce5d1890-f81c-4272-8437-4ee21221ee8e.jpg)

Create/Confirm/Cancel flow
![transactionCancel](https://user-images.githubusercontent.com/5178516/236105837-237928bc-1be9-4eb5-b673-d37559a12c0d.jpg)

Includes apis belows
- Merchant Signup
- Create Account
- Get Account
- Account Topup
- Create Transaction
- Confirm Transaction
- Verify Transaction
- Cancel Transaction

A Worker to check the expired transaction( Transaction is not completed in 5 mins)


## Setup
- Instal venv:
python3 -m venv env
- Activate env
source env/bin/activate
- Run service:
python3 src/main.py

