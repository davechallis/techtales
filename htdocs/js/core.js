function handleJSON(data, textStatus)
{
	if(data)
	{
		$("#graph").empty();
		var img = $("<img />");
		img.attr("src", data.url);
		img.appendTo("#graph");
		$("#throbber").fadeOut(function() { $("#graph").fadeIn(); });
	}
	else
	{
		$("#graph").empty();
		$("#throbber").fadeOut();
	}
}

function getCombinedSiteGraph()
{
	$("#graph").fadeOut(function()
	{
			$("#throbber").fadeIn();
			var siteurl1 = $("#siteurl1").val();
			var siteurl2 = $("#siteurl2").val();
			var tag = $("#tag").val();
			$.getJSON("/service/comparechart", {url1:siteurl1, url2:siteurl2, field:tag}, handleJSON);
	});
}


function getSiteGraph()
{
	$("#graph").fadeOut(function()
	{
			$("#throbber").fadeIn();
			var siteurl = $("#siteurl").val();
			var tag1 = $("#tag1").val();
			var tag2 = $("#tag2").val();
			var tag3 = $("#tag3").val();
			$.getJSON("/service/chart", {url:siteurl,fields:[tag1,tag2,tag3].join(",")}, handleJSON);
	});
}
