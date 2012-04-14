${ import cgi, urllib, hashlib }$
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

info = conn.nickserv.get_info(conn.username)

}$

<header>
	<div id="session">
${
		try:
			email = info['Email']
		except:
			email = 'test@example.com'

		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?" + urllib.urlencode({'s': '40'})
		emit('<img src="%s" alt="%s">logged in as <strong>%s</strong>.' % (gravatar_url, email, conn.username))
}$
		<br><a href="/user/logout">logout</a>
	</div>
	<h1 id="logo">Atheme Web</h1>
</header>

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
