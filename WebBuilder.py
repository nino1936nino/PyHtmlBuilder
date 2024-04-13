import FuncOfCode
from FuncOfCode import Html
import os

def up_bar():
    title = input('What do you want to write in the big bar?: ')
    with open('projects/'+webname+'/style.txt', 'a') as f:
             f.write('.big-bar{\n')
             f.write('    background-color: #333;\n')  
             f.write('    color: #fff;\n')
             f.write('    padding: 20px;\n')
             f.write('    text-align: center;\n')
             f.write('    font-size: 24px;\n')
             f.write('}\n')
    with open('projects/'+webname+'/body.txt', 'a') as f:
             f.write('<div class="big-bar">\n')
             f.write('<h1>'+title+'</h1>\n')


answer = input('do you want to create a website?' )


if answer == ('yes'): 
        webname = input ('how are you calling your website?')
        folder_path = 'projects/'+webname
        os.makedirs(folder_path)
    
        with open('projects/'+webname+'/head.txt', "a") as f:
            f.write("<!DOCTYPE html>\n")
            f.write('<html lang="en">\n')
            f.write("<html>\n")
            f.write(' <meta charset="UTF-8">\n')
            f.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
            f.write('<title>'+webname+'</title>\n')
        with open('projects/'+webname+'/style.txt', "a") as f:
            f.write('<style>\n')        
        with open('projects/'+webname+'/body.txt', "a") as f:
            f.write('</style>\n')
            f.write('<body>\n')
        with open('projects/'+webname+'/body2.txt', "a") as f:
            f.write('</body>\n')

        while True: 
            answer = input('what do you want to do? ')
            if answer.lower() == 'up_bar':
                up_bar()
            if answer.lower() == 'centerinfo':
                text = input('What do you want to write')
                html_instance = Html(webname , text) 
                html_instance.CenterInfo()
            if answer.lower()== 'close':
                break
            if answer.lower() == "compile":
                with open('projects/'+webname+'/head.txt', 'r') as f:
                 source_text = f.read()
                with open('projects/'+webname+'/index.html', 'w') as f:
                 f.write(source_text)
                with open('projects/'+webname+'/style.txt', 'r') as f:
                 source_text = f.read()
                with open('projects/'+webname+'/index.html', 'a') as f:
                    f.write(source_text)
                with open('projects/'+webname+'/body.txt', 'r') as f:
                    source_text = f.read()
                with open('projects/'+webname+'/index.html', 'a') as f:
                    f.write(source_text)
                with open('projects/'+webname+'/body.txt', 'r') as f:
                 source_text = f.read()
                with open('projects/'+webname+'/index.html', 'a') as f:
                 f.write(source_text)


                                       
                    
elif answer != ('yes'.lower()):
    print('I see you do not want to create a website')      
    

