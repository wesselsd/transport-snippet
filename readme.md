## Description

This project shows how to write a simple rest API client.

It uses the opendata transport api [docs](https://transport.opendata.ch/docs.html)  to next few buses leaving
from a specific tram station in Zurich.


### Design

`/opendata` contains only the code necessary to fetch data from the API, but no business logic.
