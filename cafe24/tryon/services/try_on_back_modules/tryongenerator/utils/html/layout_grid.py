
from tryon.services.try_on_back_modules.tryongenerator.utils.html.txts import *


def grid(img_urls):
    front = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
            .layout-grid {
                width: 46vw;
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                align-items: center;
                justify-content: center;


            }  
            .layout-grid>* {
                margin: 0 0.5vw;
                display: flex;
                align-items: center;
                justify-content: center;


            }
        </style>
        </head>
        <body>
        <div style="background-color: #f6f5ef;" class="col-xs-1" align="center">

        <div class="layout-grid">
    '''

    middle = ''

    for idx, url in enumerate(img_urls):
        img_src = f'<img src="{url}">'
        middle += img_src
        if (idx + 1) % 2 == 0:
            middle += f'''
            <div style="display: block; margin-top: 3vh; grid-column-start: 1;text-align: center; grid-column-end: 4; align-items: start;">
                <h1> {get_head()} </h1>
                <div style="width: 35vw; font-style: italic; margin-left: auto; margin-right: auto;  margin-bottom: 5vh;"> 
                    "{get_content()}"
                </div> 
            </div>                
            '''.replace("\n", "") 

    end = '''
        </div>
        </div>
    </body>
    </html>
    '''

    return front + middle + end
