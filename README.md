# beedash
A super janky Beeminder dashboard


## Setting auth token.

Get your auth token from https://www.beeminder.com/settings/advanced_settings

You can either edit the settings.py file directly *or* set an environment variable:
```
export BEEMINDER_AUTH_TOKEN = [token from above url]
```

## Running

python beedash.py

## Output

Will write output to a file `beedash.html` in the current directory.

You can run a simple python http server to view the file 
```
python -m SimpleHTTPServer 8000
```
and access the file at: http://localhost:8000/beedash.html


