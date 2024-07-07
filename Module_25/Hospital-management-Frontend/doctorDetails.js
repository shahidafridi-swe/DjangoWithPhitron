const getParams = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    displayDoctorAppoinmentTime(param)
    fetch(`https://test-thto.onrender.com/doctor/list/${param}`)
    .then((res)=> res.json())
    .then((data)=> displayDoctorDetails(data))

    fetch(`https://test-thto.onrender.com/doctor/review/?doctorId=${param}`)
    .then((res)=> res.json())
    .then((data) => displaySingleDoctorReview(data)) 
    

}

const displayDoctorDetails = (doctor) => {
    const parent = document.getElementById("doctor-details")
    const div = document.createElement("div")
    
    div.innerHTML = `
    
        <div class="row bg-banner p-5 rounded-pill text-white">
          <div class="col-md-4 d-flex justify-content-center align-items-center">
            <img class="rounded-circle w-100" src=${doctor.image} alt="">
          </div>
          <div class="col-md-8">
            <h2 class="">${doctor.full_name}</h2>
            <h6 class="text-warning">${doctor.specialization}</h6>
            <h4 class="text-warning">${doctor.designation}</h4>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quaerat nulla, suscipit quas soluta quisquam non iste harum magni vero in est enim culpa odio quos sequi odit at voluptatem consectetur eaque sunt temporibus inventore, omnis ea. Repellendus, quidem quisquam.</p>
            <h5 class="text-warning">Fees: ${doctor.fee} BDT</h5>
            <button type="button" class="btn bg-banner text-white" data-bs-toggle="modal" data-bs-target="#staticBackdrop">
            Take Appoinment
            </button>
       
          </div>
        </div>

    `
    parent.appendChild(div)
}

const displaySingleDoctorReview = (reviews) => {
    reviews.forEach((review) => {
      const parent = document.getElementById('single-doctor-review')
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


const displayDoctorAppoinmentTime = (id) => {
    fetch(`https://test-thto.onrender.com/doctor/availabletime/?doctorId=${id}`)
    .then((res)=> res.json())
    .then((data) => {
        data.forEach((appTime) => {
            const parent = document.getElementById("doctor-appointment-times");
            const option = document.createElement("option");
            option.value = appTime.id;
            option.innerText = appTime.name;
            parent.appendChild(option);
        })
    })
}

const handleAppointment = () => {
    const param = new URLSearchParams(window.location.search).get("doctorId");
    const appointmentType = document.getElementsByName("appointmentType");
    const selectedAppointmentType = Array.from(appointmentType).find((button)=>button.checked);
    const symptom = document.getElementById("inputSymptom").value;
    const appointmentTime = document.getElementById("doctor-appointment-times")
    const selectedAppointmentTime = appointmentTime.options[appointmentTime.selectedIndex];

    const info = {
        appointment_type: selectedAppointmentType.value,
        appointment_status: "Pending",
        time: selectedAppointmentTime.value,
        symptom: symptom,
        cancel: false,
        patient: 1,
        doctor: param,
      };
      console.log(info)
    fetch("https://test-thto.onrender.com/appointment/", {
        method: "POST",
        headers: {"content-type": "application/json"},
        body: JSON.stringify(info),
    })
    .then((res)=> res.json())
    .then((data)=>{
        console.log(data)
    })
}
getParams();