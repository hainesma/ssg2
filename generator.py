#!/usr/bin/env python3
import os
import glob
import markdown

if not os.path.exists('public'):
    os.mkdir('public')

for f in glob.iglob('book/*.md'):
    with open(f, 'r') as file:
        raw = file.read()
        html = markdown.markdown(raw)

    file_name = os.path.basename(f)
    destination = os.path.join("public", os.path.splitext(file_name)[0] + ".html")

    with open(destination, 'w') as file:
        file.write(r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>hainesma</title>
  <link href='https://fonts.googleapis.com/css?family=Open+Sans&display=swap' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
<header>
<svg width="400" height="200">
<polygon class="yard" points="
15 140
0 200
400 200
350 140
115 140
"></polygon>
<polygon class="house" points="
25 83
25 150
115 150
115 68
78 30
25 83
"></polygon>
<polyline class="roof" points="
10 98
78 30
130 83
"></polyline>
<polygon class="chimney" points="
46 62
46 22
54 22
54 54
46 62
"></polygon>
<rect class="door" x="43" y="93" width="18" height="57"></rect>
<rect class="window" x="82" y="93" width="15" height="21"></rect>
<rect class="window" x="63" y="57" width="15" height="22"></rect>
<ellipse class="smoke" cx="47" cy="18" rx="4" ry="2"/>
    <animate attributeName="cx" values="47;40;47" dur="7s" repeatCount="indefinite" />
</ellipse>
<ellipse class="smoke" cx="40" cy="12" rx="6" ry="3"/>
    <animate attributeName="cx" values="40;30;40" dur="10s" repeatCount="indefinite" />
</ellipse>
<ellipse class="smoke" cx="28" cy="5" rx="8" ry="4"/>
    <animate attributeName="cx" values="28;13;28" dur="14s" repeatCount="indefinite" />
</ellipse>
</svg>
''')
        file.write(html)
        file.write(r'''
</header>
</body>
</html>''')