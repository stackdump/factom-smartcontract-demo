## Last update

Tue Sep 11 12:30:59 CDT 2018

### WIP:

- [ ] show how state of board could be written as a snapshot event

### BACKLOG:

- [ ] include validation keys in the inital chain entry
- [ ] Add an audit.py to detect bad games
- [ ] Extend client.py to query all entries (needed to finish ./src/audit.py)

```
factom-cli get allentries c7070d6a0a81ecf11b17d117fd8e1b50d4f07436926f541b2f84a682b67e1c0b
```

- was able to see all the API calls being made using tcpflow

```
sudo tcpflow -c -i lo tcp port 8088
```

### COMPLETE:

- [x] show signed events
- [x] show key generation
- [x] show signature validation 
- [x] chain creation signature validation 
