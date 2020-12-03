# dumblr
dummy tumblr | built for cis192


### how to run locally

make sure django + python is properly installed on your system. then, run the following commands on your command line.

clone the repo
```
git clone https://github.com/gracejiang/dumblr
```

navigate to repo
```
cd dumblr
```

run server
```
python3 manage.py runserver
```

### todo

- [] switch post url routing from primary key to post id
- [] show 5 fields of post model
- [] change post rendering from html to md


### notes to self [ignore]

* when updating css, run ```python3 manage.py collectstatic```