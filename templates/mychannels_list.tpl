${ include("header") }$

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
                emit("<tr><td>%(channel)s</td><td>%(flags)s</td><td><a href='#'>more info</a></td></tr>" % chan)
	}$

</table>
</div>

${ include("footer") }$
