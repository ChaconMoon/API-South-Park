# South Park API

<img src="docs/img/Banner API.png">
An API REST that conatains data from the the episodes, characters, songs and games from the TV show South Park

### Getting Started

Requierements:

Docker: https://www.docker.com/

### Initialize the API

Open a Command-Line
```powershell
docker-compose build # Build the API Project Image
```

Start the container
```powershell
docker-compose up -d # Start container with the API and the database
```

Stop the container
```powershell
docker-compose down # Stops and deletes the container
```

This intilice the API in the port 8000 of your computer

### How to use it

To search a character:

```url
http://localhost:8000/character/{id}
```

To search a episode:

```url
http://localhost:8000/episode/{id}
```

To search a Paramount + Special:

```url
http://localhost:8000/special/{id}
```

To search a Family:

```url
http://localhost:8000/family/{id}
```
To search a one alterego of a character:

```url
http://localhost:8000/character/{id}/alterego/{alter-ego-id}
```

To search a all the alteregos of a character:

```url
http://localhost:8000/character/{id}/alteregos
```

### Acknowledgments for the inspiration

The Rick and Morty API: https://rickandmortyapi.com/a

Other South Park API: https://spapi.dev/