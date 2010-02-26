function handleJSON(data, textStatus)
{
	alert(data.url);
}

$.getJSON("/service/chart", {url:"www.ecs.soton.ac.uk",field:"link"}, handleJSON);

