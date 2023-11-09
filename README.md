# 7PAM2000 Applied Data Science 1 (Assignment)

## Instructions
Your task is to apply three types of visualisation methods (graphs) to extract meaningful
information. Find below a link list for good sources of data, but you are welcome to find
other sources. Please check the quality. Some data sets can be quite messy and are better
avoided in your first assignment.
1. Produce a line plot showing multiple lines with proper labels and legend. Describe
what conclusions you can draw from this plot.
2. Produce graphs using two other visualisation methods. Explain why you picked this
type of graph and describe what conclusions you can draw. Marks will be awarded
for plausible choices of graphs. The choice does not need to be the perfect one, but
at least one type will not a good choice if you visualise exactly the same data three
times. Note, that we consider it not exactly the same, if you do a line plot of a time
series and then use a pie chart to visualise relative sizes for a selected time.


### Data Source
https://finances.worldbank.org/browse?limitTo=datasets

https://finances.worldbank.org/Loans-and-Credits/IDA-Statement-of-Credits-and-Grants-Latest-Availab/ebmi-69yj


### How to run
Download the csv data and put in the root directory

### Setup python virtual environment and install packages
`python3 -m venv assignment_env`

`source assignment_env/bin/activate`

`pip install requirements.txt`

then run 

```
python main.py
```