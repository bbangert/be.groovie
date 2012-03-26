import json
import re
import os
import subprocess

import requests


date_regex = re.compile(r'(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})')


def pull_posts(blog, api_key):
    api_url = 'http://api.tumblr.com/v2/blog/%s/posts?api_key=%s&limit=2000'
    call_url = api_url % (blog, api_key)
    r = requests.get(call_url)
    posts = json.loads(r.content)
    return posts


def html2rst(html):
    p = subprocess.Popen(['pandoc', '--from=html', '--to=rst'],
                         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return p.communicate(html)[0]


def dump_posts(posts):
    post_links = []
    for post in posts:
        if post['type'] not in ['text']:
            continue
        d = date_regex.match(post['date']).groupdict()
        os.system("mkdir -p %s/%s/%s" % (d['year'], d['month'], d['day']))
        slug = post['post_url'].split('/')[-1].replace('-', '_')
        link = '%s/%s/%s/%s' % (d['year'], d['month'], d['day'], slug)
        post_links.append(link)
        bar = '=' * len(post['title'])
        with open('%s.rst' % link, 'wb') as f:
            print post
            f.writelines([post['title'].encode('utf-8'), '\n', bar, '\n\n'])
            if post['type'] == 'text':
                body = html2rst(post['body'].encode('utf-8'))
                f.writelines([body, '\n\n'])
            elif post['type'] == 'link':
                desc = html2rst(post['description'].encode('utf-8'))
                f.writelines(['Link: `%s <%s>`_\n\n' % (post['title'].encode('utf-8'), post['url'].encode('utf-8'))])
                f.write(desc + '\n\n'),
            f.writelines(['.. author:: default\n', '.. categories:: %s\n' % ', '.join(post['tags']),
                          '.. comments::\n'])
    return post_links
