$(function() {
	init();

	function init() {
		// 默认显示第一个相册
		var first = $('.ph-sidenav li')[0];
		var f_gname = $("button", $(first)).text();
		refresh_photo(f_gname);
	}

	function register() {

		$('.ph-sidenav li').click(function() {
			var gname = $("button", this).text();
			refresh_photo(gname);
		});

		$('.op-delete').click(function() {
			delete_photo(this);
		});


		$('#edit-btn').click(function() {
			var txt = $('#edit-btn').text();
			if (txt == '编辑相册') {
				$('#edit-btn').text('取消编辑');
				$('.ops-btns').show();
			} else {
				$('#edit-btn').text('编辑相册');
				$('.ops-btns').hide();
			}
		});

	}

	function refresh_photo(gname) {
		$.get('photo-by-gname', {
			gname: gname,
		}, function (data) {
			$('#photo-list').html(data);
			register();
		});
	}

	function delete_photo(cur) {
		var url = $(cur).parent().parent().find('a img').attr('src');
		// http://bcs.duapp.com/allphotos/2011/IMG_5810_thumb.JPG?sign=MBO:ZnzhNMuZPIGjst5pdBbRIIdG:rqWx7FkK5wN%2BKyRQTNOwc8elAL8%3D
		var re = /allphotos(\/\w+\/[^?]+)\?/;
		var pname = url.match(re)[1];
		pname = pname.replace('_middle', '');
		pname = pname.replace('_thumb', '');
		$.post('delete-photo', {
			pname: pname,
		}, function(data) {
			$(cur).closest('div.col-md-3').remove();
		});
	}

});
