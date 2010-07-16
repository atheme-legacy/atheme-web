${ include("header") }$

<div class="boxhead">
	<h2>Write Memo</h2>
</div>
<div class="boxbody">

<table width="100%">

<form action="write_commit" method="POST">

<tr>
	<th>To</th>
	<td><input name="to" type="text" value="${ emit(to) }$"></td>
</tr>

<tr>
	<th>Message</th>
	<td><input name="message" type="text"></td>
</tr>

<tr>
	<td colspan="2"><input type="submit" value="Send Memo"></td>
</tr>

</form>

</div>

${ include("footer") }$
