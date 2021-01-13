const input = document.querySelector('#leave_comment')
const buttons = document.querySelector('#buttons')
const cancel = document.querySelector('#cancel')
const reply_button = document.querySelectorAll('.reply_button')
const reply_change = document.querySelectorAll('.reply_change')
const reply_delete = document.querySelectorAll('.reply_delete')
const reply_reply = document.querySelectorAll('.reply_reply_button')
const show_reply = document.querySelectorAll('.show_reply')
const comments = document.querySelectorAll('.comment')
const answers = document.querySelectorAll('.answer')
const count_comments = document.querySelector('.count_comments')
let count = comments.length

if (count % 100 >= 11 && count % 100 <= 19) {
    count_comments.innerText = count + ' коментариев'
} else {
    switch (count % 10) {
        case 1:
            count_comments.innerText = count + ' комментарий'
            break
        case 2:
            count_comments.innerText = count + ' комментария'
            break
        case 3:
            count_comments.innerText = count + ' комментария'
            break
        case 4:
            count_comments.innerText = count + ' комментария'
            break
        default:
            count_comments.innerText = count + ' комментариев'

    }
}

if (input != null) {
    input.addEventListener('click', function () {
        buttons.style.display = 'flex'
    })
}

if (cancel != null) {
    cancel.addEventListener('click', function () {
        buttons.style.display = 'none'
    })
}


reply_button.forEach(element => {
    const comment = element.closest('.comment_info')
    element.addEventListener('click', function () {
        const forms_reply = document.querySelectorAll('.leave_reply_form')
        const forms = document.querySelectorAll('.change_form')
        const form = comment.querySelector('.leave_reply_form')
        const hide_form = form.querySelector('.hide_form')
        const input_submit = form.querySelector('.input_submit')

        forms_reply.forEach(element => {
            element.style.display = 'none'
        })

        forms.forEach(element => {
            element.style.display = 'none'
        })

        input_submit.setAttribute('name', 'reply')
        form.style.display = 'flex'

        hide_form.addEventListener('click', function () {
            form.style.display = 'none'
            input_submit.removeAttribute('name')
        })
    })
})


reply_change.forEach(element => {
    element.addEventListener('click', function () {
        const forms_reply = document.querySelectorAll('.leave_reply_form')
        const forms = document.querySelectorAll('.change_form')
        const comment = element.closest('.comment_info')
        const form = comment.querySelector('.change_form')
        const hide_form = form.querySelector('.hide_form')
        const comment_text = comment.querySelector('.comment_text').textContent
        const reply_input = form.querySelector('.reply_input')
        const input_submit = form.querySelector('.input_submit')
        const span = comment.querySelector('span')
        input_submit.setAttribute('name', 'change')

        forms_reply.forEach(element => {
            element.style.display = 'none'
        })

        forms.forEach(element => {
            element.style.display = 'none'
        })

        if (span) {
            reply_input.addEventListener('input', function (event) {
                text = span.textContent + ' '
                if (this.value.length <= text.length) {
                    let position = this.selectionStart + 1
                    this.value = text
                    this.setSelectionRange(position, position)
                }
            })
        }

        reply_input.value = comment_text
        input_submit.value = 'Редактировать'
        form.style.display = 'flex'

        hide_form.addEventListener('click', function () {
            reply_input.value = ''
            form.style.display = 'none'
            input_submit.value = 'Ответить'
            input_submit.removeAttribute('name')
        })
    })
})

reply_delete.forEach(element => {
    element.addEventListener('click', function () {
        const forms_reply = document.querySelectorAll('.leave_reply_form')
        const forms = document.querySelectorAll('.change_form')
        const comment = element.closest('.comment_info')
        const form = comment.querySelector('.change_form')
        const hide_form = form.querySelector('.hide_form')
        const comment_text = comment.querySelector('.comment_text').textContent
        const reply_input = form.querySelector('.reply_input')
        const input_submit = form.querySelector('.input_submit')

        forms_reply.forEach(element => {
            element.style.display = 'none'
        })

        forms.forEach(element => {
            element.style.display = 'none'
        })

        input_submit.setAttribute('name', 'delete')
        reply_input.setAttribute('disabled', 'True')
        reply_input.value = comment_text
        input_submit.value = 'Удалить'
        form.style.display = 'flex'

        hide_form.addEventListener('click', function () {
            reply_input.value = ''
            form.style.display = 'none'
            input_submit.value = 'Ответить'
            input_submit.removeAttribute('name')
            reply_input.removeAttribute('disabled')
        })
    })
})

