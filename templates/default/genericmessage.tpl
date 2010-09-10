${ include("header", conn=conn) }$

<div class="boxhead">
	<h2>Message</h2>
</div>
<div class="boxbody">
${ emit(message) }$
</div>

${ include("footer") }$
