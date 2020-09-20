# DarebeeCrawler
Crawler to scrape all workouts from darebee

## To run
Before running selenium and beatifulsoup4 should be installed.
It can be installed **globally** by ```pip install -r requirements.txt```
After installation you can run the program with ```python .\crawler.py```

## Output
Program will download all workouts in the darebee.com/workouts link, and categorize them by the type, focus and difficulty of the workout.

### Problems
For some workouts focusses and types cannot be detected.
These workouts are saved in the current working directory, divided by their difficulty.
