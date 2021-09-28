import os
# used to retrieve files matching a specified pattern
import glob
import markdown
import yaml
import frontmatter

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
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
    <title>hainesma.com</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Abel&family=Fira+Code:wght@400;500&family=Montserrat:ital,wght@0,300;1,300&family=Pragati+Narrow:wght@400;700&display=swap" rel="stylesheet">
    <script src="https://kit.fontawesome.com/0959eabcb3.js" crossorigin="anonymous"></script>
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
<footer>
<div id="footer-content">
<a href="https://github.com/hainesma">
<i class="fab fa-github"></i>
</a>
<a href="https://www.linkedin.com/in/hainesma/ssg2">
<i class="fab fa-linkedin"></i>
</a>
<h6>
&#169 Mark Haines
</h6>
</div>
</footer>
</body>
</html>''')