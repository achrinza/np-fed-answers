/*
    Copyright (c) 2019 Rifa I. Achrinza
    This document is licensed under MIT license (See LICENSE for details)
    SPDX-Short-Identifier: MIT
*/

const deliveryDate = document.querySelector('input[name=deliver-date]');

const calcPrice = () => {
    let finalPriceCalc = 0;
    const priceCalc = document.querySelector('.price-calc');
    const selectedAddons = document.querySelectorAll('select[name=addons] option:checked');
    const selectedSize = document.querySelector('input[name=size]:checked');
    const selectedToppings = document.querySelectorAll('fieldset[name=toppings] input:checked');

    if (selectedSize != null) {
        switch (selectedSize.value) {
            case 'Small':
                finalPriceCalc += 22;
                break;
            case 'Medium':
                finalPriceCalc += 28;
                break;
            case 'Large':
                finalPriceCalc += 35;
                break;
        }
    }

    if (selectedToppings != null) {
        finalPriceCalc += 2 * selectedToppings.length;
    }

    if (selectedAddons != null) {
        selectedAddons.forEach(x => {
            switch (x.value) {
                case 'Buffalo Wings':
                    finalPriceCalc += 5;
                    break;
                case 'Garlic Bread':
                    finalPriceCalc += 3;
                    break;
            }
        });
    }

    priceCalc.innerHTML = `Total price for your order is $${finalPriceCalc}`;
}

const allFormInputs = document.querySelectorAll('input, select');

allFormInputs.forEach(x => {
    x.addEventListener('input', calcPrice);
})

deliveryDate.min = new Date().toISOString().split('T')[0];
deliveryDate.max = new Date(new Date().setDate(new Date().getDate() + 7)).toISOString().split('T')[0];
