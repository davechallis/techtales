function handleJSON(data, textStatus)
{
	var img = $("<img />");
	img.attr("src", data.url);
	img.appendTo("#graphbox");
}

$.getJSON("/service/chart", {url:"www.ecs.soton.ac.uk",field:"link"}, handleJSON);

