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
    descriptionEl.textContent = description;

    holidayEl.append(nameEl);
    holidayEl.append(dateEl);
    holidayEl.append(descriptionEl);

    return holidayEl;
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

if(window.location.pathname === "/today.html") window.onload = getToday;
if(window.location.pathname === "/results.html") window.onload = getDate;
