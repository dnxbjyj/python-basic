# coding:utf-8
from jinja2 import Environment,FileSystemLoader
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def main():
    env = Environment(loader = FileSystemLoader('./'))
    tpl = env.get_template('page_template.txt')
    
    with open('page.txt','w+') as fout:
        render_content = tpl.render(my_title = 'My Index Page')
        fout.write(render_content)
        
if __name__ == '__main__':
    main()