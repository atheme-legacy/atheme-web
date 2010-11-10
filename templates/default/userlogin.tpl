<html>
<head>
	<title>Login</title>
	<link rel="stylesheet" href="/static?file=style.css" type="text/css">
</head>
<body>

	<div style="margin-top: 20%;">
	<center>

		<img src="/static?file=logo.png">

		<form action="process_login" method="post">

		<div style="width: 20%">

			<div class="boxhead">
				<h2>Login</h2>
			</div>

			<div class="boxbody">

				<table width="100%" style="font-size: 100%">

				<tr>
					<td>Nickname</td>
					<td><input name="nickname" type="text"></td>
				</tr>

				<tr>
					<td>Password</td>
					<td><input name="password" type="password"></td>
				</tr>

				<tr>
					<td>
						<a href="/user/register">Register</a>
					</td>

					<td>
						<input value="Log in" type="submit">
					</td>
				</tr>
	
				</table>

			</div>

		</form>

	</center>
	</div>
	
</body>
</html>
