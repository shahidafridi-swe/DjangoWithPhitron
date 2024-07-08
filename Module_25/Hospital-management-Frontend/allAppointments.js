const loadAllAppointments = () =>{
    const patient_id = localStorage.getItem("patient_id")
    fetch(`https://test-thto.onrender.com/appointment/?patient_id=${patient_id}`)
    // fetch(`https://test-thto.onrender.com/appointment/?patient_id=1`)
    .then((res)=> res.json())
    .then((data)=> {
        console.log(data)
        data.forEach((item)=>{
            const parent = document.getElementById("table-body")
            const tr = document.createElement("tr")
            tr.innerHTML = `
            
                <th scope="row">${item.id}</th>
                <td>${item.email}</td>
                <td>${item.appointment_type}</td>
                <td>${item.symptom}</td>
                <td>${item.appointment_status}</td>
                
                <td>X</td>
            
            `
            parent.appendChild(tr)
        })
        
    })
};
loadAllAppointments();