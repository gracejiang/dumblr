# dumblr
dummy tumblr | built for cis192



## find the github repo here:

[github repo](https://github.com/gracejiang/dumblr)




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



### examples of working result

*landing and blog pages*

![example-1](assets/example-1.gif)



*markdown conversion*

![example-2](assets/example-2.gif)

### ignore this

**todos**:

- [x] switch post url routing from primary key to post id
- [x] show 5 fields of post model
- [x] change post rendering from html to md
- [ ] fix package installation errors | venv stuff | deploy



**notes to self**:

* when updating css, run ```python3 manage.py collectstatic```