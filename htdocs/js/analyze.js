function populate1(url, tag1, tag2, tag3)
{
	$("#siteurl").val(url);
	$("#tag1").val(tag1);
	$("#tag2").val(tag2);
	$("#tag3").val(tag3);
	$("#submit").click();
}

$(function() {

$("#submit").click(getSiteGraph);

});



