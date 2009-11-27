${ include("header") }$

${ memo = conn.memoserv.read(id) }$

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

<a href="delete?id=${ emit(id) }$">Delete this memo.</a><br>
<a href="list">Return to memo list.</a>

${ include("footer") }$
