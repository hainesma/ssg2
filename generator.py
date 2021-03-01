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
<svg width="300" height="200">
<polyline points="
25 75
25 165
145 165
145 55
"></polyline>
<polyline points="
5 95
95 5
165 75
"></polyline>
<polyline points="
55 45
55 2
65 2
65 35
"></polyline>
<rect x="45" y="98" width="23" height="67"></rect>
<rect x="100" y="98" width="20" height="25"></rect>
<rect x="70" y="45" width="18" height="30"></rect>
</svg>
''')
        file.write(html)
        file.write(r'''
</header>
</body>
</html>''')