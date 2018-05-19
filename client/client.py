import http.client


def main():

    conn = http.client.HTTPConnection("localhost:8888")
    headers = {"Content-type": "application/json",
               "Accept": "application/json"}
    conn.request("GET", "/resource", "", headers)
    response = conn.getresponse()
    print(str(response.status) + " " + str(response.reason))
    data = response.read()
    conn.close()
    print(data)


if __name__ == '__main__':
    main()