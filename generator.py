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
15 40
15 85
75 85
75 30
"></polyline>
<polyline points="
5 50
50 5
85 40
"></polyline>
<polyline points="
30 25
30 2
35 2
35 20
"></polyline>
<rect x="25" y="48" width="12" height="37"></rect>
<rect x="53" y="48" width="10" height="14"></rect>
<rect x="38" y="23" width="9" height="15"></rect>
</svg>
''')
        file.write(html)
        file.write(r'''
</header>
</body>
</html>''')