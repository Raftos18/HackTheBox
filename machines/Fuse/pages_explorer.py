import requests 

for month in range(1, 13):
    for day in range(1, 32):

        month_str = str(month)
        day_str = str(day)

        if (month < 10):
            month_str = '0' + month_str

        if (day < 10):
            day_str = '0' + day_str


        url = 'http://fuse.fabricorp.local/papercut/logs/html/papercut-print-log-2020-{}-{}.htm'.format(month_str, day_str)        

        res = requests.get('http://fuse.fabricorp.local/papercut/logs/html/papercut-print-log-2020-{}-{}.htm'.format(month_str, day_str))

        if (res.status_code != 404):
            print(url)
            print(res.status_code)
        else:
            print("...")