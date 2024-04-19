
                const question = document.getElementsByClassName("question");
question[0].classList.replace('hide', 'active');

const endTime = new Date().getTime() + 10000;
const audio = document.getElementById("myAudio");

// nãp consegui fazer funcionar
audio = new Audio('../audio/audio.mp3')
audio.play()

const button = document.querySelector('#confirmButton');
button.addEventListener('click', (e) => {

    const getSelectedAlternative = (elements) => {
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i].querySelector('input');
            if (element.checked) {
                return element;
            }
        }
    }

    const activeQuestion = document.querySelector('.question.active');
    const alternatives = activeQuestion.getElementsByClassName('alternative');
    const selectedAlternative = getSelectedAlternative(alternatives);

    if (selectedAlternative.getAttribute('data-isanswer') == "True") {
        window.alert("Parabens, você acertou")
    } else {
        window.alert("Ops, você errou")
    }
})

const changeQuestion = (timer) => {
    const questions = document.getElementsByClassName("question")
    for (let i = 1; i < questions.length; i++) {
        const nextQuesion = questions[i];
        const prevQuesion = questions[i-1];

        if (prevQuesion.classList.contains("active") &&  nextQuesion.classList.contains("hide")) {
            prevQuesion.classList.replace('active', 'hide');
            nextQuesion.classList.replace('hide', 'active');
            timer.endTime = new Date().getTime() + (Math.floor(Math.random() * (7 - 3 + 1)) + 3) * 60000;
            timer.startCountdown();

            audio.play();
            audio.onplay = function() {
                setTimeout(() => {
                    audio.pause();
                }, 60000); // Pausa o áudio após 10 segundos (10000 milissegundos)
            };
        }
    }
}


const timerHtmlElement = document.getElementById('time');
const timer = new Timer({ 
    endTime, 
    'element': timerHtmlElement,
    'stopCountdownCallBack': changeQuestion
});

timer.startCountdown();

