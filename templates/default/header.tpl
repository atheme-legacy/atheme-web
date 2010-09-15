${ import cgi }$
<html>
<head>
	<title>Atheme Services Web Interface</title>
	<link rel="stylesheet" href="/static?file=style.css" type="text/css">
</head>
<body>
<div id="header">
</div>
${

from athemeweb.classpublisher import webinfo

from athemeweb.pageset import build_page_set 
set = build_page_set(conn)

}$

<ul id="navlinks">
${

for page in set.keys():
    if page in webinfo.environ['SCRIPT_NAME']:
        emit('<li class="selected"><a href="/user/%s">%s</a></li>' % (page, set[page]['title']))
    else:
        emit('<li><a href="/user/%s">%s</a></li>' % (page, set[page]['title']))

}$
</ul>
<div id="content">
