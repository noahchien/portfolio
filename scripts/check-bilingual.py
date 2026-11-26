from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import re
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):super().__init__();self.refs=[];self.ids=[];self.lang=None;self.text=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='html':self.lang=a.get('lang')
        if 'id' in a:self.ids.append(a['id'])
        for key in ('href','src'):
            if key in a:self.refs.append(a[key])
    def handle_data(self,data):self.text.append(data)
for name,lang,switch in [('index.html','zh-Hant','en.html'),('en.html','en','index.html')]:
    p=Page();p.feed((root/'docs'/name).read_text(encoding='utf8'))
    assert p.lang==lang,(name,p.lang)
    assert switch in p.refs,(name,'language switch absent')
    assert len(p.ids)==len(set(p.ids)),(name,'duplicate ids')
    for ref in p.refs:
        u=urlsplit(ref)
        if u.scheme or ref.startswith('#'):continue
        assert (root/'docs'/u.path).exists(),(name,ref)
    if lang=='en':assert not re.search('[\u3400-\u9fff]',''.join(t for t in p.text if t.strip()!='中文')), 'Untranslated visible English text'
for file in root.rglob('*.en.md'):
    if '.git' in file.parts:continue
    for ref in re.findall(r'\]\(([^)]+)\)',file.read_text(encoding='utf8')):
        if urlsplit(ref).scheme or ref.startswith('#'):continue
        assert (file.parent/ref).exists(),(file,ref)
print('Both language pages, language switches, English copy, and local document links passed.')
