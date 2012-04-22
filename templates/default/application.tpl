${ import cgi, urllib, hashlib }$
<html>
<head>
	<title>Atheme Services Web Interface</title>
	<link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/themes/base/jquery-ui.css" type="text/css"/>
	<link rel="stylesheet" href="/static/jquery-menu.css" type="text/css">
	<link rel="stylesheet" href="/static/atheme-web.css" type="text/css">
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js"></script>
	<script type="text/javascript" src="/static/jquery-menu.js"></script>
	<script type="text/javascript" src="/static/application.js"></script>
</head>
<body>

${

from athemeweb.classpublisher import webinfo

info = conn.nickserv.get_info(conn.username)

}$

${ include("dialogs", conn=conn, info=info) }$

<header>
	<div id="session">
${
		try:
			email = info['Email']
		except:
			email = 'test@example.com'

		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?" + urllib.urlencode({'s': '40'})
		emit('<img id="avatar" src="%s" alt="%s">' % (gravatar_url, email))
}$
	</div>
	<div id="session-menu-content" style="display: none">
		<ul>
			<li style="line-height: 24px; vertical-align: middle; margin-bottom: 5px;">
${
		try:
			email = info['Email']
		except:
			email = 'test@example.com'

		gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?" + urllib.urlencode({'s': '24'})
		emit('<img id="miniav" src="%s" alt="%s" style="float: left; margin-right: 5px;"> <span style="font-weight: bold">%s</span></li>' % (gravatar_url, email, conn.username))
}$
			</li>
			<li><a href="#" onClick="$('#change-password-dialog').dialog('open')">change password</a></li>
			<li><a href="/user/logout">logout</a></li>
		</ul>
	</div>
	<h1 id="logo">Atheme Web</h1>
</header>

${ include("menu", conn=conn, info=info) }$

<div id="content"></div>

</body>
</html>
