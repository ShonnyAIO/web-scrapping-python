import requests
from bs4 import BeautifulSoup
import json
url = (
    f'https://www.degustavenezuela.com/caracas/search?filters=eyJmaWx0ZXJzIjp7fSwic2NvcmVfcmFuZ2UiOnt9LCJwcmljZV9yYW5nZSI6Mywic29ydCI6ImZvb2QifQ==')
response = requests.get(url)
print(response)
data = response.text     # a `bytes` object
soup = BeautifulSoup(data)
results = soup.findAll('script', {'type': 'text/javascript'})

for resultados in results:
    print(resultados)

"""
for i in r:
    if '$scope.products' in i:
        jsonStr_products = i
        jsonStr_products = jsonStr_products.split('$scope.products = [')[1]
        jsonStr_products = jsonStr_products.rsplit('];', 1)[0]
        file.write(jsonStr_products)
        # Aqui logro sacar los productos, pero tengo a las farmacias en el siguiente scope
        jsonStr_farmas = i
        jsonStr_farmas = jsonStr_farmas.split('$scope.farmas = [')[1]
        jsonStr_farmas = jsonStr_farmas.rsplit('];', 1)[0]
        file2.write(jsonStr_farmas)
"""

"""
for result in results:
    if 'var shows = [' in result.text:
        jsonStr = result.text

        jsonStr = jsonStr.split('var shows = [')[1]
        jsonStr = jsonStr.rsplit('];', 1)[0]

        jsonStr_list = jsonStr.split('{"Id":')[1:]

        for each in jsonStr_list:
            each = jsonStr_list[0]
            w = 1
            if each[-1] == ',':
                each = each.rstrip(',')

            jsonTemp = '{"Id":' + each
            jsonObj = json.loads(jsonTemp)

            r.append(jsonObj)
"""
