${ import cgi }$
<html>
<head>
	<title>Atheme Services Web Interface</title>
	<link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/themes/base/jquery-ui.css" type="text/css"/>
	<link rel="stylesheet" href="/static/atheme-web.css" type="text/css">
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js"></script>
	<script type="text/javascript" src="/static/application.js"></script>
</head>
<body>

${

from athemeweb.classpublisher import webinfo

from athemeweb.pageset import build_page_set 
set = build_page_set(conn)

}$

<div id="header">
	<img src="/static/logo.png" alt="Atheme Web Interface">
</div>

<div id="tabs">
<ul>
${

for page in set:
    if page['path'] in webinfo.environ['SCRIPT_NAME']:
        emit('<li class="selected"><a href="/user/%s">%s</a></li>' % (page['path'], page['title']))
    else:
        emit('<li><a href="/user/%s">%s</a></li>' % (page['path'], page['title']))

}$
</ul>
</div>

</body>
</html>
