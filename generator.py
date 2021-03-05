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
25 63
25 130
115 130
115 48
"></polyline>
<polyline points="
10 78
78 10
130 63
"></polyline>
<polyline points="
48 40
48 2
55 2
55 34
"></polyline>
<rect x="43" y="73" width="18" height="57"></rect>
<rect x="82" y="73" width="15" height="21"></rect>
<rect x="63" y="37" width="15" height="22"></rect>
</svg>
''')
        file.write(html)
        file.write(r'''
</header>
</body>
</html>''')