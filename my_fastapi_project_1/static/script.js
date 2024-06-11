let currentQuestionIndex = 0;
let quizQuestions = [];
let correctAnswers = 0;
let timer; // Объявляем переменную timer в глобальной области видимости

function startQuiz() {
    fetch('/quiz')
        .then(response => response.json())
        .then(questions => {
            quizQuestions = questions;
            currentQuestionIndex = 0;
            correctAnswers = 0;
            showQuestion();
        });
}

function showQuestion() {
    clearTimeout(timer);
    if (currentQuestionIndex < quizQuestions.length) {
        let quizContainer = document.getElementById('quiz-container');
        quizContainer.innerHTML = ''; // Очищаем контейнер
        let q = quizQuestions[currentQuestionIndex];
        let questionElem = document.createElement('div');
        questionElem.innerHTML = `<h2>${q.question}</h2>`;
        q.choices.forEach(choice => {
            let choiceElem = document.createElement('div');
            choiceElem.innerHTML = `<input type="radio" name="question${currentQuestionIndex}" value="${choice}"> ${choice}`;
            questionElem.appendChild(choiceElem);
        });
        quizContainer.appendChild(questionElem);
        let nextButton = document.createElement('button');
        nextButton.innerText = 'Следующий';
        nextButton.onclick = nextQuestion;
        quizContainer.appendChild(nextButton);

        startTimer();
    } else {
        showResults();
    }
}

function nextQuestion() {
    let selectedAnswer = document.querySelector(`input[name="question${currentQuestionIndex}"]:checked`);
    if (selectedAnswer && selectedAnswer.value === quizQuestions[currentQuestionIndex].answer) {
        correctAnswers++;
    }
    currentQuestionIndex++;
    showQuestion();
}

function startTimer() {
    let timeLeft = 20;
    let quizContainer = document.getElementById('quiz-container');
    let timerElem = document.createElement('div');
    timerElem.id = 'timer';
    timerElem.innerText = `Осталось времени: ${timeLeft} секунд`;
    quizContainer.appendChild(timerElem);

    timer = setInterval(() => {
        timeLeft--;
        timerElem.innerText = `Осталось времени: ${timeLeft} секунд`;
        if (timeLeft <= 0) {
            clearInterval(timer);
            nextQuestion();
        }
    }, 2000);
}

function showResults() {
    let quizContainer = document.getElementById('quiz-container');
    quizContainer.innerHTML = `Вы ответили правильно на ${correctAnswers} из ${quizQuestions.length} вопросов.`;
}
