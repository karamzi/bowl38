const li = document.querySelectorAll('li')
const number1 = document.querySelectorAll('.number1')
const number2 = document.querySelectorAll('.number2')
const number3 = document.querySelectorAll('.number3')
const options = document.querySelectorAll('option')

li.forEach(element => element.addEventListener('mouseenter', function (event) {
    const currentLi = event.target

    if (currentLi.querySelector('.accordion')) {
        const currentLiDiv = currentLi.querySelector('.accordion')
        currentLiDiv.style.display = 'flex'
    }

}))

li.forEach(element => element.addEventListener('mouseleave', function (event) {
    const currentLi = event.target

    if (currentLi.querySelector('.accordion')) {
        const currentLiDiv = currentLi.querySelector('.accordion')
        currentLiDiv.style.display = 'none'
    }
}))

let counter = 0
number1.forEach(element => {
    counter += 1
    element.innerText = counter
})

if (options && counter == 16) {
    options[0].remove()
}

counter = 0
number2.forEach(element => {
    counter += 1
    element.innerText = counter
})

if (options && counter == 16) {
    options[1].remove()
}

counter = 0
number3.forEach(element => {
    counter += 1
    element.innerText = counter
})

if (options && counter == 16) {
    options[2].remove()
}
