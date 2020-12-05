# dumblr
dummy tumblr | built for cis192

### examples of working result

*landing and blog pages*

![example-1](assets/example-1.gif)



*markdown conversion*

![example-2](assets/example-2.gif)



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

make sure all packages are installed

```
pip install -r requirements.txt
```

run the server

```
python3 manage.py runserver
```





### ignore this

**requirements**:

- [x] url routing to each post based off post id
- [x] shows 5 fields of post model
- [x] post renders from md to html



**notes to self**:

* when updating css, run ```python3 manage.py collectstatic```