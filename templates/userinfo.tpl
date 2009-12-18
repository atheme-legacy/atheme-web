${ include("header") }$

<div style="width: 49%; margin-left: 0.5em; float: right;">

<div class="boxhead">
	<h2>Set Password</h2>
</div>
<div class="boxbody">
	<form action="update_password" method="POST">
	<table width="100%">
		<tr>
			<th>New Password</th>
			<td><input type="password" name="new_password"></td>
		</tr>
		<tr>
			<td colspan="2"><input type="submit" value="Set New Password"></td>
		</tr>
	</table>
	</form>
</div>
	
${ include("footer") }$
