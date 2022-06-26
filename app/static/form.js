const form = document.getElementById('form')

form.addEventListener('submit', function (e) {
    e.preventDefault()

    const payload = new FormData(form);

    fetch('/api/timeline_post', {
        method: 'POST',
        body:payload
    })

    .then(res => res.json())

    form.reset()
})

fetch('http://127.0.0.1:5000/api/timeline_post').then(res => res.json()).then(data => {
    console.log("Here is the data print:")
    console.log(data.timeline_posts.length)
    for(let i=0;i<data.timeline_posts.length;i++){
        document.body.onload = addElement(data.timeline_posts[i])
    }
}).catch(error => console.log("ERROR"))

function addElement(data){
    var place = document.getElementById("time_text")

    // create a new div element
    const newDiv = document.createElement("div");
  
    // and give it some content
    const newContent = document.createTextNode(data.name + " " + data.email + " " + data.created_at + " " + data.content);
  
    // add the text node to the newly created div
    newDiv.appendChild(newContent);
    newDiv.classList.add("form-list-text");
  
    // add the newly created element and its content into the DOM
    const currentDiv = document.getElementById("div1");
    place.insertBefore(newDiv, currentDiv);
}