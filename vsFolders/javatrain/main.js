function Matte(operator) {
    let InputElement1 = document.getElementById("tal1");
    let InputElement2 = document.getElementById("tal2");

    let tal1 = parseFloat(InputElement1.value);
    let tal2 = parseFloat(InputElement2.value);

    let outputElement = document.getElementById("output");
    
    if (!isNaN(tal1) && !isNaN(tal2)) {
        let resultat;
        
        switch (operator) {
            case 'addera':
                resultat = tal1 + tal2;
                break;
            case 'subtrahera':
                resultat = tal1 - tal2;
                break;
            case 'multi':
                resultat = tal1 * tal2;
                break;
            case 'dividera':
                resultat = tal1 / tal2;

                break;
            default:
                resultat = "Ogiltig operation";
        }

        outputElement.textContent = "Resultat: " + resultat;
    } else {
        outputElement.textContent = "Ogiltiga tal";
    }
}
