${ import cgi }$
<html>
<head>
	<title>services.staticbox.net</title>
	<link rel="stylesheet" href="/static?file=staticbox-style.css" type="text/css">
</head>
<body>
${

from athemeweb.classpublisher import webinfo

from athemeweb.pageset import build_page_set 
set = build_page_set(conn)

}$
<div id="wrapper">
<div id="header">
	<div id="rightside">
		<h1>services admin</h1>
		<ul id="links">
			<li><a href="http://staticbox.net/">staticbox</a></li>
			<li><a href="http://services.staticbox.net/">services admin</a></li>
			<li><a href="http://webchat.staticbox.net/">webchat</a></li>
			<li><a href="http://stats.staticbox.net/">statistics</a></li>
${

for page in set:
    if page['path'] in webinfo.environ['SCRIPT_NAME']:
        emit('<li class="selected"><a href="/user/%s">%s</a></li>' % (page['path'], page['title']))
    else:
        emit('<li><a href="/user/%s">%s</a></li>' % (page['path'], page['title']))
}$
		</ul>
	</div>
	<img src="/static?file=staticbox-logo.png" alt="StaticBox">
</div>
<div id="page">

