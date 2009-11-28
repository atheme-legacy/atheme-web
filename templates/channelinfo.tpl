${ include("header") }$

${ access_list = conn.chanserv.get_access_list(channel) }$

<div class="boxhead">
	<h2>Access List for ${ emit(channel) }$</h2>
</div>
<div class="boxbody">
<table width="100%">

<tr>
	<th>Entry</th>
	<th>Nickname / Hostmask</th>
	<th>Access Flags</th>
	<th>Options</th>
</tr>
	${
	    for chan in access_list:
                from urllib import quote_plus
                chan['channelurl'] = quote_plus(channel)
                emit("<tr><td>%(id)s</td><td>%(nick)s</td><td>%(flags)s</td><td><a href='edit_flags?channel=%(channelurl)s&nick=%(nick)s'>edit flags</a> - <a href='remove_flags?channel=%(channelurl)s&nick=%(nick)s'>remove flags</a></td></tr>" % chan)
	}$

</table>
</div>

${ include("footer") }$
