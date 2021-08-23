
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
                max-width: 600px;
                margin: 0 auto;
                align-self: center;
                justify-content: center;
            }

            .layout-zigzag > div {
                display: flex;
                border-radius: 5px;
                padding: 1em;
                justify-content: center;
                color: #d9480f;
            }
            
            .layout-zigzag {
                display: grid;
                align-self: center;
                justify-content: center;
                grid-template-columns: 1fr 1fr;
            }
            .layout-zigzag div:nth-of-type(even) {
                grid-column: 2;
            }
    '''

    default_name = "style_"
    for idx in range(len(img_urls)):
        overall = ''''''
        next_idx_name = '.'+default_name+str(idx+1)
        grid_row = ''' { grid-row: '''
        grid_row += str(idx+1)
        grid_row += ''';} '''

        overall += overall+next_idx_name+grid_row
        front+= overall

    front_second = '''
        </style>
        </head>
        <body>
        
        <div style="background-color: #f6f5ef;"> 
            <div class="layout-zigzag"> 
    '''

    middle = ''
    
    for url in range(len(img_urls)):
        each_line = f'''<div class="{default_name+str(url+1)}">'''
        img_src = f'<img src="{img_urls[url]}">'
        end_line = f'''</div> '''
        middle += each_line + img_src + end_line

    end = '''
            </div>
        </div>
    </body>
    </html>
    '''

    return front + front_second + middle + end
