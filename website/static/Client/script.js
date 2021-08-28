let client_name = document.querySelector("#name")
let verify_button = document.querySelector("#verify")
let loading = document.querySelector("#loading")
let message = document.querySelector("#message")


verify_button.onclick= () => {
    loading.classList.remove("hidden")
    console.log(client_name.value)
    fetch("/verify", {
        method:"POST",
        body: JSON.stringify({name: client_name.value})
    }).then(res =>{
        loading.classList.add("hidden")
        res.json().then(data=>{
            let download = data.response.verify ? `<span id='download' onClick='download("${data.response.filename}")'>disini</span>` :""
            message.innerHTML = data.response.txt + download 
            console.log(data.response)
        })
    })
}

function download(name){
    fetch("/download", {
        method:'POST',
        body:JSON.stringify({filename: name})
    }).then(res=>{
        console.log(res)
    }).catch(err=>{
        console.log(err)
    })
}