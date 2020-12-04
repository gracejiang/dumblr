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

make sure all packaged are installed
```
pip install -r requirements.txt
```

run the server
```
python3 manage.py runserver
```

### todo

- [x] switch post url routing from primary key to post id
- [x] show 5 fields of post model
- [x] change post rendering from html to md


### notes to self [ignore]

* when updating css, run ```python3 manage.py collectstatic```