html

<!doctype html>

<html lang="en">
    <head>
        <title>

        </title>
    </head>
    <body>

    </body>
</html>

body commands:
<p> #new paragraph
<br> #\n
<h1/h2/h3> t #the lower the number the bigger the letters
<ul> #creates a list of dots
<ol> #creates a list of ascendant numbers
    <li> #add items to the list
<tr> #creates a table row
    <td> #adds table data
<img src="image name">
<video control muted> #examples
    <source src="video name" type= "video/mp4">
<a href="link.com">Rename The Link</a>
<input>
<button>name</button>
<header class = "(cssClass)">
<main class = "(cssClass)">
<footer class="(cssClass)">
padding-left; #push all content x to right
{{  }} #jinja placeHolder

head commands:
<meta name="viewport" content="initial-scale1, width=device-width"> #adjust the page to the users device
<link href="cssFile.css" rel="stylesheet">
<script> #js code

<form action="/source", method="get">
method="post" #same as get but it doesn't show the input in the url

{% block x %} {% endblock %}
#if declared, extensions will use it to replace it with information
#if used, put the content

{% extendes "file.html" %}
