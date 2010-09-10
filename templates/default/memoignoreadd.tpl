${ include("header", conn=conn) }$

<div class="boxhead">
	<h2>Add Memo Ignore</h2>
</div>
<div class="boxbody">

Enter the account you wish to add to the ignore list and click Ignore.

<form action="ignore_add_commit" method="POST">
	<input name="account" type="text">
	<input type="submit" value="Ignore"><br><br>
</form>

</div>

${ include("footer") }$
