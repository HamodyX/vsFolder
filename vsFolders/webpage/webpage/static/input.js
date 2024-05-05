function enter(){
    let Command = document.getElementById("action");
    let textElement = document.getElementById("texts_container");
    let buttonEnter = document.getElementById("EnterB");
    let currencyDiv = document.getElementById("currencyCall");


    if (/Mobi|Android/i.test(navigator.userAgent)) {
        if(Command.value === "help"){
            textElement.style.display = "block"
            Command.style.transform = "translateY(-100px)"
            buttonEnter.style.transform = "translateY(-100px)"
            if(Command.value === "About me"){

            }else if(Command.value === "Discord"){
                
            }else if(Command.value === "Launch"){

            }else if(Command.value === "CurrencyEx"){

            }else if(Command.value === "Github"){

            }else{

            }

        }
    }
}

function currency(){
    let header = document.getElementById("hTitle");
    let primary = document.getElementById("primary").value;
    let secondary = document.getElementById("secondary").value;
    const data = { primary: primary, secondary: secondary };

     fetch('/api/data', {
         method: 'POST',
         headers: {
             'Content-Type': 'application/json'
         },
         body: JSON.stringify(data)
     })
     .then(response => response.json())
     .then(result => {
         console.log('Success:', result);
         header.innerHTML = result.message;
     })
     .catch(error => {
         console.error('Error:', error);
     });
}
