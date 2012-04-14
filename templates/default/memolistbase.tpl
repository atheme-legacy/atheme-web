${ list = conn.memoserv.list() }$

<div>

<div class="boxhead">
	<h2>Memo List</h2>
</div>
<div class="boxbody">
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
                emit("<tr><td><a href='/user/memo/read?id=%(id)s'>%(id)s</a></td><td>%(from)s</td><td>%(sent)s</td></tr>" % memo)
                i = i + 1
	}$
</table>
</div>

</div>
