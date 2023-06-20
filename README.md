# Link-compressor

## Run:

Use `docker-compose build` and `docker-compose up` to run application.

## Usage:

1. Go to interactive http://localhost:5000/docs
2. Try out `squeeze` method
3. Take some link, for example https://www.youtube.com/watch?v=dQw4w9WgXcQ
4. Execute
5. Take `short` parametr from json:
    ```json
    {
    "id": 1,
    "short": "195NX", // <--- you need this strange symbols
    "target": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "counter": 0
    }
    ```
6. Paste short link after http://localhost:5000/s/
7. Back to `docker-compose` process and stop it
8. Delete container by `docker-compose rm`
9. Run new container with `docker-compose up`
10. Check that http://localhost:5000/s/{YOUR_SHORT_LINK} redirect you to the original link
