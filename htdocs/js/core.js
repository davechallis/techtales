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
			var siteurl = $("#siteurl1").val();
			var siteurl = $("#siteurl2").val();
			var tag1 = $("#tag").val();
			$.getJSON("/service/combined", {url1:siteurl, url2:siteurl2, field:tag1}, handleJSON);
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

