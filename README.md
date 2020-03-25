# soachart
A heatmap that displays soa zones for .se servers. 

## How to set up
Start by cloning my repo.

```bash
$ git clone https://github.com/ballardinimarta/soachart.git
```
Go to the repos directory 

```bash
$ cd soachart
```

Install requirements.txt

```bash
$ pip install -r requirements.txt
``` 

# For soa chart with adjustable time
## Set the time
If you want to see the chart from a specific timeframe, go to measurements.py and change 'starttime' and 'stoptime'. Default in my code is 
```
# 03/09-2020 03.00
starttime = 1583719200
# 03/09-2020 06.00
stoptime = 1583730000
```
The times are set in unix timestamps.

## How to run
To run the chart use:
```bash
$ python3 soa_heatmap.py
```

## Output
After running the script the chart should pop up in your browser.

### Output as HTML file
Or if you want the chart as a HTML file you can remove the hashtag from the comment on the last line in soa_heatmap.py, on default if you clone the code will look like this
```
# Display the plot
fig.show()

# Write HTML file
#fig.write_html("path/to/file.html")

```
So if you want the HTML file you change it to
```
# Display the plot
#fig.show()

# Write HTML file
fig.write_html("path/to/file.html")

```
Then change the path to where you would like to have it and the name of the file.

# For a soachart for the last 24 hours

## How to run
To run the chart use:
```bash
$ python3 soa_heatmap_24.py
```

## Output
After running the script the chart should pop up in your browser.

### Output as HTML file
Or if you want the chart as a HTML file you can remove the hashtag from the comment on the last line in soa_heatmap.py, on default if you clone the code will look like this
```
# Display the plot
fig.show()

# Write HTML file
#fig.write_html("path/to/file.html")

```
So if you want the HTML file you change it to
```
# Display the plot
#fig.show()

# Write HTML file
fig.write_html("path/to/file.html")

```
Then change the path to where you would like to have it and the name of the file.