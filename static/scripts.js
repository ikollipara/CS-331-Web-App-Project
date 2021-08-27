/**
 * Scripts.js
 * Ian Kollipara
 */

const API = "http://localhost:8000/api"

function createHolidayElement(name, date, description) {
    const nameEl = document.createElement("h1");
    const dateEl = document.createElement("p");
    const descriptionEl = document.createElement("p");
    const holidayEl = document.createElement("section");

    nameEl.textContent = name;
    dateEl.textContent = date;
    descriptionEl.textContent = descriptionEl;

    holidayEl.append([nameEl, dateEl, descriptionEl]);
}

function getToday() {
    fetch(`${API}/today`)
        .then(res => res.json())
        .then(json => json.forEach(holiday => {
            let section = document.querySelector("#holidays");
            let el = createHolidayElement(holiday.name, holiday.date, holiday.description);
            section.append(el);
        }))
}

function getDate() {
    fetch(`${API}/date${window.location.search}`)
        .then(res => res.json())
        .then(json => json.forEach(holiday => {
            let section = document.querySelector("#holidays");
            let el = createHolidayElement(holiday.name, holiday.date, holiday.description);
            section.append(el);
        }))
}