# steam_population_checker
check the population of steam games, send notification when above threshold

Only dependency is notify2

`$ pip install notify2 dbus-python`

Make sure your pip is the same as the one you're running the program with, you may need to use `pip3`. 

To start in terminal and run in background:

```
$ python3 path/to/steam_population_checker.py 608800 20 [your key kere] &
$ disown
```

This will notify when there are at least 20 people playing 608800 (Guns of Icarus Alliance)

This script should run on windows too, but I don't know how you install python dependencies on windows, I'm sure there's a bazillion tutorials. 
