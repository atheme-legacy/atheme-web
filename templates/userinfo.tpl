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

</div>

<div style="width: 49%; margin-right: 0.5em;">

${ user_info = conn.nickserv.get_info(conn.username) }$

<div class="boxhead">
	<h2>Information about ${ emit(conn.username) }$</h2>
</div>
<div class="boxbody">
	<table>
${
for k in user_info.keys():
    emit("<tr><th>%s</th><td>%s</td></tr>" % (k, user_info[k]))
}$
	</table>
</div>

</div>
	
${ include("footer") }$
