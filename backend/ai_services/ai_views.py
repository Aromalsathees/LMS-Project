from admin_panel .models import *

def call_ai(prompt):
 
    url =  ()
    headers = {
        'content-Type':'application/json'
    }

    data = {
        'contents':[
            'parts':[
                {
                    'text':prompt
                }
            ]
        ]
    }

    response = requests.post(url ,headers=headers , json=data)
    result = response.json()
    return result['candinates'][0]['content']['parts'][0]['text']

def Grammer_correction(prompt):
    call_ai(prompt)
    return call_ai(prompt)

def simple_explanation(prompt):
    call_ai(prompt)
    return call_ai(prompt)

def practice_sentence(prompt):
    call_ai(prompt)
    return call_ai(prompt)


