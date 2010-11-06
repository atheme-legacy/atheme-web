${ include("header", conn=conn) }$

${ list = conn.memoserv.ignore_list() }$

<div style="width: 20%; margin-left: 0.5em; float: right;">

<div class="boxhead">
        <h2>Actions</h2>
</div>
<div class="boxbody">
        <div style="text-align: center"><a href="ignore_add">Add Ignore</a></div>
        <div style="text-align: center"><a href="ignore_list">View Ignore List</a></div>
        <div style="text-align: center"><a href="ignore_clear">Clear Ignore List</a></div>
        <div style="text-align: center"><a href="write">Write Memo</a></div>
</div>

</div>

<div style="width: 79%; margin-right: 0.5em;">

<div class="boxhead">
	<h2>Memo Ignore List</h2>
</div>
<div class="boxbody">
<table width="100%">

<tr>
	<th>ID</th>
	<th>Account</th>
	<th>Actions</th>
</tr>
	${
	    i = 1
	    for memo in list:
                memo['id'] = i
                emit("<tr><td>%(id)s</td><td>%(account)s</td><td><a href='ignore_delete?account=%(account)s'>delete</a></tr>" % memo)
                i = i + 1
	}$

</table>
</div>

</div>

${ include("footer") }$
