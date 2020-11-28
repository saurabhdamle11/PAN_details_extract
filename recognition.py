import requests
import os
import json

def ocr_space_file(filename, overlay=False, api_key='***********', language='eng'):
    

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r

path = '/home/saurabh/Code/WebAPI/static/image/'
files = os.listdir(path)
idx = len(files) - 1

def extract_values():

    path = '/home/saurabh/Code/WebAPI/static/image/'
    files_count = len(os.listdir(path))
    print(files_count)
    if files_count != 0:
        idx = files_count - 1

        text = ocr_space_file(os.path.join(path,files[idx]))
        print(type(text.content.decode()))
        content_json = text.content.decode('utf8').replace("'", '"')
        data = json.loads(content_json)

        parsed = data['ParsedResults'][0]['ParsedText']
        contents = parsed.split('\r')
        value = 'Name:',contents[1], '\nDate of Birth:',contents[3],'\nPAN number:',contents[5]
        return ''.join(value)
    else:
        return ''
    

extract_values()

#End of package
