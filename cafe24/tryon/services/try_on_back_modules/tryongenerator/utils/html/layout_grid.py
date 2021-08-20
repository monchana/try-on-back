
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
        display: grid;
        grid-template-columns: repeat(3, 1fr);
            }  
            .layout-grid>* {
            }
        </style>
        </head>
        <body>
        <div class="layout-grid">
    '''

    middle = ''

    for url in img_urls:
        img_src = f'<img src="{url}">'
        middle += img_src

    end = '''
        </div>
    </body>
    </html>
    '''

    return front + middle + end
