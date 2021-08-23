
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
            justify-content: center;
            align-self: center;

            margin: 0 auto;
            margin-bottom: 1.0rem;
        }
        </style>
    </head>
    <body>
        <div class="col-xs-1" align="center">
            <div class="layout-line">
    '''
    
    middle = ''

    for url in img_urls:
        img_src = f'<img src="{url}">'
        middle += img_src
    
    end = '''
        </div>
        </div>
    </body>
    </html>
    '''

    return front+middle+end