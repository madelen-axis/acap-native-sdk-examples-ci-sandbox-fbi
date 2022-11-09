import os
import sys
import requests


class TestHelloWorld:
    ACAP_SPECIFIC_NAME = "hello_world"

    def GetTheArchitecture():
        headers = {
        # Already added when you pass json= but not when you pass data=
        # 'Content-Type': 'application/json',
        }

        json_data = {
            'apiVersion': '1.0',
            'method': 'getProperties',
            'params': {
                'propertyList': [
                    'Architecture',
                ],
            },
        }

        response = requests.post('http://85.235.16.137:8012/camera1/axis-cgi/basicdeviceinfo.cgi', headers=headers, json=json_data, verify=False, auth=('root', 'F1J2M3*JFoaHDaeNL@v3'))
        return response.text

    print(GetTheArchitecture())
    # print(response.status_code)
    # print(response.text)

    def GetTheLogs():

        headers = {
            'Content-Type': 'application/json',
        }

        params = {
            'appname': 'hello_world',
        }

        response = requests.get('http://85.235.16.137:8012/camera1/axis-cgi/admin/systemlog.cgi', params=params, headers=headers, verify=False, auth=('root', 'F1J2M3*JFoaHDaeNL@v3'))

        return response.text

    print(GetTheLogs())
                    
    

















####################################################################################################################################

# response = requests.post('http://85.235.16.137:8012/camera1/axis-cgi/basicdeviceinfo.cgi', auth=('root', 'F1J2M3*JFoaHDaeNL@v3'))
# print(response.text)


# if len(sys.argv) != 4:
#     print("Usage: firmware-status.py 85.235.16.137:8012/camera1/ root F1J2M3*JFoaHDaeNL@v3")
#     sys.exit(1)

# ip = sys.argv[1]
# username = sys.argv[2]
# password = sys.argv[3]

# auth = requests.auth.HTTPDigestAuth(username, password)
# body = {
#     "apiVersion": "1.4",
#     "method": "getProperties"
# }

# r = requests.post("http://{}/axis-cgi/basicdeviceinfo.cgi".format(ip), json=body,  auth=auth)

# print(r.status_code)
# print(r.text)


####################################################################################################
# auth_handler = urllib.request.HTTPBasicAuthHandler()
# auth_handler.add_password(realm='Hello-world Application',
#                           uri='http://85.235.16.137:8012/camera1/axis-cgi/basicdeviceinfo.cgi',
#                           user='root',
#                           passwd='F1J2M3*JFoaHDaeNL@v3')
# opener = urllib.request.build_opener(auth_handler)
# # ...and install it globally so it can be used with urlopen.
# urllib.request.install_opener(opener)
# urllib.request.urlopen('http://85.235.16.137:8012/camera1/axis-cgi/basicdeviceinfo.cgi')

############################################################################################################


