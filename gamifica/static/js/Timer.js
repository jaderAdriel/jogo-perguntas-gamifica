class Timer {
    constructor(props) {
        this.start = props.startTime || new Date().getTime();
        this.endTime = props.endTime || this.start;
        this.element = props.element;
        this.stopCountdownCallBack = props.stopCountdownCallBack || function() {};
    }

    update() {
        const currentTime = new Date().getTime();
        const timeDiff = (this.endTime - currentTime) / 1000;

        let seconds = Math.round(timeDiff);
        if (seconds <= 0) {
            this.stopCountdown();
            return;
        }

        let minutes = Math.floor(seconds / 60);
        seconds = seconds % 60;

        const format = (value) => {
            return value < 10 ? `0${value}` : value;
        }

        this.text = `${format(minutes)}:${format(seconds)}`;
    }

    startCountdown() {
        this.intervalId = setInterval(() => {
            this.update();
            this.element.innerText = this.text;
        }, this.increment);
    }

    stopCountdown() {
        clearInterval(this.intervalId);
        this.element.innerText = "00:00"; // Atualiza o texto para "00:00" quando o countdown parar
        this.stopCountdownCallBack(this); // Chama o callback de parada, se definido
    }
}
