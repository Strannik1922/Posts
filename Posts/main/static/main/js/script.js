const title = document.querySelector('#text-title')
const category = document.querySelector('#text-category')
const content = document.querySelector('#text-content')

const button = document.querySelector('#button_post')
const button_get = document.querySelector('#button_get')
const posts = document.querySelector('#posts')

let count = 0

title.addEventListener('input', function (event) {
    if (event.data) {
        count += 1
        console.log(count)
    }
    else {
        count -= 1
        console.log(count)
    }
})

let prevLength = 0
category.addEventListener('change', function () {
    const selectedOption = category.options[category.selectedIndex].textContent.length

    count += selectedOption - prevLength
    prevLength = selectedOption
    console.log(count, prevLength, selectedOption)
})

content.addEventListener('input', function (event) {
    if (event.data) {
        count += 1
        console.log(count)
    }
    else {
        count -= 1
        console.log(count)
    }
})

button.addEventListener("click", function() {
    let xhr = new XMLHttpRequest();
    let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    xhr.open("POST", "/");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.setRequestHeader("X-CSRFToken", csrf_token);

    xhr.onload = function() {
    if (xhr.status === 200) {
      document.getElementById("result").innerHTML = xhr.responseText;
    }
    };

    xhr.send(JSON.stringify({count: count}));
})

button_get.addEventListener("click", function() {
    if (posts.style.display === "none") {
        posts.style.display = "block"
    } else {
        posts.style.display = "none"
    }
})