function handleJSON(data, textStatus)
{
	alert("HAI");
}

$.getJSON("/service/chart", {url:"www.ecs.soton.ac.uk",field:"link"}, handleJSON);

