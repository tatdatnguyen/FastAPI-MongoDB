# FastAPI-MongoDB
## Installation
**In terminal**

``
pip install fastapi motor uvicorn
``

Install the database

``
sudo apt update
sudo apt install -y mongodb 
``


## Run the code
**Start the database**

``
sudo systemctl start mongod
``

**Run the server**

``
uvicorn main:app --reload
``
