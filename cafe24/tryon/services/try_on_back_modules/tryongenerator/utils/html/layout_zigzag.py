from tryon.services.try_on_back_modules.tryongenerator.utils.html.txts import get_content, get_head
def zigzag(img_urls):

    front = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
             .layout-zigzag {
                width: 46vw;
                margin: 0 auto;
                align-self: center;
                justify-content: center;
            }

            .layout-zigzag div:nth-of-type(even) {
                grid-column: 2;
            }
        </style>
        </head>
        <body>
        
        <div style="background-color: #f6f5ef;"> 
            <div class="layout-zigzag"> 
    '''

    middle = ''
    
    for url_idx in range(len(img_urls)):
        if url_idx % 2 == 0:
            middle += f'''
            <div style="display: flex; margin-bottom: 1vh; justify-content: center;">
                <img style="width: 192px; height: 256px;" src="{img_urls[url_idx]}">
                <div style="position: relative; text-align: start; margin-top: auto; margin-bottom: auto;  padding-left: 5vw;">
                    <h1> {get_head()} </h1>
                    <div style="width: 20vw; font-style: italic"> 
                        "{get_content()}"
                    </div> 
                </div>                
            </div>
        '''
        else:
            middle += f'''
            <div style="display: flex; margin-bottom: 1vh; justify-content: center;">
                <div style="position: relative; text-align: start; margin-top: auto; margin-bottom: auto; padding-right: 5vw;">
                    <h1> {get_head()} </h1>
                    <div style="width: 20vw; font-style: italic"> 
                        "{get_content()}"
                    </div> 
                </div>            
                <img style="width: 192px; height: 256px;" src="{img_urls[url_idx]}">
            </div>'''

    end = '''
            </div>
        </div>
    </body>
    </html>
    '''

    return front + middle + end
