/*
    Copyright (c) 2019 Rifa I. Achrinza
    This document is licensed under MIT license (See LICENSE for details)
    SPDX-Short-Identifier: MIT
*/

const currentDate = new Date();

const greeting = `Good ${currentDate.getHours < 12 ? 'morning' : 'afternoon'}, ${prompt('Enter your name:')}`;

document.querySelector('h1').innerHTML = greeting;

alert(greeting);
