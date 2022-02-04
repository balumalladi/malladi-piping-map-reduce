import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 7) : 
    country_name,country_iso2,week,category,weekly_rank,show_title,cumulative_weeks_in_top_10 = datalist

    # print intermediate key-value pairs to standard output
    print(country_name,"\t",cumulative_weeks_in_top_10)