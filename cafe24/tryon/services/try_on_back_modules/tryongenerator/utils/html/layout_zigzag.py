
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
                max-width: 940px;
                margin: 0 auto;
            }

            .layout-zigzag > div {
                border: 2px solid #e9ab58;
                border-radius: 5px;
                background-color: rgba(233, 171, 88, 0.5);
                padding: 1em;
                color: #d9480f;
            }

            .layout-zigzag {
                display: grid;
                grid-template-columns: 1fr 1fr;
            }
            .layout-zigzag div:nth-of-type(even) {
                grid-column: 2;
            }
    '''

    default_name = ".style_"
    for idx in range(len(img_urls)):
        overall = ''''''
        next_idx_name = default_name+str(idx+1)
        grid_row = ''' {\n grid-row: '''
        grid_row += str(idx+1)
        grid_row += ''';\n}\n'''

        overall += overall+next_idx_name+grid_row
        front+= overall

    front_second = '''
        </style>
        </head>
        <body>
        <div class="layout-zigzag">
    '''

    middle = ''
    
    for url in range(len(img_urls)):
        each_line = f'''<div class="{default_name+str(url+1)}">\n'''
        img_src = f'<img src="{img_urls[url]}">\n'
        end_line = f'''</div>\n'''
        middle += each_line + img_src + end_line

    end = '''
        </div>
    </body>
    </html>
    '''

    return front + front_second + middle + end