// Ответ на ответ на комментарий
reply_reply.forEach(element => {
    element.addEventListener('click', function () {
        const forms_reply = document.querySelectorAll('.leave_reply_form')
        const forms = document.querySelectorAll('.change_form')
        const comment = element.closest('.comment_info')
        const form = comment.querySelector('.leave_reply_form')
        const hide_form = comment.querySelector('.hide_form')
        const reply_input = comment.querySelector('.reply_input')
        let name = comment.querySelector('.comment_name').textContent
        const input_submit = comment.querySelector('.input_submit')

        forms_reply.forEach(element => {
            element.style.display = 'none'
        })

        forms.forEach(element => {
            element.style.display = 'none'
        })

        input_submit.setAttribute('name', 'reply')
        name = '@' + name + ', '
        reply_input.value = name

        reply_input.addEventListener('input', function (event) {
            if (this.value.length <= name.length) {
                let position = this.selectionStart + 1
                this.value = name
                this.setSelectionRange(position, position)

            }
        })

        form.style.display = 'flex'

        hide_form.addEventListener('click', function () {
            form.style.display = 'none'
            input_submit.removeAttribute('name')

        })
    })
})


show_reply.forEach(element => {
    const comment = element.closest('.comment_info')
    const answers = comment.querySelector('.answers')
    const count_answer = comment.querySelectorAll('.answer').length

    if (count_answer == 0) {
        element.innerText = ''
    } else if (count_answer % 100 >= 11 & count_answer % 100 <= 19) {
        element.innerText = 'показать ' + count_answer + ' ответов'
    } else {
        switch (count_answer % 10) {
            case 1:
                element.innerText = 'показать ' + count_answer + ' ответ'
                break
            case 2:
                element.innerText = 'показать ' + count_answer + ' ответа'
                break
            case 3:
                element.innerText = 'показать ' + count_answer + ' ответа'
                break
            case 4:
                element.innerText = 'показать ' + count_answer + ' ответа'
                break
            default:
                element.innerText = 'показать ' + count_answer + ' ответов'

        }
    }

    element.addEventListener('click', function () {

        if (getComputedStyle(answers).display == 'none') {
            answers.style.display = 'block'

            if (count_answer % 100 >= 11 & count_answer % 100 <= 19) {
                element.innerText = 'скрыть ' + count_answer + ' ответов'
            } else {
                switch (count_answer % 10) {
                    case 1:
                        element.innerText = 'скрыть ' + count_answer + ' ответ'
                        break
                    case 2:
                        element.innerText = 'скрыть ' + count_answer + ' ответа'
                        break
                    case 3:
                        element.innerText = 'скрыть ' + count_answer + ' ответа'
                        break
                    case 4:
                        element.innerText = 'скрыть ' + count_answer + ' ответа'
                        break
                    default:
                        element.innerText = 'скрыть ' + count_answer + ' ответов'

                }
            }

        } else {
            answers.style.display = 'none'

            if (count_answer == 1) {
                element.innerText = 'Покзать 1 ответ'
            } else if (count_answer < 5 && count_answer > 1) {
                element.innerText = 'Показать ' + count_answer + ' ответа'
            }
        }

    })
})

comments.forEach(element => {
    const letter = element.querySelector('.comment_name').textContent.charAt(0)
    const comment_letter = element.querySelector('.comment_letter')

    comment_letter.innerText = letter
})

answers.forEach(element => {
    const letter = element.querySelector('.comment_name').textContent.charAt(0)
    const comment_letter = element.querySelector('.answer_letter')

    comment_letter.innerText = letter
})
