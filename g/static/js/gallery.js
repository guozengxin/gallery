$(function() {
	init();

	function init() {
		$('.ph-sidenav li').click(function() {
			var gname = $("button", this).text();
			refresh_photo(gname);
		});

		$('#edit-btn').click(function() {
			active_edit();
		});


		// 默认显示第一个相册
		var first = $('.ph-sidenav li')[0];
		var f_gname = $("button", $(first)).text();
		refresh_photo(f_gname);
	}

	function active_edit() {
		
	}

	function refresh_photo(gname) {
		$.get('photo-by-gname', {
			gname: gname,
		}, function (data) {
			$('#photo-list').html(data);
		});
	}

});
