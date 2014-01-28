function eraseText()
{
    document.getElementById("inputtext").value="";
};

$(document).ready(
function() { 
	$("#submitbutton").click( function (){
	alert("Request sent: Processing!");
	
				var rake = "RAKE: \n ";
				var naive = "NAIVE: \n ";
				var crakr = "CRAKR:  \n ";
				$("#outputtext").text(rake);
				$("#naivetext").text(naive);
				$("#ctext").text(crakr);

	
	
	
	
	$.post("../add", { "text" : document.getElementById("inputtext").value},
			function(data)
			{	
				data = JSON.parse(data)
				var rake = "RAKE: \n ";
				var naive = "NAIVE: \n ";
				var crakr = "CRAKR: \n ";
				for (item in data.rake)
				{
				    rake = rake + data.rake[item] + ', ';
				}
				for (item in data.naive)
				{
				    naive = naive + data.naive[item] + ', ';
				}
				for (item in data.crakr)
				{
				    crakr = crakr + data.crakr[item] + ', ';
				}
				$("#outputtext").text(rake);
				$("#naivetext").text(naive);
				$("#ctext").text(crakr);
			});

	});
});

/*
$("#subitbutton").click(function(){
  alert (document.getElementById("inputtext").value);
  $.post("../add", { "text" : document.getElementById("inputtext").value }, function(data,status){
	alert ("Posted!2"+data);
	
  });
});




function post_to_url(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);
            form.appendChild(hiddenField);
         }
    }

    document.body.appendChild(form);
    form.submit();
	alert("Form submitted");
}



$(function () {
$("#sub").click(
function()
{
 try{   
    var el = $('#i1').val();
	alert(el);
 }
 catch(ex){alert(ex);}
 
}
);  
});
*/
