"""Produce a complete English static page; fail if Chinese copy lacks a translation."""
from html.parser import HTMLParser
from html import escape
from pathlib import Path
import json, re

root=Path(__file__).resolve().parents[1]
translations=json.loads((root/'scripts/translations.en.json').read_text(encoding='utf8'))
missing=set()
def translate(value):
    stripped=value.strip()
    if stripped in translations:
        return value[:len(value)-len(value.lstrip())]+translations[stripped]+value[len(value.rstrip()):]
    if re.search('[\u3400-\u9fff]',value):missing.add(value)
    return value
class EnglishPage(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=False);self.parts=[]
    def handle_decl(self,decl):self.parts.append('<!'+decl+'>')
    def handle_starttag(self,tag,attrs):
        output=[]
        for key,value in attrs:
            if value is not None:
                if key=='lang':value='en'
                elif key=='href' and value=='en.html':value='index.html'
                elif key=='href' and value.endswith('/about.md'):value=value.replace('/about.md','/about.en.md')
                elif key=='href' and '/projects/' in value and value.endswith('.md'):value=value[:-3]+'.en.md'
                elif key=='content' and value.endswith('/assets/cover.svg'):value=value.replace('cover.svg','cover-en.svg')
                elif key=='hreflang' and value=='en':value='zh-Hant'
                elif key=='aria-label' and value=='English version':value='中文版'
                elif key=='data-language':value='en'
                else:value=translate(value)
            output.append(key if value is None else key+'="'+escape(value,quote=True)+'"')
        self.parts.append('<'+tag+(' '+' '.join(output) if output else '')+'>')
    def handle_startendtag(self,tag,attrs):self.handle_starttag(tag,attrs);self.parts[-1]=self.parts[-1][:-1]+'/>'
    def handle_endtag(self,tag):self.parts.append('</'+tag+'>')
    def handle_data(self,data):self.parts.append(escape(translate(data),quote=False))
    def handle_entityref(self,name):self.parts.append('&'+name+';')
    def handle_charref(self,name):self.parts.append('&#'+name+';')
    def handle_comment(self,data):self.parts.append('<!--'+data+'-->')
p=EnglishPage();p.feed((root/'docs/index.html').read_text(encoding='utf8'))
if missing:raise SystemExit('Missing translations: '+json.dumps(sorted(missing),ensure_ascii=True))
english=''.join(p.parts).replace('>English</a>','>中文</a>').replace('id="diagram-center" x="115" y="151">Engineering','id="diagram-center" x="115" y="151">Build')
english=english.replace('src="site.js"','src="site.js"')
(root/'docs/en.html').write_text(english,encoding='utf8')
print('English page generated; untranslated Chinese strings: 0')
