New Blog Software Again!
========================

I've been using tumblr_ for awhile and while its useful when posting
random stuff I should've posted to Facebook instead (images, links, videos,
etc.), writing my text in HTML was just icky. Markdown isn't a huge
improvement and I was really itching to write all my posts in reST_ as I
already know it quite well from writing my docs using Sphinx_.

I considered using blogofile_, but it seems to be
abandoned and it's not trivial to add normal reST_ style code highlighting.
Then I saw tinkerer_, which is basically just a few
extensions on top of Sphinx_... perfect!

The Migration
-------------

For anyone considering migrating from tumblr_, here's my simple dump
script that pulled all my posts I cared about out of tumblr_ and dropped them
into directories for tinkerer_ ::

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
                    body = html2rst(post['body'].encode('utf-8').replace('’', "'"))
                    f.writelines([body, '\n\n'])
                elif post['type'] == 'link':
                    desc = html2rst(post['description'].replace('’', "'").encode('utf-8'))
                    f.writelines(['Link: `%s <%s>`_\n\n' % (post['title'].encode('utf-8'), post['url'].encode('utf-8'))])
                    f.write(desc + '\n\n'),
                f.writelines([
                    '.. author:: default\n', '.. categories:: %s\n' % ', '.join(post['tags']),
                    '.. comments::\n', '   :url: %s' % post['post_url']
                ])
        return post_links

It's quite nice that I get all the Sphinx_ extensions for use
in my blog, and there's no more mental context switching to write a blog
post vs. writing project documentation for my open-source projects.

Dropping a graphviz diagram into my blog also became trivial.

.. graphviz::

   digraph foo {
       "awesome" -> "sphinx";
       "awesome" -> "tinkerer";
   }

The Bad News
------------

It's not perfect, tinkerer_ is still very beta. But I can wrap my head around
it, and its easy to extend. I've already made a `little modification in my own
fork <https://bitbucket.org/bbangert/tinkerer>`_ which allows me to specify
URL's for the comments to ensure I get the right disqus threads on the old
blog posts I ported. This wasn't a flawless process due to how the main
reactions and comments thing on the main pages look, they're a bit off for the
legacy posts... but at least the comments and such show up fine once you
click in so I'll live with it.

There's no category specific RSS feeds at the moment, so I'll need to hack that
in so that I can get relisted on the Python aggregators. I also will likely
update the theme, right now I'm just using 'minimal' which isn't bad.

Since this is more for just posts, I dropped the other tumblr_ things like
links and videos to retain just **content**. I don't think this is too negative
but some might want all the types tumblr_ supports.

Overall, I'm quite happy with it thus far. We'll see how I feel in a few
months, and hopefully I'll be blogging more since there's less friction involved
since I get to use the Sphinx_ tools I'm quite familiar with.


.. _blogofile: http://www.blogofile.com/
.. _tinkerer: http://tinkerer.me/
.. _Sphinx: http://sphinx.pocoo.org/
.. _reST: http://docutils.sourceforge.net/rst.html
.. _tumblr: http://tumblr.com/

.. author:: default
.. categories:: python, sphinx
.. comments::
