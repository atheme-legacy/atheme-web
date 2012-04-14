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
});
