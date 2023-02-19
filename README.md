# "Restaurant-Kitchen-Service"

  This project was created for the kitchen workers of a restaurant or cafe.
Cooks can log into their account, view what dishes they need to cook,
the ingredients for each dish, what type of dish a particular dish belongs to,
and view the profiles of other workers.

Also in this app you can:

- register/delete cook profiles
- create/delete new types of food, dishes, ingredients
- update information about chefs, dishes, ingredients and dish types
- pin/unpin a dish from your profile

---

[Restaurant-kitchen project deployed to render](https://kitchen-service-i4dp.onrender.com)

Installing / Getting started
A quick introduction of the minimal setup you need

- git clone https://github.com/KolyaZakharov/Restaurant-Kitchen-Service.git
- cd restaurant_kitchen_service
- python -m venv venv
- venv\Scripts\activate
- pip install -r requirements.txt
- copy .env.sample -> .env and populate with all required data
  (SECRET_KEY - It's a django secret key used for hashing
etc.)
- python manage.py migrate
---
## For login
**Login:** `admin`

**Password**   `admin`
