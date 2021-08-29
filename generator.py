import os
# used to retrieve files matching a specified pattern
import glob
import markdown

if not os.path.exists('public'):
    os.mkdir('public')

# collect all the .md files in the 'book' folder
for f in glob.iglob('book/*.md'):
    # take each markdown file (in 'read' mode) and store it as 'file'
    with open(f, 'r') as file:
        # read the contents of each file and store said contents as 'raw'
        raw = file.read()
        # convert the content into HTML and store it as 'html'
        html = markdown.markdown(raw)
    # store the basename of the markdown file as 'file_name'
    file_name = os.path.basename(f)
    # build the file path for the new HTML file and store it as 'destination'
    destination = os.path.join("public", os.path.splitext(file_name)[0] + ".html")
    # take each newly created file path (in 'write' mode) 
    with open(destination, 'w') as file:
        # write to the file the substance of the template as well as the newly converted HTML
        file.write('''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>hainesma.com</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
<header id="header">
<a id="homelink" href="index.html">

<img id="icon" src="./static/house.png">

<span id="hainesma">hainesma.com</span>
</a> 

</header>
<div id="main">
''')
        file.write(html)
        file.write('''
</div>
</body>
</html>''')