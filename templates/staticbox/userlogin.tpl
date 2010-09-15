${ include("header", conn=None) }$

	<div style="margin-top: 17%;">
	<center>

		<form action="process_login" method="post">

		<table width="350" style="background: #ddd; border-radius: 1em; -moz-border-radius: 1em; -webkit-border-radius: 1em; padding: 1em;">

			<tr>
				<td>Account name:</td>
				<td><input name="nickname" type="text" style="width: 100%"></td>
			</tr>

			<tr>
				<td>Password:</td>
				<td><input name="password" type="password" style="width: 100%"></td>
			</tr>

			<tr>
				<td colspan="2" style="text-align: center;">
					<input value="Log in" type="submit">
				</td>
			</tr>
	
		</table>

		</form>

	</center>
	</div>
	
${ include("footer") }$
