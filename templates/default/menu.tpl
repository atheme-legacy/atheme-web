${ import cgi, urllib, hashlib }$

<div id="menu">
<ul>
	<li><strong>Account</strong></li>
	<li><a href="/user/account">Overview</a></li>
	<li><a href="/user/account_settings">Change e-mail, settings and preferences</a></li>
	<li><a href="/user/memo/list">Message Inbox</a></li>
</ul>

<ul>
	<li><strong>Channels</strong></li>
	<li><a href="/user/channel/list">Channel List</a></li>
${ list = conn.nickserv.list_own_access() }$
	<li>
		Your channels: ${ emit('') }$
		<ul>
${
	for chan in list:
		emit('<li><a href="/user/channel/info?channel=%s">%s</a></li>' % (urllib.quote_plus(chan['channel']), chan['channel']))
}$
		</ul>
	</li>
</ul>

${
	if conn.has_privilege('general:viewprivs'):
		include("opermenu", conn=conn, info=info)
}$

</div>
