${ include("header", conn=conn) }$

<div class="boxhead">
	<h2>Forward Memo</h2>
</div>
<div class="boxbody">

Enter the account you wish to forward the memo to and click Forward.

<form action="forward_commit" method="POST">
	<input name="message_id" type="hidden" value="${ emit(message_id) }$">
	<input name="to" type="text" value="${ emit(to) }$">
	<input type="submit" value="Forward"><br><br>
</form>

</div>

${ include("footer") }$
