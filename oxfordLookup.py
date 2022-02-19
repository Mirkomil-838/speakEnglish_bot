from pprint import pprint
import requests
app_id = "b2436411"
app_key = "dc54d2e242d0abd87e3e1dbc55286250"
language = "en-gb"

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()

    if 'error' in res.keys():
        return False
    definitions = ''
    output = {}
    try:
        if word_id == 'get':
            definitions += res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0]
        elif res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0].get('definitions'):
            for i in range(len(res['results'])):
                for sense in res['results'][i]['lexicalEntries'][0]['entries'][0]['senses']:
                    definitions += f"👉  {sense['definitions'][0]} \n"
    except:
        pass
    output['definitions'] = definitions

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audioFile'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

if __name__ == "__main__":
    from pprint import pprint
    pprint(getDefinitions("get"))
