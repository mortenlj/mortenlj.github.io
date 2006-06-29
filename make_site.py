#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Things to do after a commit to the webrepo.

This script is run by the commit-hook.
"""

import os
import time
import traceback

logfile = open("/tmp/commit-hook.log","a")

rst2html = "/usr/bin/rst2html.py -g -d -t -s --stylesheet=\"/site.css\" --link-stylesheet %s %s"

def make_html():
  logfile.write("make_html\n")
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
Documents in %s
===============

%s

.. Autogenerated at %s
"""

def extract_title(filename):
  logfile.write("extract_title\n")
  f = open(filename,"r")
  for line in f:
    if line.startswith("<title>"):
      return line[7:-8]

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
  logfile.write("make_index\n")
  files = list()
  indexfile = os.path.join(directory,"index.rst")
  if os.path.exists(indexfile):
    indextime = os.path.getmtime(indexfile)
  else:
    indextime = 0
  for f in os.listdir(directory):
    name, ext = os.path.splitext(f)
    if ext == ".html" and os.path.getmtime(os.path.join(directory,f)) > indextime:
      files.append( (extract_title(os.path.join(directory,f)), f) )
  if len(files) > 0:
    index = open(indexfile,"w")
    text = TEMPLATE % ( directory.title(),
                        files_to_list(files),
                        time.strftime() )
    index.write( text )
    index.close()

def svn_update():
  logfile.write("svn_update\n")
  os.system("/usr/bin/svn up --username mortenlj --password 1024epcy")
  
if __name__ == "__main__":
  try:
    os.chdir("/var/www/localhost/htdocs")
    svn_update()
    make_index("musings")
    make_html()
  except:
    logfile.write(traceback.format_exc())
