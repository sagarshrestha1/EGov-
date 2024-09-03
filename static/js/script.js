function updateTimeAndDate() {
    const timeElement = document.getElementById("time");
    const dateElement = document.getElementById("date");

    const now = new Date();

    const timeOptions = { hour: '2-digit', minute: '2-digit', second: '2-digit' };
    const dateOptions = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };

    const currentTime = now.toLocaleTimeString(undefined, timeOptions);
    const currentDate = now.toLocaleDateString(undefined, dateOptions);

    timeElement.textContent = ` ${currentTime}`;
    dateElement.textContent = ` ${currentDate}`;
}

updateTimeAndDate();
setInterval(updateTimeAndDate, 1000);
