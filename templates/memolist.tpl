${ include("header") }$

${ list = conn.memoserv.list() }$

<table width="100%">

<tr>
	<th>ID</th>
	<th>From</th>
	<th>Sent</th>
</tr>
	${
	    i = 1
	    for memo in list:
                memo['id'] = i
                emit("<tr><td><a href='read?id=%(id)s'>%(id)s</a></td><td>%(from)s</td><td>%(sent)s</td></tr>" % memo)
                i = i + 1
	}$

</table>

<a href="/user/dashboard">Return to dashboard</a>

${ include("footer") }$
