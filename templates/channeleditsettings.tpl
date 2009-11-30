${ include("header") }$

${ channel_flags = conn.chanserv.get_channel_flags(channel) }$

<div class="boxhead">
	<h2>Settings for ${ emit(channel) }$</h2>
</div>
<div class="boxbody">
<form action="settings_commit" method="POST">
<input name="channel" type="hidden" value="${ emit(channel) }$">

<center>
<table>
${
def is_checked(flag):
    if flag is True:
        return "checked"
    return ""

for flag in channel_flags.keys():
    emit("<tr><th>%s</th><td><input type='checkbox' name='%s' value='ON' %s></td></tr>" % (flag, flag, is_checked(channel_flags[flag])))
}$
</table>
</center>

<input type="submit" value="Change Settings">

</form>

</div>

${ include("footer") }$
