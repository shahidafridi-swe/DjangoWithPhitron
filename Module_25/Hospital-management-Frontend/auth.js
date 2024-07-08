const handleRegistration = (event) =>{
    event.preventDefault();
    const username = getValue("username");
    const first_name = getValue("first_name");
    const last_name = getValue("last_name");
    const email = getValue("email");
    const password = getValue("password");
    const confirm_password = getValue("confirm_password");
    const info = {username,first_name, last_name,email,password,confirm_password};

    if (password === confirm_password){
        document.getElementById('password-error-message').innerText=""
        if (/^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$/.test(password)){
            console.log(info)  
            
            fetch("https://test-thto.onrender.com/patient/register/", 
            {
                method: "POST",
                headers: {"content-type":"application/json"},
                body: JSON.stringify(info),
            })
            .then((res)=>res.json())
            .then((data)=>console.log(data))
            .then((err)=> console.log(err))
        }
        else{
            document.getElementById('password-error-message').innerText="Password should must have at least a number and special charecter."
        }
    }
    else{
        document.getElementById('password-error-message').innerText="Your given two password didn't match."

    }

};

const getValue = (id) => {
    value = document.getElementById(id).value;
    return value
};


const handleLogin = (event) => {
    event.preventDefault();
    const username = getValue("login-username");
    const password = getValue("login-password");
    console.log({username, password})
    fetch("https://test-thto.onrender.com/patient/login/",
        {
            method: "POST",
            headers: {"content-type":"application/json"},
            body: JSON.stringify({username, password}),
        }
    )
    .then((res)=> res.json())
    .then((data)=> {
        console.log(data)
        if(data.user_token && data.user_id){
            localStorage.setItem("token", data.token);
            localStorage.setItem("user_id", data.user_id);
            window.location.href = "index.html";
        }
    })
};