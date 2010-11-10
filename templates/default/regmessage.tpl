<html>
<head>
	<title>Registration</title>
	<link rel="stylesheet" href="/static?file=style.css" type="text/css">
</head>
<body>

	<div style="margin-top: 20%;">
	<center>

		<img src="/static?file=logo.png">

		<form action="process_registration" method="post">

		<div style="width: 20%;">

			<div class="boxhead">
				<h2>Registration</h2>
			</div>

			<div class="boxbody">
				<div>${ print message }$</div>
				<div><a href="/user/login">Proceed to login</a></div>
			</div>
	
		</div>

		</form>

	</center>
	</div>
	
</body>
</html>
