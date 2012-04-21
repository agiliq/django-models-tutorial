An interactive queryset tutorial inspired by [Githug](https://github.com/Gazler/githug).

### Usage ###
python app.py

### Contributing ###
Modify levels.py and send a pull request.

### Adding Level ###
Each level is a dictionary with these keys.
1. `test`: A callable which will decide if current level is passed
2. `question`: A string which will be shown once each level
3. `question`: A string which will be shown each time a level is passed. (Until you give the correct answer.)
4. `goodbye`: A string which is shown after you pass a level
