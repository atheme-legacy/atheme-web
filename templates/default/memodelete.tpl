${ include("header", conn=conn) }$

${ memo = conn.memoserv.read(id) }$

<p>This memo will be deleted:</p>

<table width="100%">

<tr>
	<th>ID</th>
	<td>${ emit(id) }$</th>
</tr>

<tr>
	<th>From</th>
	<td>${ emit(memo['from']) }$</th>
</tr>

<tr>
	<th>Sent On</th>
	<td>${ emit(memo['sent']) }$</th>
</tr>

<tr>
	<th>Memo Text</th>
	<td>${ emit(memo['message']) }$</th>
</tr>

</table>

<p>Are you sure you wish to delete it?</p>

<a href="/user/memo/delete_confirm?id=${ emit(id) }$">Yes</a><br>
<a href="/user/memo/list">No</a>

${ include("footer") }$
