#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Things to do after a commit to the webrepo."""

import os

rst2html = "rst2html.py -g -d -t -s --stylesheet=\"/site.css\" --link-stylesheet %s %s"

def make_html():
  for root, dirs, files in os.walk("."):
    for f in files:
      oldname = os.path.join(root,f)
      name, ext = os.path.splitext(f)
      if ext == ".rst":
        newname = os.path.join(root,name + ".html")
        if not os.path.exists(newname) or os.path.getmtime(oldname) > os.path.getmtime(newname):
          print "Updating %s" % oldname
          os.system(rst2html % (oldname, newname))

def svn_update():
  os.system("svn up")
  
if __name__ == "__main__":
  #svn_update()
  make_html()
