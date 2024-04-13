import os
class Html:
    
    
    def __init__(self, webname , text):
           self.webname =  webname
           self.text= text
    
    
    def CenterInfo(self):
        with open('projects/'+self.webname+'/style.txt', 'a') as f:
            f.write('.h2{\n')
            f.write('    color: #fff;\n')
            f.write('    text-align: center;\n')
            f.write('    font-size: 18px;\n')
            f.write('}\n')
        with open('projects/'+self.webname+'/body.txt', 'a') as f:
            f.write('<h2>' + self.text + '</h2>\n')
