# 0x06. Star Wars API

## Description

This project involves writing a script that prints all characters of a Star Wars movie using the Star Wars API.

## Requirements

- The first positional argument passed is the Movie ID (e.g., 3 = “Return of the Jedi”).
- Display one character name per line in the same order as the “characters” list in the `/films/` endpoint.
- Use the Star Wars API.
- Use the `request` module.

## Usage

### Example

```sh
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/0x06$
```

## Resources

- [swapi-api.hbtn.io](https://swapi-api.hbtn.io/)
- [request module](https://github.com/request/request)
