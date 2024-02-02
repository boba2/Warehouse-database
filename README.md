# Warehouse Database

MongoDB database to store information about warehouse availability.<br>
Communication with database through FastAPI.

## Setup

1. Clone repository

``` git clone https://github.com/KonradBorowik/Warehouse-database.git ```

2. Build Docker image

``` docker build -t kb_warehouse_database . ```

3. Run container

``` docker run -d --name mycontainer -p 80:80 kb_warehouse_database ```

## Explore endpoints

``` http://localhost/docs# ```