<html>
<head>
	<title>Registration</title>
	<link rel="stylesheet" href="/static/style.css" type="text/css">
</head>
<body>

	<div style="margin-top: 20%;">
	<center>

		<img src="/static/logo.png">

		<form action="process_registration" method="post">

		<div style="width: 20%">

			<div class="boxhead">
				<h2>Registration</h2>
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
					<td>E-Mail Address</td>
					<td><input name="email" type="email"></td>
				</tr>

				<tr>
					<td colspan="2" style="text-align: center;">
						<input value="Register Account" type="submit">
					</td>
				</tr>
	
				</table>
			</div>

		</div>

		</form>

	</center>
	</div>
	
</body>
</html>
