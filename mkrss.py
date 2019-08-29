
# pip install feedgen
from feedgen.feed import FeedGenerator
import os,sys,re,subprocess
import datetime

#title:  "Sincere Flattery in the Early Arcade Industry"
re_title  = re.compile('^title: \s+"(.+)"', re.M)
re_title2 = re.compile('^#\s+(.+)', re.M)
re_text   = re.compile('^(\w.+)$', re.M)

ROOTURL = 'https://mywebsite.com/blog/'
AUTHOR = {'name':'8bitworkshop','email':'info@8bitworkshop.com'}

fg = FeedGenerator()
fg.id(ROOTURL)
fg.title('My Blog')
fg.language('en')
fg.link(href=ROOTURL+'feed.xml', rel='self')
fg.description('The online IDE for 8-bit retro developers.')

for fn in sys.argv[1:]:
    title = None
    s = open(fn,'r').read()
    if s.find('markdeep.') < 0:
        print(fn + " has no markdeep")
        continue
    m = re_title.search(s)
    if m:
        title = m.group(1)
    m = re_title2.search(s)
    if m:
        title = m.group(1)
    if not title:
        print(fn + " has no title")
        continue
    id = ROOTURL + fn
    m = re_text.findall(s)
    desc = ' '.join(m)
    fe = fg.add_entry()
    fe.id(id)
    fe.title(title)
    ctime = os.path.getctime(fn)
    fe.updated(str(datetime.datetime.fromtimestamp(ctime)) + " +0000")
    fe.description(desc)
    fe.author(AUTHOR)
    fe.link( href=id )

fg.atom_file('feed.xml', pretty=True) # Write the ATOM feed to a file
fg.rss_file('rss.xml', pretty=True) # Write the RSS feed to a file
print("Done.")

