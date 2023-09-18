var callAPI = (name, date, time, place) => {
    //validate form
    if ((name == null || name == "") || (date == null || date == "") ||
    (time == null || time == "") || (place == null || place == "")) {
      alert("Please Fill In All Required Fields");
      
      return false;
    }

    //call API
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "name": name, "date": date, "time": time, "place": place });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("https://66m5bteg6d.execute-api.us-east-1.amazonaws.com/dev", requestOptions)
    .then(response => response.text())
    .then(result => displayResult(result))
    .catch(error => console.log('error', error));
}

var displayResult = (result) => {

    var e = JSON.parse(result);

    document.getElementById('user-result').innerHTML = `
    <h2 class="user-greeting" id="to-scroll">Hello ${e.name}, your Zodiac is ${e.zodiac}!</h2>
    <h4 class="user-greeting-sub">Birthday: ${e.time} - ${e.date}, in ${e.place}.</h4>
    <h3 class="user-aspects">Appearance & Health</h3>
    <p>${e.appearance}</p>
    <h3 class="user-aspects">Character</h3>
    <p>${e.character}</p>
    <h3 class="user-aspects">Career</h3>
    <p>${e.career}</p>
    <h3 class="user-aspects">Relationship</h3>
    <p>${e.relationship}</p>
    <h3 class="user-aspects">Suitable works</h3>
    <p>${e.suworks}</p>
    <h3 class="user-aspects">Suitable partners</h3>
    <p>${e.supns}</p>
    `

    const element = document.getElementById("to-scroll");
    element.scrollIntoView({ behavior: "smooth", inline: "nearest" });
}