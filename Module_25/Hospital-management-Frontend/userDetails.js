const loadUserDetails = () => {
    const user_id = localStorage.getItem("user_id")
    fetch(`https://test-thto.onrender.com/users/${user_id}`)
    .then((res)=>res.json())
    .then((data)=> {
        console.log(data)

    const parent = document.getElementById("user-details")
    const div = document.createElement("div")
    div.innerHTML = `
        <div class="row bg-banner p-5 rounded-pill text-white">
          <div class="col-md-4 d-flex justify-content-center align-items-center">
            <img class="rounded-circle w-100" src='./Images/man-1.jpg' alt="">
          </div>
          <div class="col-md-8">
            <h2 class="">${data.username}</h2>
            <h6 class="text-warning">${data.email}</h6>
            <h6 class="text-warning">${data.first_name}</h6>
       
          </div>
        </div>

    `
    parent.appendChild(div)
    })
};
loadUserDetails();


