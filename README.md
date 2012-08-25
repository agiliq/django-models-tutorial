An interactive queryset tutorial inspired by [Githug](https://github.com/Gazler/githug).

### Usage ###
python app.py

### Contributing ###
Modify levels.py and send a pull request.

### Adding Level ###
Each level is a dictionary with these keys.

1. `test`: A callable which will decide if current level is passed. This should return True if level is cleared, False otherwise.
2. `greet`: A string which will be shown once each level
3. `question`: A string which will be shown each time a level is passed. (Until you give the correct answer.)
4. `goodbye`: A string which is shown after you pass a level
5. `setup`: (optional) A callable which can be used to setup the stage for the current level. It show return a dictionary which will be available to the user.

### Gameplay ###
Each level (from levels.py) is played in order. You need to give the correct answer for a level before you are taken to the next level. User 
input is `eval`ed and compared against correct result. As we want to compare results, `eval` is the only option. (String comparision of input won't do.)

### Todo ###

1. Add tests
2. Allow choosing levels.py file. (To allows more tutorials)
3. Write more levels

