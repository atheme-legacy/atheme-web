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
});
