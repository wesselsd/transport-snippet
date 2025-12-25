## Description

This project shows how to write a simple rest API client.

It uses the opendata transport api [docs](https://transport.opendata.ch/docs.html)  to next few buses leaving
from a specific tram station in Zurich.

This program just fetches all currently running connections from Meierhofplatz and 
displays the fastest connection to Zurich HB.

### Output
```
The fastest tram from Meierhofplatz to Zurich hb:
Tram number 50 to Zürich, Auzelg
Leaves Zürich, Meierhofplatz at 2025-12-25 19:40:49+01:00
arrives at Zürich, Sihlquai/HB at 2025-12-25 19:56:00+01:00
```

### Design

`/opendata` contains only the code necessary to fetch data from the API, but no business logic.
`main.py` contains all business logic.
