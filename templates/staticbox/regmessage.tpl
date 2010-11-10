${ include("header", conn=None) }$

	<div style="margin-top: 17%;">
	<center>

		<form action="process_login" method="post">

		<table width="350" style="background: #ddd; border-radius: 1em; -moz-border-radius: 1em; -webkit-border-radius: 1em; padding: 1em;">

			<tr>
				<th colspan="2">Registration</th>
			</tr>

			<tr>
				<td>${ print message }$</td>
			</tr>

			<tr>
				<td><a href="/user/login">Proceed to login</a></td>
			</tr>

		</table>

		</form>

	</center>
	</div>
	
${ include("footer") }$
