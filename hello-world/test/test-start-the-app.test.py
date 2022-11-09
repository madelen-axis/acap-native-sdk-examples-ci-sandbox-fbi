import requests

def GetTheLogs():
        headers = {
            'Content-Type': 'application/json',
        }

        params = {
            'appname': 'hello_world',
        }

        response = requests.get('http://85.235.16.137:8012/camera1/axis-cgi/admin/systemlog.cgi', params=params, headers=headers, verify=False, auth=('root', 'F1J2M3*JFoaHDaeNL@v3'))
        # logs.append(response.text)
        # last_elem = logs[len(logs) - 1]
        # return (last_elem)
        return response.text
print(GetTheLogs())

