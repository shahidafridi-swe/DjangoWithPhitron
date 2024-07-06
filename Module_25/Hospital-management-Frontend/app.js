const loadServices = () => {
  fetch("https://testing-8az5.onrender.com/services/")
  .then((res) => res.json())
  .then((data) => displayService(data))
  .catch((err) => console.log(err))
};

const displayService = (services) => {
  services.forEach(service => {
      const parent = document.getElementById("service-container")
      const li = document.createElement("li")
      li.innerHTML = `
      
      <div class="card shadow h-100">
          <div class="ratio ratio-16x9">
              <img src=${service.image} class="card-img-top" loading="lazy" alt="...">
          </div>
          <div class="card-body  p-3 p-xl-5">
              <h3 class="card-title h5">${service.name}</h3>
              <p class="card-text">${service.description.slice(0,150)}</p>
              <a href="#" class="btn btn-primary bg-banner">Details</a>
          </div>
      </div>
      
      `;
      parent.appendChild(li);
  });
}

loadServices();

const loadDoctors = (value) => {
  document.getElementById("doctors").innerHTML = ""
  document.getElementById("nodata").style.display= "none"
  document.getElementById("loading-doctors").style.display="block"
  fetch(`https://smart-care.onrender.com/doctor/list/?search=${value?value:""}`)
  .then((res) => res.json())
  .then((data) => {
    document.getElementById("loading-doctors").style.display="none"
    if(data.results.length>0){
      displayDoctor(data?.results);
    }
    else{
      document.getElementById("doctors").innerHTML = ""
      document.getElementById("nodata").style.display= "block"

    }
  })
  .catch((err) => console.log(err))
};

const displayDoctor = (doctors) =>{
  doctors?.forEach(doctor => {
    parent = document.getElementById("doctors");
    const div = document.createElement("div");
    div.classList.add("col");
    div.innerHTML = `

    <div class="card">
    <img src=${doctor.image} class="card-img-top " alt="...">
        <div class="card-body">
        <h5 class="card-title my-text">${doctor.user}</h5>
        <h6 class="my-text">${doctor.designation}</h6>
          ${doctor?.specialization?.map((item)=>{
            return `<button class="btn bg-banner text-white" disabled> ${item}</button>`
          })}
          <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        </div>
        <div class="card-footer">
            <button class="btn bg-banner"> 
              <a class="text-decoration-none text-white" target="_blank" href="doctorDetails.html?doctorId=${doctor.id}">Details</a>
            </button>
        </div>
    </div>
    
    `
    parent.appendChild(div);
  });
};

loadDoctors();

const loadDesignation = () => {
  fetch("https://smart-care.onrender.com/doctor/designation/")
  .then((res)=>res.json())
  .then((data)=> {
    data.forEach((item)=>{
      const parent = document.getElementById("drop-designation");
      const li = document.createElement("li")
      li.innerHTML = `
        <a class="dropdown-item" href="#">${item.name}</a>
      `
      parent.appendChild(li)
    })
  })
  .catch((err)=>console.log(err))
}

loadDesignation();

const loadSpecialist = () => {
  fetch("https://smart-care.onrender.com/doctor/specialization/")
  .then((res)=>res.json())
  .then((data)=> {
    data.forEach((item)=>{
      const parent = document.getElementById("drop-specialist");
      const li = document.createElement("li")
      li.innerHTML = `
        <span class="dropdown-item" onclick="loadDoctors('${item.name}')">${item.name}</span>
      `
      parent.appendChild(li)
    })
  })
  .catch((err)=>console.log(err))
}

loadSpecialist();

const handleSearch = () =>{
  const value = document.getElementById("doctor-search").value;
  loadDoctors(value);
}

const loadReview = () =>{
  fetch("https://test-thto.onrender.com/doctor/review/")
  .then((res)=>res.json())
  .then((data)=> displayReview(data))
  .catch((err)=> console.log(err))
}
const displayReview = (reviews) => {
  reviews.forEach((review) => {
    const parent = document.getElementById('review-container')
    const li = document.createElement("li")
    li.innerHTML = `
      <div class="border text-center rounded p-3">
        <img class="rounded-circle" src="./Images/girl.png" alt="">
        <h3>${review.reviewer}</h3>
        <p>${review.body.slice(0,100)}</p>
        <h5>${review.rating}</h5>
      </div>
    `
    parent.appendChild(li)
  })
}
loadReview();