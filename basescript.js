function scrollInMainDiv(id) {
    "use strict";
    window.scrollBy({
        top: document.getElementById(id).getBoundingClientRect().top - 50, 
        behavior: "smooth", 
    });
}

function parseParamsLocation() {
    let params = new URLSearchParams(window.location.search);
    let scroll_value = params.get("location");
    if (scroll_value !== null) {
        let element = document.getElementById("title-" + scroll_value);
        if (element !== null) {
            scrollInMainDiv("title-" + scroll_value);
        }
    }
}
