function populate2(url1, url2, tag1)
{
	$("#siteurl1").val(url1);
	$("#siteurl2").val(url2);
	$("#tag").val(tag1);
	$("#submit").click();
}
$(function() {

$("#submit").click(getCombinedSiteGraph);

});




