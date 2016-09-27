from urllib import request  # same as import urllib.request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&d=2&e=9&f=2016&g=d&a=7&b=19&c=2004&ignore=.csv'


def download_stock_data(csv_url):
    response = request.urlopen(csv_url)  # creates a connection to the file
    csv = response.read()  # reads the data from the url
    csv_str = str(csv)  # converts all the data into a string
    lines = csv_str.split("\\n")  # takes a string and split it
    dest_url = r'goog.csv'  # gives the file a name (r is raw)
    fx = open(dest_url, "w")  # allows us to write to the file
    for line in lines:
        fx.write(line + "\n")  # writes to the file, adds breaks
    fx.close()


download_stock_data(goog_url)
