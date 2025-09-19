# South Park API

<img src="docs/img/Banner API.png">

A REST API that contains data from the episodes, characters, songs, and games from the TV show South Park.

## Getting Started with Docker

Requierements **[Run as Docker Contianer]**:

- Docker: https://www.docker.com/

### Initialize the API _[As a Docker Container]_
Open a Command-Line:
```powershell
docker-compose build # Build the API Project Image
```

Start the container:
```powershell
docker-compose up -d # Start container with the API and the database
```
**This initializes the API on port 8000 of your computer.**

Initialize the database with the default data:
```powershell
docker exec -it southpark_api-db-1  pg_dump -U southpark southpark_api > init.sql
```

Stop the container:
```powershell
docker-compose down # Stops and deletes the container
```

## Getting Started with Python

Requierements **[Run as Python project]**:

 - Python >=3.13
 - Poetry >=2.1.1
 - A PostgreSQL Database, a remote database or a Docker Container with a PostgreSQL database.
 - A PostgreSQL Client in the CLI.


### Initialize the API _[As a Python project]_
Create and activate the Poetry virtual environment:
```powershell
poetry env activate #And activate the created env
```

Install the dependencies:
```powershell
poetry install
```

Rename the file `.env_example` to `.env` and add the connection URL for your database:
```
DATABASE_URL="YOUR POSTGRESQL DATABASE URL HERE"
```

Copy the database content to your remote database:
```powershell
psql "YOUR POSTGRESQL DATABASE URL HERE" < init.sql
```


### Endpoints

To search for a character:
```url
http://localhost:8000/character/{id}
```

To search for an episode:
```url
http://localhost:8000/episode/{id}
```

To search for a Paramount+ Special:
```url
http://localhost:8000/special/{id}
```

To search for a Family:
```url
http://localhost:8000/family/{id}
```

To search for an alter ego of a character:
```url
http://localhost:8000/character/{id}/alterego/{alter-ego-id}
```

To search for all the alter egos of a character:
```url
http://localhost:8000/character/{id}/alteregos
```

To search for a song:
```url
http://localhost:8000/song/{id}
```

To search for an album:
```url
http://localhost:8000/album/{id}
```

To search for a Chinpokomon:
```url
http://localhost:8000/chinpokomon/{id}
```

### Acknowledgments

Inspiration for this project was drawn from:

- The Rick and Morty API: https://rickandmortyapi.com/
- Other South Park API: https://spapi.dev/