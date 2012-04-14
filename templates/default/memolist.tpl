${ include("header", conn=conn) }$

<div style="width: 20%; margin-left: 0.5em; float: right;">

<div class="boxhead">
        <h2>Actions</h2>
</div>
<div class="boxbody">
	<div style="text-align: center"><a href="/user/memo/ignore_add">Add Ignore</a></div>
	<div style="text-align: center"><a href="/user/memo/ignore_list">View Ignore List</a></div>
	<div style="text-align: center"><a href="/user/memo/ignore_clear">Clear Ignore List</a></div>
	<div style="text-align: center"><a href="/user/memo/write">Write Memo</a></div>
</div>

</div>

<div style="width: 79%; margin-right: 0.5em;">

${ include("memolistbase", conn=conn) }$

</div>

${ include("footer") }$
