${ include("header", conn=conn) }$

${ list = conn.nickserv.list_own_access() }$

<div class="boxhead">
	<h2>Channels You Have Access To</h2>
</div>
<div class="boxbody">
<table width="100%">

<tr>
	<th>Channel</th>
	<th>Access Flags</th>
	<th>Options</th>
</tr>
	${
	    for chan in list:
                from urllib import quote_plus
                chan['channelurl'] = quote_plus(chan['channel'])
                emit("<tr><td>%(channel)s</td><td>%(flags)s</td><td><a href='info?channel=%(channelurl)s'>more info</a></td></tr>" % chan)
	}$

</table>
</div>

${ include("footer") }$
