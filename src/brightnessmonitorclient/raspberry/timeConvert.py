import datetime

# converts given seconds passed since 1 Jan 1970
# back into readable time
def convertback(seconds):
    return datetime.datetime.fromtimestamp(seconds)