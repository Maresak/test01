'''
Created on 2019. 1. 16.

@author: Park Hyun Woo
'''

import json
import urllib.request


# [1] 웹이미지(url형식)의 주소를 input 값으로 하여 OCR 요청 & 응답

def open_ocr_run():
    url = "http://localhost:9292/ocr"  # URL
    d = {'img_url': 'https://seoul-p-studio.bunjang.net/product/84362602_4_1526631008_w640.jpg',
         'engine': 'tesseract'}

    # 문자열을 바이트로 변환
    params = json.dumps(d).encode("utf-8")
    req = urllib.request.Request(url, data=params, headers={
                                 'content-type': 'application/json'})
    response = urllib.request.urlopen(req)

    # 바이트를 문자열로 변환
    value = response.read().decode('utf8')

    print("========OCR 결과를 찍어요=========")
    print(value)


if __name__ == "__main__":
    open_ocr_run()
