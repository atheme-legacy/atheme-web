${ import cgi }$
<html>
<head>
	<title>services.staticbox.net</title>
	<link rel="stylesheet" href="/static?file=staticbox-style.css" type="text/css">
</head>
<body>
${

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

for page in set.keys():
    emit('<li><a href="/user/%s">%s</a></li>' % (page, set[page]['title']))

}$
			<li><a href="/user/account">My Account</a></li>
			<li><a href="/user/channel/list">My Channels</a></li>
			<li><a href="/user/memo/list">Memo List</a></li>
			<li><a href="/user/memo/ignore_list">Memo Ignores</a></li>
			<li><a href="/user/memo/write">Write Memo</a></li>
			<li><a href="/user/logout">Logout</a></li>
		</ul>
	</div>
	<img src="/static?file=staticbox-logo.png" alt="StaticBox">
</div>
<div id="page">

