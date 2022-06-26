// fetch('http://127.0.0.1:5000/api/timeline_post', {
//     method:"POST",
//     headers:{
//         'Content-Type':'application/json'
//     },
//     body: JSON.stringify({
//         name: "User 1",
//         email:"test@email.com",
//         content: "JavaScript test"
//     })
// }).then(res => {
//     return res.json()
// }).then(data => console.log(data)).catch(error => console.log("ERROR"))

// document.getElementById("time_text").innerHTML = "New Text"


// const url = 'http://127.0.0.1:5000/api/timeline_post'
// const formEl = document.querySelector('form')
// formEl.addEventListener('submit', async (e) => {
//     e.preventDefault()
//     alert("alert")
//     console.log("Submit Button")

//     const formData = new FormData(formEl)
//     const formDataSerialized = Object.fromEntries(formData)
//     // console.log(formDataSerialized, "formDataSerialized")
//     const jsonObject = { ...formDataSerialized, sendToSelf: formDataSerialized.sendToSelf ? true : false }
//     console.log("jsonObject:")
//     jsonObject.email = "AwaitEmail"
//     jsonObject.created_at = "AwaitDate"
//     jsonObject.content = "AwaitContent"
//     console.log(jsonObject)

//     try{
//         const response = await fetch(url, {
//             method: 'POST',
//             body: JSON.stringify(jsonObject),
//             headers: {
//                 'Content-Type':'application/json'
//             }
//         })
//         const json = await response.json()
//         console.log("Await Done:")
//         console.log(json)
//     }catch(e){
//         console.error(e)
//         alert("there was an error")
//     }
// })

// console.log("end 1")

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

    // const prePayload = new FormData(form)
    // const payload = new URLSearchParams(prePayload)

    // console.log([...payload])

    // fetch('http://127.0.0.1:5000/api/timeline_post', {
    //     method: "POST",
    //     body:payload,
    // })
    //     .then(res => res.json())
    //     .then(data => console.log(data))
    //     .catch(err => console.log(err))
})

/*

const myForm = document.getElementById("myForm")

myForm.addEventListener("submit", (e) => {
    e.preventDefault()
    console.log("Form has been submitted!")

    console.log(document.getElementById("name").value)
    console.log(document.getElementById("email").value)
    console.log(document.getElementById("content").value)

    // const request = new XMLHttpRequest()
    // request.open("post","")
    // request.onload = function(){
    //     console.log(request.responseText)
    // }
    // request.send(new FormData(myForm))
})*/


fetch('http://127.0.0.1:5000/api/timeline_post').then(res => res.json()).then(data => {
    console.log("Here is the data print:")
    console.log(data.timeline_posts.length)
    for(let i=0;i<data.timeline_posts.length;i++){
        // console.log(data.timeline_posts[i])
        // document.getElementById("time_text").src = URL.createObjectURL(data)
        // const doc = document.getElementById("time_text")
        // doc = "hi"

        // console.log(data)
        
        document.body.onload = addElement(data.timeline_posts[i])
        
        // document.getElementById("time_text").innerHTML = data.timeline_posts[i].name


    }
    // document.getElementById("time_text").src = URL.createObjectURL(data)
}).catch(error => console.log("ERROR"))

// document.getElementById("time_text").innerHTML = data

// console.log("About to fetch")
// fetch('http://127.0.0.1:5000/api/timeline_post').then(response => {
//     console.log(response)
//     return response.blob()
// }).then(blob => {
//     console.log(blob)
//     document.getElementById('time_text').src = URL.createObjectURL(blob)
// })

function addElement(data){
    var place = document.getElementById("time_text")

    // create a new div element
    const newDiv = document.createElement("div");
  
    // and give it some content
    const newContent = document.createTextNode(data.name + " " + data.email + " " + data.created_at + " " + data.content);
    // console.log("In function")
    // console.log(data.name)
    // console.log(data.email)
    // console.log(data.created_at)
    // console.log(data.content)
  
    // add the text node to the newly created div
    newDiv.appendChild(newContent);
    newDiv.classList.add("form-list-text");
  
    // add the newly created element and its content into the DOM
    const currentDiv = document.getElementById("div1");
    place.insertBefore(newDiv, currentDiv);
}