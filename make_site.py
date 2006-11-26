#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Things to do after a commit to the webrepo.

This script is run by the commit-hook.
"""

import os
import time
import traceback

rst2html = "/usr/bin/rst2html.py -g -d -t -s --stylesheet=\"/site.css\" --link-stylesheet %s %s"
svncmd = "svn up"

def make_html():
  for root, dirs, files in os.walk("."):
    for f in files:
      oldname = os.path.join(root,f)
      name, ext = os.path.splitext(oldname)
      if ext == ".rst":
        newname = name + ".html"
        if name == "cv":
          newname += ".en"
        if not os.path.exists(newname) or os.path.getmtime(oldname) > os.path.getmtime(newname):
          os.system(rst2html % (oldname, newname))

TEMPLATE="""
%s
%s

%s

.. Autogenerated at %s
"""

def extract_title(filename):
  f = open(filename,"r")
  for line in f:
    if line.startswith("<title>"):
      return line[7:-9]

TEXTLINE = "* `%s`_"
LINKLINE = ".. _`%s`: %s"

def files_to_list(files):
  texts = list()
  links = list()
  for title, filename in files:
    texts.append( TEXTLINE % title )
    links.append( LINKLINE % (title, filename) )
  return "%s\n\n%s\n" % ( "\n".join(texts), "\n".join(links) )
  
def make_index(directory):
  files = list()
  indexfile = os.path.join(directory,"index.rst")
  if os.path.exists(indexfile):
    indextime = os.path.getmtime(indexfile)
  else:
    indextime = 0
  for f in os.listdir(directory):
    name, ext = os.path.splitext(f)
    if ext == ".html" and not name == "index":
      files.append( (extract_title(os.path.join(directory,f)), f) )
  if len(files) > 0:
    index = open(indexfile,"w")
    title = "Documents in %s" % directory.title()
    text = TEMPLATE % ( title, "="*len(title),
                        files_to_list(files),
                        time.asctime() )
    index.write( text )
    index.close()
    name, ext = os.path.splitext(indexfile)
    newname = name + ".html"
    os.system(rst2html % (indexfile, newname))

def update():
  os.system(svncmd)

if __name__ == "__main__":
  if os.path.exists("/tmp/commit-hook.log"):
    os.chdir("/var/www/localhost/htdocs")
    update()
    make_html()
    make_index("musings")
    os.unlink("/tmp/commit-hook.log")
