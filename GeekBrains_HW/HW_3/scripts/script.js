function getEmail() {
    let inputValue = document.getElementById("myInput").value;
    
    if (inputValue.length == 0) {
        alert("You forgot to enter your email!!!!");
    } else {
        alert("Your email address has been send!");
    };
    
}