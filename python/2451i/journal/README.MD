# Local Setup

1. Make sure you have python installed and MySQL database running
1. Import database dumpt: `mysql -uroot -p < db/migrations/*.sql`
1. set database user password in __helpers/db.py -> getPool__ function
1. Install dependencies: `pip install -r requirements`
1. `python app.py`


# Project Structure

1. _entities_ folder contains modules that describe entities and their fields
1. _inputs_ folder contains modules the works with user input for each entity and operation
1. _services_ folder contains service modules for each entity that is responsible for performing operations (insert, update, search etc.)
1. _helpers_ folder contains helper modules like DB