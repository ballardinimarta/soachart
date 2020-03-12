# Soachart
A heatmap that displays soa zones for .se servers. 

# How to set up
Start by cloning my repo.

```bash
$ git clone https://github.com/ballardinimarta/soachart.git
```
Go to the repos directory 

```bash
$ cd soachart
```

Activate venv

```bash
$ source venv/bin/activate
```

Install requirements.txt

```bash
$ pip install -r requirements.txt
``` 
# Set the time
If you want to see the chart from a specific timeframe, go to measurements.py and change 'starttime' and 'stoptime'. Default in my code is 
```
# 03/09-2020 03.00
starttime = 1583719200
# 03/09-2020 06.00
stoptime = 1583730000
```
The times are set in unix timestamps.

# How to run
To run the chart use:
```bash
$ python3 soa_heatmap.py
```

# Output
After running the script it will first print some warnings, and then the chart should pop up in your browser.

