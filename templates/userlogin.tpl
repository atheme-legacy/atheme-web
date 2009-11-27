<html>
<head>
	<title>Login</title>
	<link rel="stylesheet" href="/static?file=style.css" type="text/css">
</head>
<body style='background: #cacaca;'>

	<div style="margin-top: 20%;">
	<center>

		<img src="/static?file=logo.png">

		<form action="process_login" method="post">

		<table width="350" style="background: #dddddd; border: 1px #999 solid;">

			<tr>
				<td>Nickname</td>
				<td><input name="nickname" type="text"></td>
			</tr>

			<tr>
				<td>Password</td>
				<td><input name="password" type="password"></td>
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
	
</body>
</html>
