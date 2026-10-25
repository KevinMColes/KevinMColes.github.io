"""Check the static site using only Python's standard library."""
from pathlib import Path
from html.parser import HTMLParser
import json, re
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.links=[];self.h1=0;self.ids=set();self.canonical=[];self.images=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a: self.ids.add(a['id'])
  if t=='h1': self.h1+=1
  if t=='a':self.links.append(a.get('href',''))
  if t=='img':self.images.append(a)
  if t=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href'))
pages=['index.html','about/index.html','speaking/index.html','book/index.html','media/index.html']
for name in pages:
 text=(root/name).read_text();p=Page();p.feed(text)
 assert p.h1==1,(name,'expected one H1')
 route='/' if name=='index.html' else '/'+name.removesuffix('index.html')
 assert p.canonical==['https://kevinmcoles.com'+route],(name,p.canonical)
 assert 'data:image' not in text and '<button' not in text,(name,'leftover mockup control or embedded image')
 assert ' hidden' not in text and '<form' not in text,(name,'hidden page or fake form')
 assert not re.search(r'\bKevin Coles\b',text),(name,'missing middle initial')
 graph=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',text,re.S).group(1))['@graph']
 person=next(g for g in graph if g['@type']=='Person')
 assert person['name']=='Kevin M. Coles' and person['@id']=='https://kevinmcoles.com/#person'
 for link in p.links:
  if link.startswith(('https://','mailto:')):continue
  path,_,fragment=link.partition('#')
  target=(root/path.lstrip('/')) if path else root/name
  if target.is_dir():target=target/'index.html'
  assert target.is_file(),(name,'missing link',link)
  if fragment:
   q=Page();q.feed(target.read_text());assert fragment in q.ids,(name,'missing anchor',link)
 for image in p.images:
  assert (root/image['src'].lstrip('/')).is_file(),(name,'missing image')
  assert image.get('alt') and image.get('width') and image.get('height'),(name,'image metadata')
 assert text.count('aria-current="page"')==1,(name,'navigation active state')
 print('PASS',name)
assert (root/'CNAME').read_text().strip()=='kevinmcoles.com'
assert (root/'downloads/the-first-ten-minutes.pdf').is_file()
print('PASS domain, retained download, all local links, image assets and structured data')

for name in ['index.html','book/index.html']:
 text=(root/name).read_text()
 assert text.count('data-uid="6c1df4a9a1"')==1,(name,'expected one real Kit embed')
 assert 'https://kevin-m-coles.kit.com/6c1df4a9a1/index.js' in text
 assert 'id="updates"' in text
print('PASS real Kit embeds on Home and Book')
