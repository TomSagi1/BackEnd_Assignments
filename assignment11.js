function myFunction(e) {
    num = document.getElementById("number");
    url = "https://reqres.in/api/users/"+num.value
    fetch(url).then(
        response => response.json()
    ).then((response_obj) => {
        console.log(response_obj.data)
        return users_in_html(response_obj.data)
    }
    ).catch(
        error => console.log(error)
    )
}

function users_in_html(response_obj) {
    const current_main = document.querySelector("main");
    current_main.innerHTML = `
        <img src="${response_obj.avatar}" alt="Profile Pic"/>
        <div>
            <span>${response_obj.first_name} ${response_obj.last_name}</span>
            <br>
            <a href="mailto:${response_obj.email}">Send Email!</a>
            <br><br>
        </div>
    `;
}