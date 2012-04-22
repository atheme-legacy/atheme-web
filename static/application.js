$(document).ready(function() {
	$("input:submit").button();
	$("#tabs").tabs({
		load: function(event, ui) {
			$(ui.panel).delegate('a', 'click', function(event) {
				$(ui.panel).load(this.href);
				event.preventDefault();
			});
		}
	});
	$("#avatar").menu({
		content: $("#session-menu-content").html(),
		showSpeed: 0,
		callerOnState: null,
	});

	/* initial page for when appshell is constructed */
	$("#content").load('/user/account');
	$("#content").delegate('a', 'click', function(event) {
		$('#content').load(this.href);
		event.preventDefault();
	});
	$("#menu ul li").each(function() {
		$(this).delegate('a', 'click', function(event) {
			$('#content').load(this.href);
			event.preventDefault();
		});
	});

	/* set up dialogs */
	$("#change-password-dialog").dialog({autoOpen: false});
});
