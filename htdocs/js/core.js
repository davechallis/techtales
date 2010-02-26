function handleJSON(data, textStatus)
{
	if(data)
	{
		$("#graph").empty();
		var img = $("<img />");
		img.attr("src", data.url);
		img.appendTo("#graph");
		$("#throbber").fadeOut();
		$("#graph").fadeIn();
	}
}

function getSiteGraph()
{
	$("#throbber").fadeIn();
	var siteurl = $("#siteurl").val();
	var tag1 = $("#tag1").val();
	var tag2 = $("#tag2").val();
	var tag3 = $("#tag3").val();
	$.getJSON("/service/chart", {url:siteurl,fields:[tag1,tag2,tag3].join(",")}, handleJSON);

	$("#graph").fadeOut();
}

$(function() {

$("#submit").click(getSiteGraph);

});


