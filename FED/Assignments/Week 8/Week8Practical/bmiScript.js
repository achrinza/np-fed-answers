/*
    Copyright (c) 2019 Rifa I. Achrinza
    This document is licensed under MIT license (See LICENSE for details)
    SPDX-Short-Identifier: MIT
*/

const heightInput = document.querySelector('.block-bmi-calc__height-input');
const weightInput = document.querySelector('.block-bmi-calc__weight-input');
const resultOutput = document.querySelector('.block-bmi-calc__results');

const calculateBMI = (height, weight) => {
    return weight / height ** 2;
}

const updateCalculator = () => {
    const bmiValue = calculateBMI(heightInput.value, weightInput.value);
    let bmiStatus;

    if (isNaN(bmiValue) || !isFinite(bmiValue)) {
        resultOutput.innerHTML = `Invalid values keyed.`;
        return;
    }

    if (bmiValue < 18.5) {
        bmiStatus = 'under weight';
    } else if (bmiValue < 23) {
        bmiStatus = 'normal weight';
    } else if (bmiValue < 27.5) {
        bmiStatus = 'over weight';
    } else {
        bmiStatus = 'obese';
    }
    resultOutput.innerHTML = `Your BMI is ${bmiValue.toFixed(2)}. You are ${bmiStatus}`;
}

heightInput.addEventListener('input', () => {
    updateCalculator();
});

weightInput.addEventListener('input', () => {
    updateCalculator();
});

updateCalculator();
