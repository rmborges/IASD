iss_data = open('iss.txt', 'r')

while True:
    line = iss_data.readline()
    print(line)
    if not line:
        break
