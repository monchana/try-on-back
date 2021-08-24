from tryon.services.try_on_back_modules.tryongenerator.utils.html.txts import get_content, get_head


def line(img_urls):
    front = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
        .layout-line {
            max-width: 50%;
        }
        .layout-line > * {
            display: block;
            justify-content: start;
            align-self: center;

            margin: 0 auto;
            margin-bottom: 1.0rem;
        }
        </style>
    </head>
    <body>
        <div style="background-color: #f6f5ef;" class="col-xs-1" align="center">
            <div class="layout-line">
    '''
    
    middle = ''

    for url in img_urls:
        img_src = f'<img src="{url}">'
        middle += f'''
        <div style="display: flex"> 
            {img_src} 
            <div style="position: relative; text-align: start">
                <h1 style=""> {get_head()} </h1>
                <div style="position: absolute; width: 33vw; font-style: italic"> 
                    "{get_content()}"
                </div> 
            </div>
        </div>
        '''.replace("\n", "")
    
    end = '''
        </div>
        </div>
    </body>
    </html>
    '''

    return front+middle+end