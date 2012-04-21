<html>
<head>
	<title>Login</title>
	<link rel="stylesheet" href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/themes/base/jquery-ui.css" type="text/css"/>
	<link rel="stylesheet" href="/static/atheme-web.css" type="text/css">
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
	<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.18/jquery-ui.min.js"></script>
	<script type="text/javascript" src="/static/application.js"></script>
</head>
<body>

	<div style="margin-top: 20%;">
	<center>

		<img src="/static/logo.png">

		<div id="tabs" style="width: 20%">
		<ul>
			<li><a href="#login">Login</a></li>
			<li><a href="#register">Register</a></li>
		</ul>

		<div id="login">

		<form action="process_login" method="post">
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
				<td colspan="2" style="text-align: center;">
					<input value="Log in" type="submit">
				</td>
			</tr>
	
			</table>
		</form>

		</div>

		<div id="register">

		<form action="process_registration" method="post">
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
		</form>

		</div>

		</div>
	</center>
	</div>
</body>
</html>
