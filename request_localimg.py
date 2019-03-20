'''
Created on 2019. 1. 16.

@author: Park Hyun Woo
'''

import base64
import json
import urllib.request


# [2] 로컬에 저장된 이미지파일을 base64 인코딩하여 OCR 요청 & 응답

def open_ocr_run():
    # 로컬이미지를 base64 인코딩

    # img_path = "OCR하기위한 이미지파일명.jpg"
    img_path = "data/skew_correct/skew_corrected06.png"
    image_content = base64.b64encode(
        open(img_path, 'rb').read()).decode("utf-8")

    # 요청 URL
    url = "http://localhost:9292/ocr"

    # 한글만 OCR 하는 경우 {'lang': 'kor'}
    # 영어만 OCR 하는 경우 {'lang': 'eng'}
    # 한글과 영어 둘다 OCR 하는 경우 {'lang': 'kor+eng'}
    d = {'img_base64': image_content, 'engine': 'tesseract',
         'engine_args': {'lang': 'eng'}}

    # 문자열을 바이트로 변환
    params = json.dumps(d).encode("utf-8")
    req = urllib.request.Request(url, data=params, headers={
                                 'content-type': 'application/json'})
    response = urllib.request.urlopen(req)
    value = response.read().decode('utf8')

    print("========OCR 결과를 찍어요=========")
    print(value)


if __name__ == "__main__":
    open_ocr_run()


'''
이미지 전처리 관련 #1: 텍스트가 아닌 픽셀을 제거할 수 있습니다

{'img_base64':'http://imgurl',
    'engine':'tesseract',
    'engine_args':{'lang':'kor+eng'}, 
    'preprocessors':['stroke-width-transform']}
    


이미지 전처리 관련 #2: 이미지가 검은 배경의 흰 텍스트 인 경우에 반전시킬 수 있습니다

{'img_base64':'이미지객체',
    'engine':'tesseract',
    'engine_args':{'lang':'kor+eng'}, 
    'preprocessors':['stroke-width-transform'], 
    'preprocessor-args':{'stroke-width-transform':'1'}}
'''
