${ include("header") }$

${ channel_info = conn.chanserv.get_channel_info(channel) }$

<div style="width: 20%; margin-left: 0.5em; float: right;">

<div class="boxhead">
	<h2>Information about ${ emit(channel) }$</h2>
</div>
<div class="boxbody">
	<table width="100%">

${
for k in channel_info.keys():
    emit("<tr><th>%s</th><td>%s</td></tr>" % (k, channel_info[k]))
}$

	</table>
</div>

</div>

${ access_list = conn.chanserv.get_access_list(channel) }$

<div style="width: 79%; margin-right: 0.5em;">

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

</div>

${ include("footer") }$
