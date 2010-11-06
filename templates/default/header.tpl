${ import cgi }$
<html>
<head>
	<title>Atheme Services Web Interface</title>
	<link rel="stylesheet" href="/static?file=style.css" type="text/css">
</head>
<body>

${

from athemeweb.classpublisher import webinfo

from athemeweb.pageset import build_page_set 
set = build_page_set(conn)

}$

<div id="header">
	<img src="/static?file=logo.png" alt="Atheme Web Interface">

<div id="navbar">
<ul id="links">
${

for page in set:
    if page['path'] in webinfo.environ['SCRIPT_NAME']:
        emit('<li class="selected"><a href="/user/%s">%s</a></li>' % (page['path'], page['title']))
    else:
        emit('<li><a href="/user/%s">%s</a></li>' % (page['path'], page['title']))

}$
</ul>
</div>

</div>

<div id="page">
