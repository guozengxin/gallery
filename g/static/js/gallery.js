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

		$('.op-edit').click(function() {
			showEdit(this);
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

		$('#save').click(function() {
			save_info();
		});

	}

	function get_pname(url) {
		var re = /allphotos(\/\w+\/[^?]+)\?/;
		// http://bcs.duapp.com/allphotos/2011/IMG_5810_thumb.JPG?sign=MBO:ZnzhNMuZPIGjst5pdBbRIIdG:rqWx7FkK5wN%2BKyRQTNOwc8elAL8%3D
		var pname = url.match(re)[1];
		pname = pname.replace('_middle', '');
		pname = pname.replace('_thumb', '');
		return pname;
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
		var pname = get_pname(url);
		$.post('delete-photo', {
			pname: pname,
		}, function(data) {
			$(cur).closest('div.col-md-3').remove();
		});
	}

	function save_info() {
		var url = $('#edit-img').attr('src');
		var pname = get_pname(url);
		var topic = $('#photo-topic-input').val();
		var desc = $('#photo-desc-input').val();
		var labels = $('#photo-labels-input').val();
		$.post('save-info', {
			pname: pname,
			topic: topic,
			desc: desc,
			labels: labels
		}, function(data) {
			var obj = JSON.parse();
			$('#message').text(obj.message);
		});
	}

	//显示灰色 jQuery 遮罩层  
	function showEdit(cur) {  
		//定位图片url，并计算图片名
		var url = $(cur).parent().parent().find('a img').attr('src');

		var bh = $("body").height();  
		var bw = $("body").width();  
		$("#maskbg").css({  
			height:bh,  
			width:bw,  
			display:"block"  
		});  
		$(".close a").click(closeEdit);
		$("#pop-div img").attr('src', url);
		var t = ($(window).height() - $('#pop-div').height()) / 2;
		$('#pop-div').css('top', t);
		$("#pop-div").show();
	}  

	//关闭灰色 jQuery 遮罩  
	function closeEdit() {  
		$("#maskbg,#pop-div").hide();  
	}  

});
