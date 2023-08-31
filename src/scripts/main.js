var callAPI = (name, place) => {
    //validate form
    var a = document.forms["Form"]["name"].value;
    var b = document.forms["Form"]["date"].value;
    var c = document.forms["Form"]["time"].value;
    var d = document.forms["Form"]["place"].value;
    if ((a == null || a == "") || (b == null || b == "") || (c == null || c == "") || (d == null || d == "")) {
      alert("Please Fill In All Required Fields");
      return false;
    }

    //call API
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({ "name": name, "place": place });
    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
    };

    fetch("https://66m5bteg6d.execute-api.us-east-1.amazonaws.com/dev", requestOptions)
    .then(response => response.text())
    .then(result => document.getElementById('user-result').innerHTML += JSON.parse(result).body)
    .catch(error => console.log('error', error));
}