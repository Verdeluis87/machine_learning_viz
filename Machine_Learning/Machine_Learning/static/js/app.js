function clearResponse()
{
 document.getElementById('response').innerHTML="";
}

function getResponse()
{
    // var data = JSON.parse('data.result');
    document.getElementById('response').innerHTML= data.result;
    console.log(data.result)
}

// Submit Button handler
function handleSubmit() {
    // @TODO: YOUR CODE HERE
    // Prevent the page from refreshing
    d3.event.preventDefault();
  
    // Filter the data
    clearResponse();
    getResponse();

};

d3.select("#filter-btn").on("click",handleSubmit);