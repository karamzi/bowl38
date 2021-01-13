let menu_button = document.querySelector('.menu')


menu_button.addEventListener('click', function () {
    let nav = document.querySelector('.nav')
    let accordion = document.querySelectorAll('.accordion')

    if (nav.style.display === 'block') {
        nav.style.display = 'none'
        accordion.forEach(element => {
            element.style.display = 'none'
        })
    }
    else {
        nav.style.display = 'block'
    }
})

li.forEach(element => {
    element.addEventListener('click', function () {
        let all_accordions = document.querySelectorAll('.accordion')
        let accordion = element.querySelector('.accordion')

        all_accordions.forEach(element => {
            element.style.display = 'none'
        })

        if (accordion.style.display === 'block') {
            accordion.style.display = 'none'
        }
        else {
            accordion.style.display = 'block'
        }
    })
})
