function showText(index) {
    let textElement = document.getElementById("text-" + index);

    if (textElement.style.display === "none" || textElement.style.display === "") {
        textElement.style.display = "flex";
    } else {
        textElement.style.display = "none";
    }
}
