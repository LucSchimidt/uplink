function setCookie(name, value) {
    document.cookie = name + '=' + encodeURIComponent(value) + '; path=/';
}

function getCookie(name) {
    var cookieName = name + '=';
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookieArray = decodedCookie.split(';');
    for (var i = 0; i < cookieArray.length; i++) {
        var cookie = cookieArray[i].trim();
        if (cookie.indexOf(cookieName) === 0) {
            return cookie.substring(cookieName.length);
        }
    }
    return '';
}

window.addEventListener('beforeunload', function(event) {
    var formData = JSON.stringify($('#personalize-form').serializeArray());

    setCookie('formData', formData);

    window.location.href = '/plataform/temas/';
});

window.onload = function() {
    var formData = JSON.parse(decodeURIComponent(getCookie('formData')));

    document.querySelector('[name="title"]').value = formData[1].value;

    document.querySelector('[name="titulo-1"]').value = formData[2].value;
    document.querySelector('[name="link-1"]').value = formData[3].value;
    document.querySelector('[name="titulo-2"]').value = formData[4].value;
    document.querySelector('[name="link-2"]').value = formData[5].value;
    document.querySelector('[name="titulo-3"]').value = formData[6].value;
    document.querySelector('[name="link-3"]').value = formData[7].value;

    document.querySelector('[name="insta-link"]').value = formData[8].value;
    document.querySelector('[name="face-link"]').value = formData[9].value;
    document.querySelector('[name="tiktok-link"]').value = formData[10].value;
    document.querySelector('[name="youtube-link"]').value = formData[11].value;
    document.querySelector('[name="twitter-link"]').value = formData[12].value;
    document.querySelector('[name="threads-link"]').value = formData[13].value;

};