${ include("header", conn=conn) }$

${

flags = None
if nick:
    try:
        flags = conn.chanserv.get_access_flags(channel, nick)
    except:
        pass

if flags is None:
    flags = ''

}$

<div class="boxhead">
	<h2>Add / Edit Channel Access Entry</h2>
</div>
<div class="boxbody">

<table width="100%">

<form action="set_flags" method="POST">

<input type="hidden" name="channel" value="${ emit(channel) }$">

<tr>
	<th>User</th>
	<td><input name="nick" type="text" value="${ emit(nick) }$"></td>
</tr>

<tr>
	<th>Flags</th>
	<td><input name="flags" type="text" value="${ emit(flags) }$"></td>
</tr>

<tr>
	<td colspan="2"><input type="submit" value="Change Flags"></td>
</tr>

</form>

</div>

${ include("footer") }$
